# myWeather
A simple Python script to get command line weather using api.weather.gov
- The return city isn't always what is given, but relatively close. TODO.

# Usage
```
$ export GEOCODE_API_KEY=your_geocode_api_key
$ python3 -m venv py3.13.1_weather_venv
$ source py3.13.1_weather_venv/bin/activate
(py3.13.1_weather_venv)$ python myWeather.py

Enter a location: new hope, pa

Weather forecast for New Hope, PA

Forecast:

---
This Afternoon: A chance of snow. Cloudy, with a high near 29. North wind around 5 mph. Chance of precipitation is 30%. New snow accumulation of less than half an inch possible.


---
Tonight: A slight chance of snow before 11pm. Mostly cloudy, with a low around 19. Northwest wind 5 to 15 mph. Chance of precipitation is 20%. New snow accumulation of less than half an inch possible.


---
Tuesday: Mostly sunny, with a high near 31. Northwest wind 15 to 20 mph, with gusts as high as 40 mph.


---
Tuesday Night: Mostly clear, with a low around 18. Northwest wind 10 to 15 mph, with gusts as high as 25 mph.


---
Wednesday: Sunny, with a high near 30. Northwest wind 10 to 15 mph, with gusts as high as 30 mph.


---
Wednesday Night: Partly cloudy, with a low around 15.


---
Thursday: Mostly sunny, with a high near 30.


---
Thursday Night: Mostly clear, with a low around 21.


---
Friday: Sunny, with a high near 36.


---
Friday Night: Mostly cloudy, with a low around 22.


---
Saturday: A slight chance of snow after 7am. Partly sunny, with a high near 35.


---
Saturday Night: A slight chance of snow before 7pm. Partly cloudy, with a low around 22.


---
Sunday: Mostly sunny, with a high near 37.


---
Sunday Night: Partly cloudy, with a low around 20.
```
