
from dataclasses import dataclass

@dataclass(frozen=True)
class Persona:
    _dni: int
    _nombre: str

    def __post_init__(self):
        if self._dni <= 0:
            raise ValueError("El dni debe ser mayor que 0.")

        self._validar_nombre(self._nombre, "nombre")

        if len(self._nombre) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres.")

    @staticmethod
    def _validar_nombre(valor: str, campo: str):
        if not valor:
            raise ValueError(f"El {campo} no puede estar vacío.")
       

        if not valor[0].isupper():
            raise ValueError(
                f"El {campo} debe comenzar con mayúscula."
            )

    @property
    def dni(self) -> int:
        return self._dni

    @property
    def nombre(self) -> str:
        return self._nombre
