import tkinter

class Converter:
    def __init__(self):
        # Создаем главное окно
        self.main_window = tkinter.Tk()
        # Создаем рамки
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame_1 = tkinter.Frame(self.main_window)
        self.mid_frame_2 = tkinter.Frame(self.main_window)
        self.res_frame_1 = tkinter.Frame(self.main_window)
        self.res_frame_2 = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        # Заполняем рамку top_frame
        # Создаем виджет с описанием запроса количества топлива в баке
        self.promt_label_1 = tkinter.Label(self.top_frame, 
                                         text='Введите количество топлива в баке: ')
        self.promt_label_1.pack(side='left', padx=(60, 1), pady=5)
        # Создаем поле ввода значения для количества топлива в баке
        self.galon_entry = tkinter.Entry(self.top_frame, width=6)
        self.galon_entry.pack(side='left', padx=5, pady=5)
        # Создаем дополнительное описание для количества топлива в баке с единицами
        # измерения
        self.prompt_label_1_add = tkinter.Label(self.top_frame, text=
                                                'галлонов')
        self.prompt_label_1_add.pack(side='left', padx=5, pady=5)
        # Упаковываем top_frame
        self.top_frame.pack()
        
        # Заполняем рамку mid_frame1_1
        # Создаем виджет с описанием запроса ввода пробега в милях
        self.promt_label_2 = tkinter.Label(self.mid_frame_1, 
                                         text='Введите пробег в милях на полном баке: ')
        self.promt_label_2.pack(side='left', padx=(5, 1), pady=5)
        # Создаем поле ввода значения пробега в милях
        self.milage_entry = tkinter.Entry(self.mid_frame_1, width=6)
        self.milage_entry.pack(side='left', padx=(3, 5), pady=5)
        # Создаем доп. текстовое поле для указания единиц измерения
        self.prompt_label_2_add = tkinter.Label(self.mid_frame_1, text=
                                                'миль')
        self.prompt_label_2_add.pack(side='left', padx=5, pady=5)
        # Упаковывем рамку mid_frame_1
        self.mid_frame_1.pack()
        
        # Заполняем рамку mid_frame_2
        # Создаем виджет для запроса ввода расхода в л/100 км
        self.promt_label_3 = tkinter.Label(self.mid_frame_2, 
                                         text='Введите расход в литрах/100 км : ')
        self.promt_label_3.pack(side='left', padx=(4, 1), pady=5)
        # Создаем поле ввода значения расхода в л/100 км
        self.kilometrs_entry = tkinter.Entry(self.mid_frame_2, width=6)
        self.kilometrs_entry.pack(side='left', padx=(3, 5), pady=5)
        # Упаковываем рамку mid_frame_2
        self.mid_frame_2.pack()
        
        # Заполняем рамку res_frame_1
        # Создаем виджет описывающий выводимый результат расчета расхода по милям
        self.prompt_milage_result_1 = tkinter.Label(self.res_frame_1, text=
                                                  'Расход по данным пробега и объема бака:')
        self.prompt_milage_result_1.pack(side='left', padx=(1,6), pady=5)
        # Связыввем значение с функцией обратного вызова
        self.milage_p_gal = tkinter.StringVar()
        # Создаем поле вывода результата
        self.milage_result = tkinter.Label(self.res_frame_1, textvariable=
                                           self.milage_p_gal)
        self.milage_result.pack(side='left', padx=5, pady=5)
        # Создаем дополнительное поле с единицами измерения после поля вывода результата
        self.prompt_milage_result_1_add = tkinter.Label(self.res_frame_1, text=
                                                  'миль/гал')
        self.prompt_milage_result_1_add.pack(side='left', padx=(1,6), pady=5)
        # Упаковываем рамку res_frame_1
        self.res_frame_1.pack()
        
        # Заполняемрамку res_frame_2
        # Создаем виджет описывающий выводимый результат расчета расхода по киллометрам
        self.prompt_milage_result_2 = tkinter.Label(self.res_frame_2, text=
                                                  'Расход по данным пробега л/100 км:')
        self.prompt_milage_result_2.pack(side='left', padx=(1,6), pady=5)
        # Связыввем значение с функцией обратного вызова
        self.milage_p_gal_km = tkinter.StringVar()
        # Создаем поле вывода результата
        self.milage_result_km = tkinter.Label(self.res_frame_2, textvariable=
                                           self.milage_p_gal_km)
        self.milage_result_km.pack(side='left', padx=5, pady=5)
        # Создаем дополнительное поле с единицами измерения после поля вывода результата
        self.prompt_milage_result_2_add = tkinter.Label(self.res_frame_2, text=
                                                  'миль/гал')
        self.prompt_milage_result_2_add.pack(side='left', padx=(1,6), pady=5)
        # Упаковываем рамку res_frame_1
        self.res_frame_2.pack()
        
        # Заполняем рамку button_frame.
        # Создаем кнопку расчета результата по милям
        self.milage_button = tkinter.Button(self.button_frame, text='Расчет по милям',
                                            command=self.evaluete_millage_p_gal)
        self.milage_button.pack(side='left', padx=5, pady=5)
        # Создаем кнопку расчета результата по километрам
        self.kilometr_button = tkinter.Button(self.button_frame, text='Расчет по км',
                                              command=self.evaluete_l_p_km)
        self.kilometr_button.pack(side='left', padx=5, pady=5)
        # Создаем кнопку выхода из грифического интерфейса
        self.quit_button = tkinter.Button(self.button_frame, text='Выход',
                                          command=self.main_window.destroy)
        self.quit_button.pack(side='left', padx=5, pady=5)
        # Упаковываем рамку button_frame.
        self.button_frame.pack()
        
        # Входим в главный цикл
        tkinter.mainloop()
        
    # Функция вычисления расхода по милям
    def evaluete_millage_p_gal(self):
        # Получаем значения из поля ввода запаса топлива в баке и миль
        litres = float(self.galon_entry.get())
        miles = float(self.milage_entry.get())
        # Выполняем расчет расхода топлива
        consumption = miles / litres
        # Выводим результат
        self.milage_p_gal.set(consumption)
    
    # Функция вычисления расхода по киллометрам
    def evaluete_l_p_km(self):
        # Получаем значение из поля ввода расхода л/100 км
        km_consumption = float(self.kilometrs_entry.get())
        # Выполняем расчет расхода топлива
        consumption = 235.215 / km_consumption
        # Выводим результат
        self.milage_p_gal_km.set(consumption)  
    
if __name__ == '__main__':
    converter = Converter()