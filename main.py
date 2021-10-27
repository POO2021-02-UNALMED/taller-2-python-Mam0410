class Asiento:
    def __init__(self,col,pre,reg):
        self.color=col
        self.precio=pre
        self.registro=reg
    def cambiarColor(self,col):
        if col == "rojo" or col== "negro" or col== "blanco" or col== "amarillo" or col== "verde" :
            self.color=col
        
class Auto :
    cantidadCreados = 0
    def __init__(self,a,b,c,d,e,f):
        self.modelo=a
        self.precio=b
        self.asientos=c
        self.marca =d 
        self.motor= e
        self.registro = f

    def cantidadAsientos(self):
        c=0
        for i in self.asientos:
            if isinstance(i,Asiento) == True:
                c+=1
        return c

    def verificarIntegridad(self):
        original="Auto original"
        chiviado="Las piezas no son originales"
        c=""
        for i in self.asientos:
            if isinstance(i,Asiento) == True:
                if i.registro == self.motor.registro and  i.registro == self.registro and self.registro== self.motor.registro:
                    c=original
                else:
                    c=chiviado
                    break
        return c        

class Motor:
    def __init__(self,a,b,c):
        self.numeroCilindros=a
        self.tipo=b
        self.registro=c

    def cambiarRegistro(self,registro):
        self.registro=registro
        
    def asignarTipo(self,tipo):
        if tipo == "electrico" or tipo=="gasolina":
             self.tipo=tipo




