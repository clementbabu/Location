import requests
import json
import time

def get_api_data():
    # Replace 'your_api_endpoint' with the actual API endpoint you want to query
    api_url = 'https://tracking.vigitech.uk/api/positions'
    username = 'ace@uel.ac.uk'
    password = '3PAVzsDLGk'
    try:
        response = requests.get(api_url, auth=(username, password))
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

def save_data_to_file(data):
    timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'data_{timestamp}.json'
    
    with open(filename, 'w') as file:
        json.dump(data, file)
    
    print(f"Data saved to {filename}")

def main():
    while True:
        api_data = get_api_data()
        
        if api_data:
            save_data_to_file(api_data)
        

if __name__ == "__main__":
    main()
