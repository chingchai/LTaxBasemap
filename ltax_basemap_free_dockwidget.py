# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LTaxBasemapFreeDockWidget
                                 A QGIS plugin
 LTax Basemap free for qgis2.x
                             -------------------
        begin                : 2021-05-19
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Attagorn Srinarong / LTMAP, LTaxSmartGroup, SmartLTax
        email                : attagorn@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

from .ltax_basemap_free_dockwidget_base import *
class LTaxBasemapFreeDockWidget(QtGui.QDockWidget, Ui_LTaxBasemapFreeDockWidgetBase):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(LTaxBasemapFreeDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

