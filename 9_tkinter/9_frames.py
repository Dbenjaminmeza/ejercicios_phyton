import tkinter as tk


ventana = tk.Tk()
ventana.title("mi proyecto")
ventana.geometry("500x300")

frame_1 = tk.Frame(ventana)
frame_1.configure(width= 300, height= 200, bg="red",bd=5)#bd = borde
frame_1.pack()

frame_2 = tk.Frame(frame_1)
frame_2.configure(width= 100, height= 60, bg="blue",bd=5)
frame_2.pack()

ventana.mainloop()