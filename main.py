import tkinter as tk
import os
from tkinter import filedialog, Text, ttk

root = tk.Tk()
root.title('Ajuda TI Conibase')
root.iconbitmap('./icone_favicon.ico')
root.iconphoto(True, tk.PhotoImage(file='./logo.png'))


canvas = tk.Canvas(root, height=800, width=940, bg="white")
canvas.pack()

frame = tk.Frame(root, bg="#f2f2f2")
frame.place(width=200, height=250, x=20, y=20)
label = tk.Label(frame, text="Atalho do\n GIX sumiu", font="Arial 18 bold")
label.place(y=50, x=30)
btnSos = tk.Button(frame, text="Clique Aqui !", fg="#fff", bg="#df0209", padx=20, pady=5, font="Arial 15 bold", activebackground="#b21117", activeforeground="#fff")
btnSos.place(y=180, x=12)


frame1 = tk.Frame(root, bg="#f2f2f2")
frame1.place(width=200, height=250, x=250, y=20)
label1 = tk.Label(frame1, text="Usuario ficou\n preso neste\n terminal?", font="Arial 18 bold")
label1.place(y=50, x=20)
btnTerminal = tk.Button(frame1, text="Clique Aqui !", fg="#fff", bg="#df0209", padx=20, pady=5, font="Arial 15 bold", activebackground="#b21117", activeforeground="#fff")
btnTerminal.place(y=180, x=12)

frame2 = tk.Frame(root, bg="#f2f2f2")
frame2.place(width=200, height=250, x=480, y=20)
label2 = tk.Label(frame2, text="Usuario ficou\n preso mas não\n sabe em qual\n terminal?", font="Arial 18 bold")
label2.place(y=30, x=5)
btnAllTerminal = tk.Button(frame2, text="Clique Aqui !", fg="#fff", bg="#df0209", padx=20, pady=5, font="Arial 15 bold", activebackground="#b21117", activeforeground="#fff")
btnAllTerminal.place(y=180, x=12)

frame3 = tk.Frame(root, bg="#f2f2f2")
frame3.place(width=200, height=250, x=710, y=20)
label3 = tk.Label(frame3, text="Servidor lento\n e/ou Travando?", font="Arial 18 bold")
label3.place(y=50, x=2)
btnServer = tk.Button(frame3, text="Clique Aqui !", fg="#fff", bg="#df0209", padx=20, pady=5, font="Arial 15 bold", activebackground="#b21117", activeforeground="#fff")
btnServer.place(y=180, x=12)


frame4 = tk.Frame(root, bg="#f2f2f2")
frame4.place(width=800, x=65, y=320)
progress = ttk.Progressbar(frame4, orient = tk.HORIZONTAL, length = '22c', mode = 'determinate') 
progress.pack()
root.mainloop()