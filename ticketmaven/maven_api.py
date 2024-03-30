import requests

# Replace <your_token> with your actual token value
def create_activity(desc):
    headers = {'Authorization': 'Token cf454946ce19df4376d9c66bcca49c15d7bf8c0c'}

    #  userid 2066037
    # Sandydog0.
    # Data to be sent in the POST request (replace with your actual data)
    data = {
        'activity_type': 'New Activity',
        'description': 'Navigated to Home Tickets section'
    }

    # Send the POST request to add an activity
    response = requests.get('https://ticketmaven.com/api/teams/', headers=headers)

    # Check if the request was successful (status code 201 for created)
    if response.status_code == 200:
        # Print the response content (newly created activity)
        print(response.json()[0])
        username=response.json()[0]["username"]
        password=response.json()[0]["password"]
    else:
        # Print an error message if the request was unsuccessful
        print(f"Error: {response.status_code} - {response.reason}")


create_activity("hello")