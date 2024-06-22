from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk 

root = tk.Tk()
root.title("IMAGE SLIDESHOW VIEWER")
root.geometry('1080x1080')

#list of the image
image_paths = [
    r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2023-11-02 191549.png",
    r"C:\Users\DELL\Pictures\Screenshots\hritik.png",
    r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2023-11-02 191615.png",
    r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2024-01-12 212138.png",
    r"C:\Users\DELL\Pictures\Screenshots\Screenshot 2023-11-02 190949.png",
]

image_size = (720,720)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text='play slideshow', command=start_slideshow)
play_button.pack()


root.mainloop()

