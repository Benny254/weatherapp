from django.shortcuts import render
import requests

def weather_app(request):
  url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk'
  weather_data = []
  
    
  return render(request, 'main/weather_page.html')
    

  
  return render(request, 'main/weather_page.html', {'weather_data': weather_data})