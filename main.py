import customtkinter as CTk
import tkinter
import price

from string import digits
from PIL import Image

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('460x370')
        self.title("Credits to @zxpixty")
        self.resizable(False, True)

        self.logo = CTk.CTkImage(dark_image=Image.open('img.png'), size = (460, 150))
        self.logo_label = CTk.CTkLabel(master=self, text='', image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.first_num_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.first_num_frame.grid(row = 1, column = 0, padx = (20, 20), sticky = "nsew")

        self.second_num_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.second_num_frame.grid(row = 2, column = 0, padx = (20, 20), pady=(20, 20), sticky = "nsew")

        self.entry_final_num_frame = CTk.CTkFrame(master=self, fg_color='transparent')
        self.entry_final_num_frame.grid(row = 3, column = 0, padx = (20, 20), pady=(20, 20), sticky = "nsew")

        self.entry_first_num = CTk.CTkEntry(master=self.first_num_frame, placeholder_text="Введите начальную цену", width = 300)
        self.entry_first_num.grid(row = 0, column = 0, padx = (0, 20))

        self.entry_second_num = CTk.CTkEntry(master=self.second_num_frame, placeholder_text="Введите количество покупок", width = 300)
        self.entry_second_num.grid(row = 0, column = 0, padx = (0, 20))

        self.entry_final_num = CTk.CTkEntry(master=self.entry_final_num_frame, width=150)
        self.entry_final_num.grid(row=0, column=0, padx=(0, 20))

        self.button_score = CTk.CTkButton(master=self.first_num_frame, text = "Вычислить", width = 100,
                                          command=self.generate_score)
        
        self.button_score.grid(row=0, column=1)
        
        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=4, column=0, padx=(20, 20), pady=(20, 0), sticky='nsew')

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text = 'Животные', variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.appereance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=['Light', 'Dark', 'System'],
                                                             command=self.change_appereance_mode_event)
        self.appereance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))
        self.appereance_mode_option_menu.set('Light')
        

    def change_appereance_mode_event(self, new_appereance_mode):
        CTk.set_appearance_mode(new_appereance_mode)
        
    
    def get_value(self):
        chars = ''.join(self.cb_digits_var.get())

        return chars

    def generate_score(self):
        self.entry_final_num.insert(0, str(price.calculate_final_price(initial_price=int(self.entry_first_num.get()), num_pricing=int(self.entry_second_num.get()))))
        self.entry_first_num.delete(0, 'end')
        self.entry_second_num.delete(0, 'end')

if __name__ == "__main__":
    app = App()
    app.mainloop()
