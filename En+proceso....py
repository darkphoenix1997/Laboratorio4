
# coding: utf-8

# In[ ]:

#Txt y muestra n primeras lineas
t = raw_input("¿Como se llama el archivo de texto?:")

def lineas():
  fa = open("hola.txt")
  for i, linea in enumerate (fa):
    if i>7:
      break
    print linea
    print i
lineas()
fa.close()

#Entero n y muestra n primeras lineas
n = int(raw_input("Escriba su numero entero:"))

def lineas():
  fa = open("hola.txt")
  for i, linea in enumerate (fa):
    if i>7:
      break
    print linea
    print i
lineas()
fa.close()

#Concatenar
c = raw_input("Nombre de su primer archivo text:)
a = raw_input("Nombre de su segundo archivo text:)
fa = open("hola.txt", "r")
fb = open("hola2.txt, "w")

outfile = open("texto.txt", "a")
outfile.close()

infile = open("texto.txt", "r")
print("Hola")
print(infile.read())
infile.close()

