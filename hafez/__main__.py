from os import system

def run():
    try:
        system("uvicorn hafez.main:app")
    except:
        print("Can't run uvirorn")

