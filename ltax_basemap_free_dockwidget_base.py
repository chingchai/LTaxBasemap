# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ltax_basemap_free_dockwidget_base.ui'
#
# Created: Wed May 19 14:34:45 2021
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LTaxBasemapFreeDockWidgetBase(object):
    def setupUi(self, LTaxBasemapFreeDockWidgetBase):
        LTaxBasemapFreeDockWidgetBase.setObjectName(_fromUtf8("LTaxBasemapFreeDockWidgetBase"))
        LTaxBasemapFreeDockWidgetBase.resize(298, 190)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(280, 150))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 241, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setIconSize(QtCore.QSize(32, 32))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/osm2.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, _fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/terrain1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, _fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/imagery.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, _fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/map11.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, _fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/map7.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, _fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/LTaxBasemapFree/icons/satellite2.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, _fromUtf8(""))
        self.btnLoad = QtGui.QPushButton(self.tab)
        self.btnLoad.setGeometry(QtCore.QRect(10, 70, 241, 31))
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 251, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 90, 131, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        LTaxBasemapFreeDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(LTaxBasemapFreeDockWidgetBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LTaxBasemapFreeDockWidgetBase)

    def retranslateUi(self, LTaxBasemapFreeDockWidgetBase):
        LTaxBasemapFreeDockWidgetBase.setWindowTitle(_translate("LTaxBasemapFreeDockWidgetBase", "LTax BaseMap Free.", None))
        self.label.setText(_translate("LTaxBasemapFreeDockWidgetBase", "Basemap :", None))
        self.comboBox.setItemText(0, _translate("LTaxBasemapFreeDockWidgetBase", "Open Street Map", None))
        self.comboBox.setItemText(1, _translate("LTaxBasemapFreeDockWidgetBase", "Google Terrian", None))
        self.comboBox.setItemText(2, _translate("LTaxBasemapFreeDockWidgetBase", "Google Satellite Map", None))
        self.comboBox.setItemText(3, _translate("LTaxBasemapFreeDockWidgetBase", "Google Hybrid Map", None))
        self.comboBox.setItemText(4, _translate("LTaxBasemapFreeDockWidgetBase", "ESRI Topo Map", None))
        self.comboBox.setItemText(5, _translate("LTaxBasemapFreeDockWidgetBase", "ESRI Satellite Map", None))
        self.btnLoad.setText(_translate("LTaxBasemapFreeDockWidgetBase", "Load", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("LTaxBasemapFreeDockWidgetBase", "LTax Basemap Free.", None))
        self.label_2.setText(_translate("LTaxBasemapFreeDockWidgetBase", "<html><head/><body><p>LTax BaseMap Free.</p></body></html>", None))
        self.label_3.setText(_translate("LTaxBasemapFreeDockWidgetBase", "by Attagorn Srinarong (TongzGIS)", None))
        self.label_4.setText(_translate("LTaxBasemapFreeDockWidgetBase", "Line ID: attagorn", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("LTaxBasemapFreeDockWidgetBase", "About", None))

import resources

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LTaxBasemapFreeDockWidgetBase = QtGui.QDockWidget()
    ui = Ui_LTaxBasemapFreeDockWidgetBase()
    ui.setupUi(LTaxBasemapFreeDockWidgetBase)
    LTaxBasemapFreeDockWidgetBase.show()
    sys.exit(app.exec_())

