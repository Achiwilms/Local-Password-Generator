# Python program to create a basic GUI
# application using the customtkinter module

import customtkinter as ctk
import tkinter as tk

# Settings
# modes
ctk.set_appearance_mode("System")

# themes
ctk.set_default_color_theme("blue")

# geometry
appWidth, appHeight = 720, 480


# App Class
class pwd_app(ctk.CTk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

        # app title
		self.title("Random Password Generator")
	
		# geometry
		self.geometry(f"{appWidth}x{appHeight}")
		
        # title label
		self.title_label = ctk.CTkLabel(self, text="Random Password Generator")
		self.title_label.pack(padx=10, pady=10)
        
        # password box
		self.pwd_box = ctk.CTkTextbox(self, width=600, height=100)	
		self.pwd_box.pack(padx=10, pady=10)
		
        # password length label
		self.pwd_len_lable = ctk.CTkLabel(self, text="Password Length")
		self.pwd_len_lable.pack()
		
		# password length silder
		self.slider = ctk.CTkSlider(self, from_=0, to=40, command=self.slider_event)        
		self.slider.pack(padx=10, pady=10)

		# option: Uppercase
		self.add_uppercase = ctk.StringVar(value=False)
		self.option_upc = ctk.CTkCheckBox(self, text="Uppercase", variable=self.add_uppercase, onvalue=True, offvalue=False, command=self.check_box_state)
		self.option_upc.pack(padx=10, pady=10)

		# option: Lowercase
		self.add_lowercase = ctk.StringVar(value=False)
		self.option_loc = ctk.CTkCheckBox(self, text="Lowercase", variable=self.add_lowercase, onvalue=True, offvalue=False, command=self.check_box_state)
		self.option_loc.pack(padx=10, pady=10)

		# option: Number
		self.add_number = ctk.StringVar(value=False)
		self.option_num = ctk.CTkCheckBox(self, text="Number", variable=self.add_number, onvalue=True, offvalue=False, command=self.check_box_state)
		self.option_num.pack(padx=10, pady=10)				

		# option: Symbol
		self.add_symbol = ctk.StringVar(value=False)
		self.option_sym = ctk.CTkCheckBox(self, text="Symbol", variable=self.add_symbol, onvalue=True, offvalue=False, command=self.check_box_state)
		self.option_sym.pack(padx=10, pady=10)

		# generate buttom
		self.gen_buttom = ctk.CTkButton(self, text="Generate", command=self.pwd_generation)
		self.gen_buttom.pack(padx=10, pady=10)
				    
	def slider_event(self, value):
		print(int(value))
	
	def check_box_state(self):
		print(self.add_symbol.get())

	def pwd_generation(self):
		print("generate")


if __name__ == "__main__":
	app = pwd_app()
	app.mainloop()