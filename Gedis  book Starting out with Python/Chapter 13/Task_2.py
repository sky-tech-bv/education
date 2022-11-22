import tkinter

class Translation:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Перевод с латыни')
        
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_exit_button()
        
        tkinter.mainloop()
        
        
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(self.main_window,
                                          text='Выберите слово для перевода')
        self.prompt_label.pack(padx=5, pady=5)
        
        
    def __build_listbox(self):
        self.__words = ['sinister', 'dexter', 'medium']
        self.words_listbox = tkinter.Listbox(self.main_window,
                                             height=0, width=0)
        self.words_listbox.pack(padx=5, pady=5)
        self.words_listbox.bind('<<ListboxSelect>>', self.__display_translation)
        for word in self.__words:
            self.words_listbox.insert(tkinter.END, word)
        
        
    def __build_output_frame(self):
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)
        self.output_description_label = tkinter.Label(self.output_frame,
                                                      text='Перевод: ')
        self.output_description_label.pack(side='left', padx=(1, 5), pady=5)
        self.__translation = tkinter.StringVar()
        self.output_label = tkinter.Label(self.output_frame, textvariable=
                                          self.__translation)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)
        
        
    def __build_exit_button(self):
        self.exit_button = tkinter.Button(self.main_window, text='Выход',
                                          command=self.main_window.destroy)
        self.exit_button.pack(padx=5, pady=5)
        
        
    def __display_translation(self, event):
        index = self.words_listbox.curselection()
        word = self.words_listbox.get(index[0])
        if word == 'sinister':
            self.__translation.set('Левый')
        elif word == 'dexter':
            self.__translation.set('Правый')
        elif word == 'medium':
            self.__translation.set('Центральный')   
            
if __name__ == '__main__':
    translation = Translation()