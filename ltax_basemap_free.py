# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LTaxBasemapFree
                                 A QGIS plugin
 LTax Basemap free for qgis2.x
                              -------------------
        begin                : 2021-05-19
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Attagorn Srinarong / LTMAP, LTaxSmartGroup, SmartLTax
        email                : attagorn@gmail.com
 ***************************************************************************/

"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources
from qgis.core import *
# Import the code for the DockWidget
from ltax_basemap_free_dockwidget import LTaxBasemapFreeDockWidget
import os.path


class LTaxBasemapFree:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgisInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'LTaxBasemapFree_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&LTax Basemap Free')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'LTaxBasemapFree')
        self.toolbar.setObjectName(u'LTaxBasemapFree')

        #print "** INITIALIZING LTaxBasemapFree"

        self.pluginIsActive = False
        self.dockwidget = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):

        return QCoreApplication.translate('LTaxBasemapFree', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/LTaxBasemapFree/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u''),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING LTaxBasemapFree"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD LTaxBasemapFree"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&LTax Basemap Free'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True
            if self.dockwidget == None:
                self.dockwidget = LTaxBasemapFreeDockWidget()

            self.dockwidget.closingPlugin.connect(self.onClosePlugin)
            self.dockwidget.btnLoad.clicked.connect(self.loadmap)
            self.iface.addDockWidget(Qt.LeftDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

    def loadmap(self):
        maps = []
        maps.append([u'Open Street Map','https://b.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png','xyz'])
        maps.append([u'Google Terrian','https://mt1.google.com/vt/lyrs%3Dp%2Ctraffic%26z%3D%7Bz%7D%26x%3D%7Bx%7D%26y%3D%7By%7D%26hl%3Dth','xyz'])
        maps.append([u'Google Satellite Map','https://mt1.google.com/vt/lyrs%3Ds%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&hl=th','xyz'])
        maps.append([u'Google Hybrid Map','https://mt1.google.com/vt/lyrs%3Dy%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&hl=th','xyz'])
        maps.append([u'ESRI Topo Map','https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D','xyz'])
        maps.append([u'ESRI Satellite Map','https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/%7Bz%7D/%7By%7D/%7Bx%7D','xyz'])

        smap = self.dockwidget.comboBox.currentText()
        print(smap)
        for amap in maps:
            if smap == amap[0]:
                print(amap[0], amap[1])
                if amap[2] == 'xyz':
                    self.create_xyz(amap[1], amap[0])
                elif amap[2] == 'wms':
                    self.create_wms(amap[1], amap[0])
                elif amap[2] == 'arcgis':
                    self.create_arcgis(amap[1], amap[0])
                return

    def create_xyz(self, url_path, map_name):

        rlayer = QgsRasterLayer('type=xyz&url='+url_path+'&zmax=19&zmin=0',map_name,'wms')
        if rlayer.isValid():

            QgsMapLayerRegistry.instance().addMapLayer(rlayer)
        else:
            print(u'โหลด wms' + map_name + ' ไม่ได้!!!')

