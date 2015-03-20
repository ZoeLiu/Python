#! /bin/bash

cat turnstile_data_master_with_weather.csv | python ridership_by_weather_mapper.py | sort | python ridership_by_weather_reducer.py
