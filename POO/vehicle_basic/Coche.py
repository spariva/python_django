import Vehiculo as v

class Coche(v.Vehiculo):
    def __init__(self, matricula: str, num_ruedas: int = 4):
        if len(matricula) < 5:
            #raise tipo de error que se lanza
            raise Exception("La matrícula debe tener al menos 5 caracteres")
        super().__init__(matricula, num_ruedas)

    def tocar_bocina(self):
        print("Meh, meeeh!")
        
    def __str__(self):
        return "Coche con matrícula " + self.matricula
    