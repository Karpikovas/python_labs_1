from tkinter import *


class ClientAppGUI:

    def __init__(self, network):

        def count_callback(expr):

            result_field.delete(1.0, END)
            result_field.insert(1.0, "Processing")
            resp = network.send_to_server(expr)
            if resp:
                result_field.delete(1.0, END)
                result_field.insert(1.0, resp)

        window = Tk()

        # инициализация виджетов
        expr_input = Entry(window, width=300, bd=2)
        count = Button(window, text="Посчитать", command=lambda: count_callback(expr_input.get()))
        result_label = Label(window, text="Результат выражения:")
        result_field = Text(window, width=300, bd=2)

        # инсталяция виджетов
        expr_input.pack()
        count.pack()
        result_label.pack()
        result_field.pack()

        # конфигурация окна
        window.title("Текстовый калькулятор")
        w = window.winfo_screenwidth()  # ширина экрана
        h = window.winfo_screenheight()  # высота экрана
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 200  # смещение от середины
        h = h - 200
        window.geometry('400x400+{}+{}'.format(w, h))

        self.window = window

    def install(self):
        self.window.mainloop()
