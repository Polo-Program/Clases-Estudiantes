import os, time

def limpiarConsola():
    os.system('cls' if os.name == "nt" else "clear")

negro = "\033[30m"
rojo = "\033[31m"
verde = "\033[32m"
blanco = "\033[37m"
cerrar = "\033[0m"


class Estudiante:
    def __init__(self, nombreEs, edadEs, carreraEs, arancelEs):
        self.nombre = nombreEs
        self.edad = edadEs
        self.carrera = carreraEs
        self.arancel = arancelEs
    def mostrar(self):
        arancelNuevo = f"{self.arancel:,.0f}".replace(",",".")
        print(f"{verde}" '=' * 45)
        print(F"{rojo}            DATOS ESTUDIANTE      {cerrar}\n")
        print(f"   Nombre     : {self.nombre}")
        print(f"   Edad       : {self.edad}")
        print(f"   Carrera    : {self.carrera}")
        print(f"   Arancel    : {arancelNuevo}")
        print(f"{verde}" '=' * 45 )

estudiante1 = Estudiante("Jean Paul Cáceres Acuña", 23, "Ingeneria en programacion", 1000000)
estudiante2 = Estudiante("Antu Lincoñir", 18, "Ingeneria en Reelcion", 2000000)
estudiante3 = Estudiante("Guillermo Contreras", 18, "Ingeneria en Masturbacion", 1000000000)
estudiante4 = Estudiante("Basty Hormazabal", 20, "Kinesiologia", 10000000)

limpiarConsola()

estudiante1.mostrar()
estudiante2.mostrar()
estudiante3.mostrar()
estudiante4.mostrar()