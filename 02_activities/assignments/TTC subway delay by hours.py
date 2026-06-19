import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("/Users/springzhou/DSI/visualization/02_activities/assignments/TTC Subway Delay Data since 2025.csv")

# 2. Keep the rows that contains real delays 
# Because some rows, incidents were logged but min-daley=0
# if we do not drop them, the viz looks different.
df = df[df["Min Delay"] > 0]

# 3. Extract the hour from the "Time" column (format is "HH:MM")
# the times look like "06:10", we only keep the hours
df["Hour"] = df["Time"].str[:2].astype(int)

# 4. Count how many delays happened in each hour.
delays_per_hour = df.groupby("Hour").size()

# 5. Draw the bar chart
x = delays_per_hour.index
y = delays_per_hour.values

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x, y, color="#1f77b4", edgecolor="black")
ax.set_title("TTC Subway Delays by Hour of Day (Since 2025)", fontsize=14, fontweight="bold")
ax.set_xlabel("Hour of day (24h)")
ax.set_ylabel("Number of delays")
ax.set_xticks(range(24))
ax.grid(axis="y", linestyle="--", alpha=0.4)

# 6. Annotate the worst hour.
ax.annotate("peak hour:6am", xy=(6, 835), ha="center", color="hotpink", fontweight="bold")
fig.text(0.99, 0.01,
         "Source: City of Toronto Open Data, TTC Subway Delay Data.",
         ha="right", va="bottom", fontsize=8, color="gray")

plt.tight_layout()
plt.savefig("ttc_delays_by_hour.png", dpi=150)
plt.show()

