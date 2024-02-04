import Coche as c #alias para no sobreescribir el nombre de la clase

class Camion(c.Coche):
    def __init__(self, matricula: str, num_ruedas: int = 8, lista_cajas: list = []):
        if len(matricula) < 5:
            #raise tipo de error que se lanza
            raise Exception("La matrícula debe tener al menos 5 caracteres")
        super().__init__(matricula, num_ruedas)
        self.lista_cajas = lista_cajas
        
        
    def tocar_bocina(self):
        print("Mok, mook!")
        
    def __str__(self):
        return "Camion con matrícula " + self.matricula