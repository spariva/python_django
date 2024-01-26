
import Vehiculo as v

class Moto(v.Vehiculo):
    #None porque no puedes poner un param sin por defecto despues de uno con por defecto
    def __init__(self, matricula: str, num_ruedas: int = 2, tipo = None):
        if len(matricula) < 5:
            #raise tipo de error que se lanza
            raise Exception("La matrícula debe tener al menos 5 caracteres")
        elif (tipo != 'naked' or 'scooter' or 'honda'):
            raise Exception("La moto tiene que ser de tipo naked, scooter u honda")
        super().__init__(matricula, num_ruedas)        
        self.tipo = tipo
        
    def tocar_bocina(self):
        print("Pi, pii!")
        
    def __str__(self):
        return "Moto con matrícula " + self.matricula


