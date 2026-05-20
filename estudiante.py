class Estudiante:
    def __init__(self, nombreEs, notaEs):
        self.__nombre = nombreEs
        self.__nota = notaEs

    #Getters
    def getNombre(self):
        return self.__nombre
    def getNota(self):
        return self.__nota
    
    #Setters
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    def setNota(self, nuevaNota):
        self.__nota = nuevaNota

    #Metodo para mostrar si reprobo o aprobo
    def resultado(self):
        if self.getNota() >= 4.0:
            print(f"El alumno {self.__nombre} ha aprobado")
        else:
            print(f"El estudiante {self.__nombre} ha reprobado")
        print("=" * 45)

    #Metodo para mostrar informacion
    def imprimir(self):
        print("=" * 45)
        print(f"Nombre Estudiante  :   {self.getNombre()}")
        print(f"Nota               :   {self.getNota()}")

#Objetos 
objetoEstudiante = Estudiante("Jean Cáceres", 35)
objetoEstudiante.imprimir()
objetoEstudiante.resultado()
objetoEstudiante2 = Estudiante("Basty Hormazabal", 70)
objetoEstudiante2.setNota(1.5)
objetoEstudiante2.imprimir()
objetoEstudiante2.resultado()


class Auto:
    def __init__(self, marcaAuto, colorAuto, kmRecoridos):
        self.__marca = marcaAuto
        self.__color = colorAuto
        self.__km = kmRecoridos

    def getMarca(self):
        return self.__marca
    def getColor(self):
        return self.__color
    def getKm(self):
        return self.__km
    def setMarca(self, nuevaMarca):
        self.__marca = nuevaMarca
    def setColor(self, nuevoColor):
        self.__marca = nuevoColor
    def setKm(self, nuevoKm):
        self.__km = nuevoKm

    def mostrarInformacion(self):
        print(f"Marca  :    {self.getMarca()}")
        print(f"color  :    {self.getColor()}")
        print(f"KM     :    {self.getKm()}")

objetoAuto = Auto("Toyota", "Rojo", 10000)

objetoAuto.mostrarInformacion()
objetoAuto.setColor("Verde")
objetoAuto.mostrarInformacion()
