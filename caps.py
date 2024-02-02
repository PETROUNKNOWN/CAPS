import tkinter as tk

def convert_to_uppercase():
    input_text = entry.get("1.0", tk.END).strip()
    converted_text = input_text.upper()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)

def copy_to_clipboard():
    output_text = result_text.get(1.0, tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(output_text)

root = tk.Tk()
root.title("CAPSIFY")

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

# Create and customize widgets
entry = tk.Text(root, height=8, width=60, font=font_style, bg=ash_grey, fg=neon_green, padx=0, pady=0, wrap=tk.WORD, highlightbackground=ash_grey, highlightthickness=0)
entry.pack(pady=10)

convert_button = tk.Button(root, text="CAPSIFY", command=convert_to_uppercase, bg=neon_pink, fg=button_text_color, font=font_style, relief=tk.RAISED, bd=0, highlightthickness=0)
convert_button.pack(pady=5)

result_text = tk.Text(root, height=8, width=60, font=font_style, bg=ash_grey, fg=neon_green, padx=0, pady=0, wrap=tk.WORD, highlightbackground=ash_grey, highlightthickness=0)
result_text.pack(pady=10)

copy_button = tk.Button(root, text="COPY", command=copy_to_clipboard, bg=neon_pink, fg=button_text_color, font=font_style, relief=tk.RAISED, bd=0, highlightthickness=0)
copy_button.pack(pady=5)

root.mainloop()
