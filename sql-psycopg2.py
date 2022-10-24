import psycopg2

# Connect to chinook database
connection = psycopg2.connect(database="chinook")


# build cursor object of the database
cursor = connection.cursor()

# query 1 - select all the records from the artists table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the name column from artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only queen from the artist table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# fetch the results (multiple)
# results = cursor.fetchall()


# fetch the result (single)
results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
