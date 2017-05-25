import wx

APP_EXIT = 1

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(500, 400))
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self, -1)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        quitMI = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')

        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')

        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import blah...')
        imp.Append(wx.ID_ANY, 'Import yes...')

        fileMenu.Append(wx.ID_ANY, '&Test', imp)

        fileMenu.Append(quitMI)

        menubar.Append(fileMenu, '&File')

        txtCtrl = wx.TextCtrl(panel, pos=(50,50), size=(100,20))
        btn = wx.Button(panel, label='Search', pos=(150, 48))
        
        btn.Bind(wx.EVT_BUTTON, self.PrintText)

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        self.SetSize((400, 400))
        self.Center()
        self.Show()

    def PrintText(self, e):
        print(txtCtrl.GetValue())

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    Example(None, 'Testestest')
    app.MainLoop()


if(__name__ == '__main__'):
    main()
