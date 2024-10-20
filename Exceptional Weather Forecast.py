try:
    # Task 1 / # Task 2 - Catching a ValueError
    temperature_input = int(input("Enter the temperature in degrees Fahrenheit: "))
except (ValueError):
        print("Entry is invalid. Please enter a numerical temperature.")
else: 
    # Task 2 - function to convert / Task # 3 - else block to print the conversion
    def temperature_conversion(temperature_input):
        celsius_temperature = (temperature_input - 32) * 5/9
        return celsius_temperature

    celsius_conversion = temperature_conversion(temperature_input)

    print(f"{temperature_input}°F converted to celsius is {celsius_conversion}°C.")
# Task 4:
finally:
     print("Thanks for using the Fahrenheit to Celsius converter!")
