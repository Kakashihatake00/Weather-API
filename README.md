# 🌦️ Streamlit Weather App

A simple, real-time weather dashboard built with **Python** and **Streamlit**. This application allows users to search for any city and retrieve current weather conditions (temperature and wind speed) using the Open-Meteo API.

## 🚀 Features

* **City Search:** Type in any city name to find its location.
* **Automatic Geocoding:** Converts city names into Latitude/Longitude automatically.
* **Real-time Data:** Fetches the latest temperature and wind speed.
* **No API Key Required:** Uses the free Open-Meteo public APIs.
* **Error Handling:** Gracefully handles invalid city names or connection errors.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** [Streamlit](https://streamlit.io/)
* **HTTP Requests:** `requests` module
* **Data Source:** [Open-Meteo API](https://open-meteo.com/) (Geocoding & Forecast)

## 📦 Installation

Follow these steps to set up the project locally.

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/weather-app.git](https://github.com/your-username/weather-app.git)
cd weather-app
2. Install dependencies
You need streamlit and requests to run this app.
Bash
pip install streamlit requests

📂 Project Structure
weather-app/
├── app.py              # Main application script
├── README.md           # Project documentation
└── requirements.txt    # Dependencies (optional)
📝 Usage
Enter the name of a city in the text box (e.g., "London", "Mumbai", "New York").

Click the "Get Weather" button.

View the detected country, coordinates, current temperature, and wind speed.

🔮 Future Improvements
Add a 7-day forecast.

Include humidity and precipitation data.

Add a database to save favorite cities (SQL/SQLite).

Improve UI with weather icons.

🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

📄 License
This project is open-source and available under the MIT License.


### Optional: Add a `requirements.txt`
To make it easier for others to install your project, you should also create a file named `requirements.txt` in the same folder with the following content:

```text
streamlit
requests
