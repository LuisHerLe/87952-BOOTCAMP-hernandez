from datetime import date

from models.persona import Persona


class Repositoriopersonas:

    def __init__(self):
        self.__personas: list[Persona] = []
        self.__cargar_datos_prueba()

    def __cargar_datos_prueba(self):
        self.__personas.append(
            Persona(1, "Juan Perez")
        )
        self.__personas.append(
            Persona(2, "Maria Gomez")
        )
        self.__personas.append(
            Persona(3, "Carlos Lopez")
        )
        self.__personas.append(
            Persona(4, "Ana Martinez")
        )
        self.__personas.append(
            Persona(5, "Pedro Rodriguez")
        )

    def guardar(self, persona: Persona) -> None:
        self.__personas.append(persona)
        print(f"Se agregó {persona}")

    def obtener_por_dni(self, dni: int) -> Persona | None:
        for persona in self.__personas:
            if persona.dni == dni:
                return persona

        return None

    def obtener_todos(self) -> list[Persona]:
        return self.__personas.copy()

    def eliminar(self, dni: int) -> bool:
        persona = self.obtener_por_dni(dni)

        if persona is None:
            return False

        self.__personas.remove(persona)
        return True
