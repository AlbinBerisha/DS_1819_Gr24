import socket
import tkinter
from tkinter import *

class ClientTk(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.display = True

        self.title("Klienti")
        self.geometry("240x240")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.onClose)

        client = Client()
        loginFrame = LoginFrame(self, client)

        while self.display:
            self.update_idletasks()
            self.update()

            if client.messageSent:
            	(returdedData, address) = client.receiveData()
            	client.messageSent = False

    def onClose(self):
        self.display = False
        self.destroy()

class LoginFrame(Frame):
    def __init__(self, parent, client):
        Frame.__init__(self, parent)
        self.pack(fill = BOTH, expand = 1)

        self.button = Button(self, text = "Click Me!")
        self.button.pack()