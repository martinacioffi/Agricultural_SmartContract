## Pull weather data from http://meteostat.net
Need to input **location** and **time range**.<br/>
API credentials stored in *config.ini* file.<br/>
Logging data stored in *weather_logging.log* file.<br/>



### Terminology clarifications
After having emailed meteostat and requiring some terminology clarifications, this is what we get:

*precipitation_3* is the precipitation within the previous three hours. Same for *precipitation_6* for the previous six hours.

| Code  | Weather Condition |
| ------------- | ------------- |
| 1  | Clear  |
| 2  | Fair  |
| 3  | Cloudy  |
| 4  | Overcast  |
| 5  | Fog  |
| 6  | Freezing Fog  |
| 7  | Light Rain  |
| 8  | Rain  |
| 9  | Heavy Rain  |
| 10  | Freezing Rain  |
| 11  | Heavy Freezing Rain  |
| 12  | Sleet  |
| 13  | Heavy Sleet  |
| 14  | Light Snowfall  |
| 15  | Snowfall  |
| 16  | Heavy Snowfall  |
| 17  | Rain Shower  |
| 18  | Heavy Rain Shower  |
| 19  | Sleet Shower  |
| 20  | Heavy Sleet Shower  |
| 21  | Snow Shower  |
| 22  | Heavy Snow Shower  |
| 23  | Lightning  |
| 24  | Hail  |
| 25  | Thunderstorm  |
| 26  | Heavy Thunderstorm  |
| 27  | Storm  |