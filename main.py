

# CLASE 01 -Programación Backend con Python

class Mago:
    def __init__(self,nombre,vida,nivel,energia):
        self.nombre = nombre
        self.vida = vida
        self.magia = nivel
        self.energia = energia
    def atacar(self,objetivo):
        if self.energia >= 10:
            self.energia = self.energia - 10
            dano = 10
            objetivo.vida -= dano
            
            if objetivo.vida < 0:
                objetivo.vida = 0

            print(f"{self.nombre} ha atacado a {objetivo.nombre} y ha recibido {dano} de daño")
            print(f"Vida de {objetivo.nombre} : {objetivo.vida}")
            print(f"Energia de {self.nombre} : {self.energia}")
        else:
            print(f"{self.nombre} no tienes suficiente energia")

    def curar(self,objetivo):
        if self.energia >= 12:
            self.energia = self.energia - 12
            curacion = 15
            objetivo.curar(curacion)
            objetivo.vida += 15

            if objetivo.vida > 30:
                objetivo.vida = 30

            print(f"{self.nombre} ha curado a {objetivo.nombre} y ha recuperado {curacion} de vida")
            print(f"Vida de {objetivo.nombre} : {objetivo.vida}")
            print(f"Energia de {self.nombre} : {self.energia}")
        else:
            print(f"{self.nombre} no tienes suficiente energia")




mago1 = Mago("mago1",40,10,15)
mago2 = Mago("mago2",40,15,20)


mago1.atacar(mago2)
mago2.curar(mago2)