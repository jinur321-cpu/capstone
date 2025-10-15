# ============================================================
# Capstone Project: Weather Data Analysis and Visualization
# ============================================================

# 🧰 Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 📂 Step 1: Load the Dataset
# ============================================================

# You can replace this with your actual CSV file
# Example: data = pd.read_csv("weather_data.csv")

# For demonstration, let's create a sample dataset
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Temperature': np.random.normal(30, 5, 365),   # Avg 30°C ± 5
    'Humidity': np.random.uniform(40, 90, 365),    # 40–90%
    'WindSpeed': np.random.uniform(2, 10, 365),    # 2–10 m/s
    'Rainfall': np.random.choice([0, 0, 0, 5, 10, 20, 50], 365)  # Random rainfall
})

print("✅ Dataset Loaded Successfully!")
print(data.head())

# ============================================================
# 🧹 Step 2: Data Cleaning
# ============================================================

print("\nChecking for missing values...")
print(data.isnull().sum())

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Drop any missing values if found
data = data.dropna()

# Remove duplicates (if any)
data = data.drop_duplicates()

print("\n✅ Data cleaned successfully!")

# ============================================================
# 📊 Step 3: Data Analysis
# ============================================================

# Average monthly temperature
monthly_avg_temp = data.groupby(data['Date'].dt.month)['Temperature'].mean()

# Total annual rainfall
annual_rainfall = data.groupby(data['Date'].dt.year)['Rainfall'].sum()

# Correlation between variables
correlation = data.corr(numeric_only=True)

print("\n📈 Average Monthly Temperature:")
print(monthly_avg_temp)

print("\n🌧️ Annual Rainfall:")
print(annual_rainfall)

print("\n🔗 Correlation Matrix:")
print(correlation)

# ============================================================
# 📉 Step 4: Data Visualization
# ============================================================

plt.style.use('seaborn-v0_8')
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Temperature'], color='orange')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# ------------------------------------------------------------

plt.figure(figsize=(8,5))
monthly_avg_temp.plot(kind='bar', color='skyblue')
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# ------------------------------------------------------------

plt.figure(figsize=(8,5))
plt.bar(annual_rainfall.index, annual_rainfall.values, color='teal')
plt.title("Annual Rainfall")
plt.xlabel("Year")
plt.ylabel("Total Rainfall (mm)")
plt.show()

# ------------------------------------------------------------

plt.figure(figsize=(8,5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Between Weather Parameters")
plt.show()

# ============================================================
# 🧾 Step 5: Insights / Summary
# ============================================================

print("\n====================== Summary ======================")
print("📊 The weather data was analyzed successfully.")
print("🌡️ Monthly temperature trends and annual rainfall visualized.")
print("💧 Correlation heatmap shows how parameters relate.")
print("=====================================================")

# Example conclusion message
print("""
Conclusion:
-----------
After analyzing the weather data, we observed that temperature tends to rise during summer months,
while rainfall is concentrated during monsoon season. A moderate negative correlation between
humidity and temperature suggests that high humidity often corresponds to lower temperatures.
""")
