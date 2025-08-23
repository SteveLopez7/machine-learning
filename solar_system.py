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

def showPlanets():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    data = requests.get(url).json()
    print("\n::: PLANETS :::")
    for b in data["bodies"]:
        if b["isPlanet"]:
            print("-", b["englishName"])

def showMoons():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    data = requests.get(url).json()
    print("\n::: MOONS :::")
    for b in data["bodies"]:
        if b.get("aroundPlanet"):
            print("-", b["englishName"])

def showStars():
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isComet,eq,true"
    data = requests.get(url).json()
    print("\n::: STARS :::")
    for b in data.get("bodies", []):
        print("-", b["englishName"])

def showAsteroid():
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isComet,eq,true"
    data = requests.get(url).json()
    print("\n::: ASTEROID :::")
    for b in data.get("bodies", []):
        print("-", b["englishName"])

def showComets():
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter[]=isComet,eq,true"
    data = requests.get(url).json()
    print("\n::: COMETS :::")
    for b in data.get("bodies", []):
        print("-", b["englishName"])

def mainMenu():
    while True:
        print("\n:::: MAIN MENU ::::")
        print("1. Planetas")
        print("2. Moons")
        print("3. Cometas")
        print("4. Stars")
        print("5. Asteroid")
        print("6. Salir")

        choice = input("Seleccione una opción: ")
        if choice == "1":
            showPlanets()
        elif choice == "2":
            showMoons()
        elif choice == "3":
            showComets()
        elif choice == "4":
            showStars()
        elif choice == "5":
            showAsteroid()        
        elif choice == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


# #Call main function
# getData()
mainMenu()
