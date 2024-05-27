#DSC 510
#Week 12
#Final Programming Project
#Author Salina Najera
#11/15/2022

import requests as req
def getUnit():
    while True:
        choice = int(input('\nChoose a temperature unit to show the temperature:\n1. Celcius\n2. Fahrenheit.\n3. Kelvin\n'))
        if choice == 1:
            return 'metric'
        elif choice == 2:
            return 'imperial'
        elif choice == 3:
            return ''
        else:
            print('Invalid Selection.\n')

def printData(data):

    try:
        currTemp = data['main']['temp']
        minTemp = data['main']['temp_min']
        maxTemp = data['main']['temp_max']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
    except KeyError:
        print('\nInvalid Coordinates, City or ZipCode\n')
        return
    print(f"Current Weather Conditions For {data['name']}")
    print(f"Current Temperature: {currTemp} degrees")
    print(f"High Temperature: {maxTemp} degrees")
    print(f"Low Temperature: {minTemp} degrees")
    print(f"Pressure: {pressure}hPa")
    print(f"Humidity: {humidity}%")
    print(f"Descriptive: {description}")

def main():
    API_key = '58fbdfbb31c6f4211fb7442ffd537111'
    api = ''
    headers = {'Accept': 'application/json'}
    try:
        userInput = int(input('\n1. Check weather by Coordinates.\n2. Check weather by City Name.\n3. Check weather by Zip Code.\n\nSelect an option from above: '))
        while True:
            if userInput == 1:
                limit = 1
                lat = float(input('Enter Latitude of the location: '))
                lon = float(input('Enter Longitute of the location: '))
                # lat = 51.5072
                # lon = 0.1276
                long_lat_api = f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API_key}'

                geoCode = req.get(long_lat_api, headers= headers)
                geoCodeData = geoCode.json()
                try:
                    stateCode = geoCodeData[0]['state']
                    city = geoCodeData[0]['name']
                    unit = getUnit()
                    if unit == '':
                        api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}'
                    else:
                        api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}&units={unit}'
                    break
                except KeyError:
                    print('Invalid coordinates. Try Again.\n')
                    continue
            elif userInput == 2:
                city = input('Enter a valid city name: ')
                stateCode = input('Enter the state of the city (must be the complete state name, no abbreviations): ')
                unit = getUnit()
                if unit == '':
                    api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}'
                else:
                    api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}&units={unit}'
                break
            elif userInput == 3:
                zipCode = input('Input a valid zip code: ')
                city = zipCode+' Area'
                unit = getUnit()
                if unit == '':
                    api = f'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={API_key}'
                else:
                    api = f'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={API_key}&units={unit}'
                break
            else:
                print('Invalid selection.\n')
                main()

        weather = req.get(api, headers= headers)
        weatherData = weather.json()
        printData(weatherData)

        stop = input("Do you want to continue? if yes then type 'y', otherwise press any key: ")

        if stop.lower() == 'y':
            main()
        else:
            exit()
    except ValueError:
        print('Invalid selection.\n')
        main()



if __name__ == '__main__':
    print('----------------------------------------------')
    print('--------WELCOME TO WEATHER DATA STATION--------')
    print('----------------------------------------------')
    main()
