# Weather Wizard

This is a Python script that retrieves the weather forecast for a given city using the OpenWeatherMap API.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed
- Required Python modules: `requests`, `json`, `sys`, `os`, `dotenv`
- An API key from OpenWeatherMap

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/onkarr19/weatherWizard.git
   ```

2. Change into the project directory:

    ```bash
    cd weatherWizard
    ```

3. Install the required Python modules:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the project directory and add your OpenWeatherMap API key:

    ```plaintext
    OPENWEATHERAPP_API_KEY=your_api_key
    ```

## Usage

To retrieve the weather forecast for a specific city, run the following command:

```bash
python main.py <city_name>
```

Replace <city_name> with the name of the city you want to get the weather forecast for.