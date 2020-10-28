import tkinter as tk

def f_to_c():
  f = ent_temp.get()
  c = (5/9) * (float(f) - 32)
  lbl_result["text"] = f"{round(c, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_temp = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temp.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command = f_to_c
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, collumn=2, padx=10)

window.mainloop()
