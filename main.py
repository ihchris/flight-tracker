import requests

# Replace with your FlightAware API key
API_KEY = 'your_flightaware_api_key'

# Example: Track a flight by flight number
def track_flight(flight_number):
    url = f"https://flightxml.flightaware.com/json/FlightXML2/FlightInfoEx?ident={flight_number}&howMany=1"
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'FlightInfoExResult' in data:
            flight_info = data['FlightInfoExResult']['flights'][0]
            print(f"Flight {flight_info['ident']} is {flight_info['status']} from {flight_info['origin']} to {flight_info['destination']}")
        else:
            print("Flight information not available.")
    else:
        print(f"Error fetching data: {response.status_code}")

# Example usage
if __name__ == '__main__':
    flight_number = 'UA123'  # Replace with an actual flight number
    track_flight(flight_number)
