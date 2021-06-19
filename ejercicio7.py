#para presentar valores de la lista- se conoce como ciclos anidados
listanotas =[(30,40),(20,40,35),(78,50,40)]
suma=0
cont=0
for notas in listanotas:
    #print(notas)
    par=0
    #cont1=0
    print(notas)
    for nota in notas:
        print(nota)
        cont=cont+1
        suma=suma + nota
        par=nota
        #cont1=cont1+1
    #propar=par/cont1
    propar=par/len(notas)
    print("notas parciales={}  promedio parcial= {}".format(propar,par))
total=suma/cont
#print("El promedio es: ",total)
print("total de notas= {} - total de notas= {} - promedio= {}".format(suma,cont,total))