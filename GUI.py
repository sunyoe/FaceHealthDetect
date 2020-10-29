import cv2
import copy
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtCore import QDir,pyqtSlot
from GUIDesign import *
from faceHealthDetect import *
# from faceTest import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.CameraTimer = QtCore.QTimer()
        #摄像头
        self.CAM_NUM = 0
        self.Flag_Image = 0 #0表示无图像，1表示开启摄像头读取图像，2表示打开图像文件

        #信息区
        self.UserName = ""
        self.Gender = -1
        self.report = "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest"
        self.faceColor = ""
        self.faceGloss = ""

        #图像区
        self.VideoMode = 0#定义图像输出模式
        self.EdgeTractThrehold1 = 50
        self.EdgeTractThrehold2 = self.EdgeTractThrehold1+200
        self.VideoFlag = 0


        self.setupUi(self)
        self.slot_init()


    def slot_init(self):
        self.button_CaptureAnalyse.clicked.connect(self.Analyze)
        self.button_SaveReport.clicked.connect(self.SaveReport)
        self.CameraTimer.timeout.connect(self.ShowCamera)#每次倒计时溢出，调用函数刷新页面
        self.actionOpenImage.triggered.connect(self.OpenImage)
        self.actionOpenCamera.triggered.connect(self.OpenCamera)
        self.actionCloseCamera.triggered.connect(self.CloseCamera)
        self.actionClearImage.triggered.connect(self.ClearImage)
        self.horizontalSlider_EdgeTract.valueChanged.connect(self.SliderChangeValue)

    def OpenCamera(self):#打开摄像头，启动倒计时
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 后一个参数用来消一个奇怪的warn
        if self.CameraTimer.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                QtWidgets.QMessageBox.warning(self,'warning',"请检查摄像头与电脑是否连接正确",buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.CameraTimer.start(30)
                self.Flag_Image = 1
        else:
            self.CameraTimer.stop()
            self.cap.release()
            self.label_ShowCamera.clear()

    def ShowCamera(self):
        self.VideoFlag = 0
        if self.radioButton_NormalImage.isChecked():
            self.VideoMode = 0
        elif self.radioButton_EdgeTract.isChecked():
            self.VideoMode = 2
        elif self.radioButton_FaceTract.isChecked():
            self.VideoMode = 1

        flag, self.image = self.cap.read()

        if self.VideoMode == 0:
            ShowVideo = cv2.resize(self.image, (660, 495))
        elif self.VideoMode == 1:
            if self.VideoFlag == 0:
                ShowVideo = faceDetect(self.image, self.VideoFlag)
        elif self.VideoMode == 2:
            self.edge = cv2.Canny(self.image,self.EdgeTractThrehold1,self.EdgeTractThrehold2)
            ShowVideo = cv2.resize(self.edge, (660,495))

        ShowVideo = cv2.cvtColor(ShowVideo, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(ShowVideo.data, ShowVideo.shape[1], ShowVideo.shape[0],
                                 QtGui.QImage.Format_RGB888)
        self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def CloseCamera(self):
        self.CameraTimer.stop()
        self.cap.release()
        self.label_ShowCamera.clear()
        self.label_ShowCamera.setPixmap(QtGui.QPixmap("background.png"))
        self.Flag_Image = 0

    def Analyze(self):#要思考未打开摄像头时按下“拍照”的问题
        self.VideoFlag = 1
        self.UserName = self.lineEdit_UserName.text()
        if self.radioButton_Male.isChecked():
            self.Gender = 1
        elif self.radioButton_Female.isChecked():
            self.Gender = 0

        if self.Gender == -1 and self.UserName == "":
            QtWidgets.QMessageBox.warning(self, 'warning', "请输入姓名和选择性别", buttons=QtWidgets.QMessageBox.Ok)
        elif self.Gender == -1 and self.UserName != "":
            QtWidgets.QMessageBox.warning(self, 'warning', "请选择性别", buttons=QtWidgets.QMessageBox.Ok)
        elif self.Gender != -1 and self.UserName == "":
            QtWidgets.QMessageBox.warning(self, 'warning', "请输入姓名", buttons=QtWidgets.QMessageBox.Ok)
        else:
            if self.Flag_Image == 0:
                QtWidgets.QMessageBox.warning(self, 'warning', "无图像输入")
            else:
                if self.Flag_Image == 1:
                    self.Flag_Image = 0
                    # flag, self.image = self.cap.read()

                    self.faceColor, self.faceGloss, self.image = faceDetect(self.image, self.VideoFlag)
                    # print(self.faceColor, self.faceGloss)

                    ShowCapture = cv2.resize(self.image, (660,495))
                    ShowCapture = cv2.cvtColor(ShowCapture, cv2.COLOR_BGR2RGB)
                    showImage = QtGui.QImage(ShowCapture.data, ShowCapture.shape[1], ShowCapture.shape[0],
                                            QtGui.QImage.Format_RGB888)
                    self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))
                    self.CameraTimer.stop()
                elif self.Flag_Image == 2:
                    self.Flag_Image = 0
                    self.faceColor, self.faceGloss, self.image = faceDetect(self.image, self.VideoFlag)
                    ShowCapture = cv2.resize(self.image, (660,495))
                    ShowCapture = cv2.cvtColor(ShowCapture, cv2.COLOR_BGR2RGB)
                    showImage = QtGui.QImage(ShowCapture.data, ShowCapture.shape[1], ShowCapture.shape[0],
                                            QtGui.QImage.Format_RGB888)
                    self.label_ShowCamera.setPixmap(QtGui.QPixmap.fromImage(showImage))

            # 根据人脸检测情况和人员信息，生成诊断结果
            SkinResults, GlossResults = CreateDetectResults(self.faceColor, self.faceGloss)
            # pdfCreate(filename, name, sex, faceColor, faceGloss, SkinResults, GlossResults)
            image = "DiagnoseResult.jpg"
            wordCreate(self.UserName, self.Gender, self.faceColor, self.faceGloss, SkinResults, GlossResults, image)
            # 生成PDF报告
            wordfile = "D:\GitDoc\FaceHealthDetect\FaceDiagnoseResults.docx"
            pdffile = "D:\GitDoc\FaceHealthDetect\FaceDiagnoseResults.pdf"
            word2pdf(wordfile, pdffile)

            if self.Gender == 0 : gender = "女"
            if self.Gender == 1 : gender = "男"
            self.report = "姓名: %s \n" %self.UserName + "性别: %s \n" %gender + \
                "您的面部诊断结果: \n" + "    肤色诊断结果: %s \n" %self.faceColor + "    皮肤光泽诊断结果: %s \n" %self.faceGloss + \
                "诊断结果分析: \n %s \n" %SkinResults + "    %s" %GlossResults
            self.textEdit_Report.setPlainText(self.report)

    def OpenImage(self):#打开已有文件
        curPath = QDir.currentPath()
        imagePath,imgType = QFileDialog.getOpenFileName(self,"打开图片",curPath," *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        print(imagePath)
        img = QtGui.QPixmap(imagePath).scaled(self.label_ShowCamera.width(), self.label_ShowCamera.height())
        self.image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
        self.label_ShowCamera.setPixmap(img)
        self.Flag_Image = 2

    def ClearImage(self):
        if self.Flag_Image == 1:
            self.CameraTimer.stop()
            self.cap.release()
            self.label_ShowCamera.clear()
            self.textEdit_Report.clear()
            self.Flag_Image = 0
        else:
            self.textEdit_Report.clear()
        self.textEdit_Report.clear()

    def SliderChangeValue(self):
        self.EdgeTractThrehold1 = self.horizontalSlider_EdgeTract.value()

    def SaveReport(self):
        self.textEdit_Report.setPlainText("已保存")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())