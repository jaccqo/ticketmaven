import requests

# Replace <your_token> with your actual token value
headers = {'Authorization': 'Token fa80e4af445ecc6dcadf221962720edfe1bccd75'}

# Send GET request to retrieve user profiles
response = requests.get('http://localhost:8000/api/activities/', headers=headers)

# Data to be sent in the POST request (replace with your actual data)
data = {
    'activity_type': 'New Activity',
    'description': 'This is a new activity.'
}

# Send the POST request to add an activity
response = requests.post('http://localhost:8000/api/activities/', headers=headers, data=data)

# Check if the request was successful (status code 201 for created)
if response.status_code == 201:
    # Print the response content (newly created activity)
    print(response.json())
else:
    # Print an error message if the request was unsuccessful
    print(f"Error: {response.status_code} - {response.reason}")