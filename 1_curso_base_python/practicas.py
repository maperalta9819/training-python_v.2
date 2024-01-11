person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Escribe tu solución 👇
person.update({"twitter" : "@nicobytes"})
#print(person.keys())
person.update({"name" : "Felipe"})
#print(person.items())
person.pop("age")
print(list(person.keys()))
print(list(person.values()))