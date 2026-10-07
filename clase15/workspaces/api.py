from datetime import date

from flask import Flask, jsonify, request

from models.alumno import Alumno
from models.persona import Persona
from repositories.alumno_repository import RepositorioAlumnos
from services.alumno_service import AlumnoService
from repositories.persona_repository import Repositoriopersonas
from services.persona_service import PersonaService

app = Flask(__name__)

repositorio = RepositorioAlumnos()
repo_personas = Repositoriopersonas()

# ----------- ALUMNOS ----------- 
@app.get("/alumnos")
def obtener_alumnos():
    alumnos = repositorio.obtener_todos()

    return jsonify([
        {
            "legajo": alumno.legajo,
            "nombre": alumno.nombre,
            "apellido": alumno.apellido,
            "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
        }
        for alumno in alumnos
    ])


@app.get("/alumnos/<int:legajo>")
def obtener_alumno(legajo):
    alumno = repositorio.obtener_por_legajo(legajo)

    if alumno is None:
        return jsonify({
            "error": "Alumno no encontrado"
        }), 404

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    })


@app.post("/alumnos")
def agregar_alumno():
    datos = request.get_json()

    alumno = Alumno(
        datos["legajo"],
        datos["nombre"],
        datos["apellido"],
        date.fromisoformat(datos["fechaDeNacimiento"])
    )
    
    servicio = AlumnoService()

    try:
        servicio.agregar_alumno(alumno)
    except ValueError as error:
        return jsonify(
            {
                "error": str(error)
            }
        ), 409

    return jsonify({
        "legajo": alumno.legajo,
        "nombre": alumno.nombre,
        "apellido": alumno.apellido,
        "fechaDeNacimiento": alumno.fecha_de_nacimiento.isoformat()
    }), 201
    
# ----------- PERSONAS -----------     
@app.get("/personas")
def obtener_personas():
    personas = repo_personas.obtener_todos()

    return jsonify([
        {
            "dni": persona.dni,
            "nombre": persona.nombre
        }
        for persona in personas
    ])


@app.get("/personas/<int:dni>")
def obtener_persona(dni):
    persona = repo_personas.obtener_por_dni(dni)

    if dni is None:
        return jsonify({
            "error": "Persona no encontrada"
        }), 404

    return jsonify({
        "dni": persona.dni,
        "nombre": persona.nombre
    })


@app.post("/personas")
def agregar_persona():
    datos = request.get_json()

    persona = Persona(
        datos["dni"],
        datos["nombre"]
    )
    
    servicio = PersonaService()

    try:
        servicio.agregar_persona(persona)
    except ValueError as error:
        return jsonify(
            {
                "error": str(error)
            }
        ), 409

    return jsonify({
        "dni": persona.dni,
        "nombre": persona.nombre
    }), 201
    
    

if __name__ == "__main__":
    app.run(debug=True)
