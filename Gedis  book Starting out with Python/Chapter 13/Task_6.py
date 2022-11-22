import tkinter
import tkinter.messagebox

class AutoService:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        self.cd_choice_1 = tkinter.IntVar()
        self.cd_choice_2 = tkinter.IntVar()
        self.cd_choice_3 = tkinter.IntVar()
        self.cd_choice_4 = tkinter.IntVar()
        self.cd_choice_5 = tkinter.IntVar()
        self.cd_choice_6 = tkinter.IntVar()
        self.cd_choice_7 = tkinter.IntVar()
        
        self.cd_choice_1.set(0)
        self.cd_choice_2.set(0)
        self.cd_choice_3.set(0)
        self.cd_choice_4.set(0)
        self.cd_choice_5.set(0)
        self.cd_choice_6.set(0)
        self.cd_choice_7.set(0)
        
        self.cd1 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена масла',
                                       variable=self.cd_choice_1)
        self.cd2 = tkinter.Checkbutton(self.top_frame,
                                       text='Смазочные работы',
                                       variable=self.cd_choice_2)
        self.cd3 = tkinter.Checkbutton(self.top_frame,
                                       text='Промывка радиатора',
                                       variable=self.cd_choice_3)
        self.cd4 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена трансмиссионной жидкости',
                                       variable=self.cd_choice_4)
        self.cd5 = tkinter.Checkbutton(self.top_frame,
                                       text='Осмотр',
                                       variable=self.cd_choice_5)
        self.cd6 = tkinter.Checkbutton(self.top_frame,
                                       text='Замена глушителя выхлопа',
                                       variable=self.cd_choice_6)
        self.cd7 = tkinter.Checkbutton(self.top_frame,
                                       text='Перестановка шин',
                                       variable=self.cd_choice_7)
        
        self.cd1.pack()
        self.cd2.pack()
        self.cd3.pack()
        self.cd4.pack()
        self.cd5.pack()
        self.cd6.pack()
        self.cd7.pack()
        self.top_frame.pack()
        
        self.__result = tkinter.StringVar()
        self.prompt_label = tkinter.Label(self.mid_frame, text=
                                          'Стоимость работ:')
        self.result_label = tkinter.Label(self.mid_frame, textvariable=
                                          self.__result, relief='ridge')
        self.prompt_label_add = tkinter.Label(self.mid_frame, text=
                                             'USD')
        self.prompt_label.pack(side='left', padx=(5, 1), pady=5)
        self.result_label.pack(side='left', ipadx=2, ipady=2, padx=5, pady=3)
        self.prompt_label_add.pack(side='right', padx=5, pady=5)
        self.mid_frame.pack()
        
        self.button_evaluate = tkinter.Button(self.button_frame, text='Рассчитать',
                                              command=self.show_result)
        self.quit_button = tkinter.Button(self.button_frame, text='Выход',
                                          command=self.main_window.destroy)
        self.button_evaluate.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='right', padx=5, pady=5)
        self.button_frame.pack()
        
        tkinter.mainloop()
        
        
    def show_result(self):
        result = 0
        self.message = 'Выбраны пункты:\n'
        if self.cd_choice_1.get() == 1:
            result += 500
            self.message += 'Выбран пункт 1\n'
        if self.cd_choice_2.get() == 1:
            result += 300
            self.message += 'Выбран пункт 2\n'
        if self.cd_choice_3.get() == 1:
            result += 700
            self.message += 'Выбран пункт 3\n'
        if self.cd_choice_4.get() == 1:
            result += 1000
            self.message += 'Выбран пункт 4\n'
        if self.cd_choice_5.get() == 1:
            result += 800
            self.message += 'Выбран пункт 5\n'
        if self.cd_choice_6.get() == 1:
            result += 1300
            self.message += 'Выбран пункт 6\n'
        if self.cd_choice_7.get() == 1:
            result += 1300
            self.message += 'Выбран пункт 7\n'
        self.message += f'Cумма затрат составляет - {result:,.2f} USD'
        self.__result.set(result)
        tkinter.messagebox.showinfo('Выбор', self.message)
        
        
        
if __name__ == '__main__':
    service = AutoService()