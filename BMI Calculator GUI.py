# tkinter
import tkinter
from tkinter import *
    
# Def function for BMI Calculation
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
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
    else:
        per = 0

        percentiles_boy = [5, 10, 25, 50, 75, 85, 90, 95]
        percentiles_girl = [5, 10, 25, 50, 75, 85, 90, 95]

        if gender == "Boy":
            percentiles = percentiles_boy
            
            for boy_age_percentiles in [
            [14.7, 15.1, 15.7, 16.6, 17.6, 18.2, 18.6],
            [14.3, 14.7, 15.3, 16, 16.8, 17.3, 17.7],
            [14, 14.3, 14.9, 15.6, 16.4, 16.9, 17.3],
            [13.8, 14.1, 14.7, 15.4, 16.3, 16.8, 17.3],
            [13.7, 14, 14.6, 15.4, 16.4, 17, 17.5],
            [13.7, 14, 14.7, 15.5, 16.6, 17.4, 18],
            [13.8, 14.1, 14.8, 15.8, 17.1, 18, 18.7],
            [14, 14.3, 15.1, 16.2, 17.6, 18.6, 19.5],
            [14.2, 14.6, 15.5, 16.6, 18.2, 19.4, 20.3],
            [14.6, 15, 15.9, 17.2, 18.9, 20.2, 21.2],
            [15, 15.5, 16.4, 17.8, 19.7, 21, 22.1],
            [15.5, 16, 17, 18.5, 20.4, 21.9, 23],
            [16, 16.5, 17.6, 19.2, 21.2, 22.7, 23.8],
            [16.6, 17.1, 18.3, 19.9, 22, 23.5, 24.6],
            [17.1, 17.7, 18.9, 20.6, 22.7, 24.2, 25.4],
            [17.7, 18.3, 19.6, 21.2, 23.4, 24.9, 26.1],
            [18.2, 18.9, 20.2, 21.9, 24.1, 25.7, 26.9],
            [18.7, 19.4, 20.7, 22.5, 24.8, 26.4, 27.6],
            [19.1, 19.8, 21.2, 23, 25.4, 27.1, 28.4],
        ][age - 2]:
                if bmi < boy_age_percentiles:
                    per = percentiles.pop(0)
                    break

        elif gender == "Girl":
            percentiles = percentiles_girl

            for girl_age_percentiles in [
            [14.4, 14.8, 15.5, 16.4, 17.4, 18, 18.4, 18.8],
            [14, 14.3, 14.9, 15.7, 16.6, 17.2, 17.6, 18],
            [13.7, 14, 14.6, 15.3, 16.2, 16.8, 17.3, 17.7],
            [13.5, 13.8, 14.4, 15.2, 16.1, 16.8, 17.3, 17.8],
            [13.4, 13.7, 14.4, 15.2, 16.3, 17.1, 17.7, 18.3],
            [13.4, 13.8, 14.5, 15.5, 16.7, 17.6, 18.3, 18.9],
            [13.5, 13.9, 14.7, 15.8, 17.3, 18.3, 19.2, 19.8],
            [13.7, 14.2, 15.1, 16.3, 18, 19.1, 20.1, 20.7],
            [14, 14.5, 15.5, 16.9, 18.7, 20, 21, 21.5],
            [14.4, 14.9, 16, 17.5, 19.5, 20.9, 22, 22.5],
            [14.8, 15.4, 16.5, 18.1, 20.2, 21.7, 23, 23.5],
            [15.3, 15.9, 17.1, 18.7, 21, 22.6, 23.9, 24.5],
            [15.8, 16.4, 17.6, 19.4, 21.7, 23.3, 24.7, 25.3],
            [16.3, 16.9, 18.2, 19.9, 22.3, 24, 25.5, 26.1],
            [16.8, 17.4, 18.7, 20.5, 22.9, 24.7, 26.1, 26.7],
            [17.2, 17.8, 19.1, 20.9, 23.4, 25.2, 26.7, 27.3],
            [17.6, 18.2, 19.5, 21.3, 23.8, 25.7, 27.3, 27.9],
            [17.8, 18.4, 19.7, 21.6, 24.2, 26.1, 27.8, 28.3],
            [17.8, 18.5, 19.8, 21.7, 24.5, 26.5, 28.3, 28.8]
        ][age - 2]:
                 if bmi < girl_age_percentiles:
                      per = percentiles.pop(0)
                      break

        if per < 5:
            result_label.config(text=f"Your BMI is: {bmir} and it is underweight.")
        elif per < 85:
            result_label.config(text=f"Your BMI is: {bmir} and it is normal weight.")
        elif per < 95:
            result_label.config(text=f"Your BMI is: {bmir} and it is overweight.")
        else:
            result_label.config(text=f"Your BMI is: {bmir} and it is obesity.")

# window
root = tkinter.Tk()
root.title("BMI Calculator")
root.iconbitmap("icon.ico")
root.minsize(width=300, height=230)
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

calculate_button = tkinter.Button(root, text = "Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

# Main cycle
root.mainloop()