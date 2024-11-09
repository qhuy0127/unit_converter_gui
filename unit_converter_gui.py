import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Style
        style = ttk.Style()
        style.configure("TLabel", padding=5, font=("Arial", 10))
        style.configure("TButton", padding=5, font=("Arial", 10))
        style.configure("TEntry", padding=5, font=("Arial", 10))
        
        # Conversion types
        self.conversion_types = {
            "Temperature (Celsius ↔ Fahrenheit)": ["c2f", "f2c"],
            "Distance (Kilometers ↔ Miles)": ["km2mi", "mi2km"],
            "Weight (Kilograms ↔ Pounds)": ["kg2lb", "lb2kg"]
        }
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Category selection
        ttk.Label(main_frame, text="Select Category:").grid(row=0, column=0, sticky=tk.W)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(main_frame, textvariable=self.category_var, 
                                         values=list(self.conversion_types.keys()), 
                                         state="readonly", width=30)
        self.category_combo.grid(row=0, column=1, pady=5)
        self.category_combo.bind("<<ComboboxSelected>>", self.update_conversion_options)
        
        # Conversion direction
        ttk.Label(main_frame, text="Select Conversion:").grid(row=1, column=0, sticky=tk.W)
        self.direction_var = tk.StringVar()
        self.direction_combo = ttk.Combobox(main_frame, textvariable=self.direction_var, 
                                          state="readonly", width=30)
        self.direction_combo.grid(row=1, column=1, pady=5)
        
        # Input value
        ttk.Label(main_frame, text="Enter Value:").grid(row=2, column=0, sticky=tk.W)
        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(main_frame, textvariable=self.value_var, width=32)
        self.value_entry.grid(row=2, column=1, pady=5)
        
        # Convert button
        self.convert_btn = ttk.Button(main_frame, text="Convert", command=self.convert)
        self.convert_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Result display
        self.result_var = tk.StringVar()
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, 
                                    font=("Arial", 12, "bold"))
        self.result_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Set initial category
        self.category_combo.set("Temperature (Celsius ↔ Fahrenheit)")
        self.update_conversion_options()

    def update_conversion_options(self, event=None):
        category = self.category_var.get()
        if category == "Temperature (Celsius ↔ Fahrenheit)":
            options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
        elif category == "Distance (Kilometers ↔ Miles)":
            options = ["Kilometers to Miles", "Miles to Kilometers"]
        else:
            options = ["Kilograms to Pounds", "Pounds to Kilograms"]
            
        self.direction_combo['values'] = options
        self.direction_combo.set(options[0])

    def convert(self):
        try:
            # Get the value to convert
            value = float(self.value_var.get())
            
            # Get conversion type
            category = self.category_var.get()
            direction = self.direction_combo.get()
            
            # Perform conversion
            if category == "Temperature (Celsius ↔ Fahrenheit)":
                if direction == "Celsius to Fahrenheit":
                    result = (value * 9/5) + 32
                    self.result_var.set(f"{value}°C = {result:.2f}°F")
                else:
                    result = (value - 32) * 5/9
                    self.result_var.set(f"{value}°F = {result:.2f}°C")
                    
            elif category == "Distance (Kilometers ↔ Miles)":
                if direction == "Kilometers to Miles":
                    result = value * 0.621371
                    self.result_var.set(f"{value} km = {result:.2f} mi")
                else:
                    result = value * 1.60934
                    self.result_var.set(f"{value} mi = {result:.2f} km")
                    
            else:  # Weight conversion
                if direction == "Kilograms to Pounds":
                    result = value * 2.20462
                    self.result_var.set(f"{value} kg = {result:.2f} lb")
                else:
                    result = value * 0.453592
                    self.result_var.set(f"{value} lb = {result:.2f} kg")
                    
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()