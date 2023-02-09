def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit = 32
print(f'{fahrenheit}°F is equivalent to {fahrenheit_to_centigrade(fahrenheit)}°C.')

