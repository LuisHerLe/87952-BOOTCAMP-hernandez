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
    
    def eliminar_persona_por_dni(self, dni: int) -> str:
        if self.repo.obtener_por_dni(dni) is None:
            raise ValueError(f"No existe la persona con dni {dni}")
        
        return self.repo.eliminar(dni)
    
    def modificar_persona(self, dni: int, nuevo_nombre: str) -> Persona:
        persona_existente = self.repo.obtener_por_dni(dni)

        if persona_existente is None:
            raise ValueError(f"No se encontró una persona con el dni {dni}")

        persona_actualizada = Persona(dni, nuevo_nombre)
        
        resultado = self.repo.modificar_persona(persona_actualizada)
        
        return resultado    
