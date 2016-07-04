from Primos import *
from Totiente import *
from Mdc import *
from Caracteres import *
from Descifrar import *

#numeros primos
p = 11
q = 13
primos = Primos()
totiente = Totiente()
mdc = Mdc()

n = primos.getMultiPrimos(p,q)
t = totiente.getTotiente(p,q)
e = mdc.getMdc(t)
#por enquanto usamos 13
print("Multiplicacao de primos:",n)
print("Funcao totiente:",t)
e = 13
print("e com MDC:",e)

caracteres = Caracteres()
car = caracteres.getCaracteres()
texto = "david turati"
cifra = []
chavePublica = [n,e]
print("Chave publica",chavePublica)

#Cifrar
for valor in texto:
    #print(car[valor])
    res = car[valor]
    res = (res **chavePublica[1]) % chavePublica[0]
    cifra.append(res)
print("Texto Original:",texto)
print("Texto cifrado, criptografado:",cifra)

descifrar = Descifrar()
chavePrivada = descifrar.euclides(t,e)
chavePrivada.append(n)
print("Chave privada",chavePrivada)


textoOriginal = descifrar.decifrar(cifra,chavePrivada,car)
print("\nTexto Original descriptografada:", textoOriginal)









