import os

def zodiac(month:int,day:int) -> str:
    result = str
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        result = "Aries"
    elif (month == 4 and day >= 21) or (month == 5 and day <= 20):
        result = "Tauro"
    elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        result = "Geminis"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        result = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 23):
        result = "Leo"
    elif (month == 8 and day >= 24) or (month == 9 and day <= 22):
        result = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        result = "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        result = "Escorpio"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        result = "Sagitario"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
        result = "Capricornio"
    elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        result = "Acuario"
    elif (month == 2 and day >= 20) or (month <= 3 and day <= 20):
        result = "Picis"
    return result

x = True
while x == True:
    print("Calculo del zodiaco")
    day = int(input("Dia de nacimiento: "))
    month = int(input("Mes de nacimiento: "))
    print("El signo zodiacal es:", zodiac(month,day))
    #os.system("pause")
    if day==55:
        x = False