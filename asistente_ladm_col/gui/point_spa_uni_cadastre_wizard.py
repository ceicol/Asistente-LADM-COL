# -*- coding: utf-8 -*-
"""
/***************************************************************************
                              Asistente LADM_COL
                             --------------------
        begin                : 2017-11-14
        git sha              : :%H$
        copyright            : (C) 2017 by Germán Carrillo (BSF Swissphoto)
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import os

from qgis.core import (QgsProject, QgsVectorLayer, QgsSpatialIndex, Qgis,
                       QgsMapLayerProxyModel)
from qgis.PyQt.QtCore import QSettings, QCoreApplication
from qgis.PyQt.QtWidgets import QWizard

from ..utils.qt_utils import (make_file_selector, enable_next_wizard,
                              disable_next_wizard)
from ..utils import get_ui_class
from ..config.table_mapping_config import (BOUNDARY_POINT_TABLE,
                                           SURVEY_POINT_TABLE)
from ..config.help_strings import HelpStrings

WIZARD_UI = get_ui_class('wiz_add_points_cadastre.ui')

class PointsSpatialUnitCadastreWizard(QWizard, WIZARD_UI):
    def __init__(self, iface, db, qgis_utils, parent=None):
        QWizard.__init__(self, parent)
        self.setupUi(self)
        self.iface = iface
        self._db = db
        self.qgis_utils = qgis_utils
        self.help_strings = HelpStrings()

        # Auxiliary data to set nonlinear next pages
        self.pages = [self.wizardPage1, self.wizardPage2, self.wizardPage3]
        self.dict_pages_ids = {self.pages[idx] : pid for idx, pid in enumerate(self.pageIds())}

        # Set connections
        self.btn_browse_file.clicked.connect(
            make_file_selector(self.txt_file_path,
                               file_filter=QCoreApplication.translate("PointsSpatialUnitCadastreWizard",'CSV Comma Separated Value (*.csv)')))
        self.txt_file_path.textChanged.connect(self.fill_long_lat_combos)
        self.txt_delimiter.textChanged.connect(self.fill_long_lat_combos)

        self.restore_settings()

        self.txt_file_path.textChanged.emit(self.txt_file_path.text())

        self.rad_boundary_point.toggled.connect(self.point_option_changed)
        self.rad_csv.toggled.connect(self.adjust_page_2_controls)
        self.point_option_changed() # Initialize it
        self.button(QWizard.FinishButton).clicked.connect(self.finished_dialog)
        self.currentIdChanged.connect(self.current_page_changed)

        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.PointLayer)

        self.txt_help_page_2.setHtml(self.help_strings.WIZ_ADD_POINTS_CADASTRE_PAGE_2_OPTION_CSV)

        self.wizardPage2.setButtonText(QWizard.FinishButton,
                                       QCoreApplication.translate("PointsSpatialUnitCadastreWizard",
                                            "Import"))
        self.txt_help_page_3.setHtml(self.help_strings.WIZ_ADD_POINTS_CADASTRE_PAGE_2_OPTION_CSV)

    def nextId(self):
        """
        Set navigation order. Should return an integer. -1 is Finish.
        """
        if self.currentId() == self.dict_pages_ids[self.wizardPage1]:
            if self.rad_boundary_point.isChecked():
                return self.dict_pages_ids[self.wizardPage2]
            elif self.rad_survey_point.isChecked():
                return self.dict_pages_ids[self.wizardPage2]
        elif self.currentId() == self.dict_pages_ids[self.wizardPage2]:
            if self.rad_csv.isChecked():
                return self.dict_pages_ids[self.wizardPage3]
            elif self.rad_refactor.isChecked():
                return -1
        elif self.currentId() == self.dict_pages_ids[self.wizardPage3]:
            return -1
        else:
            return -1

    def current_page_changed(self, id):
        """
        Reset the Next button. Needed because Next might have been disabled by a
        condition in a another SLOT.
        """
        enable_next_wizard(self)

        if id == self.dict_pages_ids[self.wizardPage2]:
            self.adjust_page_2_controls()
        elif id == self.dict_pages_ids[self.wizardPage3]:
            self.fill_long_lat_combos("")


    def adjust_page_2_controls(self):
        if self.rad_refactor.isChecked():
            self.lbl_refactor_source.setEnabled(True)
            self.mMapLayerComboBox.setEnabled(True)

            disable_next_wizard(self)
            self.wizardPage2.setFinalPage(True)
            self.txt_help_page_2.setHtml(
                self.help_strings.get_refactor_help_string(
                    BOUNDARY_POINT_TABLE if self.rad_boundary_point.isChecked() else SURVEY_POINT_TABLE,
                    True))

        elif self.rad_csv.isChecked():
            self.lbl_refactor_source.setEnabled(False)
            self.mMapLayerComboBox.setEnabled(False)

            enable_next_wizard(self)
            self.wizardPage2.setFinalPage(False)
            self.txt_help_page_2.setHtml(self.help_strings.WIZ_ADD_POINTS_CADASTRE_PAGE_2_OPTION_CSV)

    def point_option_changed(self):
        if self.rad_boundary_point.isChecked():
            self.gbx_page_2.setTitle(QCoreApplication.translate("PointsSpatialUnitCadastreWizard", "Load data to Boundary Points..."))
            self.txt_help_page_1.setHtml(self.help_strings.WIZ_ADD_POINTS_CADASTRE_PAGE_1_OPTION_BP)
        else: # self.rad_survey_point is checked
            self.gbx_page_2.setTitle(QCoreApplication.translate("PointsSpatialUnitCadastreWizard", "Load data to Survey Points..."))
            self.txt_help_page_1.setHtml(self.help_strings.WIZ_ADD_POINTS_CADASTRE_PAGE_1_OPTION_SP)

    def finished_dialog(self):
        self.save_settings()

        if self.rad_refactor.isChecked():
            if self.rad_boundary_point.isChecked():
                output_layer_name = BOUNDARY_POINT_TABLE
            elif self.rad_survey_point.isChecked():
                output_layer_name = SURVEY_POINT_TABLE

            if self.mMapLayerComboBox.currentLayer() is not None:
                self.qgis_utils.show_etl_model(self._db,
                                               self.mMapLayerComboBox.currentLayer(),
                                               output_layer_name)
            else:
                self.iface.messageBar().pushMessage("Asistente LADM_COL",
                    QCoreApplication.translate("PointsSpatialUnitCadastreWizard",
                                               "Select a source layer to set the field mapping to '{}'.").format(output_layer_name),
                    Qgis.Warning)

        elif self.rad_csv.isChecked():
            self.prepare_copy_csv_points_to_db()

    def prepare_copy_csv_points_to_db(self):
        csv_path = self.txt_file_path.text().strip()

        if not csv_path or not os.path.exists(csv_path):
            self.iface.messageBar().pushMessage("Asistente LADM_COL",
                QCoreApplication.translate("PointsSpatialUnitCadastreWizard",
                                           "No CSV file given or file doesn't exist."),
                Qgis.Warning)
            return

        target_layer = BOUNDARY_POINT_TABLE if self.rad_boundary_point.isChecked() else SURVEY_POINT_TABLE

        res = self.qgis_utils.copy_csv_to_db(csv_path,
                                    self.txt_delimiter.text(),
                                    self.cbo_longitude.currentText(),
                                    self.cbo_latitude.currentText(),
                                    self._db,
                                    target_layer)

    def fill_long_lat_combos(self, text):
        csv_path = self.txt_file_path.text().strip()
        self.cbo_longitude.clear()
        self.cbo_latitude.clear()
        if os.path.exists(csv_path):
            self.button(QWizard.FinishButton).setEnabled(True)

            fields = self.get_fields_from_csv_file(csv_path)
            if not fields:
                self.button(QWizard.FinishButton).setEnabled(False)
                return

            self.cbo_longitude.addItems(fields)
            self.cbo_latitude.addItems(fields)

            # Heuristics to suggest values for x and y
            lowercase_fields = [field for field in fields]
            x_potential_names = ['x', 'lon', 'long', 'longitud', 'longitude', 'este', 'east', 'oeste', 'west']
            y_potential_names = ['y', 'lat', 'latitud', 'latitude', 'norte', 'north']
            for x_potential_name in x_potential_names:
                if x_potential_name in lowercase_fields:
                    self.cbo_longitude.setCurrentText(x_potential_name)
                    break
            for y_potential_name in y_potential_names:
                if y_potential_name in lowercase_fields:
                    self.cbo_latitude.setCurrentText(y_potential_name)
                    break

        else:
            self.button(QWizard.FinishButton).setEnabled(False)


    def get_fields_from_csv_file(self, csv_path):
        if not self.txt_delimiter.text().strip():
            return []

        errorReading = False
        try:
            reader  = open(csv_path, "r")
        except IOError:
            errorReading = True
        line = reader.readline().replace("\n", "")
        reader.close()
        if not line:
            errorReading = True
        else:
            return line.split(self.txt_delimiter.text().strip())

        if errorReading:
            self.iface.messageBar().pushMessage("Asistente LADM_COL",
                QCoreApplication.translate("PointsSpatialUnitCadastreWizard",
                                           "It was not possible to read field names from the CSV. Check the file and try again."),
                Qgis.Warning)
        return []

    def save_settings(self):
        settings = QSettings()
        settings.setValue('Asistente-LADM_COL/wizards/points_add_points_type', 'boundary_point' if self.rad_boundary_point.isChecked() else 'survey_point')
        settings.setValue('Asistente-LADM_COL/wizards/points_load_data_type', 'csv' if self.rad_csv.isChecked() else 'refactor')
        settings.setValue('Asistente-LADM_COL/wizards/points_add_points_csv_file', self.txt_file_path.text().strip())
        settings.setValue('Asistente-LADM_COL/wizards/points_csv_file_delimiter', self.txt_delimiter.text().strip())

    def restore_settings(self):
        settings = QSettings()
        point_type = settings.value('Asistente-LADM_COL/wizards/points_add_points_type') or 'boundary_point'
        if point_type == 'boundary_point':
            self.rad_boundary_point.setChecked(True)
        else:
            self.rad_survey_point.setChecked(True)

        load_data_type = settings.value('Asistente-LADM_COL/wizards/points_load_data_type') or 'csv'
        if load_data_type == 'refactor':
            self.rad_refactor.setChecked(True)
        else:
            self.rad_csv.setChecked(True)

        self.txt_file_path.setText(settings.value('Asistente-LADM_COL/wizards/points_add_points_csv_file'))
        self.txt_delimiter.setText(settings.value('Asistente-LADM_COL/wizards/points_csv_file_delimiter'))