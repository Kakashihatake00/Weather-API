import requests
import streamlit as st
st.title("Welcome to the APP") 
st.write("Type city name to get the weather")
city_name = st.text_input("Enter the city name")

if st.button("Get Weather"):
    try:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": city_name,
            "count" : 1

        }
        geo_r = requests.get(geo_url, params=geo_params)
        geo_data = geo_r.json()
        if "results" in geo_data:

    
            url = "https://api.open-meteo.com/v1/forecast"
            location = geo_data["results"][0]
            lat = location["latitude"]
            lon = location["longitude"]
            country = location.get("country", "Unknown")
            st.success(f"Found {city_name} in {country} (Lat: {lat}, Lon: {lon})")
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": "true"
            }
            r = requests.get(url, params=params)
            weather = r.json()
            current = weather['current_weather']

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Temperature", f"{current['temperature']} °C")
            with col2:
                st.metric("Wind Speed", f"{current['windspeed']} km/h")

        # added comment here 
        else:
            st.error("Error: Could not fetch weather. Check coordinates.")
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
