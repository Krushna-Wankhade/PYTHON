# importing required libraries
import mysql.connector





dataBase = mysql.connector.connect( host="localhost",
user="root", password="12345678@aB", database="mydatabase58"
)





sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" 
values = [
('Aditya', 'Bawda'),
('Ganesh', 'Akudri'),
('Sanket', 'Pimpri'),
('Yash', 'Bhosari'),
('Ritesh', 'Karvenagar'),
('Swaraj', 'Moshi'),
]
