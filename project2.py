import pandas as pd
import requests
import json
from datetime import datetime, timedelta

# Function to get data for a specific date
def get_vegetable_data(date):
    """
    Fetches vegetable market data for a given date from the API.
    
    Args:
    date (str): The date in YYYY-MM-DD format for which to fetch data.
    
    Returns:
    list: A list of vegetable data dictionaries or an empty list if the request fails.
    """
    url = f"https://vegetablemarketprice.com/api/dataapi/market/uttarpradesh/daywisedata?date={date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json().get("data", [])
    except requests.RequestException as e:
        print(f"Error fetching data for {date}: {e}")
        data = []
    
    return data

# Initialize a list to store the data
data_list = []

# Define the date range for the data collection
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)

# Loop through each date in the specified range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    daily_data = get_vegetable_data(date_str)
    
    # Process each entry in the daily data
    for entry in daily_data:
        # Append the processed entry to the data list
        data_list.append({
            "Date": date_str,
            "State": "Uttar_Pradesh",
            "Vegetable Name": entry.get("vegetablename", "N/A"),
            "Wholesale Price": entry.get("price", "N/A"),
            "Retail Price": entry.get("retailprice", "N/A"),
            "Mall Price": entry.get("shopingmallprice", "N/A"),
            "Unit": entry.get("units", "N/A"),
            "Vegetable Image": entry.get("vegetableimage", "N/A")
        })
    
    # Move to the next day
    current_date += timedelta(days=1)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data_list)

# Save the DataFrame to a CSV file
csv_path = r"C:\Users\prakh\Desktop\cei interships\project 2\stock_data.csv"

df.to_csv(csv_path, index=False)

# Display the first few rows of the DataFrame
print("Data scraping and saving completed.")
print(df.head())
