import sqlite3

print("Creando DATABASE")

db = sqlite3.connect(":memory:")
cur = db.cursor()

print("DATABASE CREATED")
print("-----------------------------------------------------")
print("Creando tablas...")

cur.execute('''CREATE TABLE IF NOT EXISTS Customer (
                id integer PRIMARY KEY,
                firstname varchar(255),
                lastname varchar(255) )''')

print("Tabla Customer creada.")

cur.execute('''CREATE TABLE IF NOT EXISTS Item (
                id integer PRIMARY KEY,
                title varchar(255),
                price decimal )''')


print("Tabla Item creada.")

cur.execute('''CREATE TABLE IF NOT EXISTS BoughtItem (
                ordernumber integer PRIMARY KEY,
                customerid integer,
                itemid integer,
                price decimal,
                CONSTRAINT customerid
                    FOREIGN KEY (customerid) REFERENCES Customer(id),
                CONSTRAINT itemid
                    FOREIGN KEY (itemid) REFERENCES Item(id) )''')

print("Tabla BoughtItem creada.")
print("-----------------------------------------------------")
print("Introduciendo datos...")

cur.execute('''INSERT INTO Customer(firstname, lastname)
               VALUES ('Bob', 'Adams'),
                      ('Amy', 'Smith'),
                      ('Rob', 'Bennet');''')

print("Datos de Customer introducidos.")

cur.execute('''INSERT INTO Item(title, price)
               VALUES ('USB', 10.2),
                      ('Mouse', 12.23),
                      ('Monitor', 199.99);''')

print("Datos de Item introducidos.")

cur.execute('''INSERT INTO BoughtItem(customerid, itemid, price)
               VALUES (1, 1, 10.2),
                      (1, 2, 12.23),
                      (1, 3, 199.99),
                      (2, 3, 180.00),
                      (3, 2, 11.23);''') # Discounted price

print("Datos de BoughtItem introducidos")
print("DATOS INTRODUCIDOS")
print("-----------------------------------------------------")

print("Numero de datos en Customer:")
cur.execute("SELECT count(firstName) FROM Customer")
#print("Datos en TABLA Customer: " + numUs )
print(cur.fetchall())

print("Numero de datos en Item:")
cur.execute("SELECT count(title) FROM Item")
print(cur.fetchall())

print("Numero de datos en BoughtItem:")
cur.execute("SELECT count(itemid) FROM BoughtItem")
print(cur.fetchall())
