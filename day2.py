#Q1: Initialize an Array, Add a New Number, and Print the Updated Array (Using NumPy)

import numpy as np

# Initialize an array with 5 numbers
array = np.array([1, 2, 3, 4, 5])

# Add a new number to the array
new_number = 6
array = np.append(array, new_number)

# Print the updated array
print("Updated Array:", array)

#Q2: Add Multiple Elements to an Array Based on User Input (Using NumPy)

import numpy as np

# Create an empty array
array = np.array([])

# Get the number of elements to add from the user
num_elements = int(input("Enter the number of elements to add: "))

# Add elements to the array based on user input
for _ in range(num_elements):
    element = float(input("Enter an element: "))  # Using float for numerical input
    array = np.append(array, element)

# Print the final array
print("Final Array:", array)

#Q3: Read JSON Data from a URL and Print Specific Keys
import json

# JSON data (manually copied from the given URL)
json_data = '''
{
    "date": "2024-08-20",
    "explanation": "The explanation for the image or video.",
    "hdurl": "http://apod.nasa.gov/apod/image/2408/sample.jpg",
    "media_type": "image",
    "service_version": "v1",
    "title": "Sample Title",
    "url": "http://apod.nasa.gov/apod/image/2408/sample.jpg"
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Print the specific keys
print("Explanation:", data.get("explanation"))
print("Title:", data.get("title"))

#Q4: Send a GET Request and Print the JSON Response Using requests Module

import requests

# URL for the API endpoint
url = "http://api.open-notify.org/iss-now.json"

# Send GET request
response = requests.get(url)

# Print JSON response
print("JSON Response:", response.json())


#Q5: Extract and Print Specific Data from the JSON Response

import requests

# URL for the API endpoint
url = "http://api.open-notify.org/iss-now.json"

# Send GET request
response = requests.get(url)
data = response.json()

# Extract and print specific data
print("Latitude:", data["iss_position"]["latitude"])
print("Longitude:", data["iss_position"]["longitude"])
print("Timestamp:", data["timestamp"])

#Q6: Write ISS Location Data to a CSV File Using Pandas

import pandas as pd
import requests
from time import sleep

# URL for the API endpoint
url = "http://api.open-notify.org/iss-now.json"

# List to hold data
data_list = []

# Collect data (at least 100 records)
for _ in range(100):
    response = requests.get(url)
    data = response.json()
    record = {
        "latitude": data["iss_position"]["latitude"],
        "longitude": data["iss_position"]["longitude"],
        "timestamp": data["timestamp"]
    }
    data_list.append(record)
    sleep(1)  # Sleep for a short time to avoid overwhelming the API

# Create DataFrame
df = pd.DataFrame(data_list)

# Write to CSV
df.to_csv("iss_location_data.csv", index=False)

print("Data written to 'iss_location_data.csv'")
