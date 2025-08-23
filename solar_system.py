'''
Dev: Steve López    Date: 22-08-2025
Description: Get all data about solar system.
'''
import os
import requests

os.system('clear')
def getData(): 
    print(":::SOLAR SYSTEM DATA:::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"

    try:
        #Request to API
        response = requests.get(url)
        response.raise_for_status()
        #Object to JSON (JS Object Notation)
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"API error: {e}")
#Call main function
getData()