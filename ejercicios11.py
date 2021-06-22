from ejercicio10 import cargos

class empleados:
    suma=0
    def __init__(self,nom,ced,sue,carg):
        self.codg=self.generarcodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=carg
    def mostrar(self):
        print('codig: {} nombre: {} cargo: {}-{}'.format(self.codg,self.nombre,self.cargo.codg,self.cargo.descripcion))
    def generarcodigo(self):
        empleados.suma=empleados.suma+1
        return empleados.suma

cargo1=cargos("docente")
emp1=empleados("Daniel","0987456321",500,cargo1)
emp1.mostrar()
cargo2=cargos("Analista")
emp2=empleados("Ana","0123654789",600,cargo2)
emp2.mostrar()
