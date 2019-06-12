import tkinter as tk

def main():
    window = tk.Tk()
    window.overrideredirect(True)
    window.title("Recognize face")
    window.resizable(0,0)

    def cap():
        from Capture_image import main
        name = str(txt.get())
        main(name)
        window.destroy()
        print("Capture Successful")

    window.geometry('640x480')
    window.configure(background='black')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    message = tk.Label(window, text="FACE RECOGNITION SYSTEM", bg="black", fg="white",
                       width=25,
                       height=3, font=('times', 25, ' bold '))
    message.place(x=70, y=10)


    lbl = tk.Label(window, text="Name", width=20, height=1, fg="white", bg="black", font=('times', 15, ' bold '))
    lbl.place(x=50, y=140)

    txt = tk.Entry(window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
    txt.place(x=250, y=140)

    btn1 = tk.Button(window, text="SUBMIT", width=10, height=1, fg="black", bg="white", font=('times', 15, ' bold '),command=cap)
    btn1.place(x=250, y=230)

    quitWindow = tk.Button(window, text="QUIT", command=window.destroy, fg="black", bg="white", width=10, height=1,
                           activebackground="black", font=('times', 15, ' bold '))
    quitWindow.place(x=250, y=280)

    window.mainloop()



if __name__ == '__main__':
    main()
