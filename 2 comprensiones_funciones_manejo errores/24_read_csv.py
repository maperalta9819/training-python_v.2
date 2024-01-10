import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = dict(iterable)
      data.append(country_dict)
    return data
num_select=int(input("Ingresa el numero del pais que buscas=> "))
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[num_select])