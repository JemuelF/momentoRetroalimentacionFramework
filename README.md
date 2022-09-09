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
