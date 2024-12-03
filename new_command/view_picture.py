#!/usr/bin/python3

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

class ViewPicture:
    def __init__(
        self,
        picture_size:tuple=(500,707),
    ):
        self.picture_size = picture_size
        self.image_path = "/home/RoboSys/robosys2024/pictures/menue.jpg"
  
  
    def done(self) -> None:
        image = self.__get_image()
        label = tk.Label(root,image=image)
        label.pack()
        root.mainloop()
        
      
    def __get_image(self) -> ImageTk.PhotoImage:
        image = Image.open(self.image_path)
        resized = image.resize(self.picture_size,Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized)
        return tk_image
      
if __name__ == "__main__":
    view = ViewPicture()
    view.done()      
