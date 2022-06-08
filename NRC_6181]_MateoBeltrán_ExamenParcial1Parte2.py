'''
Se crea la clase vacía "Calculo", la cual se encargará de resolver varios procesos matemáticos
los cuales son: determinar un factorial, determinar la suma de n enteros, un método para determinar 
si es un número primo, comparar si dos números son primos, tabla de multiplicar desde el 1 al 9.
'''

class Calculo:
    def __init__(self):
        pass
    def Factorial(self, num,factorInicial): 
        '''
        Para determinar el factorial se debe tener un 
        factor inicial, que es el número 1, con esto condicionamos
        al método para poder ejecutar el factorial
        '''
        self.num=num
        self.factorInicial=factorInicial
        factorInicial=1
        if num!=0:
            for i in range(1,num+1):
                factorInicial=factorInicial*i
                return factorInicial
    def TablaMult(numero):
        '''
        El usuario ingresa el número del cual desea tener
        la tabla de multiplicar
        '''
        numero=int(input("Ingrese su número: "))
        for i in range (numero, numero+1):
            print(i*numero)

