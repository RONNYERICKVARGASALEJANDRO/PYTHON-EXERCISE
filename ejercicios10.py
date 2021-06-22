class cargos:
    suma=0
    def __init__(self,desc='sin cargo'):
        cargos.suma=cargos.suma+1
        self.codg=cargos.suma
        self.descripcion=desc
if __name__ == "__main__":
    cargo1= cargos()
    #cargo1.codg=1
    #cargo1.descripcion='Docente'
    print(cargo1.codg,cargo1.descripcion)
        
    cargo2= cargos('director')
    print(cargo2.codg,cargo2.descripcion)

    cargo3= cargos('analista')
    print(cargo3.codg,cargo3.descripcion)
              

