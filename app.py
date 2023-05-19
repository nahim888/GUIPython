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
    result_frame = tk.LabelFrame(window, text="Risultato", padx=10, pady=10)
    result_frame.grid(row=1, column=0, sticky="WE", padx=10, pady=10)

    treeview = ttk.Treeview(result_frame)
    treeview.pack(fill="both", expand=True)

    columns = list(df.columns)
    treeview["columns"] = columns

    # Configuring treeview columns
    treeview.column("#0", width=0, stretch=tk.NO)  # Hide the first empty column
    for column in columns:
        treeview.column(column, anchor=tk.CENTER)
        treeview.heading(column, text=column)
#y
    # Inserting data into treeview
    for index, row in df.iterrows():
        treeview.insert("", tk.END, text=index, values=list(row))

    # Adjusting the width of the columns based on the content
    for column in columns:
        treeview.column(column, width=tk.FIXED)

# bottone
download_button = tk.Button(text="CLICCA QUI", command=get_dataframe)
download_button.grid(row=0, column=0, sticky="WE", pady=10, padx=10)

if __name__ == "__main__":
    window.mainloop()
