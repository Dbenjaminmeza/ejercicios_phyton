decimal = input("ingresa un numero ")

"""
FORMA CORRECTA PERO MENOS OPTIMA
    def usa_if(decimal):
    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"
    elif decimal == '2':
        return "010"
    elif decimal == '3':
        return "011"
    elif decimal == '4':
        return "100"
    elif decimal == '5':
        return "101"
    elif decimal == '6':
        return "110"
    elif decimal == '7':
        return "111"
    else:
        return "NA" """
    
tabla_switch = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }
def usa_switch(decimal):
    return tabla_switch.get(decimal, "NA")

print(usa_switch(decimal))