import processing
from qgis.core import (QgsFeatureRequest,
                       QgsExpressionContext,
                       QgsExpressionContextScope,
                       NULL,
                       QgsExpression)

from asistente_ladm_col.config.query_config import (get_structure_basic_query,
                                                    get_structure_economic_query,
                                                    get_structure_legal_query,
                                                    get_structure_physical_query,
                                                    get_structure_property_record_card_query)
from asistente_ladm_col.logic.ladm_col.data.ladm_query_objects import (OwnField,
                                                                       DomainOwnField,
                                                                       EvalExprOwnField,
                                                                       AbsRelateFields,
                                                                       RelateOwnFieldObject,
                                                                       RelateOwnFieldValue,
                                                                       RelateRemoteFieldValue,
                                                                       RelateRemoteFieldObject,
                                                                       SpatialFilterSubLevel,
                                                                       FilterSubLevel)
from asistente_ladm_col.logic.ladm_col.data.ladm_data import LADM_DATA
from asistente_ladm_col.config.mapping_config import QueryNames
from asistente_ladm_col.config.enums import (SpatialOperationType,
                                             GenericQueryType)


class LADMQuery:

    def __init__(self, qgis_utils):
        self.qgis_utils = qgis_utils
        self.ladm_data = LADM_DATA(self.qgis_utils)

    def execute_generic_query(self, db, enum_generic_query, filter_field_values):
        response = dict()
        query = dict()

        if GenericQueryType.IGAC_BASIC_QUERY == enum_generic_query:
            query = get_structure_basic_query(db.names)
        elif GenericQueryType.IGAC_PHYSICAL_QUERY == enum_generic_query:
            query = get_structure_physical_query(db.names)
        elif GenericQueryType.IGAC_LEGAL_QUERY == enum_generic_query:
            query = get_structure_legal_query(db.names)
        elif GenericQueryType.IGAC_ECONOMIC_QUERY == enum_generic_query:
            query = get_structure_economic_query(db.names)
        elif GenericQueryType.IGAC_PROPERTY_RECORD_CARD == enum_generic_query:
            query = get_structure_property_record_card_query(db.names)

        self.execute_query(db, response, query[QueryNames.LEVEL_TABLE], filter_field_values)
        return response

    def execute_property_record_card_query(self, db, filter_field_values):
        return self.execute_generic_query(db, GenericQueryType.IGAC_PROPERTY_RECORD_CARD, filter_field_values)

    def execute_economic_query(self, db, filter_field_values):
        return self.execute_generic_query(db, GenericQueryType.IGAC_ECONOMIC_QUERY, filter_field_values)

    def execute_physical_query(self, db, filter_field_values):
        return self.execute_generic_query(db, GenericQueryType.IGAC_PHYSICAL_QUERY, filter_field_values)

    def execute_legal_query(self, db, filter_field_values):
        return self.execute_generic_query(db, GenericQueryType.IGAC_LEGAL_QUERY, filter_field_values)

    def execute_basic_query(self, db, filter_field_values):
        return self.execute_generic_query(db, GenericQueryType.IGAC_BASIC_QUERY, filter_field_values)

    def execute_query(self, db, response, level_dict, filter_field_values):
        table_name = level_dict[QueryNames.LEVEL_TABLE_NAME]
        level_alias = level_dict[QueryNames.LEVEL_TABLE_ALIAS]
        layer = self.qgis_utils.get_layer(db, table_name, None, True)
        filter_sub_level = level_dict[QueryNames.FILTER_SUB_LEVEL]
        t_id_features = self.get_features_ids_sub_level(db, filter_sub_level, filter_field_values)

        response[level_alias] = list()
        dict_fields_and_alias = dict()
        for required_table_field in level_dict[QueryNames.TABLE_FIELDS]:
            if isinstance(required_table_field, OwnField):
                dict_fields_and_alias[required_table_field.field_name] = required_table_field.field_alias

        fields_names = list(dict_fields_and_alias.keys())
        select_features = self.get_features(layer, db.names.T_ID_F, fields_names, t_id_features)

        for select_feature in select_features:
            node_response = dict()
            node_response[QueryNames.ID_FEATURE_RESPONSE] = select_feature[db.names.T_ID_F]

            node_fields_response = dict()
            for field in level_dict[QueryNames.TABLE_FIELDS]:
                if isinstance(field, DomainOwnField):
                    domain_table = field.domain_table
                    domain_code = select_feature[field.field_name]
                    domain_value = self.ladm_data.get_domain_value_from_code(db, domain_table, domain_code, False)
                    node_fields_response[field.field_alias] = domain_value
                elif isinstance(field, OwnField):
                    node_fields_response[field.field_alias] = select_feature[field.field_name] if select_feature[field.field_name] != NULL else None
                elif isinstance(field, EvalExprOwnField):
                    node_fields_response[field.field_alias] = self.get_eval_expr_value(layer, select_feature, field.expression)
                elif isinstance(field, AbsRelateFields):
                    if isinstance(field, RelateRemoteFieldObject):
                        node_fields_response[field.field_alias] = self.get_relate_remote_field_object(db, field, [select_feature[db.names.T_ID_F]])
                    elif isinstance(field, RelateRemoteFieldValue):
                        node_fields_response[field.field_alias] = self.get_relate_remote_field_value(db, field, [select_feature[db.names.T_ID_F]])
                    elif isinstance(field, RelateOwnFieldObject):
                        node_fields_response[field.field_alias] = self.get_relate_own_field_object(db, field, [select_feature[db.names.T_ID_F]])
                    elif isinstance(field, RelateOwnFieldValue):
                        node_fields_response[field.field_alias] = self.get_relate_own_field_value(db, field, [select_feature[db.names.T_ID_F]])

            for dict_key in level_dict:
                if dict_key.endswith(QueryNames.LEVEL_TABLE):
                    self.execute_query(db, node_fields_response, level_dict[dict_key], [select_feature[db.names.T_ID_F]])

            node_response[QueryNames.ATTRIBUTES_RESPONSE] = node_fields_response
            response[level_alias].append(node_response)

    def get_relate_remote_field_object(self, db, field, filter_field_values):
        filter_sub_level = field.filter_sub_level
        t_id_features = self.get_relate_own_field_object(db, filter_sub_level, filter_field_values)
        return self.get_relate_own_field_value(db, field, t_id_features)

    def get_relate_remote_field_value(self, db, field, filter_field_values):
        filter_sub_level = field.filter_sub_level
        t_id_features = self.get_features_ids_sub_level(db, filter_sub_level, filter_field_values)
        return self.get_relate_own_field_value(db, field, t_id_features)

    def get_relate_own_field_object(self, db, field, filter_field_values):
        relate_layer = self.qgis_utils.get_layer(db, field.relate_table, None, True)
        dict_fields_and_alias =  self.get_dict_fields_and_alias(field.relate_table_fields)
        fields_names = list(dict_fields_and_alias.keys())
        fields_names.append(db.names.T_ID_F)

        features = self.get_features(relate_layer, field.relate_table_filter_field, fields_names, filter_field_values)

        list_relate_result = list()
        for feature in features:
            dict_relate_field = dict()
            dict_relate_field[QueryNames.ID_FEATURE_RESPONSE] = feature[db.names.T_ID_F]
            dict_attributes = dict()
            for field_relation in field.relate_table_fields:
                if isinstance(field_relation, DomainOwnField):
                    domain_table = field_relation.domain_table
                    domain_code = feature[field_relation.field_name]
                    domain_value = self.ladm_data.get_domain_value_from_code(db, domain_table, domain_code, False)
                    dict_attributes[field_relation.field_alias] = domain_value
                elif isinstance(field_relation, OwnField):
                    dict_attributes[field_relation.field_alias] = feature[field_relation.field_name] if feature[field_relation.field_name] != NULL else None
                elif isinstance(field_relation, EvalExprOwnField):
                    dict_attributes[field_relation.field_alias] = self.get_eval_expr_value(relate_layer, feature, field_relation.expression)

            dict_relate_field[QueryNames.ATTRIBUTES_RESPONSE] = dict_attributes
            list_relate_result.append(dict_relate_field)

        return list_relate_result

    def get_relate_own_field_value(self, db, field, filter_field_values):
        relate_layer = self.qgis_utils.get_layer(db, field.relate_table, None, True)
        required_field = field.relate_table_field
        dict_fields_and_alias = self.get_dict_fields_and_alias([required_field])
        fields_names = list(dict_fields_and_alias.keys())
        fields_names.append(db.names.T_ID_F)

        features = self.get_features(relate_layer, field.relate_table_filter_field, fields_names, filter_field_values)

        field_value = None
        for feature in features:
            if isinstance(required_field, DomainOwnField):
                domain_table = required_field.domain_table
                domain_code = feature[required_field.field_name]
                domain_value = self.ladm_data.get_domain_value_from_code(db, domain_table, domain_code, False)
                field_value = domain_value
            elif isinstance(required_field, OwnField):
                field_value = feature[required_field.field_name] if feature[required_field.field_name] != NULL else None
            elif isinstance(required_field, EvalExprOwnField):
                field_value = self.get_eval_expr_value(relate_layer, feature, required_field.expression)

        return field_value

    @staticmethod
    def get_eval_expr_value(layer, feature, expression):
        eval_feature = layer.getFeature(feature.id())  # this is necessary because the feature is filtered and may not have all the necessary fields
        context = QgsExpressionContext()
        scope = QgsExpressionContextScope()
        scope.setFeature(eval_feature)
        context.appendScope(scope)
        expression.prepare(context)
        display_value = expression.evaluate(context)

        return display_value

    @staticmethod
    def get_dict_fields_and_alias(table_fields):
        dict_fields_and_alias = dict()
        for required_table_field in table_fields:
            if isinstance(required_table_field, OwnField):
                dict_fields_and_alias[required_table_field.field_name] = required_table_field.field_alias
        return dict_fields_and_alias

    def get_features_ids_by_filter(self, db, filter_sub_level, filter_field_values):  # filter_field_values it is a list with only one item
        sub_level_table = filter_sub_level.sub_level_table
        required_field = filter_sub_level.required_field_sub_level_table
        sub_level_layer = self.qgis_utils.get_layer(db, sub_level_table, None, True)

        if isinstance(filter_sub_level, FilterSubLevel):
            filter_field = filter_sub_level.filter_field_in_sub_level_table
            expression = QgsExpression("{} in ({}) and {} is not null".format(filter_field, ', '.join(str(filter_field_value) for filter_field_value in filter_field_values), required_field))
            request = QgsFeatureRequest(expression)
            field_idx = sub_level_layer.fields().indexFromName(required_field)
            request.setFlags(QgsFeatureRequest.NoGeometry)
            request.setSubsetOfAttributes([field_idx])  # Note: this adds a new flag
            features_ids = [feature[required_field] for feature in sub_level_layer.getFeatures(request)]
            return features_ids

        elif isinstance(filter_sub_level, SpatialFilterSubLevel):
            level_table = filter_sub_level.level_table
            spatial_operation = filter_sub_level.spatial_operation
            level_layer = self.qgis_utils.get_layer(db, level_table, None, True)
            filter_level_layer = processing.run("native:extractbyattribute", {'INPUT': level_layer, 'FIELD': db.names.T_ID_F, 'OPERATOR': 0, 'VALUE': filter_field_values[0], 'OUTPUT': 'memory:'})['OUTPUT']

            parameters = {'INPUT': sub_level_layer, 'INTERSECT': filter_level_layer, 'OUTPUT': 'memory:'}
            if spatial_operation == SpatialOperationType.INTERSECTS_SPATIAL_OPERATION:
                parameters['PREDICATE'] = [0]  # Intersects
            elif spatial_operation == SpatialOperationType.OVERLAPS_SPATIAL_OPERATION:
                parameters['PREDICATE'] = [5]  # Overlaps
            elif spatial_operation == SpatialOperationType.CONTAINS_SPATIAL_OPERATION:
                parameters['PREDICATE'] = [1]  # Contains

            filter_sub_level_layer = processing.run("native:extractbylocation", parameters)['OUTPUT']

            features_ids = [feature[required_field] for feature in filter_sub_level_layer.getFeatures()]
            return features_ids

    def get_features_ids_sub_level(self, db, filter_sub_level, filter_field_values):
        t_id_features = list()
        for filter_field_value in filter_field_values:
            t_id_features.extend(self.get_features_ids_by_filter(db, filter_sub_level, [filter_field_value]))

        sub_filter_sub_level = filter_sub_level.filter_sub_level  # Recursivity to get features t_ids associate to the first filter
        if sub_filter_sub_level:
             return self.get_features_ids_sub_level(db, sub_filter_sub_level, t_id_features)
        else:
            return t_id_features

    @staticmethod
    def get_features(layer, filter_field, fields_names, t_id_features):
        if not t_id_features:
            return list()

        fields_idx = list()
        for field in fields_names:
            field_idx = layer.fields().indexFromName(field)
            fields_idx.append(field_idx)

        expression = QgsExpression('{} in ({})'.format(filter_field, ', '.join( str(t_id_feature) for t_id_feature in t_id_features)))
        request = QgsFeatureRequest(expression)

        request.setFlags(QgsFeatureRequest.NoGeometry)
        request.setSubsetOfAttributes(fields_idx)  # Note: this adds a new flag
        select_features = [feature for feature in layer.getFeatures(request)]
        return select_features