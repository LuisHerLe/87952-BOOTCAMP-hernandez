Pendiente instalar
    - pip install flask-cors
    - Instalar bun (Empaquetador de js)
    - Dentro del api.py
        from  flask-cors import CORS
        CORS(app)


https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=FPbD6dnIlUCa1IfSyafYxE4uGCthyi9EnQYg85vv3slUMDdKUklRTkg5M0kzWEgzMVRXNThMUDVTNy4u
Trabajo:
    - Agregar el delete para que /persona/1 borre la persona dni 1
        - Api -> Servicio -> recupera y se fija si existe -> Repositorio
    - Agregar el PUT para modificar un alumno si existe. Debería ser PUT /persona/1 para modificar el nombre (Del body) de la persona con dni 1
        - Api -> Servicio -> recupera y se fija si existe -> le modifica los datos -> Repositorio
    - Solamente el back end
    - Si la persona no existe (Según si dni) devolver un error 400
