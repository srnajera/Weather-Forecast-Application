#DSC 510
#Week 12
#Final Programming Project
#Author Salina Najera
#11/14/2022

import requests as req
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
                    api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}'
                    break
                except KeyError:
                    print('Invalid coordinates. Try Again.\n')
                    continue
            elif userInput == 2:
                city = input('Enter a valid City Name: ')
                stateCode = input('Enter a valid State of the City: ')
                api = f'https://api.openweathermap.org/data/2.5/weather?q={city},{stateCode}&appid={API_key}'
                break
            elif userInput == 3:
                zipCode = input('Input a valid zip code: ')
                city = zipCode+' Area'
                api = f'https://api.openweathermap.org/data/2.5/weather?zip={zipCode}&appid={API_key}'
                break
            else:
                print('Invalid selection.\n')
                main()
        try:
            weather = req.get(api, headers= headers)
            weatherData = weather.json()
            temp = weatherData['main']['temp']
            celcius = temp - 273.15
            fahren = (celcius * 1.8) + 32
            while True:
                choice = int(input('\nChoose a temperature unit to show the temperature:\n1. Celcius\n2. Fahrenheit.\n3. Kelvin\n'))
                if choice == 1:
                    print(f'\nTemperature of {city} in celcius is: {round(celcius,2)}\n')
                    break
                elif choice == 2:
                    print(f'\nTemperature of {city} in fahrenheit is: {round(fahren,2)}\n')
                    break
                elif choice == 3:
                    print(f'\nTemperature of {city} in kelvin is: {round(temp,2)}\n')
                    break
                else:
                    print('Invalid Selection.\n')
        except KeyError:
            print('\nInvalid Coordinates, City or ZipCode\n')

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
