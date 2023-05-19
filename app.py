import tkinter as tk
import tkinter.ttk as ttk
import pymssql
import pandas as pd

conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')

query = 'SELECT * FROM Utente'
df = pd.read_sql(query, conn)

window = tk.Tk()
width = window.winfo_screenwidth()
height  = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

window.title("PROVA")
window.grid_columnconfigure(0, weight=1)


def get_dataframe():
    #Viene creato un oggetto LabelFrame chiamato result_frame all'interno della finestra
    #window con un titolo "Risultato" e con un padding di 10 pixel sia orizzontale che verticale.
    result_frame = tk.LabelFrame(window, text="Risultato", padx=10, pady=10)
    #result_frame viene posizionato nella griglia della finestra nella riga 1 e nella colonna 0,
    #con il ridimensionamento "WE" (ovvero orizzontale) e con un padding di 10 pixel sia orizzontale che verticale.
    result_frame.grid(row=1, column=0, sticky="WE", padx=10, pady=10)


    #Viene creato un oggetto TreeView chiamato treeview all'interno di result_frame
    treeview = ttk.Treeview(result_frame)
    #treeview viene confezionato per riempire tutto lo spazio disponibile all'interno di result_frame utilizzando pack(fill="both", expand=True).
    treeview.pack(fill="both", expand=True)


    #Viene creato un elenco delle colonne del dataframe df chiamato columns.
    columns = list(df.columns)
    #Viene impostato l'attributo "columns" di treeview con l'elenco delle colonne.
    treeview["columns"] = columns

    
    treeview.column("#0", width=0, stretch=tk.NO)  #nasconde la prima colonna vuota
    for column in columns:
        treeview.column(column, anchor=tk.CENTER)#L'ancoraggio al centro (anchor=tk.CENTER) si riferisce alla posizione di allineamento del contenuto all'interno di una colonna della Treeview.
        treeview.heading(column, text=column)

    # Viene inserito il contenuto del dataframe all'interno di treeview. Viene iterato su ogni riga del dataframe utilizzando il metodo iterrows()
    for index, row in df.iterrows():
        treeview.insert("", tk.END, text=index, values=list(row))

    #Viene regolata la larghezza delle colonne in base al contenuto.
    for column in columns:
        treeview.column(column, width=tk.FIXED)

# Viene creato un oggetto Button chiamato download_button con il testo "CLICCA QUI" e il comando get_dataframe() associato al click del pulsante.
download_button = tk.Button(text="CLICCA QUI", command=get_dataframe)
#download_button viene posizionato nella griglia della finestra nella riga 0 e nella colonna 0, con il ridimensionamento "WE" (ovvero orizzontale), con un padding di 10 pixel sia orizzontale che verticale.
download_button.grid(row=0, column=0, sticky="WE", pady=10, padx=10)

if __name__ == "__main__":
    window.mainloop()
