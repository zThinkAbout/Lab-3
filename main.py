import tkinter as tk
from tkinter import messagebox
import random
import pygame

pygame.mixer.init()
pygame.mixer.music.load('wasteland.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


def gen_key(hex_str):
    dec = int(hex_str, base=16)
    sdec = str(dec).zfill(5)
    symbols = [[],[],[]]
    for i in range(len(symbols)):
        for j in range(4):
            symbols[i].append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
        symbols[i].append(sdec[i])
        random.shuffle(symbols[i])
    key = ''.join(symbols[0]) + '-' + ''.join(symbols[1]) + '-' + ''.join(symbols[2]) + " " + sdec[-2:]
    return key

def on_generate():
    n = hex_var.get()
    n = n.strip().upper()
    print("hex =", n)
    if len(n)!=5: 
        messagebox.showerror("Error", "5 symbols needed")
        return
    for i in n:
        if i not in '0123456789ABCDEF':
            messagebox.showerror("Error", "Hexadecimal symbols only")
            return
    key_var.set(gen_key(n))

root = tk.Tk()
root.title("Keygen")
root.geometry('800x450')
root.resizable(False, False)
canvas = tk.Canvas(root, width=800, height=450, highlightthickness=0)
canvas.pack()
bg = tk.PhotoImage(file='calamity.png')
canvas.create_image(0,0,image=bg,anchor='nw')
frame=tk.Frame(canvas,bg='#2b2b3d', bd=2, relief='ridge')
canvas.create_window(400, 225, window=frame)

hex_var = tk.StringVar()
key_var = tk.StringVar()

title = tk.Label(frame, text='KEYGEN', font=("Arial", 16, 'bold'), fg='cyan', bg='#2b2b3d')
title.pack(pady=5)
tk.Label(frame, text="HEX (5 symbols):", fg='white', bg = '#2b2b3d').pack()
tk.Entry(frame, textvariable=hex_var).pack()
tk.Button(frame, text="Generate", command=on_generate).pack()
tk.Entry(frame, textvariable=key_var, state="readonly").pack()

colors = [
    '#39FF14', 
    '#DC143C', 
    '#FF00FF',
    '#FF8C00',
    '#CCFF00',
    '#8A2BE2']
ind = 0
beat = 60000/130
def pulse():
    global ind
    ind = (ind+1)%len(colors)
    title.config(fg=colors[ind])
    root.after(int(beat), pulse)
pulse()
root.mainloop()