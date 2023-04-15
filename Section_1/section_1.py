import datetime
import hashlib
import logging
import os
import re
import shutil
import sys

import pandas as pd

# configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")],
)

# log the start of the script
logging.info("Starting script")

# Define paths for input, output, and archive directories
input_path = "./input/"
output_path = "./output/"
failed_path = "./failed/"
archive_path = "./archive/"

# Create a list of file paths for all files in the input directory
datafiles = [os.path.join(input_path, file) for file in os.listdir(input_path)]

# Exit the program if there are no files to process in the input directory
if not datafiles:
    logging.warning("No files to process in input directory. Exiting...")
    sys.exit()

# Concatenate all data files into a single DataFrame
df = pd.concat(map(pd.read_csv, datafiles))

# Move all processed files to the archive directory
for file in datafiles:
    shutil.move(file, os.path.join(archive_path, os.path.basename(file)))

# Create a new column indicating whether the name column is not null
df["name_check"] = ~df["name"].isna()

# Create a new column indicating whether the email column matches a valid email format
df["email_check"] = df["email"].str.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net)$")

# Convert the date of birth column to datetime format and create a new column indicating whether the age is at least 18
df["date_of_birth"] = df["date_of_birth"].apply(pd.to_datetime, errors="coerce", infer_datetime_format=True)
df["age_check"] = df["date_of_birth"].apply(lambda x: (datetime.date.today().year - x.year) >= 18)

# Convert the mobile number column to string format and create a new column indicating whether the length is 8
df["mobile_no"] = df["mobile_no"].apply(str)
df["mobile_check"] = df["mobile_no"].apply(lambda x: len(x) == 8)

# Split the DataFrame into a successful and failed DataFrame based on the four checks above
success = df["name_check"] & df["email_check"] & df["age_check"] & df["mobile_check"]
failed = df.loc[~success]

# Write the failed DataFrame to a CSV file in the failed directory
if not failed.empty:
    logging.warning(f"Writing {len(failed)} failed records to {failed_path}")
    failed.to_csv(f"{failed_path}failed_{datetime.datetime.now().strftime('%Y%m%d-%H%M')}.csv", index=False)

# Keep only the successful rows in the DataFrame
df = df.loc[success]

# Remove prefixes and suffixes from names and split names into first and last name columns
df[["name"]] = df[["name"]].fillna("")  # Fill missing names with empty string to avoid errors
prefixes_suffixes = ["DDS", "DVM", "Dr.", " II", " III", "Jr.", "MD", "Miss", "Mr.", "Mrs.", "Ms.", "PhD"]
pattern = "|".join(map(re.escape, prefixes_suffixes))
df["name"] = df["name"].apply(lambda n: re.sub(pattern, "", n, flags=re.IGNORECASE).strip() if n.count(" ") > 1 else n)
df[["first_name", "last_name"]] = df["name"].str.split(n=1, expand=True)

# Format date of birth as YYYYMMDD and generate membership ID
df["date_of_birth"] = df["date_of_birth"].dt.strftime("%Y%m%d").apply(str)
df["membership_id"] = df.apply(lambda r: f"{r['last_name']}_{hashlib.sha256(r['date_of_birth'].encode()).hexdigest()[:5]}", axis=1)

# Save processed applications to CSV file
df = df.loc[:, ["first_name", "last_name", "email", "date_of_birth", "membership_id"]]
logging.info(f"Writing {len(df)} records to {output_path}")
df.to_csv(f"{output_path}applications_{datetime.datetime.now().strftime('%Y%m%d-%H%M')}.csv", index=False)

# log the end of the script
logging.info("Script finished")
