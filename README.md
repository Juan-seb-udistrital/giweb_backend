# Django Giweb - backend Proyecto final

### Requirements

* Python 3.11

### Installation

```
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


### Endpoints

1. REST API con Django REST Framework, CRUD comentarios.
  1.1 POST para agregar comentarios
  
  -URL: '''http://127.0.0.1:8000/api/comment/'''
  -Parametros que recibe (JSON)
    ```
    {
      "title": String,
      "description": String
      "comment": String
    }
    ```
    
    ![image](https://user-images.githubusercontent.com/117322489/208281763-b17772a2-5647-4dbf-ad38-7477908646b1.png)

 1.2 GET para obtener todos los comentarios
 
  -URL: '''http://127.0.0.1:8000/api/comment/'''
    
  - El parametro created es un parametro autogenerado por django por eso no es necesario incluirlo en la petición POST
    
    ![image](https://user-images.githubusercontent.com/117322489/208281784-bde4edfb-d1cc-41ba-b94d-83a761567f05.png)

 1.3 DELETE para eliminar un comentario en especifico.
 
  -URL: '''http://127.0.0.1:8000/api/comment/{id comentario que se desea eliminar}'''
  -Ejemplo: http://127.0.0.1:8000/api/comment/2
    
   ![image](https://user-images.githubusercontent.com/117322489/208281808-dab0cc52-e671-473b-b169-fa53287c204d.png)
   ![image](https://user-images.githubusercontent.com/117322489/208281869-2fe49190-4a50-4d0a-a904-1c4d1c30dddc.png)

 1.4 PUT para actualizar todo un registro, ó PATCH para actualizar parcialmente un registro
 
  -URL: '''http://127.0.0.1:8000/api/comment/{id comentario que se modificar}/'''
  -Parametros que recibe (JSON) para el metodo PUT
    ```
    {
      "title": String,
      "description": String
      "comment": String
    }
    ```
   -Parametros que recibe (JSON) para el metodo PATCH puede ser cualquiera de los anteriores

   ![image](https://user-images.githubusercontent.com/117322489/208281923-1a45e1be-1148-4153-88e6-4cb49023bbd1.png)
   ![image](https://user-images.githubusercontent.com/117322489/208281934-017cb99a-0d45-48ab-b05d-0fdb1c293b36.png)

2. Endpoint que genera users falsos.
 -Endpoint: '''http://127.0.0.1:8000/users'''
 -Method: GET
  
  ![image](https://user-images.githubusercontent.com/117322489/208282039-bd3824cc-7c77-49ff-ba8f-1885831c9118.png)

 -Servicio consumido: **jsonplaceholder**
 -[Endpoint del servicio](https://jsonplaceholder.typicode.com/users)
 
3. Endpoint que obtiene la información de un pokemon en especifico por el nombre

 -Endpoint: '''http://127.0.0.1:8000/pokemonByName'''
 -Method: POST
 -Parametros que recibe en JSON:
  ```
    {
      "name": String
    }
  ```
  
  ![image](https://user-images.githubusercontent.com/117322489/208282253-fc63d30a-5341-4070-bcd6-071c31b56338.png)
  
 -Servicio consumido: **PokeApi**
 -[PokeApi](https://pokeapi.co/)
  
 -Imagen con el nombre de la imagen anterior en la poke api:
  
  ![image](https://user-images.githubusercontent.com/117322489/208282333-9225779a-6685-4fea-9813-3e9577b1e7a9.png)

4. Endpoint que obtiene la información de un pokemon por el id.
 -Endpoint: '''http://127.0.0.1:8000/pokemonId/{id del pokemon a buscar}'''
 -Method: GET
 -El id se puede encontrar en la anterior petición.
  
  ![image](https://user-images.githubusercontent.com/117322489/208282428-96489ce6-e063-42eb-b098-7b630dd7a3f4.png)
  
 -Servicio consumido: **PokeApi**
 -[PokeApi](https://pokeapi.co/)
  
 -Imagen con el nombre de la imagen anterior en la poke api:
  
  ![image](https://user-images.githubusercontent.com/117322489/208282453-69da1ad8-cfc0-4280-b5c6-9c2846dee888.png)

5. Endpoint que obtiene lista de caracteres de Rick y Morty
 -Endpoint: '''http://127.0.0.1:8000/characters'''
 -Method: POST
 -Parametros que recibe en JSON:
  ```
    {
      "page": Number
    }
  ```
  
  ![image](https://user-images.githubusercontent.com/117322489/208282580-1ea85362-9414-48db-8abe-1d22b63992f9.png)

 -Servicio consumido: **RickAndMorty API**
 -[RickAndMorty API](https://rickandmortyapi.com/documentation/#rest)
  
  **Petición a la API directamente**:
  
  ![image](https://user-images.githubusercontent.com/117322489/208282626-d806ef34-9773-4add-a35c-ff4afdc420b4.png)

6. Endpoint que obtiene la información de una localización de la serie de Rick and Morty por el id de la localización.
 -Endpoint: '''http://127.0.0.1:8000/location/{id de la localización}'''
 -Method: GET
  
  ![image](https://user-images.githubusercontent.com/117322489/208282675-f8c304b0-2bfc-4461-b214-b92f136d86da.png)

 -Servicio consumido: **RickAndMorty API**
 -[RickAndMorty API](https://rickandmortyapi.com/documentation/#rest)
  
  **Petición a la API directamente:**
  
  ![image](https://user-images.githubusercontent.com/117322489/208282703-834072c1-2e45-421e-bb31-57b7a93702a8.png)
