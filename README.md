Este pequeño script es algo que me toca diseñar otra vez, en el mismo puesto pero en distinta empresa, es recurrente que los formularios de login no cuenten con las validaciones suficientes conseguir el genero/sexo de la persona que rellena el formulario.
Si bien esto no soluciona todo los problemas, al unir esta tabla con un campo nuevo en tu base de datos que sea el primer nombre en minusculas de la persona,podras ver que al hacer un left join a tu tabla sin genero ,habra valores de genero que caeran sobra el valor A,donde esos pueden conseguirse mediante el uso de la api de genderize.io que posee 100 requests de nombres diarias gratis de la siguiente manera

lista_nombres_a = ['lihuel', 'lucero', 'maiten', 'mar', 'maria', 'mel', 'miqueas','neri', 'rosario', 'uriel']
name_aux = []
gender_aux = []
for name in lista_nombres_a:
    response = requests.get(f'https://api.genderize.io?name={name}')
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        name_aux.append(response.json()['name'])
        gender_aux.append(response.json()['gender'])
    else:
        print(response)
data = { "nombre": name_aux, "Género": gender_aux }
df = pd.DataFrame(data) 

y posteriormente generar un update con los valores de "df" a tu base de datos


en limpio se podria decir:

Funcionamiento:
El script define una lista de nombres que no tienen un género claro ("lista_nombres_a").
Recorre la lista y para cada nombre:
Realiza una solicitud a la API de genderize.io para obtener el género del nombre.
Si la solicitud es exitosa, guarda el nombre y el género en una lista.
Crea un DataFrame de Pandas con las listas de nombres y géneros.
Puedes usar el DataFrame para actualizar tu base de datos con los géneros de los nombres.

Limitaciones:
La API de genderize.io tiene un límite de 100 solicitudes gratuitas por día.
La API no siempre es precisa, especialmente para nombres poco comunes.

Requisitos:
Python 3
requests
pandas

Mejoras:
Puedes ampliar la lista de nombres para incluir más nombres que no tienen un género claro.
Puedes usar una API diferente para obtener el género del nombre.
Puedes mejorar la precisión del script utilizando un algoritmo de aprendizaje automático.
