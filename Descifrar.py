class Descifrar():

    def euclides(self,n,e):
        #print("Descifrar")
        #print(n,e)
        r = n
        r1 = e
        u = 1
        v = 0
        u1 = 0
        v1 = 1
        rs = 0
        us = 0
        vs = 0
        q = 0

        while (r1 != 0):
            q = int(r / r1)
            rs = r
            us = u
            vs = v
            r = r1
            u = u1
            v = v1
            r1 = rs - q*r1
            u1 = us - q*u
            v1 = vs - q*v1
        if(v < 0):
            v = v * (-1)
        return [v]

    def decifrar(self,cifra,chave,caracteres):
        res = []
        for i in cifra:
            res.append( (i**chave[0]) % chave[1] )
        #print(res)

        textoOriginal =  ""
        for i in res:
            for chave,valor in caracteres.items():
                if(i == valor):
                    textoOriginal = textoOriginal + chave
        return textoOriginal






