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

    # conversion method
    @staticmethod
    def convert_temperature(conversion_type: int, start_temp: float) -> float:
        converted_temp = None
        if conversion_type == 1: # Celsius to Kelvin
            converted_temp = round(start_temp + 273.15, 2)
            print(str(start_temp) + " degree Celsius is equal to " + str(converted_temp) + " degree Kelvin")
        elif conversion_type == 2:  # Celsius to Fahrenheit
            converted_temp = round((start_temp * 9 / 5) + 32, 2)
            print(str(start_temp) + " degree Celsius is equal to " + str(converted_temp) + " degree Fahrenheit")
        elif conversion_type == 3:  # Kelvin to Celsius
            converted_temp = round(start_temp - 273.15, 2)
            print(str(start_temp) + " degree Kelvin is equal to " + str(converted_temp) + " degree Celsius")
        elif conversion_type == 4:  # Kelvin to Fahrenheit
            converted_temp = round((start_temp - 273.15) * 9 / 5 + 32, 2)
            print(str(start_temp) + " degree Kelvin is equal to " + str(converted_temp) + " degree Fahrenheit")
        elif conversion_type == 5:  # Fahrenheit to Celsius
            converted_temp = round((start_temp - 32) * 5 / 9, 2)
            print(str(start_temp) + " degree Fahrenheit is equal to " + str(converted_temp) + " degree Celsius")
        elif conversion_type == 6:  # Fahrenheit to Kelvin
            converted_temp = round((start_temp - 32) * 5 / 9 + 273.15, 2)
            print(str(start_temp) + " degree Fahrenheit is equal to " + str(converted_temp) + " degree Kelvin")
        return converted_temp


run = TemperatureConversion.convert_temperature(TemperatureConversion.get_conversion_type(),
                                                TemperatureConversion.get_float())
