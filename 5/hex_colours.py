COLOURS = {
    "AliceBlue": "#f0f8ff",
    "Blue": "#0000FF",
    "White": "#FFFFFF",
    "Red": "#FF0000",
    "Black": "#000000",
    "Green": "00FF00"
}

def main():
    while True:
        colour_name = input("Enter colour: ").strip()
        if colour_name == "":
            break
        try:
            print(f"{colour_name} is {COLOURS[colour_name.capitalize()]}")
        except KeyError:
            print("Invalid colour")

main()