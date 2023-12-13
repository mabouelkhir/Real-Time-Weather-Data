##  Real-time Weather Data Dashboard
This project involves the creation of a real-time weather data dashboard using Kafka, Spark, Hive, Apache Airflow (on Docker), and Tableau Desktop. The data will be sourced from the OpenWeatherMap API (https://api.openweathermap.org).

## Architecture 

![image](https://github.com/mabouelkhir/Real-Time-Weather-Data/assets/95728627/098d0945-291f-439f-9187-2385810f963a)


## Applications
This project will start a docker cluster which gives access to the following frameworks/technologies.

| Framework/Technology         | Version            |
| ---------------------------- | ------------------ |
| Hadoop                       | 3.2.1              |
| Mini-Conda                   | 4.12.0             |
| Python                       | 3.9                |
| Spark                        | 3.2.2 (Scala 2.12) |
| Apache Airflow               | 2.3.3              |
| Apache Zeppelin              | 0.10.1             |
| Hive                         | 2.3.2              |
| Confluent Kafka              | 5.4.0-ce           |
| Confluent Schema Registry    | 5.4.0-ce           |
| Confluent Control Center     | 5.4.0              |

## Running the cluster
To start the cluster run the following command from the project directory.
```sh
docker-compose up
```

## Access docker containers
```sh
docker exec -it <container-name> or <container-id> /bin/bash
```
