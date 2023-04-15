import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost", database="section_2", user="postgres", password="mysecretpassword"
)

cur = conn.cursor()

with open("members.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    # Loop through each row and insert the data into the database
    count = 0
    while reader and count < 50:
        cur.execute(
            "INSERT INTO members (first_name, last_name, email, date_of_birth, member_id, above_18) VALUES (%s, %s, %s, %s, %s, %s)",
            next(reader),
        )
        count += 1

# Commit the changes to the database and close the cursor and connection objects
conn.commit()
cur.close()
conn.close()
