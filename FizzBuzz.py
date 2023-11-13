#Numeros de 1 a 100 sustituyendo multiplos de 3 y 5 por palabras
#como fizz y buzz tambien si cumple con 3 y 5 sustituir por fizzbuzz
def fizz_buzz():
   for i in range(1,101):
       if i%3==0 and i%5==0:
           print('fizz-buzz')
       elif i%3==0:
           print('fizz')
       elif i%5==0:
           print('buzz')
       else:
            print(i)
fizz_buzz()