file = open('./text.txt')
#print(file.read())

for line in file:
    print(line)

file.close()

with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    ##AHORA INTENTAMOS ESCRIBIR EN EL ARCHIVO   
    file.write('nuevas palabras para colocar aqui \n')