import tkinter as tk

window = tk.Tk()
window.geometry("900x550")
window.title("PROVA")
window.grid_columnconfigure(0, weight=1)


def download_ascii():
    if text_input.get():
        user_input = text_input.get()
        text_response = ("Ciao", user_input)
    else:
        text_response = "Aggiungi una parola o una frase al campo input!"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

#titolo
welcome_label = tk.Label(window,
                         text="Inserisci il tuo nome:",
                         font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

#casella di testo
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)

#bottone
download_button = tk.Button(text="CLICCA QUI", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)


if __name__ == "__main__":
    window.mainloop()
