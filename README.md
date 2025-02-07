# Weather Project

## Description
A Django-based weather application providing real-time weather information with fetches weather insights from OpenWeather API.

## Live Demo
View the prject - https://weather-project-beta-ashy.vercel.app/

## Prerequisites
- Python (Version 3.9)
- Django
- Git

## Installation
```bash
git clone https://github.com/harshitdohare/weatherapp.git
cd weatherapp

# Create and activate virtual environment
py -3.9 -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Unix/MacOS

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate
```

## Usage
```bash
python manage.py runserver
```
Visit `http://localhost:8000`

## Environment Setup
Create `.env` file:
```
SECRET_KEY=your_django_secret_key
WEATHER_API_KEY=your_api_key
DEBUG=True
```

## Contributing
1. Fork repository
2. Create branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push: `git push origin feature-name`
5. Create Pull Request

