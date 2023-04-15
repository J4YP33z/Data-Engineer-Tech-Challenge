## Section 1: Data Pipelines

This script processes CSV files containing member applications and generates a new CSV file with successfully processed applications. The failed applications are written to a separate CSV file in a "failed" directory.

### Requirements

- Python 3.x
- pandas library

### Configuration

The script uses the following directory paths for input, output, failed, and archive directories:

- `./input/` - Input directory containing CSV files with member applications.
- `./output/` - Output directory where processed applications are written.
- `./failed/` - Directory where failed applications are written.
- `./archive/` - Archive directory where processed files are moved to.
- `name_prefixes_suffixes`: A list of prefixes and suffixes to remove from names
  To change any of these parameters, simply edit the corresponding value in the `config.ini` file.

### Script Execution

The script can be executed manually or using a CRONTAB scheduler. If executed manually, run the following command in the terminal from the directory containing the script:

Copy code

`python section_1.py`

If using a CRONTAB scheduler, add the following line to the CRONTAB configuration file:

Copy code

`0 * * * * /usr/bin/python /path/to/script/section_1.py >> /path/to/log/crontab.log 2>&1`

This will run the script every hour at the top of the hour and log the output to a file named `crontab.log` in the specified directory.

### Script Output

The script generates the following output:

- A log file named `app.log` in the script directory, containing logging information about the script's execution.
- A CSV file containing successfully processed member applications in the output directory. The file name is in the format `applications_YYYYMMDD-HHMM.csv`, where `YYYYMMDD-HHMM` is the current date and time.
- A CSV file containing failed member applications in the failed directory. The file name is in the format `failed_YYYYMMDD-HHMM.csv`, where `YYYYMMDD-HHMM` is the current date and time.

### Troubleshooting

If the script fails to execute or produces unexpected results, check the following:

- The input directory contains CSV files with member applications.
- The output, failed, and archive directories exist and have write permissions.
- The pandas library is installed.

If the script produces error messages or exceptions, check the `app.log` file for more information about the error.
