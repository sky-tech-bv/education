import tkinter

class SuperStar:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        self.canvas.create_polygon(100,25, 47,178, 186,87, 14,87, 153, 178, fill='orange')
        self.canvas.create_text(100,108, text='  Майкл\nДжексон', anchor=tkinter.CENTER, fill='black')
        self.canvas.pack()
        
        tkinter.mainloop()
        
                  
if __name__ == '__main__':
    star = SuperStar()
    
                      