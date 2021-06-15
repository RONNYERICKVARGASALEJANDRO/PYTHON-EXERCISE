class condiciones:
    contador=0
    def __init__(self,numero=0,numero1=0):
        self.num=numero
        self.num1=numero1
        number= numero+numero1
        self.num2=number

    def uso_del_if(self):
        if self.num == self.num1:
            print('num{}, num1:{}, son iguales'.format(self.num,self.num1))
        elif self.num2 == self.num1:
            print('num{}, num1:{}, son iguales'.format(self.num,self.num1))
        else:
            print('no son iguales')

condiciones1= condiciones()
print(condiciones1.num)
print(condiciones1.num1)

condiciones2= condiciones(30,20)
print(condiciones2.num)
print(condiciones2.num1)

condiciones3= condiciones(20,10)
condiciones3.uso_del_if()


        
        
         

