
class User():

    def __init__(self, id, nombre=None, apellido=None, number=None, estatus=None) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.number = number
        self.estatus = estatus

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'number': self.number,
            'estatus': self.estatus,
        }
