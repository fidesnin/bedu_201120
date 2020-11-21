#script calcula tabla de multiplicar

#pregunta el numero
numero = input ('que numero quieres multiplicar?')
# de string lo tengo que cambiar a int
numero  = int(numero)

for n in range(10):
    r = numero * (n+1)
    print(r)
     

