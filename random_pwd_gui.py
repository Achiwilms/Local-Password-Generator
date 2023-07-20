import customtkinter as ctk
import tkinter as tk
import random
import string

# Settings
# modes
ctk.set_appearance_mode("Dark")

# themes
ctk.set_default_color_theme("blue")

# geometry
appWidth, appHeight = 720, 480


# App Class
class pwd_app(ctk.CTk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

        # app title
		self.title("Local Password Generator")
	
		# geometry
		self.geometry(f"{appWidth}x{appHeight}")

		# symbol initialization
		self.symbol_string = "@#$!%^&*()[]{=}+-*~"

		# password length
		self.pwd_len = 20;

		# password initialization
		self.pwd = "";
		
        # title label
		self.title_label = ctk.CTkLabel(self, text="Local Password Generator", font=("Segoe UI", 25))
		self.title_label.pack(padx=10, pady=10)
        
        # password box
		self.pwd_box = ctk.CTkTextbox(self, width=600, height=100, font=("Segoe UI", 22))	
		self.pwd_box.pack(padx=10, pady=10)
		
        # password length label
		self.pwd_label_font = ("Segoe UI", 16)
		self.pwd_len_label = ctk.CTkLabel(self, text="Password Length: "+str(self.pwd_len), text_color="white", font=self.pwd_label_font)
		self.pwd_len_label.pack()
		
		# password length silder
		self.slider = ctk.CTkSlider(self, from_=0, to=40, command=self.slider_event)        
		self.slider.pack(padx=10, pady=10)

		# option font
		self.option_font = ("Segoe UI", 15)
		# option: Uppercase
		self.add_uppercase = ctk.BooleanVar(value=True)
		self.option_upc = ctk.CTkCheckBox(self, text="Uppercase", variable=self.add_uppercase, onvalue=True, offvalue=False, font = self.option_font)
		self.option_upc.pack(padx=10, pady=10)
		self.option_upc.select()

		# option: Lowercase
		self.add_lowercase = ctk.BooleanVar(value=True)
		self.option_loc = ctk.CTkCheckBox(self, text="Lowercase", variable=self.add_lowercase, onvalue=True, offvalue=False, font = self.option_font)
		self.option_loc.pack(padx=10, pady=10)
		self.option_loc.select()

		# option: Number
		self.add_number = ctk.BooleanVar(value=True)
		self.option_num = ctk.CTkCheckBox(self, text="Number", variable=self.add_number, onvalue=True, offvalue=False, font = self.option_font)
		self.option_num.pack(padx=10, pady=10)				
		self.option_num.select()

		# option: Symbol
		self.add_symbol = ctk.BooleanVar(value=True)
		self.option_sym = ctk.CTkCheckBox(self, text="Symbol", variable=self.add_symbol, onvalue=True, offvalue=False, font = self.option_font)
		self.option_sym.pack(padx=10, pady=10)
		self.option_sym.select()

		# generate buttom
		self.gen_buttom = ctk.CTkButton(self, text="Generate", command=self.pwd_generation, font=("Segoe UI", 14))
		self.gen_buttom.pack(padx=10, pady=10)
				    
	def slider_event(self, value):
		# update password length
		self.pwd_len = int(value);

		# update password length label
		self.pwd_len_label.configure(text = "Password Length: "+str(self.pwd_len), text_color="white", font=self.pwd_label_font)
		return

	def pwd_generation(self):
		# password initialization
		self.pwd = "";

		# delete all text in password box
		self.pwd_box.delete("0.0", "end")  

		# option list 
		option_list = [self.add_uppercase.get(), self.add_lowercase.get(), self.add_number.get(), self.add_symbol.get()]

		# selected option
		selected_option = [index for index, value in enumerate(option_list) if value]
		
		# no option selected
		if (len(selected_option)==0):
			# error message
			self.pwd_len_label.configure(text = "[ERROR] Please select at least one option!", text_color="red", font=self.pwd_label_font)
			return
		
		# password generation
		for i in range(self.pwd_len):
			# option 
			option = random.choice(selected_option)
			match option:
				# 0 -> uppercase
				case 0:
					self.pwd += random.choice(string.ascii_uppercase)
				# 1 -> lowercase
				case 1:
					self.pwd += random.choice(string.ascii_lowercase)
				# 2 -> number
				case 2:
					self.pwd += str(random.randint(0, 9))
				# 3 -> symbol
				case 3:
					self.pwd += random.choice(self.symbol_string)
				case _:
					raise Exception("Invalid option!")
		# display password
		self.pwd_box.insert("0.0", self.pwd)
		# print(f"Password: {self.pwd}")

		return
if __name__ == "__main__":
	app = pwd_app()
	app.mainloop()