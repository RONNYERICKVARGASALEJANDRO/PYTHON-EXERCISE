frase="holaa my friends"
vocales= []
for caso in frase:
    if caso in ('a','e','i','o','u'):
        vocales.append(caso)
        print(caso,end='-')
print(vocales)
vocales=[caso for caso in frase if caso in ('a','e','i','o','u')]
print(vocales)