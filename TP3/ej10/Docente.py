from Personal import Personal

class Docente(Personal):
    def __init__(self, nombreCompleto, antiguedad, sector):
        super().__init__(nombreCompleto, antiguedad, sector)