import csv
import psycopg2
import random

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
        r = next(reader)
        # insert members
        cur.execute(
            f"INSERT INTO members (first_name, last_name, email, date_of_birth, member_id, above_18) VALUES ('{r[0]}', '{r[1]}', '{r[2]}', '{r[3]}', '{r[4]}', {r[5]})"
        )
        # insert random transactions
        for i in range(random.randint(0, 3)):
            cur.execute(
                f"INSERT INTO transactions (member_id, total_price, total_weight) VALUES ('{r[4]}', 0 ,0 )"
            )
        count += 1

# insert items
cur.execute(
    "INSERT INTO items (item_name, manufacturer_name, price, weight) VALUES \
    ('mee siam', 'prima taste', '2.22', '0.3'), \
    ('bee hoon', 'myojo', '2.83', '0.75'), \
    ('cockles', 'ocean waves', '10.0', '0.1'), \
    ('oysters', 'food explorer', '6.0', '0.3')"
)

# insert random transaction detals
cur.execute("SELECT COUNT(*) FROM transactions")
num_rows = cur.fetchone()[0]
for txn_id in range(1, num_rows + 1):
    for item_id in range(1, 5):
        cur.execute(
            f"INSERT INTO transaction_details (transaction_id, item_id, quantity) VALUES ({txn_id}, {item_id}, {random.randint(1, 5)})"
        )

# update transactions
cur.execute(
    """
    UPDATE transactions t
    SET total_price = (
        SELECT SUM(price * quantity)
        FROM transaction_details td
        JOIN items i ON td.item_id = i.item_id
        WHERE td.transaction_id = t.transaction_id
    ),
    total_weight = (
        SELECT SUM(weight * quantity)
        FROM transaction_details td
        JOIN items i ON td.item_id = i.item_id
        WHERE td.transaction_id = t.transaction_id
    );
    """
)

# Commit the changes to the database and close the cursor and connection objects
conn.commit()
cur.close()
conn.close()
