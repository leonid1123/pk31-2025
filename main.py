import mysql.connector
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
row = cur.fetchone()
print(row)
# Close connection
cnx.close()
