'''
Dev: Steve López
Description:
Get and read data from nasa API about space
Nasa API: https://api.nasa.gov/
https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={API_KEY_HERE}
'''
import os
import requests

os.system('clear')
def get_nasa_data(api_key):
    print(":: NASA INFORMATION ::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}" 
    try: 
        #API request
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data)
        name = data.get("name")
        abs_magnitude = data.get("absolute_magnitude_h")
        diam_km = data["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
        diam_ft = data["estimated_diameter"]["feet"]["estimated_diameter_max"]
        print(f"Nombre del cometa: {name}")
        print(f"Magnitud absoluta h: {abs_magnitude}")
        print(f"Diámetro máximo estimado (km): {diam_km}")
        print(f"Diámetro máximo estimado (ft): {diam_ft}")

    except requests.exceptions.RequestException as e:
        print(f"requests error: {e}")
    
NASA_API_KEY = "wV7Wbl6waSAEfWcMgerLMCDjLb4WIMIAUa3kcykd"
get_nasa_data(NASA_API_KEY)