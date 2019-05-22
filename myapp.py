import wx
import os
from importlib import reload
import webbrowser
import face_img_register
import face_recognize
import sys

main = "icon/main.png"
file_path = os.getcwd() + r'\data\logcat.csv'


class Mainui(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title="智能访客系统", size=(800, 590))
        self.SetBackgroundColour('white')
        self.Center()

        self.frame = ''
        self.RegisterButton = wx.Button(parent=self, pos=(50, 120), size=(80, 50), label='人脸注册')

        self.RecognizeButton = wx.Button(parent=self, pos=(50, 220), size=(80, 50), label='人脸识别')

        self.LogcatButton = wx.Button(parent=self, pos=(50, 320), size=(80, 50), label='日志查看')

        self.Bind(wx.EVT_BUTTON, self.OnRegisterButtonClicked, self.RegisterButton)
        self.Bind(wx.EVT_BUTTON, self.OnRecognizeButtonClicked, self.RecognizeButton)
        self.Bind(wx.EVT_BUTTON, self.OnLogcatButtonClicked, self.LogcatButton)

        # 封面图片
        self.image_cover = wx.Image(main, wx.BITMAP_TYPE_ANY).Scale(520, 360)
        # 显示图片
        self.bmp = wx.StaticBitmap(parent=self, pos=(180, 80), bitmap=wx.Bitmap(self.image_cover))

    def OnRegisterButtonClicked(self, event):
        reload(face_img_register)
        app.frame = face_img_register.RegisterUi(None)
        app.frame.Show()

    def OnRecognizeButtonClicked(self, event):
        reload(face_recognize)
        app.frame = face_recognize.RecognizeUi(None)
        app.frame.Show()

    def OnLogcatButtonClicked(self, event):
        if os.path.exists(file_path):
            # 调用系统默认程序打开文件
            os.startfile(file_path)
        else:
            wx.MessageBox(message="要先运行过一次人脸识别系统，才有日志", caption="警告")
        pass


class MainApp(wx.App):
    def OnInit(self):
        self.frame = Mainui(None)
        self.frame.Show()
        return True


app = MainApp()
app.MainLoop()
