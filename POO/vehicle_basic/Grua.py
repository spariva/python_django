import Coche as c

class Grua(c.Coche):
    def __init__(self, matricula: str, num_ruedas: int = 4, lista_vehiculos: list = []):
        if len(matricula) < 5:
            #raise tipo de error que se lanza
            raise Exception("La matrícula debe tener al menos 5 caracteres")
        super().__init__(matricula, num_ruedas)
        self.lista_vehiculos = lista_vehiculos
        
    def tocar_bocina(self):
        print("Turuuu!")
        
    def __str__(self):
        return "Grua con matrícula " + self.matricula
    
    def cargar(self, vehiculo: c.Coche):
        if vehiculo in self.lista_vehiculos:
            raise Exception("El vehiculo ya está en la grua")
        
        if vehiculo.num_ruedas > 4:
            raise Exception("La grua no puede cargar vehiculos con más de 4 ruedas")
        
        print("Cargando vehiculo " + vehiculo.matricula)
        self.lista_vehiculos.append(vehiculo)
        
    def descargar(self, vehiculo: c.Coche):
        if vehiculo not in self.lista_vehiculos:
            raise Exception("El vehiculo no está en la grua")
        
        print("Descargando vehiculo " + vehiculo.matricula)
        self.lista_vehiculos.remove(vehiculo)
    