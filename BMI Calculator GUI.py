import tkinter
from tkinter import *
    
# Def function for BMI Calculation
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height.entry_get())
    age = int(age_entry.get())
    gender = "Boy" if boy_var.get() else "Girl"

    bmi = weight / (height ** 2)
    bmir = round(bmi, 2)

    if age > 20:
        if bmi < 18.5:
            result_label.config(text=f"Your BMI is: {bmir} and it is underweight.")
        elif bmi < 25:
            result_label.config(text=f"Your BMI is: {bmir} and it is normal weight.")
        elif bmi < 30:
            result_label.config(text=f"Your BMI is: {bmir} and it is overweight.")
        else:
            result_label.config(text=f"Your BMI is: {bmir} and it is obesity.")
            


# window
root = tkinter.Tk()
root.title("BMI Calculator")
root.iconbitmap("icon.ico")
root.minsize(width=300, height=200)
root.resizable(False, False)

# Boy/Girl variables
boy_var = tkinter.BooleanVar()
girl_var = tkinter.BooleanVar()

# Labels and Entries
weight_label = tkinter.Label(root, text="Type your weight in kilograms", font=("Arial", 10, "bold"), fg="black")
weight_label.pack()

weight_entry = tkinter.Entry(root)
weight_entry.pack()

height_label = tkinter.Label(root, text="Type your height in meters", font=("Arial", 10, "bold"), fg="black")
height_label.pack()

height_entry = tkinter.Entry(root)
height_entry.pack()

age_label = tkinter.Label(root, text="Type your age", font=("Arial", 10, "bold"), fg="black")
age_label.pack()

age_entry = tkinter.Entry(root)
age_entry.pack()

boy_checkbox = tkinter.Checkbutton(root, text="Boy", variable=boy_var)
boy_checkbox.pack()

girl_checkbox = tkinter.Checkbutton(root, text="Girl", variable=girl_var)
girl_checkbox.pack()

calculate_button = tkinter.Button(root, text = "Calculate BMI")
calculate_button.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

# Main cycle
root.mainloop()