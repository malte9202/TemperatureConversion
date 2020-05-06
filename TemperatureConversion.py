class TemperatureConversion:
    # method to get the type of conversion
    @staticmethod
    def get_conversion_type() -> int:
        conversion_type = None
        print(
            "(1) Convert Celsius to Kelvin\n(2) Convert Celsius to Fahrenheit\n(3) Convert Kelvin to Celsius\n" +
            "(4) Convert Kelvin to Fahrenheit\n(5) Convert Fahrenheit to Celsius\n(6) Convert Fahrenheit to Kelvin"
        )
        while conversion_type not in [1, 2, 3, 4, 5, 6]:
            try:
                conversion_type = int(input("Choose a type of conversion by entering a number from 1 to 6: "))
                if conversion_type not in [None, 1, 2, 3, 4, 5, 6]:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 6 to choose the type of conversion.")
        return conversion_type

    # method to get the temperature that has to be converted
    @staticmethod
    def get_float(msg="Please enter the temperature to convert: ") -> float:
        while True:
            try:
                start_temp = float(input(msg))
                return start_temp
            except ValueError:
                print("The temperature has to be a numerical value.")

    @staticmethod
    def convert_celsius_to_kelvin(start_temp) -> float:
        converted_temp = round(start_temp + 273.15, 2)
        return converted_temp

    @staticmethod
    def convert_celsius_to_fahrenheit(start_temp) -> float:
        converted_temp = round((start_temp * 9 / 5) + 32, 2)
        return converted_temp

    @staticmethod
    def convert_kelvin_to_celsius(start_temp) -> float:
        converted_temp = round(start_temp - 273.15, 2)
        return converted_temp

    @staticmethod
    def convert_kelvin_to_fahrenheit(start_temp) -> float:
        converted_temp = round((start_temp - 273.15) * 9 / 5 + 32, 2)
        return converted_temp

    @staticmethod
    def convert_fahrenheit_to_celsius(start_temp) -> float:
        converted_temp = round((start_temp - 32) * 5 / 9, 2)
        return converted_temp

    @staticmethod
    def convert_fahrenheit_to_kelvin(start_temp) -> float:
        converted_temp = round((start_temp - 32) * 5 / 9 + 273.15, 2)
        return converted_temp

    @staticmethod
    def calculate_and_print_result(conversion_type, start_temp):
        if conversion_type == 1:
            print(start_temp, "°C is equal to ", TemperatureConversion.convert_celsius_to_kelvin(start_temp), "K")
        elif conversion_type == 2:
            print(start_temp, "°C is equal to ", TemperatureConversion.convert_celsius_to_fahrenheit(start_temp), "°F")
        elif conversion_type == 3:
            print(start_temp, "K is equal to ", TemperatureConversion.convert_kelvin_to_celsius(start_temp), "°C")
        elif conversion_type == 4:
            print(start_temp, "K is equal to ", TemperatureConversion.convert_kelvin_to_fahrenheit(start_temp),"°F")
        elif conversion_type == 5:
            print(start_temp, "°F is equal to ", TemperatureConversion.convert_fahrenheit_to_celsius(start_temp), "°C")
        elif conversion_type == 6:
            print(start_temp, "°F is equal to ", TemperatureConversion.convert_fahrenheit_to_kelvin(start_temp), "K")


TemperatureConversion.calculate_and_print_result(TemperatureConversion.get_conversion_type(), TemperatureConversion.get_float())




