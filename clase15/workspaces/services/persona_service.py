from models.persona import Persona
from repositories.persona_repository import Repositoriopersonas


class PersonaService:
    def __init__(self):
        self.repo = Repositoriopersonas()

    def agregar_persona(self, persona: Persona) -> None:
        if self.repo.obtener_por_dni(persona.dni) is not None:
            raise ValueError("Ya existe una persona con ese DNI.")

        self.repo.guardar(persona)

    def obtener_alumnos(self) -> list[Persona]:
        return self.repo.obtener_todos()

    def obtener_alumno_por_dni(self, dni: int) -> Persona | None:
        return self.repo.obtener_por_dni(dni)
