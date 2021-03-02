# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\git\softmech\nano.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 897)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\git\\softmech\\../../.designer/backup/ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_load = QtWidgets.QPushButton(self.centralwidget)
        self.b_load.setGeometry(QtCore.QRect(770, 10, 121, 24))
        self.b_load.setObjectName("b_load")
        self.b_protocol = QtWidgets.QPushButton(self.centralwidget)
        self.b_protocol.setGeometry(QtCore.QRect(770, 40, 121, 24))
        self.b_protocol.setObjectName("b_protocol")
        self.b_save = QtWidgets.QPushButton(self.centralwidget)
        self.b_save.setGeometry(QtCore.QRect(920, 20, 121, 24))
        self.b_save.setObjectName("b_save")
        self.b_saveprotocol = QtWidgets.QPushButton(self.centralwidget)
        self.b_saveprotocol.setGeometry(QtCore.QRect(920, 60, 121, 24))
        self.b_saveprotocol.setObjectName("b_saveprotocol")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setEnabled(True)
        self.groupBox_6.setGeometry(QtCore.QRect(1160, 20, 128, 108))
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.es_win = QtWidgets.QSpinBox(self.groupBox_6)
        self.es_win.setMinimum(3)
        self.es_win.setMaximum(9999)
        self.es_win.setProperty("value", 21)
        self.es_win.setObjectName("es_win")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.es_win)
        self.label_21 = QtWidgets.QLabel(self.groupBox_6)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.es_order = QtWidgets.QSpinBox(self.groupBox_6)
        self.es_order.setMinimum(1)
        self.es_order.setMaximum(9)
        self.es_order.setProperty("value", 3)
        self.es_order.setObjectName("es_order")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.es_order)
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.es_interpolate = QtWidgets.QCheckBox(self.groupBox_6)
        self.es_interpolate.setText("")
        self.es_interpolate.setChecked(True)
        self.es_interpolate.setObjectName("es_interpolate")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.es_interpolate)
        self.slid_alpha = QtWidgets.QSlider(self.centralwidget)
        self.slid_alpha.setGeometry(QtCore.QRect(220, 40, 22, 84))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slid_alpha.sizePolicy().hasHeightForWidth())
        self.slid_alpha.setSizePolicy(sizePolicy)
        self.slid_alpha.setMaximum(255)
        self.slid_alpha.setSingleStep(1)
        self.slid_alpha.setProperty("value", 100)
        self.slid_alpha.setOrientation(QtCore.Qt.Vertical)
        self.slid_alpha.setObjectName("slid_alpha")
        self.g_fz_single = PlotWidget(self.centralwidget)
        self.g_fz_single.setGeometry(QtCore.QRect(35, 370, 441, 192))
        self.g_fz_single.setObjectName("g_fz_single")
        self.g_fz_all = PlotWidget(self.centralwidget)
        self.g_fz_all.setGeometry(QtCore.QRect(35, 150, 441, 192))
        self.g_fz_all.setObjectName("g_fz_all")
        self.boxCP = QtWidgets.QGroupBox(self.centralwidget)
        self.boxCP.setGeometry(QtCore.QRect(400, 580, 281, 261))
        self.boxCP.setObjectName("boxCP")
        self.sel_cp = QtWidgets.QComboBox(self.boxCP)
        self.sel_cp.setGeometry(QtCore.QRect(20, 30, 69, 22))
        self.sel_cp.setObjectName("sel_cp")
        self.sel_cp.addItem("")
        self.box_cp = QtWidgets.QGroupBox(self.boxCP)
        self.box_cp.setGeometry(QtCore.QRect(10, 60, 251, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_cp.sizePolicy().hasHeightForWidth())
        self.box_cp.setSizePolicy(sizePolicy)
        self.box_cp.setObjectName("box_cp")
        self.setZeroForce = QtWidgets.QCheckBox(self.boxCP)
        self.setZeroForce.setGeometry(QtCore.QRect(20, 230, 110, 20))
        self.setZeroForce.setChecked(True)
        self.setZeroForce.setObjectName("setZeroForce")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(268, 12, 194, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.view_all = QtWidgets.QRadioButton(self.groupBox)
        self.view_all.setStyleSheet("color: red;")
        self.view_all.setChecked(True)
        self.view_all.setObjectName("view_all")
        self.horizontalLayout_4.addWidget(self.view_all)
        self.view_active = QtWidgets.QRadioButton(self.groupBox)
        self.view_active.setObjectName("view_active")
        self.horizontalLayout_4.addWidget(self.view_active)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(468, 12, 245, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.toggle_excluded = QtWidgets.QRadioButton(self.groupBox_2)
        self.toggle_excluded.setStyleSheet("color: red;")
        self.toggle_excluded.setChecked(True)
        self.toggle_excluded.setObjectName("toggle_excluded")
        self.horizontalLayout_5.addWidget(self.toggle_excluded)
        self.toggle_activated = QtWidgets.QRadioButton(self.groupBox_2)
        self.toggle_activated.setObjectName("toggle_activated")
        self.horizontalLayout_5.addWidget(self.toggle_activated)
        self.g_fizi_all = PlotWidget(self.centralwidget)
        self.g_fizi_all.setGeometry(QtCore.QRect(490, 150, 182, 192))
        self.g_fizi_all.setObjectName("g_fizi_all")
        self.g_fizi_single = PlotWidget(self.centralwidget)
        self.g_fizi_single.setEnabled(True)
        self.g_fizi_single.setGeometry(QtCore.QRect(490, 370, 182, 192))
        self.g_fizi_single.setInteractive(True)
        self.g_fizi_single.setObjectName("g_fizi_single")
        self.g_eze_all = PlotWidget(self.centralwidget)
        self.g_eze_all.setEnabled(True)
        self.g_eze_all.setGeometry(QtCore.QRect(690, 150, 254, 192))
        font = QtGui.QFont()
        font.setBold(True)
        self.g_eze_all.setFont(font)
        self.g_eze_all.setAcceptDrops(True)
        self.g_eze_all.setInteractive(True)
        self.g_eze_all.setObjectName("g_eze_all")
        self.g_eze_single = PlotWidget(self.centralwidget)
        self.g_eze_single.setEnabled(True)
        self.g_eze_single.setGeometry(QtCore.QRect(690, 360, 254, 192))
        self.g_eze_single.setObjectName("g_eze_single")
        self.g_scatter1 = PlotWidget(self.centralwidget)
        self.g_scatter1.setEnabled(True)
        self.g_scatter1.setGeometry(QtCore.QRect(970, 196, 208, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_scatter1.sizePolicy().hasHeightForWidth())
        self.g_scatter1.setSizePolicy(sizePolicy)
        self.g_scatter1.setLineWidth(0)
        self.g_scatter1.setMidLineWidth(0)
        self.g_scatter1.setAlignment(QtCore.Qt.AlignCenter)
        self.g_scatter1.setObjectName("g_scatter1")
        self.slid_cv = QtWidgets.QSlider(self.centralwidget)
        self.slid_cv.setGeometry(QtCore.QRect(40, 90, 160, 22))
        self.slid_cv.setOrientation(QtCore.Qt.Horizontal)
        self.slid_cv.setObjectName("slid_cv")
        self.quickView = QtWidgets.QPushButton(self.centralwidget)
        self.quickView.setGeometry(QtCore.QRect(910, 780, 131, 24))
        self.quickView.setObjectName("quickView")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 570, 351, 291))
        self.groupBox_5.setObjectName("groupBox_5")
        self.sel_filter = QtWidgets.QComboBox(self.groupBox_5)
        self.sel_filter.setGeometry(QtCore.QRect(30, 20, 141, 22))
        self.sel_filter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sel_filter.setAutoFillBackground(False)
        self.sel_filter.setFrame(True)
        self.sel_filter.setObjectName("sel_filter")
        self.sel_filter.addItem("")
        self.tabfilters = QtWidgets.QTabWidget(self.groupBox_5)
        self.tabfilters.setGeometry(QtCore.QRect(20, 60, 301, 191))
        self.tabfilters.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabfilters.setUsesScrollButtons(True)
        self.tabfilters.setDocumentMode(False)
        self.tabfilters.setTabsClosable(True)
        self.tabfilters.setMovable(True)
        self.tabfilters.setTabBarAutoHide(False)
        self.tabfilters.setObjectName("tabfilters")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(720, 570, 151, 251))
        self.groupBox_10.setObjectName("groupBox_10")
        self.sel_fmodel = QtWidgets.QComboBox(self.groupBox_10)
        self.sel_fmodel.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.sel_fmodel.setObjectName("sel_fmodel")
        self.sel_fmodel.addItem("")
        self.box_fmodel = QtWidgets.QGroupBox(self.groupBox_10)
        self.box_fmodel.setGeometry(QtCore.QRect(10, 70, 131, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_fmodel.sizePolicy().hasHeightForWidth())
        self.box_fmodel.setSizePolicy(sizePolicy)
        self.box_fmodel.setObjectName("box_fmodel")
        self.widget = QtWidgets.QWidget(self.groupBox_10)
        self.widget.setGeometry(QtCore.QRect(20, 170, 96, 52))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.zi_min = QtWidgets.QSpinBox(self.widget)
        self.zi_min.setMinimum(0)
        self.zi_min.setMaximum(9999)
        self.zi_min.setProperty("value", 0)
        self.zi_min.setObjectName("zi_min")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.zi_min)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.zi_max = QtWidgets.QSpinBox(self.widget)
        self.zi_max.setMinimum(0)
        self.zi_max.setMaximum(9999)
        self.zi_max.setProperty("value", 800)
        self.zi_max.setObjectName("zi_max")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.zi_max)
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(1090, 580, 151, 221))
        self.groupBox_11.setObjectName("groupBox_11")
        self.sel_emodel = QtWidgets.QComboBox(self.groupBox_11)
        self.sel_emodel.setGeometry(QtCore.QRect(10, 30, 69, 22))
        self.sel_emodel.setObjectName("sel_emodel")
        self.sel_emodel.addItem("")
        self.box_emodel = QtWidgets.QGroupBox(self.groupBox_11)
        self.box_emodel.setGeometry(QtCore.QRect(10, 60, 131, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_emodel.sizePolicy().hasHeightForWidth())
        self.box_emodel.setSizePolicy(sizePolicy)
        self.box_emodel.setObjectName("box_emodel")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_11)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 140, 96, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.ze_min = QtWidgets.QSpinBox(self.layoutWidget)
        self.ze_min.setMinimum(0)
        self.ze_min.setMaximum(9999)
        self.ze_min.setProperty("value", 0)
        self.ze_min.setObjectName("ze_min")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ze_min)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.ze_max = QtWidgets.QSpinBox(self.layoutWidget)
        self.ze_max.setMinimum(0)
        self.ze_max.setMaximum(9999)
        self.ze_max.setProperty("value", 800)
        self.ze_max.setObjectName("ze_max")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ze_max)
        self.g_scatter2 = PlotWidget(self.centralwidget)
        self.g_scatter2.setEnabled(True)
        self.g_scatter2.setGeometry(QtCore.QRect(970, 410, 208, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_scatter2.sizePolicy().hasHeightForWidth())
        self.g_scatter2.setSizePolicy(sizePolicy)
        self.g_scatter2.setLineWidth(0)
        self.g_scatter2.setMidLineWidth(0)
        self.g_scatter2.setAlignment(QtCore.Qt.AlignCenter)
        self.g_scatter2.setObjectName("g_scatter2")
        self.data_1 = QtWidgets.QComboBox(self.centralwidget)
        self.data_1.setGeometry(QtCore.QRect(970, 150, 201, 22))
        self.data_1.setObjectName("data_1")
        self.data_1.addItem("")
        self.data_2 = QtWidgets.QComboBox(self.centralwidget)
        self.data_2.setGeometry(QtCore.QRect(1010, 370, 131, 22))
        self.data_2.setObjectName("data_2")
        self.data_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(297, 1574, 44, 22))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabfilters.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nano2021"))
        self.b_load.setText(_translate("MainWindow", "Load experiment"))
        self.b_protocol.setText(_translate("MainWindow", "Load protocol"))
        self.b_save.setText(_translate("MainWindow", "Save analysis"))
        self.b_saveprotocol.setText(_translate("MainWindow", "Save protocol"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Elasticity Spectra"))
        self.label_8.setText(_translate("MainWindow", "Window"))
        self.label_21.setText(_translate("MainWindow", "Order"))
        self.label_13.setText(_translate("MainWindow", "Interpolate"))
        self.boxCP.setTitle(_translate("MainWindow", "Contact Point "))
        self.sel_cp.setItemText(0, _translate("MainWindow", "-- none --"))
        self.setZeroForce.setText(_translate("MainWindow", "Set CP force to 0"))
        self.groupBox.setTitle(_translate("MainWindow", "View"))
        self.view_all.setText(_translate("MainWindow", "All"))
        self.view_active.setText(_translate("MainWindow", "Active"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Toggle"))
        self.toggle_excluded.setText(_translate("MainWindow", "Excluded"))
        self.toggle_activated.setText(_translate("MainWindow", "Activated"))
        self.quickView.setText(_translate("MainWindow", "Inspect"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Filters"))
        self.sel_filter.setItemText(0, _translate("MainWindow", "-- add --"))
        self.groupBox_10.setTitle(_translate("MainWindow", "FModel"))
        self.sel_fmodel.setItemText(0, _translate("MainWindow", "-- none --"))
        self.label_9.setText(_translate("MainWindow", "Min ind"))
        self.label_11.setText(_translate("MainWindow", "Max ind"))
        self.groupBox_11.setTitle(_translate("MainWindow", "EModel"))
        self.sel_emodel.setItemText(0, _translate("MainWindow", "-- none --"))
        self.label_12.setText(_translate("MainWindow", "Min ind"))
        self.label_14.setText(_translate("MainWindow", "Max ind"))
        self.data_1.setItemText(0, _translate("MainWindow", "-- add --"))
        self.data_2.setItemText(0, _translate("MainWindow", "-- add --"))
        self.label_10.setText(_translate("MainWindow", "Window"))
from pyqtgraph import PlotWidget
