import tkinter as tk
import time

attempt = 0


def grant():
    window.destroy()
    from Main_menu_GUI import main
    main()


def destroy():
    window.destroy()


def authenticate():
    global attempt
    uname = user_name_value.get()
    passwd = password_value.get()
    file = open('login.txt', 'r')
    strings = file.readlines()
    file.close()

    if uname == strings[0].strip() and passwd == strings[1].strip():
        res = "Access Granted"
        message.configure(text=res)
        grant()

    else:
        attempt = attempt + 1
        res = "Access Denied"
        message.configure(text=res)

    if attempt > 3:
        window.destroy()
        attempt = 0
        update()


def update():
    class ExampleApp(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

            self.overrideredirect(True)
            self.label = tk.Label(self, text="", width="20", height="10")
            self.label.pack()
            self.remaining = 0
            self.countdown(10)

        def countdown(self, remaining=None):
            if remaining is not None:
                self.remaining = remaining

            if self.remaining <= 0:
                self.label.configure(text="time's up!")
                app.destroy()
            else:
                self.label.configure(text="LOGIN INCORRECT" + "\n\n" + " Wait for %d seconds" % self.remaining)
                self.remaining = self.remaining - 1

                self.remaining = self.remaining - 1
                self.after(1000, self.countdown)

    if __name__ == "__main__":
        app = ExampleApp()
        app.mainloop()


def exit():
    global attempt
    attempt = 10
    window.destroy()


while attempt <= 3:
    window = tk.Tk()
    window.overrideredirect(True)
    window.resizable(0, 0)
    window.title("FACE RECOGNITION SYSTEM")
    window.geometry('640x480')
    window.configure(background='black')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    message_head = tk.Label(window, text="FACE RECOGNITION SYSTEM", bg="black", fg="white", width=25, height=3,
                            font=('times', 20, 'bold'))
    message_head.place(x=130, y=10)
    message_head1 = tk.Label(window, text="Please log in to proceed!!", bg="black", fg="white", width=25, height=3,
                             font=('times', 12, 'bold'))
    message_head1.place(x=200, y=90)
    user_name_label = tk.Label(window, text="Username", width=10, height=1, bg="black", fg="white",
                               font=('times', 18, ' bold '))
    user_name_label.place(x=150, y=150)
    user_name_value = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
    user_name_value.place(x=330, y=150)
    password_label = tk.Label(window, text="Password", width=10, fg="white", bg="black", height=1,
                              font=('times', 18, ' bold '))
    password_label.place(x=150, y=200)
    password_value = tk.Entry(window, width=20, bg="white", fg="black", show="*", font=('times', 15, ' bold '))
    password_value.place(x=330, y=200)
    message = tk.Label(window, text="", bg="black", fg="white", font=('times', 15, 'bold'))
    message.place(x=240, y=250)

    message1 = tk.Label(window, text="", bg="black", fg="white", font=('times', 15, 'bold'))
    message1.place(x=180, y=400)

    login_btn1 = tk.Button(window, text="LOGIN", width=10, fg="black", bg="white", height=1,
                           font=('times', 15, ' bold '), command=authenticate)
    login_btn1.place(x=240, y=300)
    quitWindow = tk.Button(window, text="QUIT", command=exit, fg="black", bg="white", width=10, height=1,
                           activebackground="black", font=('times', 15, ' bold '))
    quitWindow.place(x=240, y=350)
    window.mainloop()
