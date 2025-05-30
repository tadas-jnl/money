#  Perdaryti biudžeto programą per kelis failus (naujame projekte)
# TODO Sukurti paleidžiamą failą (exe) iš šios biudžeto programos.
from models.zurnalas import Zurnalas
from models.komandos import Ataskaita
zurnalas = Zurnalas()

if __name__ == "__main__":
    while True:
        command = input("1 - Naujas įrašas, 2 - Ataskaita, X - Išeiti iš programos: ")
        match command:
            case '1':
                zurnalas.irasyti(input("Suma: "))
            case '2':
                ataskaita = Ataskaita()
                ataskaita.spauzdinti()
            case command if command.lower() == 'x':
                break
