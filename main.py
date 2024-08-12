import customtkinter as CTk
import tkinter
import price  # Убедитесь, что у вас есть модуль 'price' с функцией 'calculate_final_price'
from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('460x670')
        self.title("Credits to @zxpixty")
        self.resizable(False, False)

        # Фрейм для изображения (логотипа), который будет всегда на экране
        self.logo_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.logo_frame.grid(row=0, column=0, sticky="nsew")

        self.logo = CTk.CTkImage(dark_image=Image.open('img.png'), size=(460, 150))
        self.logo_label = CTk.CTkLabel(master=self.logo_frame, text='', image=self.logo)
        self.logo_label.pack()

        # Фрейм для страниц
        self.pages_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.pages_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        # Словарь для хранения страниц
        self.pages = {}

        # Создание страниц
        self.create_pages()
        self.show_page("Home")

    def create_pages(self):
        # Главная страница
        home_page = CTk.CTkFrame(master=self.pages_frame, fg_color='transparent')

        self.first_num_frame = CTk.CTkFrame(master=home_page, fg_color='transparent')
        self.first_num_frame.grid(row=1, column=0, padx=(20, 20), sticky="nsew")

        self.second_num_frame = CTk.CTkFrame(master=home_page, fg_color='transparent')
        self.second_num_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.entry_final_num_frame = CTk.CTkFrame(master=home_page, fg_color='transparent')
        self.entry_final_num_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.entry_first_num = CTk.CTkEntry(master=self.first_num_frame, placeholder_text="Введите начальную цену", width=300)
        self.entry_first_num.grid(row=0, column=0, padx=(0, 20))

        self.entry_second_num = CTk.CTkEntry(master=self.second_num_frame, placeholder_text="Введите количество покупок", width=300)
        self.entry_second_num.grid(row=0, column=0, padx=(0, 20))

        self.entry_final_num = CTk.CTkEntry(master=self.entry_final_num_frame, width=150)
        self.entry_final_num.grid(row=0, column=0, padx=(0, 20))

        self.button_score = CTk.CTkButton(master=self.first_num_frame, text="Вычислить", width=100,
                                          command=self.generate_score)
        self.button_score.grid(row=0, column=1)

        self.settings_frame = CTk.CTkFrame(master=home_page)
        self.settings_frame.grid(row=4, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

        self.appereance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=['Light', 'Dark', 'System'],
                                                             command=self.change_appereance_mode_event)
        self.appereance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))
        self.appereance_mode_option_menu.set('Light')

        # Кнопка для переключения на другую страницу
        self.switch_to_settings_button = CTk.CTkButton(master=home_page, text="Информация",
                                                       command=lambda: self.show_page("Settings"))
        self.switch_to_settings_button.grid(row=5, column=0, pady=(10, 10))

        self.pages["Home"] = home_page

        # Страница информации с добавленным скроллируемым текстом
        settings_page = CTk.CTkFrame(master=self.pages_frame, fg_color='transparent')

        self.settings_label = CTk.CTkLabel(master=settings_page, text="Полезная информация", font=("Arial", 20))
        self.settings_label.grid(row=0, column=0, pady=(20, 10))

        # Добавление скроллируемого текста
        self.scrollable_frame = CTk.CTkScrollableFrame(master=settings_page, width=400, height=300)
        self.scrollable_frame.grid(row=1, column=0, pady=(10, 10), padx=(10, 10), sticky="nsew")

        # Текст для отображения
        scrollable_text = """4. Координаты культур: 

Список составлен в зависимости от цены
Пшеница: 16 91 25 (Начальная цена $130)
Картофель: 78 91 14 (Начальная цена $1,600)
Морковь:  105 90 49 (Начальная цена $19,000)
Малина: 111 90 57 (Начальная цена $200,000)
Свёкла: 47 90 124 (Начальная цена $1.9M)
Тыква: 52 90 127 (Начальная цена $16M)
Тюльпан: 5 89 160 (Начальная цена $120M)
Хлопок: 5 89 172 (Начальная цена $820M)
Роза: -56 90 179 (Начальная цена $9.30B)
Лён: -102 90 156 (Начальная цена $56B)
Виноград: -144 89 184 (Начальная цена $590B)
Лук: -142 89 190 (Начальная цена $3,4T)
Арбуз: -156 90 152 (Начальная цена $35T)
Тростник: -138 90 123 (Начальная цена $200T)
Пион: -134 90 79 (Начальная цена $1.2Qa)
Адский нарост: -178 90 61 (Начальная цена $6.7Qa)
Хорус: -181 90 38 (Начальная цена $39Qa)

6. Координаты зданий по производству:

Список составлен в зависимости от цены
Пекарня: 118 90 81 (Начальная цена $830K)
Бар: 34 90 89 (Начальная цена $11M)
Завод: -121 90 -17 (Начальная цена $120M)
Кафе: -61 89 208 (Начальная цена $12B)
Цветочная лавка: -80 90 136 (Начальная цена $780B)
Швейная фабрика: 84 92 198 (Начальная цена $5,5T)
Домик Ведьмы: -173 90 122 (Начальная цена $42,5Qi)

8. Координаты NPC по покупке животных:

Курица: 116 90 41 (Начальная цена $9.30B)
Кролик: 70 90 76 (Начальная цена $460B)
Лошадь: 29 89 169 (Начальная цена $29.7T)
Свинка: -26 90 166 (Начальная цена $1.76Qa)
Овечка: -88 90 166 (Начальная цена $100Qa)
Коровка: -153 90 51 (Начальная цена $3.05Qi)

9.1 Фонтаны и их доход

Фонтаны дают 5% к доходу, и они складываются, всего фонтанов 3, получается 15% к доходу.

9.2 Стоимость фонтанов

Мини фонтан - $30B
Обычный фонтан - $2Т
Мега фонтан - $100Т"""

        # Добавление текста в фрейм
        self.text_label = CTk.CTkLabel(master=self.scrollable_frame, text=scrollable_text, wraplength=380, justify="left", font=("Arial", 14, "bold"))
        self.text_label.grid(row=0, column=0, padx=10, pady=10)

        self.back_button = CTk.CTkButton(master=settings_page, text="Вернуться", command=lambda: self.show_page("Home"))
        self.back_button.grid(row=2, column=0, pady=(10, 20), padx=(10, 10))

        self.pages["Settings"] = settings_page

    def change_appereance_mode_event(self, new_appereance_mode):
        CTk.set_appearance_mode(new_appereance_mode)

    def generate_score(self):
        self.entry_final_num.delete(0, 'end')
        final_price = price.calculate_final_price(
            initial_price=int(self.entry_first_num.get()),
            num_pricing=int(self.entry_second_num.get())
        )
        self.entry_final_num.insert(0, str(final_price))
        self.entry_first_num.delete(0, 'end')
        self.entry_second_num.delete(0, 'end')

    def show_page(self, page_name):
        # Прячем все страницы
        for page in self.pages.values():
            page.pack_forget()

        # Показываем выбранную страницу
        self.pages[page_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
