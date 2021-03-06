#Developed by Fernando Santamaría
#https://github.com/FerSantamaria
#2021-09-12

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def get_data():
  # Loading data from CSV
  passenger_df = pd.read_csv("data/titanic.csv")
  
  # Removing non-digits from Ticket number using regex and making 'em strings
  passenger_df['Ticket'].replace(r"\D", '', regex=True, inplace=True)
  pd.Series(['Ticket'], dtype="string")

  #Replacing NaN values with zeros and dashes
  passenger_df['Tarifa'].fillna(0, inplace=True)
  passenger_df.fillna('-', inplace=True)

  return passenger_df

def passenger_search(data):
  print("===== Consulta de información =====\n")
  search_id = input("Ingrese el número de ticket: ")
  
  if search_id.isnumeric:
      results = data.loc[data['Ticket'].str.contains(search_id)]

      if not results.empty:
        results.reset_index(drop=True, inplace=True)
        print("\n")
        print(results)
      else:
        print("\nNo se ha encontrado información para ese número de ticket")

  else:
      print(f"\nId no válido")
        
  return True

def pie_chart(data):
  dead = data[data["Sobrevivio"] == 0].count()["Sobrevivio"]
  survivor = data[data["Sobrevivio"] == 1].count()["Sobrevivio"]

  graph_data = [dead, survivor]
  graph_labels = ["Muertes", "Sobrevivientes"]

  plt.pie(graph_data, labels=graph_labels, autopct= lambda x: "{:.0f}\n{:.2f}%".format((dead + survivor)*x/100, x) )
  plt.title("Muertes y Sobrevivientes")
  plt.show()

def bar_chart(data):
  dead = data[data["Sobrevivio"] == 1]
  
  class_1 = dead[dead["Clase"] == 1].count()["Clase"]
  class_2 = dead[dead["Clase"] == 2].count()["Clase"]
  class_3 = dead[dead["Clase"] == 3].count()["Clase"]
  
  graph_data = [class_1, class_2, class_3]
  graph_labels = ["1a. Clase", "2a. Clase", "3a. Clase"]

  plt.bar(graph_labels, height=graph_data)
  plt.title("Muertes por clase")
  plt.ylabel('Muertes')
  plt.show()
  return True

def ticket_prices(data):
  print("===== Costo de Tickets (Mayor y menor) =====\n")

  min_value = data[data["Tarifa"] > 0]["Tarifa"].min()
  max_value = data["Tarifa"].max()

  print(f"\nEl costo de ticket más bajo es: ${min_value:.2f}")
  print(f"El costo de ticket más alto es: ${max_value:.2f}")

  return True

def credits(data):
    print("Desarrollado por: José Fernando Flores Santamaría")
    print("https://github.com/FerSantamaria/evaluacion-03-ds")

#Clear screen utility
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    plt.close("all")

#Menu options methods dictionary
menu_options = {
    1: passenger_search,
    2: pie_chart,
    3: bar_chart,
    4: ticket_prices,
    5: credits,
}

# ============= Main Program =============
while True: 
    # Clearing terminal screen and displaying user menu
    clear_screen()

    print("===== Análisis de datos: Caso Titanic =====\n")
    print("Opciones:")
    print("1. Buscar Pasajero(s)")
    print("2. Gráfica de muertos y sobrevivientes (Pastel)")
    print("3. Gráfica de muertes por clase (Barras)")
    print("4. Costo de Tickets (Mayor y menor)")
    print("5. Créditos")
    print("6. Salir")

    selected_option = input("\nElija una opción: ")

    selected_option = int(selected_option) if selected_option.isnumeric() else 0

    if selected_option >=1 and selected_option <= 5:
        clear_screen()

        data = get_data()
        menu_options[int(selected_option)](data)

        input("\nPresione enter para continuar...")
        clear_screen()

    elif selected_option == 6:
        print("\nTerminando ejecución")
        break

    else:
        input("\nOpción inválida. Presione enter para reintentar...")