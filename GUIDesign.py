# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIDesign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(980, 730)
        MainWindow.setMinimumSize(QtCore.QSize(980, 730))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 730))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/icons-smile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 550, 681, 101))
        self.groupBox.setMinimumSize(QtCore.QSize(681, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.button_CaptureAnalyse = QtWidgets.QPushButton(self.groupBox)
        self.button_CaptureAnalyse.setGeometry(QtCore.QRect(20, 20, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        self.button_CaptureAnalyse.setFont(font)
        self.button_CaptureAnalyse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_CaptureAnalyse.setMouseTracking(False)
        self.button_CaptureAnalyse.setAutoFillBackground(False)
        self.button_CaptureAnalyse.setStyleSheet("border:none;\n"
"color:gray;\n"
"font-size:12px;\n"
"height:40px;\n"
"padding-left:5px;\n"
"padding-right:10px;")
        self.button_CaptureAnalyse.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/icons8-FaceAnalyse-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_CaptureAnalyse.setIcon(icon1)
        self.button_CaptureAnalyse.setIconSize(QtCore.QSize(64, 64))
        self.button_CaptureAnalyse.setObjectName("button_CaptureAnalyse")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(100, 20, 20, 71))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radioButton_NormalImage = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_NormalImage.setGeometry(QtCore.QRect(150, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_NormalImage.setFont(font)
        self.radioButton_NormalImage.setObjectName("radioButton_NormalImage")
        self.radioButton_FaceTract = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_FaceTract.setGeometry(QtCore.QRect(340, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_FaceTract.setFont(font)
        self.radioButton_FaceTract.setObjectName("radioButton_FaceTract")
        self.radioButton_EdgeTract = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_EdgeTract.setGeometry(QtCore.QRect(540, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_EdgeTract.setFont(font)
        self.radioButton_EdgeTract.setObjectName("radioButton_EdgeTract")
        self.horizontalSlider_EdgeTract = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_EdgeTract.setGeometry(QtCore.QRect(510, 60, 160, 22))
        self.horizontalSlider_EdgeTract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalSlider_EdgeTract.setMinimum(51)
        self.horizontalSlider_EdgeTract.setMaximum(500)
        self.horizontalSlider_EdgeTract.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_EdgeTract.setObjectName("horizontalSlider_EdgeTract")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(11, 11, 681, 531))
        self.groupBox_2.setMinimumSize(QtCore.QSize(661, 391))
        self.groupBox_2.setMaximumSize(QtCore.QSize(1920, 1080))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_ShowCamera = QtWidgets.QLabel(self.groupBox_2)
        self.label_ShowCamera.setGeometry(QtCore.QRect(10, 20, 660, 495))
        self.label_ShowCamera.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_ShowCamera.setText("")
        self.label_ShowCamera.setPixmap(QtGui.QPixmap("background.png"))
        self.label_ShowCamera.setObjectName("label_ShowCamera")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(700, 10, 271, 531))
        self.groupBox_3.setMinimumSize(QtCore.QSize(270, 390))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_Report = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_Report.setGeometry(QtCore.QRect(20, 140, 241, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_Report.setFont(font)
        self.textEdit_Report.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_Report.setObjectName("textEdit_Report")
        self.label_SelectGender = QtWidgets.QLabel(self.groupBox_3)
        self.label_SelectGender.setGeometry(QtCore.QRect(20, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_SelectGender.setFont(font)
        self.label_SelectGender.setObjectName("label_SelectGender")
        self.radioButton_Male = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_Male.setGeometry(QtCore.QRect(120, 65, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_Male.setFont(font)
        self.radioButton_Male.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.radioButton_Female = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_Female.setGeometry(QtCore.QRect(190, 65, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_Female.setFont(font)
        self.radioButton_Female.setIconSize(QtCore.QSize(32, 32))
        self.radioButton_Female.setObjectName("radioButton_Female")
        self.label_UserName = QtWidgets.QLabel(self.groupBox_3)
        self.label_UserName.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_UserName.setFont(font)
        self.label_UserName.setObjectName("label_UserName")
        self.label_ReportOutput = QtWidgets.QLabel(self.groupBox_3)
        self.label_ReportOutput.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ReportOutput.setFont(font)
        self.label_ReportOutput.setObjectName("label_ReportOutput")
        self.button_SaveReport = QtWidgets.QPushButton(self.groupBox_3)
        self.button_SaveReport.setGeometry(QtCore.QRect(120, 90, 48, 48))
        self.button_SaveReport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_SaveReport.setStyleSheet("border:none;\n"
"color:gray;\n"
"font-size:12px;\n"
"height:40px;\n"
"padding-left:5px;\n"
"padding-right:10px;")
        self.button_SaveReport.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/icons8-save-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_SaveReport.setIcon(icon2)
        self.button_SaveReport.setIconSize(QtCore.QSize(48, 48))
        self.button_SaveReport.setObjectName("button_SaveReport")
        self.lineEdit_UserName = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_UserName.setGeometry(QtCore.QRect(120, 19, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEdit_UserName.setFont(font)
        self.lineEdit_UserName.setObjectName("lineEdit_UserName")
        self.label_SJTUlogo = QtWidgets.QLabel(self.centralwidget)
        self.label_SJTUlogo.setGeometry(QtCore.QRect(700, 550, 271, 91))
        self.label_SJTUlogo.setMinimumSize(QtCore.QSize(271, 91))
        self.label_SJTUlogo.setText("")
        self.label_SJTUlogo.setPixmap(QtGui.QPixmap("icon/SJTUlogo.png"))
        self.label_SJTUlogo.setObjectName("label_SJTUlogo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/icons8-OpenImage-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenImage.setIcon(icon3)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionOpenCamera = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/icons8-OpenCamera-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenCamera.setIcon(icon4)
        self.actionOpenCamera.setObjectName("actionOpenCamera")
        self.actionCloseCamera = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/icons8-CloseCamera-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseCamera.setIcon(icon5)
        self.actionCloseCamera.setObjectName("actionCloseCamera")
        self.actionClearImage = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/icons8-closewindow-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearImage.setIcon(icon6)
        self.actionClearImage.setObjectName("actionClearImage")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.toolBar.addAction(self.actionOpenImage)
        self.toolBar.addAction(self.actionOpenCamera)
        self.toolBar.addAction(self.actionCloseCamera)
        self.toolBar.addAction(self.actionClearImage)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Facial health"))
        self.radioButton_NormalImage.setText(_translate("MainWindow", "正常图像"))
        self.radioButton_FaceTract.setText(_translate("MainWindow", "人脸捕捉"))
        self.radioButton_EdgeTract.setText(_translate("MainWindow", "边缘检测"))
        self.label_SelectGender.setText(_translate("MainWindow", "选择性别："))
        self.radioButton_Male.setText(_translate("MainWindow", "男"))
        self.radioButton_Female.setText(_translate("MainWindow", "女"))
        self.label_UserName.setText(_translate("MainWindow", "输入姓名："))
        self.label_ReportOutput.setText(_translate("MainWindow", "报告生成："))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenImage.setText(_translate("MainWindow", "OpenImage"))
        self.actionOpenImage.setToolTip(_translate("MainWindow", "打开图像"))
        self.actionOpenCamera.setText(_translate("MainWindow", "OpenCamera"))
        self.actionOpenCamera.setToolTip(_translate("MainWindow", "打开摄像头"))
        self.actionCloseCamera.setText(_translate("MainWindow", "CloseCamera"))
        self.actionCloseCamera.setToolTip(_translate("MainWindow", "关闭摄像头"))
        self.actionClearImage.setText(_translate("MainWindow", "ClearImage"))
        self.actionClearImage.setToolTip(_translate("MainWindow", "删除图窗内容"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "保存报告"))