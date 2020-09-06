def Trim(str, limit):
    char = (str[:limit] + '...') if limit > 2 else "Panjang karakter minimal 2"
    print(char)


Trim("Ini adalah kalimat",5)