import requests
import json  # Import the json module

URL = "http://127.0.0.1:8000/api/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# get_data()



def post_data():
    data={
        'name':'Salman',
        'roll_number':77,
        'department':'BBA'
    }
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# post_data()



def update_data():
    # Define your data as a Python dictionary
    data = {
        'id': 1,
        'name': 'Hadi',
        'roll_number': 92,
        'department': 'CS'
    }

    # Convert the data dictionary to a JSON string
    headers={'content-Type':'application/json'}
    json_data = json.dumps(data)

    try:
        # Send the PUT request with the JSON data in the request body
        r = requests.put(url=URL,headers=headers,data=json_data)

        # Check the HTTP status code to ensure the request was successful
        if r.status_code == 200:
            # Attempt to parse the JSON response
            response_data = r.json()
            print(response_data)
        else:
            print(f"Request failed with status code: {r.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")

# Call the update_data() function to make the PUT request
update_data()


def delete_data():
    data={
        'id':9,
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)

# delete_data()
