# coding: utf-8
print ("Divisores")
num1 = int(input("escriba un numero mayor que cero:"))
if num1<0:
  print("le he pedido un numero entero mayor qque cero :")
else:

	for i in range(1,(num1/2) +1 ):
            if num1 % i  == 0 :
	       print(i)

