'''Ask the user for a temperature in Celsius (string input). Convert it to float, then calculate and 
print temperature in Fahrenheit.Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32'''

temparature = str(input("Weather temparature in degree celcius: "))

CelciusTemp = float(temparature)
print(f"The temparature in Floating point is {CelciusTemp}")
FarenheitTemp = (CelciusTemp * (9/5)) + 32

print(f"{CelciusTemp} Degree Celcius = {FarenheitTemp} Farenheit")