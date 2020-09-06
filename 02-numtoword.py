from num2words import num2words

def Number(value):
    return num2words(value, lang='id')

satu = Number(1)
belasan = Number(12)
puluhan = Number(30)
print(satu)
print(belasan)
print(puluhan)