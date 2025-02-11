import mysql.connector
from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("400x400+10+10")
# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="pk21",
    password="1234",
    database="phones")
# Get a cursor
cur = cnx.cursor()
# Execute a query
cur.execute("SELECT * FROM phones")
# Fetch one result
row = cur.fetchall()
phones = []
for item in row:
    phones.append(f"{item[0]} {item[1]}")

full_list = Variable(value=phones)
listbox = Listbox(listvariable=full_list, width=50)
listbox.grid(row=0, column=0)
window.mainloop()

# Close connection
cnx.close()
