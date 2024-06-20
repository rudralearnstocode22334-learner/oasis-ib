from tkinter import *
import datetime

def calculate_bmi():
    try:
        height = float(ht_val.get())
        weight = float(wt_val.get())
        bmi = weight / (height ** 2)
        bmi_res.set(f"BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
            cat_bgcol.set("yellow")
            cat_fgcol.set("black")
            cat_lab.grid(row=0, column=0, sticky="w")

            
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            cat_bgcol.set("green")
            cat_fgcol.set("white")
            cat_lab.grid(row=1, column=0, sticky="w")

        elif 25 <= bmi < 29.9:
            category = "Overweight"
            cat_bgcol.set("orange")
            cat_fgcol.set("black")
            cat_lab.grid(row=2, column=0, sticky="w")

        else:
            category = "Obesity"
            cat_bgcol.set("red")
            cat_fgcol.set("white")
            cat_lab.grid(row=3, column=0, sticky="w")
            
        bmi_category.set(f"You are: {category}")
        cat_lab.config(bg=cat_bgcol.get(),fg=cat_fgcol.get())
        bmi_label.grid(row=0, column=0)
        

        show_save_button()

    except ValueError:
        bmi_res.set("Invalid input")
        bmi_category.set("")

def save_results():
    with open("bmi_results.txt", "a") as file:
        file.write(f"Height: {ht_val.get()} m, Weight: {wt_val.get()} kg, {bmi_res.get()},Category: {bmi_category.get()}, TimeStamp: {datetime.datetime.now()}\n")
    bmi_res.set("Results saved")

def show_save_button():
    save_btn.grid(row=0, column=1)

root = Tk()

root.title("BMI Calculator")
root.geometry("600x600")

ht_val = StringVar()
wt_val = StringVar()
bmi_res = StringVar()
bmi_category = StringVar()
cat_bgcol = StringVar()
cat_fgcol= StringVar()

bmi_res.set('')
bmi_category.set('')

up_frm = Frame(root)

h1 = Label(up_frm, text="BMI Calculator", pady=5, font="Poppins 20 bold", fg="#454545", bg="#FFA559")
h1.pack(side=TOP, anchor="n", fill=X)
up_frm.pack(fill=X, side="top")

frm_2 = Frame(root, pady=15, bg="#FFE6C7")

t1 = Label(frm_2, text="Calculate your Body Mass Index", pady=10, font="Poppins 15", fg="#454545", bg="#FFE6C7")
t1.pack(anchor="n")

frm_2.pack()

frm_3 = Frame(root, pady=15, bg="#FFE6C7")

ht_lab = Label(frm_3, text="Height (m): ", padx=15, bg="#FFE6C7", font="Poppins 15 bold")
ht_lab.grid(row=0, column=0, sticky="w")

ht_entr = Entry(frm_3, textvariable=ht_val, bg="#FFA559", font="Poppins 15")
ht_entr.grid(row=0, column=1, sticky="e")

wt_lab = Label(frm_3, text="Weight (kg): ", padx=15, bg="#FFE6C7", font="Poppins 15 bold")
wt_lab.grid(row=1, column=0, sticky="w")

wt_entr = Entry(frm_3, textvariable=wt_val, bg="#FFA559", font="Poppins 15")
wt_entr.grid(row=1, column=1, sticky="e")

frm_3.pack()

frm_4 = Frame(root, bg="#FFE6C7")

calc_btn = Button(frm_4, text="Calculate BMI", command=calculate_bmi, font="Poppins 15", bg="#FFA559",padx=20)
calc_btn.pack(fill=X)

frm_4a = Frame(frm_4, bg="#FFE6C7", pady=15)

bmi_label = Label(frm_4a, textvariable=bmi_res, font="Poppins 15", padx=10,pady=10, bg="#FFA559",relief=SUNKEN)


save_btn = Button(frm_4a, text="Save Results", command=save_results, font="Poppins 15", bg="#FFA559")

frm_4a.pack()
frm_4.pack()

frm_5 = Frame(root, bg="#FFE6C7", pady=20)

cat_lab = Label(frm_5,padx=5, textvariable=bmi_category, font="Poppins 15")


Label(frm_5, text="Underweight: less than 18.5", bg="#FFE6C7", padx=5, pady=3, font="Poppins 10").grid(row=0, column=1, sticky="e")

Label(frm_5, text="Normal weight: 18.5 - 24.9", bg="#FFE6C7", padx=5, pady=3, font="Poppins 10").grid(row=1, column=1, sticky="e")

Label(frm_5, text="Overweight: 25 - 29.9", bg="#FFE6C7", padx=5, pady=3, font="Poppins 10").grid(row=2, column=1, sticky="e")

Label(frm_5, text="Obesity: greater than 30", bg="#FFE6C7", padx=5, pady=3, font="Poppins 10").grid(row=3, column=1, sticky="e")

frm_5.pack()



root.configure(bg="#FFE6C7")
root.mainloop()