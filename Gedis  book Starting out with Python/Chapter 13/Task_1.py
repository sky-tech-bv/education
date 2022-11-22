import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.message_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()
        
        self.name_label = tkinter.Label(self.message_frame, 
                                        textvariable = self.name_value)
        self.street_label = tkinter.Label(self.message_frame, 
                                          textvariable = self.street_value)
        self.csz_label = tkinter.Label(self.message_frame, 
                                       textvariable = self.csz_value)
        
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()
        
        self.message_frame.pack(padx = 20, pady = 20)
        
        self.start_button = tkinter.Button(self.button_frame, text='Показать информацию',
                                           command=self.show_info)
        self.exit_button = tkinter.Button(self.button_frame, text='Выход',
                                          command=self.main_window.destroy)
        
        self.start_button.pack(side = 'left')
        self.exit_button.pack(side = 'right')
        
        self.button_frame.pack(padx = 20, pady = (0, 10))
        
        tkinter.mainloop()
    
    def show_info(self):
        self.name_value.set('Василий Иванович Попов')
        self.street_value.set('ул. Нижнеподзадрыщинская, д. 9')
        self.csz_value.set('с. Новые сидоры, Великоугодская область, 09876')
        
my_gui = MyGUI()