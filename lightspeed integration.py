import requests
import json
import smtplib, ssl

# Set your Lightspeed POS API credentials
api_key = "lsxs_pt_vLgHxuH8mAJbIpTkxtPFTdrX2bUlXaNI"
base_url = "https://restorationthrift.vendhq.com/api/2.0"

# Define the endpoint to retrieve sales data
endpoint = "/security_events"
# Make an API request to get sales data
response = requests.get(base_url + endpoint, headers={"Authorization": f"Bearer {api_key}"})
sales_data = response.json()

formatted_json = json.dumps(sales_data, indent=4, sort_keys=True, separators=(',', ': '))
print("Sales data:")
print(formatted_json)


# Extract relevant data and calculate the average
total_sales_amount = sum(sale['amount'] for sale in sales_data['Sale'])
average_amount = total_sales_amount / len(sales_data['Sale'])

# Display the average amount
print(f"Average Sales Amount: ${average_amount:.2f}")
