from django.shortcuts import render
import requests
from django.conf import settings
from datetime import datetime

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = settings.OPENWEATHER_API_KEY  # Store your API key in settings.py
        
        # Call OpenWeatherMap API for current weather
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        
        # Call OpenWeatherMap API for 5-day forecast
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}'
        
        try:
            # Get current weather data
            weather_response = requests.get(weather_url)
            weather_response.raise_for_status()
            weather_data = weather_response.json()
            
            # Get forecast data
            forecast_response = requests.get(forecast_url)
            forecast_response.raise_for_status()
            forecast_data = forecast_response.json()
            
            # Process 5-day forecast
            forecast = []
            for item in forecast_data['list'][::8]:  # Get data for every 24 hours
                date = datetime.fromtimestamp(item['dt'])
                forecast.append({
                    'date': date.strftime('%a'),
                    'temp': round(item['main']['temp']),
                    'icon': item['weather'][0]['icon']
                })
            
            context = {
                'city': city,
                'temperature': round(weather_data['main']['temp']),
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'pressure': weather_data['main']['pressure'],
                'forecast': forecast,
                'error': None
            }
        except requests.RequestException:
            context = {
                'error': 'Could not get weather data. Please try again.'
            }
        except KeyError:
            context = {
                'error': 'City not found. Please try another city.'
            }
    else:
        context = {}
    
    return render(request, 'weather_app/index.html', context)

