# --- Assignment 5: Match Case (Menu System) ---

print("--- Welkom bij de Keuzemenu Applicatie ---")
print("1. Toon een begroeting")
print("2. Geef een motiverende quote")
print("3. Vertel een programmeer grap")
print("4. Sluit het programma")
print("------------------------------------------")

# Ask the user to input a choice
keuze = input("Maak een keuze (1-4): ")

print("------------------------------------------")

# Use Match-Case to evaluate the user's input choice
match keuze:
    case "1":
        print("Hallo! Super goed bezig met deze Python & GitHub opdracht! 👋")
    case "2":
        print("De quote van vandaag: 'De beste manier om de toekomst te voorspellen, is door hem zelf te programmeren!' 💻")
    case "3":
        print("Waarom dragen programmeurs een bril? Omdat ze niet C# ! 🤓")
    case "4":
        print("Programma afgesloten. Tot ziens! Bekijk snel GitHub voor de merges!")
    case _:
        # This acts as the default fallback
        print("Ongeldige invoer! Kies alstublieft een optie tussen 1 en 4.")

print("------------------------------------------")
