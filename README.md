# Weather Forecast Application

## Overview
This Python application serves as the culmination of the skills and knowledge gained throughout a comprehensive programming course. Designed to interface with the OpenWeatherMap API, the application provides users with the ability to retrieve and display weather forecast data based on their location, input via city name or zip code. Offering options for temperature display in Celsius, Fahrenheit, and Kelvin, the program emphasizes user-friendliness and accessibility in presenting weather information.

## Features
- **User Input for Location:** Users can enter their location using either a zip code or city name, with an additional prompt for choosing the lookup method.
- **Temperature Unit Selection:** Provides flexibility for users to select their preferred temperature units: Celsius, Fahrenheit, or Kelvin.
- **Multiple Lookups:** Allows users to perform multiple weather lookups for different locations in a single program execution, enhancing usability.
- **Data Validation and Error Handling:** Incorporates validation for user inputs and employs try blocks to manage API requests and responses gracefully, ensuring the program remains robust against invalid data entry and connectivity issues.
- **Readable Output Format:** Displays the weather forecast in a format that is easy to read and understand by the average person, avoiding technical jargon or unreadable data representations.
- **Comments and Documentation:** Utilizes meaningful comments throughout the code to document the program's functionality and decisions, aiding understanding and maintainability.

## Technical Details
- Developed in Python 3, adhering to PEP8 coding conventions for readability and standardization.
- Utilizes the Requests library for handling HTTP requests to the OpenWeatherMap API, ensuring efficient communication with the web service.
- Implements a two-step API call process: a geographical lookup to retrieve latitude and longitude based on user input, followed by a weather data request using the acquired coordinates.
- Incorporates exception handling specific to the requests library to inform users about the success of their connection attempts and to handle potential errors gracefully.

## Development Process
The development of this application followed a structured process, starting from a clear definition of requirements to the iterative development of features. Key stages included:
1. **Program Design:** Outlining the program structure and user flow based on the project requirements.
2. **API Integration:** Establishing a connection to the OpenWeatherMap API and understanding its documentation to accurately retrieve weather data.
3. **Implementation:** Coding the application with a focus on functionality, error handling, and user experience.
4. **Testing and Refinement:** Conducting thorough testing, including "non-happy path" scenarios, to ensure reliability and robustness.

## Usage
Upon launching the program, users are prompted to choose between entering a city name or a zip code for the weather lookup. Following this input, the program requests the preferred temperature unit before fetching and displaying the forecast. The application is designed to repeat this process as desired, offering flexibility for multiple inquiries.

## Conclusion
This weather forecast application represents a practical implementation of programming skills, from API interaction to user interface design and error management. It exemplifies the application of theoretical knowledge in creating a functional tool that provides real-world utility.
