from qgis.PyQt.QtCore import (QObject,
                              QCoreApplication)
from asistente_ladm_col.config.enums import EnumQualityRule
from asistente_ladm_col.config.general_config import (COLLECTED_DB_SOURCE,
                                                      SUPPLIES_DB_SOURCE)
from asistente_ladm_col.config.quality_rules_config import (QUALITY_RULE_ERROR_CODE_E100101,
                                                            QUALITY_RULE_ERROR_CODE_E100201,
                                                            QUALITY_RULE_ERROR_CODE_E100301,
                                                            QUALITY_RULE_ERROR_CODE_E100302,
                                                            QUALITY_RULE_ERROR_CODE_E100303,
                                                            QUALITY_RULE_ERROR_CODE_E100401,
                                                            QUALITY_RULE_ERROR_CODE_E200101,
                                                            QUALITY_RULE_ERROR_CODE_E200201,
                                                            QUALITY_RULE_ERROR_CODE_E200301,
                                                            QUALITY_RULE_ERROR_CODE_E200302,
                                                            QUALITY_RULE_ERROR_CODE_E200303,
                                                            QUALITY_RULE_ERROR_CODE_E200304,
                                                            QUALITY_RULE_ERROR_CODE_E200305,
                                                            QUALITY_RULE_ERROR_CODE_E200401,
                                                            QUALITY_RULE_ERROR_CODE_E200402,
                                                            QUALITY_RULE_ERROR_CODE_E200403,
                                                            QUALITY_RULE_ERROR_CODE_E200501,
                                                            QUALITY_RULE_ERROR_CODE_E300101,
                                                            QUALITY_RULE_ERROR_CODE_E300201,
                                                            QUALITY_RULE_ERROR_CODE_E300301,
                                                            QUALITY_RULE_ERROR_CODE_E300401,
                                                            QUALITY_RULE_ERROR_CODE_E300402,
                                                            QUALITY_RULE_ERROR_CODE_E300403,
                                                            QUALITY_RULE_ERROR_CODE_E300404,
                                                            QUALITY_RULE_ERROR_CODE_E300405,
                                                            QUALITY_RULE_ERROR_CODE_E300501,
                                                            QUALITY_RULE_ERROR_CODE_E300601,
                                                            QUALITY_RULE_ERROR_CODE_E300701,
                                                            QUALITY_RULE_ERROR_CODE_E300801,
                                                            QUALITY_RULE_ERROR_CODE_E300901,
                                                            QUALITY_RULE_ERROR_CODE_E300902,
                                                            QUALITY_RULE_ERROR_CODE_E300903,
                                                            QUALITY_RULE_ERROR_CODE_E301001,
                                                            QUALITY_RULE_ERROR_CODE_E301002,
                                                            QUALITY_RULE_ERROR_CODE_E301003,
                                                            QUALITY_RULE_ERROR_CODE_E301101,
                                                            QUALITY_RULE_ERROR_CODE_E301102,
                                                            QUALITY_RULE_ERROR_CODE_E301103,
                                                            QUALITY_RULE_ERROR_CODE_E320101,
                                                            QUALITY_RULE_ERROR_CODE_E400101,
                                                            QUALITY_RULE_ERROR_CODE_E400102,
                                                            # QUALITY_RULE_ERROR_CODE_E400201,
                                                            QUALITY_RULE_ERROR_CODE_E400201,
                                                            QUALITY_RULE_ERROR_CODE_E400301,
                                                            QUALITY_RULE_ERROR_CODE_E400401,
                                                            QUALITY_RULE_ERROR_CODE_E400501,
                                                            QUALITY_RULE_ERROR_CODE_E400601,
                                                            QUALITY_RULE_ERROR_CODE_E400701,
                                                            QUALITY_RULE_ERROR_CODE_E400702,
                                                            QUALITY_RULE_ERROR_CODE_E400703,
                                                            QUALITY_RULE_ERROR_CODE_E400704,
                                                            QUALITY_RULE_ERROR_CODE_E400801,
                                                            QUALITY_RULE_ERROR_CODE_E400802,
                                                            QUALITY_RULE_ERROR_CODE_E400803,
                                                            QUALITY_RULE_ERROR_CODE_E400804,
                                                            QUALITY_RULE_ERROR_CODE_E400901,
                                                            QUALITY_RULE_ERROR_CODE_E400902,
                                                            QUALITY_RULE_ERROR_CODE_E400903,
                                                            QUALITY_RULE_ERROR_CODE_E400904,
                                                            QUALITY_RULE_ERROR_CODE_E400905,
                                                            QUALITY_RULE_ERROR_CODE_E400906,
                                                            QUALITY_RULE_ERROR_CODE_E400907,
                                                            QUALITY_RULE_ERROR_CODE_E400908,
                                                            QUALITY_RULE_ERROR_CODE_E401001,
                                                            QUALITY_RULE_ERROR_CODE_E401002,
                                                            QUALITY_RULE_ERROR_CODE_E401003,
                                                            QUALITY_RULE_ERROR_CODE_E401004,
                                                            QUALITY_RULE_ERROR_CODE_E401005,
                                                            QUALITY_RULE_ERROR_CODE_E401006,
                                                            QUALITY_RULE_ERROR_CODE_E401007,
                                                            QUALITY_RULE_ERROR_CODE_E401008,
                                                            QUALITY_RULE_ERROR_CODE_E401009,
                                                            QUALITY_RULE_ERROR_CODE_E401010,
                                                            QUALITY_RULE_ERROR_CODE_E401011,
                                                            QUALITY_RULE_ERROR_CODE_E401101,
                                                            QUALITY_RULE_ERROR_CODE_E401201,
                                                            QUALITY_RULE_ERROR_CODE_E401301,
                                                            QUALITY_RULE_ERROR_CODE_E401401,
                                                            QUALITY_RULE_ERROR_CODE_E401501,
                                                            QUALITY_RULE_ERROR_CODE_E401601,
                                                            QUALITY_RULE_ERROR_CODE_E401701,
                                                            QUALITY_RULE_ERROR_CODE_E401801,
                                                            QUALITY_RULE_ERROR_CODE_E401901,
                                                            QUALITY_RULE_ERROR_CODE_E402001,
                                                            QUALITY_RULE_ERROR_CODE_E402101,
                                                            QUALITY_RULE_ERROR_CODE_E402201,
                                                            QUALITY_RULE_ERROR_CODE_E420101,
                                                            QUALITY_RULE_ERROR_CODE_E420201,
                                                            QUALITY_RULE_ERROR_CODE_E420301,
                                                            QUALITY_RULE_ERROR_CODE_E420401,
                                                            QUALITY_RULE_ERROR_CODE_E420501,
                                                            QUALITY_RULE_ERROR_CODE_E420601,
                                                            QUALITY_RULE_ERROR_CODE_E420701,
                                                            QUALITY_RULE_ERROR_CODE_E420801,
                                                            QUALITY_RULE_ERROR_CODE_E420901,
                                                            QUALITY_RULE_ERROR_CODE_E421001,
                                                            QUALITY_RULE_ERROR_CODE_E421101,
                                                            QUALITY_RULE_ERROR_CODE_E421201,
                                                            QUALITY_RULE_ERROR_CODE_E421301,
                                                            QUALITY_RULE_ERROR_CODE_E421401,
                                                            QUALITY_RULE_ERROR_CODE_E421501,
                                                            QUALITY_RULE_ERROR_CODE_E421601,
                                                            QUALITY_RULE_ERROR_CODE_E421701,
                                                            QUALITY_RULE_ERROR_CODE_E421801,
                                                            QUALITY_RULE_ERROR_CODE_E421901,
                                                            QUALITY_RULE_ERROR_CODE_E422001,
                                                            QUALITY_RULE_ERROR_CODE_E422101,
                                                            QUALITY_RULE_ERROR_CODE_E422201,
                                                            QUALITY_RULE_ERROR_CODE_E422301,
                                                            QUALITY_RULE_ERROR_CODE_E422401,
                                                            QUALITY_RULE_ERROR_CODE_E422501,
                                                            QUALITY_RULE_ERROR_CODE_E422601,
                                                            QUALITY_RULE_ERROR_CODE_E422701,
                                                            QUALITY_RULE_ERROR_CODE_E422801,
                                                            QUALITY_RULE_ERROR_CODE_E422901,
                                                            QUALITY_RULE_ERROR_CODE_E423001,
                                                            QUALITY_RULE_ERROR_CODE_E423101,
                                                            QUALITY_RULE_ERROR_CODE_E423201,
                                                            QUALITY_RULE_ERROR_CODE_E423301,
                                                            QUALITY_RULE_ERROR_CODE_E423401)

