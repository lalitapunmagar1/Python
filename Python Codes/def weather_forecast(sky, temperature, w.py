def weather_forecast(sky, temperature, wind):
    
    if sky == "cloudy" and wind == "none":
        return "It might rain."

    if temperature < 0 and sky == "clear":
        return "It might snow."
   
    if temperature > 30 and wind == "none":
        return "It might be a hot day."
 
    if sky == "clear" and wind == "windy":
        return "It might be a pleasant day."
    return "Weather conditions unclear, please check the forecast later."
def main():
    sky = input("Enter the sky condition (cloudy/clear): ")
    temperature = float(input("Enter the temperature in °C: "))
    wind = input("Enter the wind condition (none/windy): ")
    forecast = weather_forecast(sky, temperature, wind)
    print(forecast)
main()

