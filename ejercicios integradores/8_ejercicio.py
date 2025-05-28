""" Nivel 3 | Agenda de contactos {
Dado un diccionario llamado agenda que almacena contactos, donde cada clave es el
nombre de una persona y su valor otro diccionario con su teléfono y correo electrónico,
escribí un programa qué:
A- Le pida al usuario que ingrese un nombre para buscar
B- Verifique si ese nombre está en la agenda
C- Si está, muestre el número de teléfono y el email correspondiente
D- Si no está, no muestre nada
} """


agenda = {
    "benja": {
        "telefono" : 3624556782,
        "mail" : "benja@gmail.com"
    },
    "karen": {
        "telefono" : 3624556745,
        "mail" : "karen@gmail.com"
    }
}

nombre = input("ingrese un nombre a buscar: ")

if nombre in agenda:
    telefono = agenda[nombre]["telefono"]
    mail = agenda[nombre]["mail"]
    print(f"el telefono es {telefono} y el mail es {mail}")
