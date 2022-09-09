# momentoRetroalimentacionFramework


## Dataset

El dataset usado para esta evidencia es un set que contiene información acerca de distintos valores que un jugador tiene en el videojuego FIFA. Los valores que contiene son desde la edad, calificación en varios aspectos, valor de mercado, clausula de recisión, valoración general y más.

El objetivo es poder ingresar los datos a un modelo y que nos pueda dar la valoración general de los datos que hemos ingresado

## Limpieza dataset
<img width="1142" alt="image" src="https://user-images.githubusercontent.com/71990312/189453306-9387912c-c489-401d-88fe-365533f027a7.png">

Eliminamos los datos que no nos aportan nada y también transformamos algunos datos, como los precios, tenemos que eliminar el signo de euros y también transformar dependiendo si el dato tiene una 'K' o una 'M', que significa mil o millón, también los datos de precios se encuentran escalados, 1000 a 1, para mantener más pequeños los datos y evitar que eso influya en nuestro modelo de manera excesiva.


## Mapa de calor

<img width="1043" alt="image" src="https://user-images.githubusercontent.com/71990312/189453575-8684cd61-c5c6-4a42-8a15-7f2d6d7c0add.png">
Obtenemos el mapa de calor para corroborar que las características que hemos mantenido afectan a nuestra variable resultado

## División del dataset

<img width="914" alt="image" src="https://user-images.githubusercontent.com/71990312/189453648-f498285d-f462-46d8-8be8-6b0bb6d5335f.png">
Dividimos nuestro dataset en nuestro set de entrenamiento y el de validación

## Random Forest

<img width="700" alt="image" src="https://user-images.githubusercontent.com/71990312/189453713-e55cf69a-0388-473a-8322-14426df9d601.png">
Podemos ver un claro overfitting ya que en el set de entrenamiento logra un score perfecto pero cuando se usa el de validación el score baja mucho

### Gráfica set de entrenamiento
<img width="1214" alt="image" src="https://user-images.githubusercontent.com/71990312/189453802-e76d9f75-9e92-4c76-a3d0-71838202df13.png">
Se puede observar que sigue a la perfección los datos de entrenamiento

### Gráfica set de validación
<img width="439" alt="image" src="https://user-images.githubusercontent.com/71990312/189453848-8f3eb91a-fe95-4859-9d52-d214b061c1eb.png">
<img width="1126" alt="image" src="https://user-images.githubusercontent.com/71990312/189453858-ae6b168c-538c-49a8-8704-f25eac7d6b54.png">
Vemos como el modelo ya no sigue tan bien los datos de validación


## Regresión
<img width="908" alt="image" src="https://user-images.githubusercontent.com/71990312/189453932-8a502c8a-7ef1-4790-a4dd-a329ac3fdd04.png">
Vemos que aunque el score no es perfecto, se mantiene aceptable en el subset de entrenamiento y en el de validación por lo que podríamos decir que el modelo es aceptable

### Gráfica set de entrenamiento
<img width="527" alt="image" src="https://user-images.githubusercontent.com/71990312/189454029-8f64220a-8dc1-4a73-be9c-7a1071cb96b3.png">
<img width="1120" alt="image" src="https://user-images.githubusercontent.com/71990312/189454041-17a4c90f-5e2f-4c77-8e44-6e37ebdb740a.png">

Aunque los datos del modelo no siguen a la perfección los datos del set de entrenamiento podemos observar que si se mantienen estables y dentro de un rango aceptable

### Gráfica set de validación
<img width="484" alt="image" src="https://user-images.githubusercontent.com/71990312/189454055-e0787e92-6f22-4e23-85e6-ad536f3f44ba.png">
<img width="1097" alt="image" src="https://user-images.githubusercontent.com/71990312/189454074-f2e2cdcd-2c27-46c6-8d83-bb382581ea5d.png">

Vemos que el comportamiento es similar al del set de entrenamiento
