import utils
import read_csv
import charts
import pandas as pd #Se importa pandas como pd (convencionalidad)

def run():
  
  '''
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''

  '''
  Pandas se encarga de leer csv, filtrar columnas, datos etc. Aunque es importante
  conocer como podemos resolver el problema sin un módulo.
  '''

  #Dataframes en Pandas son todos los datos de donde se obtiene información
  # normalmente se definen con df
   
  df = pd.read_csv('data.csv') #Nos ahorramos el código del archivo read_csv
  df = df[df['Continent'] == 'Africa'] #Sustitución al filter

  #Obtener los valores de las columnas con Pandas
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv') #Dejamos esta línea para no corromper el código de abajo
  country = input('Type Country => ')

  #Código proveniente de utils.py
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
  

if __name__ == '__main__':
  run()