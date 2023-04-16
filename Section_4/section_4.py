import requests
import matplotlib.pyplot as plt
import pandas as pd

# Make API request to retrieve COVID-19 data for Singapore
endpoint = "https://api.covid19api.com/country/singapore/status/confirmed"
response = requests.get(endpoint)
data = response.json()

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Filter DataFrame to keep only the first entry of each month
monthly_data = df[df["Date"].dt.day == 1].copy()
monthly_data["Total Cases"] = monthly_data["Cases"].cumsum()

# Group daily new cases by month and sum them up
df["New Cases"] = df["Cases"].diff()
monthly_cases = df.groupby(pd.Grouper(key="Date", freq="M"))["New Cases"].sum()[:-1]


# Create bar chart of monthly new cases and line graph of total cases
fig, ax1 = plt.subplots()

plt.xticks(rotation=90)

ax1.bar(monthly_cases.index.strftime("%Y-%m"), monthly_cases.values, color="tab:blue")
ax1.set_xlabel("Month")
ax1.set_ylabel("New Cases", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.plot(monthly_cases.index.strftime("%Y-%m"), monthly_data["Total Cases"], color="tab:red")
ax2.set_ylabel("Total Cases", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

plt.title("Monthly New and Total COVID-19 Cases in Singapore")
plt.show()
