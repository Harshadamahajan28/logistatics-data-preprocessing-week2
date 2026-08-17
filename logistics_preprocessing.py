import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("cleaned_logistics_data.csv")
df = df.drop_duplicates()

date_cols = ["Order_Date", "Dispatch_Date", "Promised_Date", "Delivery_Date"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

df["Delivery_Time_hours"] = df["Delivery_Time_hours"].fillna(df["Delivery_Time_hours"].median())
df["Vehicle_Type"] = df["Vehicle_Type"].fillna("Unknown").astype(str).str.strip().str.title()

df["Delay_Days"] = (df["Delivery_Date"] - df["Promised_Date"]).dt.days
df["Delivery_Status"] = df["Delay_Days"].apply(lambda x: "Delayed" if x > 0 else "On-time")

Q1 = df["Delivery_Time_hours"].quantile(0.25)
Q3 = df["Delivery_Time_hours"].quantile(0.75)
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
outliers = df[(df["Delivery_Time_hours"] < lower) | (df["Delivery_Time_hours"] > upper)]
print("Potential outliers:", len(outliers))

scaler = MinMaxScaler()
cols = ["Distance_km", "Shipment_Weight_kg", "Transport_Cost"]
df[cols] = scaler.fit_transform(df[cols])

df.to_csv("processed_logistics_data.csv", index=False)
print("Preprocessing completed successfully.")
