import utils
data = [
        {
        'Country': 'Colombia',
        'Population': 500  
        },
        {
        'Country': 'Bolivia',
        'Population': 300  
        }
    ]
def run():
    keys, values = utils.get_population()
    print(keys, values)

    

    result = utils.population_by_country(data, country= input('Type Country => '))
    print(result)

if __name__ == '__main__':
    run()