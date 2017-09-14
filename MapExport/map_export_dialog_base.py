# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_export_dialog_base.ui'
#
# Created: Thu Sep 14 15:20:27 2017
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_mapExport(object):
    def setupUi(self, mapExport):
        mapExport.setObjectName(_fromUtf8("mapExport"))
        mapExport.resize(376, 453)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mapExport.sizePolicy().hasHeightForWidth())
        mapExport.setSizePolicy(sizePolicy)
        mapExport.setMinimumSize(QtCore.QSize(320, 340))
        mapExport.setSizeIncrement(QtCore.QSize(0, 0))
        mapExport.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/MapExport/icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mapExport.setWindowIcon(icon)
        mapExport.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(mapExport)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(mapExport)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exportButton = QtGui.QPushButton(mapExport)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        self.buttonBox = QtGui.QDialogButtonBox(mapExport)
        self.buttonBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.printinglabel = QtGui.QLabel(mapExport)
        self.printinglabel.setText(_fromUtf8(""))
        self.printinglabel.setObjectName(_fromUtf8("printinglabel"))
        self.horizontalLayout_6.addWidget(self.printinglabel)
        self.pageBar = QtGui.QProgressBar(mapExport)
        self.pageBar.setProperty("value", 0)
        self.pageBar.setObjectName(_fromUtf8("pageBar"))
        self.horizontalLayout_6.addWidget(self.pageBar)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.path = QtGui.QLineEdit(mapExport)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy)
        self.path.setSizeIncrement(QtCore.QSize(0, 0))
        self.path.setToolTip(_fromUtf8(""))
        self.path.setWhatsThis(_fromUtf8(""))
        self.path.setObjectName(_fromUtf8("path"))
        self.horizontalLayout_3.addWidget(self.path)
        self.browser = QtGui.QPushButton(mapExport)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setMinimumSize(QtCore.QSize(100, 23))
        self.browser.setObjectName(_fromUtf8("browser"))
        self.horizontalLayout_3.addWidget(self.browser)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 2)
        self.textBrowser = QtGui.QTextBrowser(mapExport)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        self.label = QtGui.QLabel(mapExport)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.composerSelect = QtGui.QComboBox(mapExport)
        self.composerSelect.setObjectName(_fromUtf8("composerSelect"))
        self.gridLayout.addWidget(self.composerSelect, 2, 0, 1, 2)

        self.retranslateUi(mapExport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), mapExport.reject)
        QtCore.QMetaObject.connectSlotsByName(mapExport)
        mapExport.setTabOrder(self.path, self.browser)
        mapExport.setTabOrder(self.browser, self.exportButton)
        mapExport.setTabOrder(self.exportButton, self.buttonBox)

    def retranslateUi(self, mapExport):
        mapExport.setWindowTitle(_translate("mapExport", "Map Export", None))
        self.label_2.setText(_translate("mapExport", "Select export folder:", None))
        self.exportButton.setText(_translate("mapExport", "Export", None))
        self.browser.setToolTip(_translate("mapExport", "Choose the output folder", None))
        self.browser.setText(_translate("mapExport", "Br&owse...", None))
        self.textBrowser.setHtml(_translate("mapExport", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">MapAction MapExport</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select a Print Composer, and an export folder, then click Export.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The plugin will</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- create a new folder in your export folder (if it doesn\'t exist), with the same name as the Print Composer</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- export the Print Composer as a PDF and JPG, again with the same name</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- create a zip in the export folder, with the same name, containing the exported files, with the metadata XML if it has been created </p></body></html>", None))
        self.label.setText(_translate("mapExport", "Select Print Composer:", None))

