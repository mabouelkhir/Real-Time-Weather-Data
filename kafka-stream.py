# imports
from kafka import KafkaProducer  # pip install kafka-python
import requests  # pip install requests
import json
from time import sleep
import pendulum


# Define the API endpoint
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"

# Define the Kafka Producer configuration
KAFKA_BOOTSTRAP_SERVERS = ['kafka-broker:29092']  # Change this if your Kafka Broker is running in a different server
KAFKA_TOPIC_NAME = 'weather_project'
KAFKA_PRODUCER_CONFIG = {
    'bootstrap_servers': KAFKA_BOOTSTRAP_SERVERS
}

# Define the function to fetch the weather data from the API
def get_weather_data(api_key):
    cities = [
    {"lat": 33.589886, "lon": -7.603869},
    {"lat": 6.136629, "lon": 1.222186},
    {"lat": 51.509865, "lon": -0.118092},
    {"lat": 33.2316326, "lon": -8.5007116},
    {"lat": 41.902782, "lon": 12.496366},
    {"lat": 35.6895, "lon": 139.6917},
    {"lat": 47.608013, "lon": -122.335167},
    {"lat": 30.033333, "lon": 31.233334},
    {"lat": 40.416775, "lon": -3.703790},
    {"lat": 31.70217, "lon": -6.3494}
]

    
    weather_data_list = []  # List to store weather data for all cities
    
    for city in cities:
        api_url = API_ENDPOINT.format(lat=city.get('lat'), lon=city.get('lon'), API_key=api_key)
        response = requests.get(api_url)

        if response.status_code != 200:
            raise ValueError('API returned unexpected response code')
        
        weather_data = response.json()
        # Transform the weather data schema here
        transformed_data = {
            'weather_main': weather_data['weather'][0]['main'],
            'weather_description': weather_data['weather'][0]['description'],
            'temp': weather_data['main']['temp'],
            'temp_min': weather_data['main']['temp_min'],
            'temp_max': weather_data['main']['temp_max'],
            'pressure': weather_data['main']['pressure'],
            'humidity': weather_data['main']['humidity'],
            'visibility': weather_data['visibility'],
            'wind_speed': weather_data['wind']['speed'],
            'dt': weather_data['dt'],
            'country': weather_data['sys']['country'],
            'sunrise': pendulum.from_timestamp(weather_data['sys']['sunrise']).to_datetime_string(),
            'sunset': pendulum.from_timestamp(weather_data['sys']['sunset']).to_datetime_string(),
            'timezone': weather_data['timezone'],
            'name': weather_data['name']
        }
        
        weather_data_list.append(transformed_data)  # Append transformed weather data to the list
        
    return weather_data_list  # Return the list of weather data for all cities
 # Return the list of weather data for all cities

# Define the main function
def main(api_key):
    try:
        local_timezone = pendulum.timezone('Africa/Casablanca')

        producer = KafkaProducer(**KAFKA_PRODUCER_CONFIG)
        
        weather_data = get_weather_data(api_key)
        for data in weather_data:
            # Convert the time to the local timezone
            data_time = pendulum.from_timestamp(data['dt'])
            data['dt'] = data_time.in_timezone(local_timezone).to_datetime_string()
            
            json_data = json.dumps(data)
            print(json_data)

            producer.send(KAFKA_TOPIC_NAME, json_data.encode())
        
    except Exception as e:
        print(f'Error: {e}')

main('b06bfa49f37cc189bb3e46aee94d5000')