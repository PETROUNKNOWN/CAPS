import tkinter as tk #this should come standard with Python
import pyperclip #pip install this 

def convert_to_uppercase():
    input_text = entry.get("1.0", tk.END).strip()
    converted_text = input_text.upper()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, converted_text)


def copy_to_clipboard():
    output_text = result_text.get(1.0, tk.END).strip()
    pyperclip.copy(output_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("CAPSIFY")

    entry = tk.Text(root, height=12, width=80)
    entry.pack(pady=5)

    convert_button = tk.Button(root, text="CAPSIFY", command=convert_to_uppercase)
    convert_button.pack(pady=5)

    result_text = tk.Text(root, height=12, width=80)
    result_text.pack(pady=5)

    copy_button = tk.Button(root, text="COPY", command=copy_to_clipboard)
    copy_button.pack(pady=5)

    root.mainloop()
