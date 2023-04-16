## Section 2: Databases

This project contains several files that serve different purposes related to a database implementation.

- ER_diagram.png: This file illustrates the Entity-Relationship (ER) diagram for the database schema.
- Dockerfile: This file sets up a Postgres database by utilizing the create_tables.sql file and several environment variables. The commands used to build and run the Postgres container are also provided in the file.
- create_tables.sql: This file contains the Data Definition Language (DDL) statements to create the necessary **tables and indexes** for the database schema.
- section2.py and members.csv: These files are used to populate the tables. The Python script (section2.py) utilizes the psycopg2 library to connect to the Postgres database and parse the members.csv file to fill up the members table.
- top_3_items_bought.sql and top_10_spending_members.sql: These files contain the SQL queries implemented to answer the questions posed in the assignment.

## Usage

To use the files in this project, follow these steps:

1.  Build the Docker image using the following command:
    `docker build -t pg-img .`

2.  Run the Docker container using the following command:
    `docker run --name pg-container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d pg-img`

3.  section2.py requires the psycopg2 library to be installed. Run the section2.py script to populate the tables in the database by running the following command:
    `python section2.py`

4.  Run the SQL queries in the top_3_items_bought.sql and top_10_spending_members.sql files to retrieve the desired information from the database.
