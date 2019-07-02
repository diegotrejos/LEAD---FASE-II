import copy
import struct

class n_nPaq:

    def __init__(self, cat, s, origen, dest, tipo, pos, ip, puerto, prio):
        self.categoria = cat
        self.sn = s
        self.origenNaranja = origen
        self.destinoNaranja = dest
        self.tipo = tipo
        self.posGrafo = pos
        self.ipAzul = ip
        self.puertoAzul = puerto
        self.prioridad = prio

    def serialize(self):
        paquete = struct.pack('!bHbbcH15pHI', self.categoria, self.sn, self.origenNaranja, self.destinoNaranja,
                              self.tipo.encode(),
                              self.posGrafo, self.ipAzul.encode(), self.puertoAzul, self.prioridad)
        return paquete

    def unserialize(self, byteP):
        #paquete = struct.unpack('!bHbbcH15pHI', byteP)

        self.categoria = int.from_bytes(byteP[:1], byteorder=("big"))
        self.sn = int.from_bytes(byteP[1:3], byteorder=("big"))
        self.origenNaranja = int.from_bytes(byteP[3:4], byteorder=("big"))
        self.destinoNaranja = int.from_bytes(byteP[4:5], byteorder=("big"))
        self.tipo = str(byteP[5:6])
        self.posGrafo = int.from_bytes(byteP[6:8], byteorder=("big"))
        self.ipAzul = str(byteP[8:23])
        self.puertoAzul = int.from_bytes(byteP[23:25], byteorder=("big"))
        self.prioridad = int.from_bytes(byteP[25:29], byteorder=("big"))
        
        return self

    def imprimir(self):
        print("---Contenido del Paquete---")
        print("Categoria = ", self.categoria)
        print("SN = ", self.sn)
        print("Origen Naranja = ", self.origenNaranja)
        print("Destino Naranja = ", self.destinoNaranja)
        print("Tipo = ", self.tipo)
        print("Posicion del Grafo = ", self.posGrafo)
        print("IP Azul = ", self.ipAzul)
        print("Puerto Azul = ", self.puertoAzul)
        print("Prioridad = ", self.prioridad)
        print("---------------------------")


# ----------------------------------------------------------

# para puebas
def main():
    ooPaq = n_nPaq(0, 145, 3, 6, 'r', 350, '01.02.03.04', 5050, 1000)
    ooPaq.imprimir()

    paqueteS = ooPaq.serialize()

    ooPaq.unserialize(paqueteS)

    p1 = struct.unpack('!b', paqueteS[0:1])  # categoria
    print(p1[0])
    p2 = struct.unpack('!H', paqueteS[1:3])  # SN
    print(p2[0])
    p3 = struct.unpack('!b', paqueteS[3:4])  # origen
    print(p3[0])
    p4 = struct.unpack('!b', paqueteS[4:5])  # destino
    print(p4[0])
    p5 = struct.unpack('!c', paqueteS[5:6])  # tipo
    print(p5[0])
    p6 = struct.unpack('!H', paqueteS[6:8])  # posGrafo
    print(p6[0])
    p7 = struct.unpack('!15p', paqueteS[8:23])  # IP
    print(p7[0])
    p8 = struct.unpack('!H', paqueteS[23:25])  # puerto
    print(p8[0])
    p9 = struct.unpack('!I', paqueteS[25:29])  # prioridad
    print(p9[0])


if __name__ == "__main__":
    main()
