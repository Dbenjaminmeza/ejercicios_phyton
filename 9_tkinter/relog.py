import tkinter as tk 
import time 


ventana = tk.Tk()
ventana.geometry("800x600")
ventana.minsize(200, 200)
ventana.maxsize(800, 600)
ventana.configure(bg="black")
ventana.attributes(alpha=0.9)
# ventana.resizable()#no deja achicar



relog = tk.Label(ventana, font= ("Arial",60), bg="red", fg="white")
relog.pack()



def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    relog.config(text=tiempo_actual)
    ventana.after(1000,hora)


hora()

ventana.mainloop()