ERROR_LAYER_GROUP = "ERROR_LAYER_GROUP"
RIGHT_OF_WAY_LINE_LAYER = "RIGHT_OF_WAY_LINE_LAYER"

TOOLBAR_BUILD_BOUNDARY = QCoreApplication.translate("TranslatableConfigStrings", "Build boundaries...")
TOOLBAR_MOVE_NODES = QCoreApplication.translate("TranslatableConfigStrings", "Move nodes...")
TOOLBAR_FILL_POINT_BFS = QCoreApplication.translate("TranslatableConfigStrings", "Fill Point BFS")
TOOLBAR_FILL_MORE_BFS_LESS = QCoreApplication.translate("TranslatableConfigStrings", "Fill More BFS and Less")
TOOLBAR_FILL_RIGHT_OF_WAY_RELATIONS = QCoreApplication.translate("TranslatableConfigStrings", "Fill Right of Way Relations")
TOOLBAR_IMPORT_FROM_INTERMEDIATE_STRUCTURE = QCoreApplication.translate("TranslatableConfigStrings", "Import from intermediate structure")
TOOLBAR_FINALIZE_GEOMETRY_CREATION = QCoreApplication.translate("TranslatableConfigStrings", "Finalize geometry creation")


class TranslatableConfigStrings(QObject):
    help_get_domain_code_from_value = QCoreApplication.translate("TranslatableConfigStrings", "Gets the t_id that corresponds to a domain value") + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Syntax</h4>") + \
                                         "<span class=\"functionname\">get_domain_code_from_value</span>(" \
                                         "<span class=\"argument\">domain_table</span>," \
                                         "<span class=\"argument\">value</span>," \
                                         "<span class=\"argument\">value_is_ilicode</span>," \
                                         "<span class=\"argument\">validate_conn</span>)" + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Arguments</h4>") + \
                                         "<span class=\"argument\">domain_table</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Domain table name or layer obj") + \
                                         "<br><span class=\"argument\">value</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Domain value to look for") + \
                                         "<br><span class=\"argument\">value_is_ilicode</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Whether value is iliCode or dispName") + \
                                         "<br><span class=\"argument\">validate_conn</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Whether validate connection or not") + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Examples</h4>") + \
                                         """<pre>get_domain_code_from_value( 
  'lc_condicionprediotipo',
  'NPH',
  True,
  False) → {}</pre>""".format(QCoreApplication.translate("TranslatableConfigStrings", "Gets the t_id of NPH in\n  domain lc_condicionprediotipo"))

    help_get_default_basket = QCoreApplication.translate("TranslatableConfigStrings",
                                                       "Gets the t_id of the default basket in the current DB (used for field data capture). This function creates the basket if it does not exist yet. If the DB does not support baskets, it returns None.") + \
                                      QCoreApplication.translate("TranslatableConfigStrings", "<h4>Syntax</h4>") + \
                                      "<span class=\"functionname\">get_default_basket()</span>" + \
                                      QCoreApplication.translate("TranslatableConfigStrings", "<h4>Examples</h4>") + \
                                      """<pre>get_default_basket() → {}</pre>""".format(QCoreApplication.translate("TranslatableConfigStrings",
                                                       "\nGets the t_id of\nthe default basket"))

    help_get_paired_domain_value = QCoreApplication.translate("TranslatableConfigStrings", "Gets the t_id in the target domain that corresponds to a given t_id in the source domain. Note that target DB should be in the main connection and source DB should be in the secondary connection.") + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Syntax</h4>") + \
                                         "<span class=\"functionname\">get_paired_domain_value</span>(" \
                                         "<span class=\"argument\">source_domain_table</span>," \
                                         "<span class=\"argument\">target_domain_table</span>," \
                                         "<span class=\"argument\">source_value</span>)" + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Arguments</h4>") + \
                                         "<span class=\"argument\">source_domain_table</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Source domain table name") + \
                                         "<br><span class=\"argument\">target_domain_table</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Target domain table name") + \
                                         "<br><span class=\"argument\">source_value</span> " + QCoreApplication.translate("TranslatableConfigStrings", "Domain value (t_id) in the source domain") + \
                                         QCoreApplication.translate("TranslatableConfigStrings", "<h4>Examples</h4>") + \
                                         """<pre>get_paired_domain_value(
  'gc_condicionprediotipo',
  'd_condicionprediotipo',
  423) → {}</pre>""".format(QCoreApplication.translate("TranslatableConfigStrings", "Gets the t_id of\nd_condicionprediotipo that\ncorresponds to the t_id 423\nin gc_condicionprediotipo."))

    def __init__(self):
        pass

    @staticmethod
    def tr_db_source(source):
        if source == COLLECTED_DB_SOURCE:
            return QCoreApplication.translate("TranslatableConfigStrings", "COLLECTED")
        elif source == SUPPLIES_DB_SOURCE:
            return QCoreApplication.translate("TranslatableConfigStrings", "SUPPLIES")

    @staticmethod
    def get_translatable_config_strings():
        return {
            EnumQualityRule.Point.OVERLAPS_IN_BOUNDARY_POINTS: QCoreApplication.translate("TranslatableConfigStrings", "Boundary Points should not overlap"),
            EnumQualityRule.Point.OVERLAPS_IN_CONTROL_POINTS: QCoreApplication.translate("TranslatableConfigStrings", "Control Points should not overlap"),
            EnumQualityRule.Point.BOUNDARY_POINTS_COVERED_BY_BOUNDARY_NODES: QCoreApplication.translate("TranslatableConfigStrings", "Boundary Points should be covered by Boundary nodes"),
            EnumQualityRule.Point.BOUNDARY_POINTS_COVERED_BY_PLOT_NODES: QCoreApplication.translate("TranslatableConfigStrings", "Boundary Points should be covered by plot nodes"),
            EnumQualityRule.Line.OVERLAPS_IN_BOUNDARIES: QCoreApplication.translate("TranslatableConfigStrings", "Boundaries should not overlap"),
            EnumQualityRule.Line.BOUNDARIES_ARE_NOT_SPLIT: QCoreApplication.translate("TranslatableConfigStrings", "Boundaries should not be split"),
            EnumQualityRule.Line.BOUNDARIES_COVERED_BY_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "Boundaries should be covered by Plots"),
            EnumQualityRule.Line.BOUNDARY_NODES_COVERED_BY_BOUNDARY_POINTS: QCoreApplication.translate("TranslatableConfigStrings", "Boundary nodes should be covered by Boundary Points"),
            EnumQualityRule.Line.DANGLES_IN_BOUNDARIES: QCoreApplication.translate("TranslatableConfigStrings", "Boundaries should not have dangles"),
            EnumQualityRule.Polygon.OVERLAPS_IN_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "Plots should not overlap"),
            EnumQualityRule.Polygon.OVERLAPS_IN_BUILDINGS: QCoreApplication.translate("TranslatableConfigStrings", "Buildings should not overlap"),
            EnumQualityRule.Polygon.OVERLAPS_IN_RIGHTS_OF_WAY: QCoreApplication.translate("TranslatableConfigStrings", "Rights of Way should not overlap"),
            EnumQualityRule.Polygon.PLOTS_COVERED_BY_BOUNDARIES: QCoreApplication.translate("TranslatableConfigStrings", "Plots should be covered by Boundaries"),
            EnumQualityRule.Polygon.PLOT_NODES_COVERED_BY_BOUNDARY_POINTS: QCoreApplication.translate("TranslatableConfigStrings", "Plot nodes should be covered by boundary points"),
            EnumQualityRule.Polygon.RIGHT_OF_WAY_OVERLAPS_BUILDINGS: QCoreApplication.translate("TranslatableConfigStrings", "Right of Way should not overlap Buildings"),
            EnumQualityRule.Polygon.GAPS_IN_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "Plots should not have gaps"),
            EnumQualityRule.Polygon.MULTIPART_IN_RIGHT_OF_WAY: QCoreApplication.translate("TranslatableConfigStrings", "Right of Way should not have multipart geometries"),
            EnumQualityRule.Polygon.BUILDINGS_SHOULD_BE_WITHIN_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "Buildings should be within Plots"),
            EnumQualityRule.Polygon.BUILDING_UNITS_SHOULD_BE_WITHIN_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "Building Units should be within corresponding plots"),
            EnumQualityRule.Polygon.BUILDING_UNITS_SHOULD_BE_WITHIN_BUILDINGS: QCoreApplication.translate("TranslatableConfigStrings", "Building Units should be within corresponding buildings"),
            EnumQualityRule.Polygon.OVERLAPS_IN_FDC_PLOTS: QCoreApplication.translate("TranslatableConfigStrings", "FDC plots should not overlap"),
            EnumQualityRule.Logic.PARCEL_RIGHT_RELATIONSHIP: QCoreApplication.translate("TranslatableConfigStrings", "Parcel should have one and only one Right"),
            EnumQualityRule.Logic.FRACTION_SUM_FOR_PARTY_GROUPS: QCoreApplication.translate("TranslatableConfigStrings", "Group Party Fractions should sum 1"),
            EnumQualityRule.Logic.DEPARTMENT_CODE_HAS_TWO_NUMERICAL_CHARACTERS: QCoreApplication.translate("TranslatableConfigStrings", "Check that the department field of the parcel table has two numerical characters"),
            EnumQualityRule.Logic.MUNICIPALITY_CODE_HAS_THREE_NUMERICAL_CHARACTERS: QCoreApplication.translate("TranslatableConfigStrings", "Check that the municipality field of the parcel table has three numerical characters"),
            EnumQualityRule.Logic.PARCEL_NUMBER_HAS_30_NUMERICAL_CHARACTERS: QCoreApplication.translate("TranslatableConfigStrings", "Check that the parcel number has 30 numerical characters"),
            EnumQualityRule.Logic.PARCEL_NUMBER_BEFORE_HAS_20_NUMERICAL_CHARACTERS: QCoreApplication.translate("TranslatableConfigStrings", "Check that the parcel number before has 20 numerical characters"),
            EnumQualityRule.Logic.COL_PARTY_NATURAL_TYPE: QCoreApplication.translate("TranslatableConfigStrings", "Check that parties of type natural cannot include data of a legal party"),
            EnumQualityRule.Logic.COL_PARTY_NOT_NATURAL_TYPE: QCoreApplication.translate("TranslatableConfigStrings", "Check that parties of type legal cannot include data of a natural party"),
            EnumQualityRule.Logic.PARCEL_TYPE_AND_22_POSITION_OF_PARCEL_NUMBER: QCoreApplication.translate("TranslatableConfigStrings", "Check that the type of parcel corresponds to position 22 of the parcel number"),
            EnumQualityRule.Logic.UEBAUNIT_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "Check that Spatial Units associated with Parcels correspond to the parcel type"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_BOUNDARY_POINT: QCoreApplication.translate("TranslatableConfigStrings", "Boundary point should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_SURVEY_POINT: QCoreApplication.translate("TranslatableConfigStrings", "Survey point should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_CONTROL_POINT: QCoreApplication.translate("TranslatableConfigStrings", "Control point should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_BOUNDARY: QCoreApplication.translate("TranslatableConfigStrings", "Boundary should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_PLOT: QCoreApplication.translate("TranslatableConfigStrings", "Plot should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_BUILDING: QCoreApplication.translate("TranslatableConfigStrings", "Building should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_BUILDING_UNIT: QCoreApplication.translate("TranslatableConfigStrings", "Building unit should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "Parcel should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_PARTY: QCoreApplication.translate("TranslatableConfigStrings", "Party should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_RIGHT: QCoreApplication.translate("TranslatableConfigStrings", "Right should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_RESTRICTION: QCoreApplication.translate("TranslatableConfigStrings", "Restriction should not have duplicate records"),
            EnumQualityRule.Logic.DUPLICATE_RECORDS_IN_ADMINISTRATIVE_SOURCE: QCoreApplication.translate("TranslatableConfigStrings", "Administrative source should not have duplicate records"),
            EnumQualityRule.Logic.FDC_PARCEL_PARCEL_TYPE_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel type should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_CONDITION_TYPE_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel condition should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_LAND_CATEGORY_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel land category should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_LAND_CLASS_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel land class should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_ECONOMIC_DESTINATION_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel economic destination should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_DATE_OF_PROPERTY_VISIT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel date of property visit should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_VISIT_RESULT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel visit result should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_HAS_REGISTRER_AREA_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel has register area should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_HAS_FMI_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel has fmi should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_DOCUMENT_TYPE_OF_WHO_ATTENDED_THE_VISIT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel document type of who attended the visit should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_DOCUMENT_NUMBER_OF_WHO_ATTENDED_THE_VISIT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel document number of who attended the visit should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_NAME_WHO_ATTENDED_THE_VISIT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel name of who attended the visit should not be null"),
            EnumQualityRule.Logic.FDC_PARCEL_WHO_ATTENDED_THE_VISIT_RELATION_WITH_THE_PROPERTY_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel who attended the visit related to the property should not be null"),
            EnumQualityRule.Logic.FDC_RIGHT_FRACTION_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC right fraccion should not be null"),
            EnumQualityRule.Logic.FDC_PARTY_RESIDENCE_DEPARTMENT_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC party department of residence should not be null"),
            EnumQualityRule.Logic.FDC_PARTY_RESIDENCE_MUNICIPALITY_IS_NULL: QCoreApplication.translate("TranslatableConfigStrings", "FDC party municipality of residence should not be null"),
            EnumQualityRule.Logic.FDC_RIGHT_WITH_INVALID_RIGHT_TYPE: QCoreApplication.translate("TranslatableConfigStrings", "FDC right with a invalid right type"),
            EnumQualityRule.Logic.FDC_BUILDING_UNIT_WITHOUT_QUALIFICATION_BY_TYPOLOGY: QCoreApplication.translate("TranslatableConfigStrings", "FDC building unit without qualification by typology"),
            EnumQualityRule.Logic.FDC_PARCEL_WITHOUT_ASSOCIATED_ADDRESS: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel without associated address"),
            EnumQualityRule.Logic.FDC_PARTY_WITH_INVALID_DOCUMENT_TYPE: QCoreApplication.translate("TranslatableConfigStrings", "FDC party with invalid a invalid document type"),
            EnumQualityRule.Logic.FDC_PARCEL_WITHOUT_ASSOCIATED_RIGHT: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel without associated right"),
            EnumQualityRule.Logic.FDC_RIGHT_WITHOUT_ASSOCIATED_ADMINISTRATIVE_SOURCE: QCoreApplication.translate("TranslatableConfigStrings", "FDC right without associated administrative source"),
            EnumQualityRule.Logic.FDC_PARCEL_WITHOUT_ASSOCIATED_PLOT: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel without associated plot"),
            EnumQualityRule.Logic.FDC_PARCEL_WITH_MORE_THAN_ONE_ASSOCIATED_PLOT: QCoreApplication.translate("TranslatableConfigStrings", "FDC parcel with more than one associated plot"),
            EnumQualityRule.Logic.FDC_RIGHT_BROKEN_RELATION_WITH_FDC_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "FDC right with broken relation fdc parcel"),
            EnumQualityRule.Logic.FDC_PARTY_BROKEN_RELATION_WITH_FDC_RIGHT: QCoreApplication.translate("TranslatableConfigStrings", "FDC party with broken relation fdc right"),
            EnumQualityRule.Logic.FDC_ADMINISTRATIVE_SOURCE_RIGHT_BROKEN_RELATION_WITH_FDC_RIGHT: QCoreApplication.translate("TranslatableConfigStrings", "FDC administrative source right with broken relation fdc right"),
            EnumQualityRule.Logic.FDC_ADMINISTRATIVE_SOURCE_BROKEN_RELATION_WITH_FDC_RIGHT: QCoreApplication.translate("TranslatableConfigStrings", "FDC administrative source with broken relation fdc right"),
            EnumQualityRule.Logic.EXT_ADDRESS_BROKEN_RELATION_WITH_FDC_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "ExtAddress with broken relation fdc parcel"),
            EnumQualityRule.Logic.FDC_HOUSING_MARKET_OFFERS_BROKEN_RELATION_WITH_FDC_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "FDC housing market offers with broken relation fdc parcel"),
            EnumQualityRule.Logic.FDC_RESTRICTION_BROKEN_RELATION_WITH_FDC_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "FDC restriction with broken relation fdc parcel"),
            EnumQualityRule.Logic.FDC_BUILDING_BROKEN_RELATION_WITH_FDC_PARCEL: QCoreApplication.translate("TranslatableConfigStrings", "FDC building with broken relation fdc parcel"),
            EnumQualityRule.Logic.FDC_BUILDING_UNIT_BROKEN_RELATION_WITH_FDC_BUILDING: QCoreApplication.translate("TranslatableConfigStrings", "FDC building unit with broken relation fdc building"),
            EnumQualityRule.Logic.FDC_PARTY_WITH_INVALID_DOCUMENT_NUMBER: QCoreApplication.translate("TranslatableConfigStrings", "FDC party with invalid document number"),

            # Domain errors message
            # ERROR CODES FOR POINT QUALITY RULES
            QUALITY_RULE_ERROR_CODE_E100101: QCoreApplication.translate("TranslatableConfigStrings", "Los puntos de lindero no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E100201: QCoreApplication.translate("TranslatableConfigStrings", "Los puntos de control no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E100301: QCoreApplication.translate("TranslatableConfigStrings", "Punto lindero no esta cubierto por un nodo de lindero"),
            QUALITY_RULE_ERROR_CODE_E100302: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre el punto lindero y el nodo de un lindero no está registra en la tabla puntoccl"),
            QUALITY_RULE_ERROR_CODE_E100303: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre el punto lindero y el nodo de un lindero está duplicada en la tabla puntoccl"),
            QUALITY_RULE_ERROR_CODE_E100401: QCoreApplication.translate("TranslatableConfigStrings", "El punto de lindero no está cubierto por un nodo de un terreno"),

            # ERROR CODES FOR LINE QUALITY RULES
            QUALITY_RULE_ERROR_CODE_E200101: QCoreApplication.translate("TranslatableConfigStrings", "Los linderos no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E200201: QCoreApplication.translate("TranslatableConfigStrings", "El lindero debe terminar en cambio de colindancia"),
            QUALITY_RULE_ERROR_CODE_E200301: QCoreApplication.translate("TranslatableConfigStrings", "El lindero no está cubierto por terreno"),
            QUALITY_RULE_ERROR_CODE_E200302: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre lindero y terreno está duplicada en la tabla masccl"),
            QUALITY_RULE_ERROR_CODE_E200303: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre lindero y terreno está duplicada en la tabla menosccl"),
            QUALITY_RULE_ERROR_CODE_E200304: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre lindero y terreno no está registrada en la tabla masccl"),
            QUALITY_RULE_ERROR_CODE_E200305: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre lindero y terreno no está registrada en la tabla menosccl"),
            QUALITY_RULE_ERROR_CODE_E200401: QCoreApplication.translate("TranslatableConfigStrings", "Nodo lindero no está cubierto por un punto lindero"),
            QUALITY_RULE_ERROR_CODE_E200402: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre el punto lindero y el nodo de un lindero no está registra en la tabla puntoccl"),
            QUALITY_RULE_ERROR_CODE_E200403: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre el punto lindero y el nodo de un lindero está duplicada en la tabla puntoccl"),
            QUALITY_RULE_ERROR_CODE_E200501: QCoreApplication.translate("TranslatableConfigStrings", "El lindero no debe tener nodos sin conectar"),

            # ERROR CODES FOR POLYGON QUALITY RULES
            QUALITY_RULE_ERROR_CODE_E300101: QCoreApplication.translate("TranslatableConfigStrings", "Los terrenos no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E300201: QCoreApplication.translate("TranslatableConfigStrings", "Las construcciones no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E300301: QCoreApplication.translate("TranslatableConfigStrings", "Las servidumbres de paso no deben superponerse"),
            QUALITY_RULE_ERROR_CODE_E300401: QCoreApplication.translate("TranslatableConfigStrings", "El terreno no está cubierto por linderos"),
            QUALITY_RULE_ERROR_CODE_E300402: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre terreno y lindero está duplicada en la tabla masccl"),
            QUALITY_RULE_ERROR_CODE_E300403: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre terreno y lindero está duplicada en la tabla menosccl"),
            QUALITY_RULE_ERROR_CODE_E300404: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre terreno y lindero no está registrada en la tabla masccl"),
            QUALITY_RULE_ERROR_CODE_E300405: QCoreApplication.translate("TranslatableConfigStrings", "La relación topológica entre terreno y lindero no está registrada en la tabla menosccl"),
            QUALITY_RULE_ERROR_CODE_E300501: QCoreApplication.translate("TranslatableConfigStrings", "La servidumbre de paso no se debe superponer con la construcción"),
            QUALITY_RULE_ERROR_CODE_E300601: QCoreApplication.translate("TranslatableConfigStrings", "No debe haber hueco entre terrenos"),
            QUALITY_RULE_ERROR_CODE_E300701: QCoreApplication.translate("TranslatableConfigStrings", "Servidumbre de paso no debe tener geometría multiparte"),
            QUALITY_RULE_ERROR_CODE_E300801: QCoreApplication.translate("TranslatableConfigStrings", "El nodo del terreno no está cubierto por un punto lindero"),
            QUALITY_RULE_ERROR_CODE_E300901: QCoreApplication.translate("TranslatableConfigStrings", "La construcción no está dentro de ningún terreno"),
            QUALITY_RULE_ERROR_CODE_E300902: QCoreApplication.translate("TranslatableConfigStrings", "La construcción cruza los límites de un terreno"),
            QUALITY_RULE_ERROR_CODE_E300903: QCoreApplication.translate("TranslatableConfigStrings", "La construcción está dentro de un terreno pero no dentro de su terreno correspondiente"),
            QUALITY_RULE_ERROR_CODE_E301001: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción no está dentro de ningún terreno"),
            QUALITY_RULE_ERROR_CODE_E301002: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción cruza los límites de un terreno"),
            QUALITY_RULE_ERROR_CODE_E301003: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción está dentro de un terreno pero no dentro de su terreno correspondiente"),
            QUALITY_RULE_ERROR_CODE_E301101: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción no está dentro de ninguna construcción"),
            QUALITY_RULE_ERROR_CODE_E301102: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción cruza los límites de una construcción"),
            QUALITY_RULE_ERROR_CODE_E301103: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción está dentro de una construcción pero no dentro de su construcción correspondiente"),

            QUALITY_RULE_ERROR_CODE_E320101: QCoreApplication.translate("TranslatableConfigStrings", "Los terrenos no deben superponerse"),

            # ERROR CODES FOR LOGIC QUALITY RULES
            QUALITY_RULE_ERROR_CODE_E400101: QCoreApplication.translate("TranslatableConfigStrings", "El predio tiene más de un derecho de dominio asociado"),
            QUALITY_RULE_ERROR_CODE_E400102: QCoreApplication.translate("TranslatableConfigStrings", "El predio no tiene derecho asociado"),
            # 4002 could be taken if needed
            QUALITY_RULE_ERROR_CODE_E400201: QCoreApplication.translate("TranslatableConfigStrings", "Los porcentajes de participación de la agrupación de interesados deben sumar uno (1)"),
            QUALITY_RULE_ERROR_CODE_E400301: QCoreApplication.translate("TranslatableConfigStrings", "El código de departamento debe tener dos caracteres numéricos"),
            QUALITY_RULE_ERROR_CODE_E400401: QCoreApplication.translate("TranslatableConfigStrings", "El código de municipio debe tener tres caracteres numéricos"),
            QUALITY_RULE_ERROR_CODE_E400501: QCoreApplication.translate("TranslatableConfigStrings", "El número predial debe tener 30 caracteres numéricos"),
            QUALITY_RULE_ERROR_CODE_E400601: QCoreApplication.translate("TranslatableConfigStrings", "El número predial anterior debe tener 20 caracteres numéricos"),
            QUALITY_RULE_ERROR_CODE_E400701: QCoreApplication.translate("TranslatableConfigStrings", "La razón social no debe estar diligenciada"),
            QUALITY_RULE_ERROR_CODE_E400702: QCoreApplication.translate("TranslatableConfigStrings", "El primer apellido es obligatorio y debe estar diligenciado"),
            QUALITY_RULE_ERROR_CODE_E400703: QCoreApplication.translate("TranslatableConfigStrings", "El primer nombre es obligatorio y debe estar diligenciado"),
            QUALITY_RULE_ERROR_CODE_E400704: QCoreApplication.translate("TranslatableConfigStrings", "El tipo de documento debe ser diferente de NIT"),
            QUALITY_RULE_ERROR_CODE_E400801: QCoreApplication.translate("TranslatableConfigStrings", "Razón social debe estar diligenciada"),
            QUALITY_RULE_ERROR_CODE_E400802: QCoreApplication.translate("TranslatableConfigStrings", "Primer apellido no debe estar diligenciada"),
            QUALITY_RULE_ERROR_CODE_E400803: QCoreApplication.translate("TranslatableConfigStrings", "Primer nombre no debe estar diligenciada"),
            QUALITY_RULE_ERROR_CODE_E400804: QCoreApplication.translate("TranslatableConfigStrings", "Tipo de documento debe ser NIT o Secuencial IGAC o Secuencial SNR"),
            QUALITY_RULE_ERROR_CODE_E400901: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'Bien de uso publico' la posición 22 del número predial debe ser 3"),
            QUALITY_RULE_ERROR_CODE_E400902: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'Condominio Matriz' o 'Condominio Unidad Predial' la posición 22 del número predial debe ser 8"),
            QUALITY_RULE_ERROR_CODE_E400903: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'Mejora en NPH' la posición 22 del número predial debe ser 5"),
            QUALITY_RULE_ERROR_CODE_E400904: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'Mejora en PH' la posición 22 del número predial debe ser 5"),
            QUALITY_RULE_ERROR_CODE_E400905: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'NPH' la posición 22 del número predial debe ser 0"),
            QUALITY_RULE_ERROR_CODE_E400906: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Parque Cementerio Matriz' o 'Parque Cementerio Unidad Predial' la posición 22 del número predial debe ser 7"),
            QUALITY_RULE_ERROR_CODE_E400907: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'PH Matriz' o 'PH Unidad Predial' la posición 22 del número predial debe ser 9"),
            QUALITY_RULE_ERROR_CODE_E400908: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condicion del predio es 'Vía' la posición 22 del número predial debe ser 4"),
            QUALITY_RULE_ERROR_CODE_E401001: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Bien de Uso Publico', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401002: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Condominio Matriz', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401003: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Condominio Unidad Predial', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401004: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Mejora en NPH', el predio debe tener asociado 0 terrenos y 1 construcción y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401005: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Mejora en PH', el predio debe tener asociado 0 terrenos y 1 construcción y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401006: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Parque Cementerio Matriz', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401007: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Parque Cementerio Unidad Predial', el predio debe tener asociado 1 terreno y 0 construcciones y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401008: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'PH Matriz', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401009: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'PH Unidad Predial', el predio debe tener asociado 0 terrenos y 0 construcciones y 1 unidad de construcción"),
            QUALITY_RULE_ERROR_CODE_E401010: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'Vía', el predio debe tener asociado 1 terreno y 0 construcciones y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401011: QCoreApplication.translate("TranslatableConfigStrings", "Cuando la condición del predio es 'NPH', el predio debe tener asociado 1 terreno y 0 unidades de construcción"),
            QUALITY_RULE_ERROR_CODE_E401101: QCoreApplication.translate("TranslatableConfigStrings", "Punto Lindero no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401201: QCoreApplication.translate("TranslatableConfigStrings", "Punto Levantamiento no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401301: QCoreApplication.translate("TranslatableConfigStrings", "Punto Control no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401401: QCoreApplication.translate("TranslatableConfigStrings", "Lindero no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401501: QCoreApplication.translate("TranslatableConfigStrings", "Terreno no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401601: QCoreApplication.translate("TranslatableConfigStrings", "Construcción no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401701: QCoreApplication.translate("TranslatableConfigStrings", "Unidad de Construcción no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401801: QCoreApplication.translate("TranslatableConfigStrings", "Predio no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E401901: QCoreApplication.translate("TranslatableConfigStrings", "Interesado no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E402001: QCoreApplication.translate("TranslatableConfigStrings", "Derecho no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E402101: QCoreApplication.translate("TranslatableConfigStrings", "Restricción no debe tener registros repetidos"),
            QUALITY_RULE_ERROR_CODE_E402201: QCoreApplication.translate("TranslatableConfigStrings", "Fuente Administrativa no debe tener registros repetidos"),

            QUALITY_RULE_ERROR_CODE_E420101: QCoreApplication.translate("TranslatableConfigStrings", "El tipo de predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420201: QCoreApplication.translate("TranslatableConfigStrings", "La condición de predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420301: QCoreApplication.translate("TranslatableConfigStrings", "La categoría del suelo del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420401: QCoreApplication.translate("TranslatableConfigStrings", "La clase de suelo del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420501: QCoreApplication.translate("TranslatableConfigStrings", "La destinación económica del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420601: QCoreApplication.translate("TranslatableConfigStrings", "La fecha de visita predial del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420701: QCoreApplication.translate("TranslatableConfigStrings", "El resultado de la visita del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420801: QCoreApplication.translate("TranslatableConfigStrings", "El atributo tiene área registral del  predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E420901: QCoreApplication.translate("TranslatableConfigStrings", "El atributo tiene folio de matrícula del predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421001: QCoreApplication.translate("TranslatableConfigStrings", "El atributo tipo de documento de quien atendio la visita no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421101: QCoreApplication.translate("TranslatableConfigStrings", "El atributo número de documento de quien atendio la visita no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421201: QCoreApplication.translate("TranslatableConfigStrings", "El atributo nombre de quien atendio la visita no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421301: QCoreApplication.translate("TranslatableConfigStrings", "El atributo relación con el predio no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421401: QCoreApplication.translate("TranslatableConfigStrings", "El atributo fracción del derecho no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421501: QCoreApplication.translate("TranslatableConfigStrings", "El atributo departamento de residencia del interesado no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421601: QCoreApplication.translate("TranslatableConfigStrings", "El atributo municipio de residencia del interesado no puede ser null"),
            QUALITY_RULE_ERROR_CODE_E421701: QCoreApplication.translate("TranslatableConfigStrings", "El tipo de derecho no puede ser 'Sin_Derecho'"),
            QUALITY_RULE_ERROR_CODE_E421801: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción no tiene calificación por tipología"),
            QUALITY_RULE_ERROR_CODE_E421901: QCoreApplication.translate("TranslatableConfigStrings", "El predio no tiene asociada una dirección"),
            QUALITY_RULE_ERROR_CODE_E422001: QCoreApplication.translate("TranslatableConfigStrings", "El tipo de documento no debería ser 'Secuencial'"),
            QUALITY_RULE_ERROR_CODE_E422101: QCoreApplication.translate("TranslatableConfigStrings", "El predio no tiene asociado un derecho"),
            QUALITY_RULE_ERROR_CODE_E422201: QCoreApplication.translate("TranslatableConfigStrings", "El derecho no tiene asociado una fuente administrativa"),
            QUALITY_RULE_ERROR_CODE_E422301: QCoreApplication.translate("TranslatableConfigStrings", "El predio no tiene asociado un terreno"),
            QUALITY_RULE_ERROR_CODE_E422401: QCoreApplication.translate("TranslatableConfigStrings", "El predio tiene mas de un terreno asociado"),
            QUALITY_RULE_ERROR_CODE_E422501: QCoreApplication.translate("TranslatableConfigStrings", "El derecho esta asociado a un predio que no existe"),
            QUALITY_RULE_ERROR_CODE_E422601: QCoreApplication.translate("TranslatableConfigStrings", "El interesado esta asociado a un derecho que no existe"),
            QUALITY_RULE_ERROR_CODE_E422701: QCoreApplication.translate("TranslatableConfigStrings", "El fuente_administrativa_derecho esta asociado a un derecho que no existe"),
            QUALITY_RULE_ERROR_CODE_E422801: QCoreApplication.translate("TranslatableConfigStrings", "El fuente administrativa esta asociado a un derecho que no existe"),
            QUALITY_RULE_ERROR_CODE_E422901: QCoreApplication.translate("TranslatableConfigStrings", "La dirección esta asociada a un predio que no existe"),
            QUALITY_RULE_ERROR_CODE_E423001: QCoreApplication.translate("TranslatableConfigStrings", "La oferta de mercado inmobiliario esta asociado a un predio que no existe"),
            QUALITY_RULE_ERROR_CODE_E423101: QCoreApplication.translate("TranslatableConfigStrings", "La restricción esta asociado a un predio que no existe"),
            QUALITY_RULE_ERROR_CODE_E423201: QCoreApplication.translate("TranslatableConfigStrings", "La construcción esta asociada a un predio que no existe"),
            QUALITY_RULE_ERROR_CODE_E423301: QCoreApplication.translate("TranslatableConfigStrings", "La unidad de construcción esta asociada a una construcción que no existe"),
            QUALITY_RULE_ERROR_CODE_E423401: QCoreApplication.translate("TranslatableConfigStrings", "El número de documento del interesado no debe ser '99999'"),

            ERROR_LAYER_GROUP: QCoreApplication.translate("TranslatableConfigStrings", "Validation errors"),
            RIGHT_OF_WAY_LINE_LAYER: QCoreApplication.translate("TranslatableConfigStrings", "Right of way line")
        }
