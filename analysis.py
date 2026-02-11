import pandas as pd

# Load dataset
df = pd.read_csv("data/mumbai_waste_resource_2024.csv")

print(df)

# Calculate daily economic value
df["daily_value_rs"] = df["quantity_mt_per_day"] * df["value_rs_per_mt"]

# Calculate daily CO2 savings
df["daily_co2_saved_kg"] = df["quantity_mt_per_day"] * df["co2_saved_kg_per_mt"]

# Summary
total_value = df["daily_value_rs"].sum()
total_co2 = df["daily_co2_saved_kg"].sum()

print("\nSUMMARY METRICS")
print(f"Total potential economic value per day: ₹{total_value:,.0f}")
print(f"Total potential CO₂ savings per day: {total_co2/1000:.2f} metric tonnes")

