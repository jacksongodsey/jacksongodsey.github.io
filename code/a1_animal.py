import tkinter as tk
root = tk.Tk()

wdth = 800
hght = 700
root.geometry('%dx%d' % (wdth, hght))

canvas = tk.Canvas(root, width=wdth, height=hght)
canvas.pack()

#                x0    y0   x1   y1
head_position = (350, 100, 475, 250)
eye_position  = (375, 125, 395, 145)
eye2_position = (405, 125, 425, 145)
tentacle1_pos = (200, 100, 600, 600)
tentacle1_pos2 = (300, 200, 600, 600)

head = canvas.create_oval (head_position, fill="#E8208C")
eye1 = canvas.create_oval (eye_position, fill="black")
eye2 = canvas.create_oval (eye2_position, fill="black" )
tentacle1 = canvas.create_line (tentacle1_pos)

root.mainloop()
