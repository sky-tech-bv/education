import tkinter
import tkinter.messagebox

class PhoneCall:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        self.promt_label_start = tkinter.Label(self.top_frame, text=
                                         'Программа выполняет расчет стоимости' +
                                         'звонков. Для расчетанеобходимо выбрать\n' +
                                         'временной интервал выполнения вызова и' +
                                         'ввести длину вызова в минутах.')
        self.promt_label = tkinter.Label(self.top_frame, text=
                                         'Введите длину разговора:')
        self.value_minutes = tkinter.Entry(self.top_frame, width=15)
        self.promt_label_start.pack()
        self.promt_label.pack(side='left', padx=5, pady=5)
        self.value_minutes.pack(side='right', padx=5, pady=5)
        self.top_frame.pack()
        
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.mid_frame, text=
                                       'Дневное время: с 06:00 до 17:59',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.mid_frame, text=
                                       'Вечернее время: с 18:00 до 23:59',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.mid_frame, text=
                                       'Ночное время: с 00:00 до 05:59',
                                       variable=self.radio_var,
                                       value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.mid_frame.pack()
        
        self.get_button = tkinter.Button(self.button_frame, text='По считать',
                                         command=self.get_result)
        self.quit_button = tkinter.Button(self.button_frame, text='Выход',
                                          command=self.main_window.destroy)
        self.get_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='right', padx=5, pady=5)
        self.button_frame.pack()
    
        tkinter.mainloop()
        
    
    def get_result(self):
        value = self.radio_var.get()
        hours = float(self.value_minutes.get())
        result = 0
        night = 5
        day = 10
        evening = 12
        if value == 1:
            result = day * hours
        elif value == 2:
            result = evening * hours
        elif value == 3:
            result = night * hours
        tkinter.messagebox.showinfo('Результат',
                                    f'Итого, разговор стоил Вам {result:,.2f} USD.')
                
        
if __name__ == '__main__':
    calls = PhoneCall()