# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\git\softmech\nanoindentation\nano.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 917)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.b_load = QtWidgets.QPushButton(self.groupBox_7)
        self.b_load.setObjectName("b_load")
        self.verticalLayout_10.addWidget(self.b_load)
        self.b_protocol = QtWidgets.QPushButton(self.groupBox_7)
        self.b_protocol.setObjectName("b_protocol")
        self.verticalLayout_10.addWidget(self.b_protocol)
        self.consolle = QtWidgets.QPushButton(self.groupBox_7)
        self.consolle.setObjectName("consolle")
        self.verticalLayout_10.addWidget(self.consolle)
        self.horizontalLayout_9.addWidget(self.groupBox_7)
        spacerItem = QtWidgets.QSpacerItem(1110, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.b_saveexperiment = QtWidgets.QPushButton(self.groupBox_8)
        self.b_saveexperiment.setObjectName("b_saveexperiment")
        self.verticalLayout_11.addWidget(self.b_saveexperiment)
        self.b_saveFdata = QtWidgets.QPushButton(self.groupBox_8)
        self.b_saveFdata.setObjectName("b_saveFdata")
        self.verticalLayout_11.addWidget(self.b_saveFdata)
        self.b_saveEdata = QtWidgets.QPushButton(self.groupBox_8)
        self.b_saveEdata.setObjectName("b_saveEdata")
        self.verticalLayout_11.addWidget(self.b_saveEdata)
        self.b_saveprotocol = QtWidgets.QPushButton(self.groupBox_8)
        self.b_saveprotocol.setObjectName("b_saveprotocol")
        self.verticalLayout_11.addWidget(self.b_saveprotocol)
        self.horizontalLayout_9.addWidget(self.groupBox_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.g_fz_all = PlotWidget(self.layoutWidget)
        self.g_fz_all.setObjectName("g_fz_all")
        self.verticalLayout.addWidget(self.g_fz_all)
        self.g_fz_single = PlotWidget(self.layoutWidget)
        self.g_fz_single.setObjectName("g_fz_single")
        self.verticalLayout.addWidget(self.g_fz_single)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.g_fizi_all = PlotWidget(self.layoutWidget1)
        self.g_fizi_all.setObjectName("g_fizi_all")
        self.verticalLayout_2.addWidget(self.g_fizi_all)
        self.g_fizi_single = PlotWidget(self.layoutWidget1)
        self.g_fizi_single.setEnabled(True)
        self.g_fizi_single.setInteractive(True)
        self.g_fizi_single.setObjectName("g_fizi_single")
        self.verticalLayout_2.addWidget(self.g_fizi_single)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.es_interpolate = QtWidgets.QCheckBox(self.layoutWidget2)
        self.es_interpolate.setText("")
        self.es_interpolate.setChecked(True)
        self.es_interpolate.setObjectName("es_interpolate")
        self.horizontalLayout_3.addWidget(self.es_interpolate)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.es_win = QtWidgets.QSpinBox(self.layoutWidget2)
        self.es_win.setMinimum(3)
        self.es_win.setMaximum(9999)
        self.es_win.setProperty("value", 21)
        self.es_win.setObjectName("es_win")
        self.horizontalLayout_2.addWidget(self.es_win)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.es_order = QtWidgets.QSpinBox(self.layoutWidget2)
        self.es_order.setMinimum(1)
        self.es_order.setMaximum(9)
        self.es_order.setProperty("value", 3)
        self.es_order.setObjectName("es_order")
        self.horizontalLayout.addWidget(self.es_order)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.g_eze_all = PlotWidget(self.layoutWidget2)
        self.g_eze_all.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        self.g_eze_all.setFont(font)
        self.g_eze_all.setAcceptDrops(True)
        self.g_eze_all.setInteractive(True)
        self.g_eze_all.setObjectName("g_eze_all")
        self.verticalLayout_3.addWidget(self.g_eze_all)
        self.g_eze_single = PlotWidget(self.layoutWidget2)
        self.g_eze_single.setEnabled(True)
        self.g_eze_single.setObjectName("g_eze_single")
        self.verticalLayout_3.addWidget(self.g_eze_single)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.g_scatter1 = PlotWidget(self.layoutWidget3)
        self.g_scatter1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_scatter1.sizePolicy().hasHeightForWidth())
        self.g_scatter1.setSizePolicy(sizePolicy)
        self.g_scatter1.setLineWidth(0)
        self.g_scatter1.setMidLineWidth(0)
        self.g_scatter1.setAlignment(QtCore.Qt.AlignCenter)
        self.g_scatter1.setObjectName("g_scatter1")
        self.verticalLayout_8.addWidget(self.g_scatter1)
        self.g_scatter2 = PlotWidget(self.layoutWidget3)
        self.g_scatter2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_scatter2.sizePolicy().hasHeightForWidth())
        self.g_scatter2.setSizePolicy(sizePolicy)
        self.g_scatter2.setLineWidth(0)
        self.g_scatter2.setMidLineWidth(0)
        self.g_scatter2.setAlignment(QtCore.Qt.AlignCenter)
        self.g_scatter2.setObjectName("g_scatter2")
        self.verticalLayout_8.addWidget(self.g_scatter2)
        self.verticalLayout_9.addWidget(self.splitter)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sel_filter = QtWidgets.QComboBox(self.groupBox_5)
        self.sel_filter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_filter.setAutoFillBackground(False)
        self.sel_filter.setFrame(True)
        self.sel_filter.setObjectName("sel_filter")
        self.sel_filter.addItem("")
        self.verticalLayout_5.addWidget(self.sel_filter)
        self.tabfilters = QtWidgets.QTabWidget(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabfilters.sizePolicy().hasHeightForWidth())
        self.tabfilters.setSizePolicy(sizePolicy)
        self.tabfilters.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabfilters.setUsesScrollButtons(True)
        self.tabfilters.setDocumentMode(False)
        self.tabfilters.setTabsClosable(True)
        self.tabfilters.setMovable(True)
        self.tabfilters.setTabBarAutoHide(False)
        self.tabfilters.setObjectName("tabfilters")
        self.verticalLayout_5.addWidget(self.tabfilters)
        self.horizontalLayout_5.addWidget(self.groupBox_5)
        self.boxCP = QtWidgets.QGroupBox(self.centralwidget)
        self.boxCP.setObjectName("boxCP")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.boxCP)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sel_cp = QtWidgets.QComboBox(self.boxCP)
        self.sel_cp.setObjectName("sel_cp")
        self.sel_cp.addItem("")
        self.verticalLayout_4.addWidget(self.sel_cp)
        self.box_cp = QtWidgets.QGroupBox(self.boxCP)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_cp.sizePolicy().hasHeightForWidth())
        self.box_cp.setSizePolicy(sizePolicy)
        self.box_cp.setObjectName("box_cp")
        self.verticalLayout_4.addWidget(self.box_cp)
        self.setZeroForce = QtWidgets.QCheckBox(self.boxCP)
        self.setZeroForce.setChecked(True)
        self.setZeroForce.setObjectName("setZeroForce")
        self.verticalLayout_4.addWidget(self.setZeroForce)
        self.horizontalLayout_5.addWidget(self.boxCP)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sel_fmodel = QtWidgets.QComboBox(self.groupBox_10)
        self.sel_fmodel.setObjectName("sel_fmodel")
        self.sel_fmodel.addItem("")
        self.verticalLayout_6.addWidget(self.sel_fmodel)
        self.box_fmodel = QtWidgets.QGroupBox(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_fmodel.sizePolicy().hasHeightForWidth())
        self.box_fmodel.setSizePolicy(sizePolicy)
        self.box_fmodel.setObjectName("box_fmodel")
        self.verticalLayout_6.addWidget(self.box_fmodel)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox_10)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.zi_min = QtWidgets.QSpinBox(self.groupBox_10)
        self.zi_min.setMinimum(0)
        self.zi_min.setMaximum(9999)
        self.zi_min.setProperty("value", 0)
        self.zi_min.setObjectName("zi_min")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zi_min)
        self.label_11 = QtWidgets.QLabel(self.groupBox_10)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.zi_max = QtWidgets.QSpinBox(self.groupBox_10)
        self.zi_max.setMinimum(0)
        self.zi_max.setMaximum(9999)
        self.zi_max.setProperty("value", 800)
        self.zi_max.setObjectName("zi_max")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.zi_max)
        self.verticalLayout_6.addLayout(self.formLayout)
        self.horizontalLayout_6.addWidget(self.groupBox_10)
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.sel_emodel = QtWidgets.QComboBox(self.groupBox_11)
        self.sel_emodel.setObjectName("sel_emodel")
        self.sel_emodel.addItem("")
        self.verticalLayout_7.addWidget(self.sel_emodel)
        self.box_emodel = QtWidgets.QGroupBox(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_emodel.sizePolicy().hasHeightForWidth())
        self.box_emodel.setSizePolicy(sizePolicy)
        self.box_emodel.setObjectName("box_emodel")
        self.verticalLayout_7.addWidget(self.box_emodel)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.groupBox_11)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.ze_min = QtWidgets.QSpinBox(self.groupBox_11)
        self.ze_min.setMinimum(0)
        self.ze_min.setMaximum(9999)
        self.ze_min.setProperty("value", 0)
        self.ze_min.setObjectName("ze_min")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ze_min)
        self.label_14 = QtWidgets.QLabel(self.groupBox_11)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.ze_max = QtWidgets.QSpinBox(self.groupBox_11)
        self.ze_max.setMinimum(0)
        self.ze_max.setMaximum(9999)
        self.ze_max.setProperty("value", 800)
        self.ze_max.setObjectName("ze_max")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ze_max)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.horizontalLayout_6.addWidget(self.groupBox_11)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.f_params = QtWidgets.QGroupBox(self.centralwidget)
        self.f_params.setObjectName("f_params")
        self.horizontalLayout_7.addWidget(self.f_params)
        self.e_params = QtWidgets.QGroupBox(self.centralwidget)
        self.e_params.setObjectName("e_params")
        self.horizontalLayout_7.addWidget(self.e_params)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.groupBox_9)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.slid_cv = QtWidgets.QSlider(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slid_cv.sizePolicy().hasHeightForWidth())
        self.slid_cv.setSizePolicy(sizePolicy)
        self.slid_cv.setOrientation(QtCore.Qt.Horizontal)
        self.slid_cv.setObjectName("slid_cv")
        self.verticalLayout_12.addWidget(self.slid_cv)
        self.label_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.slid_alpha = QtWidgets.QSlider(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slid_alpha.sizePolicy().hasHeightForWidth())
        self.slid_alpha.setSizePolicy(sizePolicy)
        self.slid_alpha.setMaximum(255)
        self.slid_alpha.setSingleStep(1)
        self.slid_alpha.setProperty("value", 100)
        self.slid_alpha.setOrientation(QtCore.Qt.Horizontal)
        self.slid_alpha.setObjectName("slid_alpha")
        self.verticalLayout_12.addWidget(self.slid_alpha)
        self.horizontalLayout_8.addWidget(self.groupBox_9)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabfilters.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SoftMech2021"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Load"))
        self.b_load.setText(_translate("MainWindow", "Load experiment"))
        self.b_protocol.setText(_translate("MainWindow", "Load protocol"))
        self.consolle.setText(_translate("MainWindow", "Consolle"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Save"))
        self.b_saveexperiment.setText(_translate("MainWindow", "Save experiment"))
        self.b_saveFdata.setText(_translate("MainWindow", "Save Indentation Analysis"))
        self.b_saveEdata.setText(_translate("MainWindow", "Save Elastography analysis"))
        self.b_saveprotocol.setText(_translate("MainWindow", "Save protocol"))
        self.label_13.setText(_translate("MainWindow", "Interpolate"))
        self.label_8.setText(_translate("MainWindow", "Window"))
        self.label_21.setText(_translate("MainWindow", "Order"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Filters"))
        self.sel_filter.setItemText(0, _translate("MainWindow", "-- add --"))
        self.boxCP.setTitle(_translate("MainWindow", "Contact Point "))
        self.sel_cp.setItemText(0, _translate("MainWindow", "-- none --"))
        self.setZeroForce.setText(_translate("MainWindow", "Set CP force to 0"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Force-ind model"))
        self.sel_fmodel.setItemText(0, _translate("MainWindow", "-- none --"))
        self.label_9.setText(_translate("MainWindow", "Min ind [nm]"))
        self.label_11.setText(_translate("MainWindow", "Max ind [nm]"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Elasticity Spectra model"))
        self.sel_emodel.setItemText(0, _translate("MainWindow", "-- none --"))
        self.label_12.setText(_translate("MainWindow", "Min ind [nm]"))
        self.label_14.setText(_translate("MainWindow", "Max ind [nm]"))
        self.f_params.setTitle(_translate("MainWindow", "Force-ind model params"))
        self.e_params.setTitle(_translate("MainWindow", "Elasticity Spectra model params"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Sliders"))
        self.label.setText(_translate("MainWindow", "Slide through curves"))
        self.label_2.setText(_translate("MainWindow", "Trasnparency "))
from pyqtgraph import PlotWidget
