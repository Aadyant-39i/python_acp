import tkinter as tk

def show_bio():
    name = name_entry.get()
    age = age_entry.get()
    city = city_entry.get()
    hobby = hobby_entry.get()

    bio = "Name: " + name + "\n"
    bio = bio + "Age: " + age + "\n"
    bio = bio + "City: " + city + "\n"
    bio = bio + "Hobby: " + hobby

    result_label.config(text=bio) 


window = tk.Tk()
window.title("Personal Bio Form")
window.geometry("400x400")

title_label = tk.Label(window, text="Personal Bio Form", font=("Arial", 18))
title_label.pack()

name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()

city_label = tk.Label(window, text="City:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

hobby_label = tk.Label(window, text="Hobby:")
hobby_label.pack()

hobby_entry = tk.Entry(window)
hobby_entry.pack()

submit_button = tk.Button(window, text="Show Bio", command=show_bio)
submit_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()