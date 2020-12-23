import tkinter as tk

# function to convert fahrenheit to celsius and send the valeu to lbl_result


def fahrenheit_to_celsius():
    # Convert the value of fahrenheit to celsius
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius ,2)} \N{DEGREE CELSIUS}"


window = tk.Tk()

window.title("Temperature converter")


window.resizable(height=True, width=True)


frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=2, sticky="w")


btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius,
)

lbl_result = tk.Label(master=frm_entry, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=2, pady=10)
lbl_result.grid(row=0, column=3, padx=10)

window.mainloop()
