from tkinter import Tk, Label, Entry, Button, Radiobutton, StringVar
from tkinter.font import Font
from tkinter.messagebox import showerror
import math

__version__ = "0.1"

class BeltSpeedUI():
	
	def __init__(self, root):
		
		set_font = Font(family = "Calibri Light")
		solution_font = Font(family = "Calibri Light")
		bg_color = "white"
		
		#All the Labels
		self.label_diameter = Label(root, text = "Diameter [in]",
		font = set_font, bg = bg_color)
		
		self.label_rpm = Label(root, text = "RPM Out [revs per min]",
		font = set_font, bg = bg_color)
		
		self.label_tspeed = Label(root, text = "Tangential Velocity [feet per min]",
		font = set_font, bg = bg_color)
		
		#All the Entries
		self.diameter_var = StringVar()
		self.rpm_var = StringVar()
		self.tspeed_var = StringVar()

		self.entry_diameter = Entry(root, textvariable = self.diameter_var)
		
		self.entry_rpm = Entry(root, textvariable = self.rpm_var,
		disabledbackground = "#CCEECC")
		
		self.entry_tspeed = Entry(root, textvariable = self.tspeed_var,
		disabledbackground = "#CCEECC")
		
		self.btn_calculate = Button(root, text = "Calculate",
		width = 50,
		relief = "flat",
		font = set_font)
		
		#String_Vars for Radiobuttons
		self.var_check = StringVar()
		
		self.entry_check_rpm = Radiobutton(root, 
		variable = self.var_check, value = "rpm",
		bg = "white", command = lambda: self.set_rpm())
			
		self.entry_check_tspeed = Radiobutton(root, 
		variable = self.var_check, value = "tspeed",
		bg = "white", command = lambda: self.set_tspeed())
		
		self.var_check.set("rpm")
		self.set_rpm()
		
		#Setting the Widgets
		self.label_diameter.grid(row = 0, column = 0, sticky = "E")
		self.label_rpm.grid(row = 1, column = 0, sticky = "E")
		self.label_tspeed.grid(row = 2, column = 0, sticky = "E")
		
		self.entry_diameter.grid(row = 0, column = 1)
		self.entry_rpm.grid(row = 1, column = 1)
		self.entry_tspeed.grid(row = 2, column = 1)
		
		self.entry_check_rpm.grid(row = 1, column = 2)
		self.entry_check_tspeed.grid(row = 2, column = 2)
		
		self.btn_calculate.grid(row = 3, column = 0, columnspan = 3)
		
	def set_rpm(self):
		
		self.entry_rpm.configure(state = "normal")
		self.rpm_var.set('')
		self.entry_tspeed.configure(state = "disabled")
		self.tspeed_var.set('')
		
		self.label_rpm.configure(fg = "black")
		self.label_tspeed.configure(fg = "green")
		
	def set_tspeed(self):
		
		self.entry_rpm.configure(state = "disabled")
		self.rpm_var.set('')
		self.entry_tspeed.configure(state = "normal")
		self.tspeed_var.set('')
		
		self.label_rpm.configure(fg = "green")
		self.label_tspeed.configure(fg = "black")
		
class BeltSpeedModel():
		
	def calculate_rpm(self, diameter, tspeed):
		
		return (tspeed * 12) / (diameter * math.pi)
	
	def calculate_tspeed(self, diameter, rpm):
	
		return (math.pi*rpm*diameter)/12

class BeltSpeedController():
	
	def __init__(self, root):
		
		self.app = BeltSpeedUI(root)
		self.model = BeltSpeedModel()
		
		self.app.btn_calculate.configure(command = lambda: self.calculate())

	def calculate(self):
		
		try:
			diameter = float(self.app.entry_diameter.get())
			
			if self.app.var_check.get() == "rpm":
				
				rpm = float(self.app.entry_rpm.get())
				self.solution = self.model.calculate_tspeed(diameter, rpm)
				self.app.tspeed_var.set(int(round(self.solution, 0)))
			
			else:	
				
				tspeed = float(self.app.entry_tspeed.get())
				self.solution = self.model.calculate_rpm(diameter, tspeed)
				self.app.rpm_var.set(int(round(self.solution, 0)))
		except ValueError as e:
			showerror("Value Error",
			f"Make sure entries are numbers, no letters are allowed.\nEmpty fields will also generate this error.\n\n\nPython Error: {e}")
		except ZeroDivisionError as e:
			showerror("Zero Division Error",
			f"Re-evaluate your entries, you're dividing by zero.\n\n\nPython Error: {e}")
			
if __name__ == "__main__":
	
	root = Tk()
	root.configure(bg = "white")
	BeltSpeedController(root)
	root.mainloop()
