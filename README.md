# google-finder-script
Python script for find people on Google Finder

Note: The name is list type and must have minimum 1 element`['name']` and maximum 3 elements `['name', 'last name', 'mother's last name']`

```
import finder

name = ['pedro','perez']
finder.peopleFinder(name)
```
Response example
```
return:

[
  {
    "name": "Pedro Perez",
    "url_to_google": "http://google.org/personfinder/2017-puebla-mexico-earthquake/view?family_name=&given_name=&id=2017-puebla-mexico-earthquake.personfinder.google.org%2Fperson.*****&query_location=&query_name=Pedro+Perez&role=seek",
    "photo": "http://google.org/personfinder/global/no-photo.png",
    "direccion": "Direccion no disponible",
    "estado": "Estado: No especificado"
  },
  {
    "name": "luis alberto perez pedro",
    "url_to_google": "http://google.org/personfinder/2017-puebla-mexico-earthquake/view?family_name=&given_name=&id=2017-puebla-mexico-earthquake.personfinder.google.org%2Fperson.*****&query_location=&query_name=Pedro+Perez&role=seek",
    "photo": "http://google.org/personfinder/2017-puebla-mexico-earthquake/photo?id=*****",
    "direccion": "Dirección no disponible ",
    "estado": "Estado: No especificado"
  },
  {
    "name": "Pedro miguel (cintia) Marín perez",
    "url_to_google": "http://google.org/personfinder/2017-puebla-mexico-earthquake/view?family_name=&given_name=&id=2017-puebla-mexico-earthquake.personfinder.google.org%2Fperson.*****&query_location=&query_name=Pedro+Perez&role=seek",
    "photo": "http://google.org/personfinder/global/no-photo.png",
    "direccion": "Direccion no disponible",
    "estado": "Estado: No especificado"
  },
  {
    "name": "Pedro Pérez Padilla",
    "url_to_google": "http://google.org/personfinder/2017-puebla-mexico-earthquake/view?family_name=&given_name=&id=2017-puebla-mexico-earthquake.personfinder.google.org%2Fperson.*****&query_location=&query_name=Pedro+Perez&role=seek",
    "photo": "http://google.org/personfinder/global/no-photo.png",
    "direccion": "Direccion no disponible",
    "estado": "Estado: No especificado"
  }
]
```
