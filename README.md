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

