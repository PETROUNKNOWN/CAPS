import tkinter as tk
import customtkinter as ctk

def convert_to_uppercase():
    input_text = entry.get("1.0", tk.END).strip()
    converted_text = input_text.upper()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)

def convert_to_lowercase():
    input_text = entry.get("1.0", tk.END).strip()
    converted_text = input_text.lower()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)

def copy_to_clipboard():
    output_text = result_text.get(1.0, tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(output_text)

root = ctk.CTk()
root.title("CAPS")

#fonts and colors
font_style = ("Verdana", 12)
bg_color = "#000000"
button_color = "#4caf50"
button_text_color = "white"
neon_green = "#16FF00"
neon_red = "#FF0303"
neon_pink = "#F806CC"
baby_blue = "#068FFF"
ash_grey = "#040D12"

root.configure(bg=bg_color)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

entry=ctk.CTkTextbox(root,height=300,width=600,wrap="word",fg_color="#101010",border_color="#ff0000",border_width=1)
entry.grid(row=0,column=0,columnspan=3,sticky="nsew",pady=(10,5),padx=10)

uppercase_button=ctk.CTkButton(root,width=130,height=40,text="Upper Case",command=convert_to_uppercase,fg_color="#101010",border_color="#ff0000",border_width=1,hover_color="#990000")
uppercase_button.grid(row=1,column=0,sticky="nsew",pady=5,padx=(10,2))
lowercase_button=ctk.CTkButton(root,width=130,height=40,text="Lower Case",command=convert_to_lowercase,fg_color="#101010",border_color="#ff0000",border_width=1,hover_color="#990000")
lowercase_button.grid(row=1,column=1,sticky="nsew",pady=5,padx=2)
copy_button=ctk.CTkButton(root,width=130,height=40,text="Copy",command=copy_to_clipboard,fg_color="#101010",border_color="#ff0000",border_width=1,hover_color="#990000")
copy_button.grid(row=1,column=2,sticky="nsew",pady=5,padx=(2,10))

result_text=ctk.CTkTextbox(root,height=300,width=600,wrap="word",fg_color="#101010",border_color="#ff0000",border_width=1)
result_text.grid(row=2,column=0,columnspan=3,sticky="nsew",pady=(5,10),padx=10)

root.mainloop()
