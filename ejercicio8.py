listalunmos=[{"nombre":'erick',"final":90},{"nombre":'juan',"final":20},{"nombre":'ronny',"final":30}]
acum=0
cont=0
for alumnos in listalunmos:
    print(alumnos)
    for clave,valor in alumnos.items():
        print(clave,":",valor)
        if clave=="final":
            acum=acum+valor
    cont+=1
print(acum/cont)
