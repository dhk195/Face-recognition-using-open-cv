import tkinter as tk  # for gui


def main():
    notify = ""
    window = tk.Tk()
    window.overrideredirect(True)
    window.title("Face Recognition System")
    window.resizable(0, 0)  # non resizable window

    def detect():
        from Detect_face import main
        main()

    def capture():
        from Get_detail_GUI import main
        main()
        notify = "Successful capture"
        notification_label.configure(test=notify)

    def training():
        from Train_image import main
        main()
        notify = "Training Successful"
        notification_label.configure(text=notify)

    def recog():
        from Recognize_face import main
        main()

    window.geometry('640x480')  # main window size
    window.configure(background='gray')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    message = tk.Label(window, text="FACE RECOGNITION SYSTEM", bg="gray", fg="white",
                       width=25,
                       height=3, font=('times', 25, ' bold '))

    message.place(x=70, y=10)

    btn1 = tk.Button(window, text="Detect Face", width=20, height=1, fg="black", bg="white",
                     font=('times', 15, ' bold '), command=detect)
    btn1.place(x=200, y=110)

    btn2 = tk.Button(window, text="Capture Image", width=20, height=1, fg="black", bg="white",
                     font=('times', 15, ' bold '), command=capture)
    btn2.place(x=200, y=160)

    btn3 = tk.Button(window, text="Train Image", width=20, height=1, fg="black", bg="white", font=('times', 15, 'bold'),
                     command=training)
    btn3.place(x=200, y=210)

    btn4 = tk.Button(window, text="Recognize Face", width=20, height=1, fg="black", bg="white",
                     font=('times', 15, 'bold'), command=recog)
    btn4.place(x=200, y=260)

    quitWindow = tk.Button(window, text="Logout", command=window.destroy, fg="black", bg="white", width=20, height=1,
                           activebackground="black", font=('times', 15, ' bold '))
    quitWindow.place(x=200, y=310)
    notification_label = tk.Label(window, text="", width=20, fg="white", bg="gray", font=('times', 15, ' bold '))
    notification_label.place(x=200, y=370)

    window.mainloop()


if __name__ == '__main__':
    main()
