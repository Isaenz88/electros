import numpy as np
import math

coordinates = []

def getCoords(gro):
	coordinates = []
	atomtypes = []
	archivo = open(gro, "r")
	for line in archivo:
		linea = line.split()
		if (len(linea) == 7):
			coordinates.append((float(linea[4]),float(linea[5]),float(linea[6])))
			atomtypes.append(linea[2])
	return [len(coordinates),coordinates,atomtypes]



def calcularDistancias(lista):

	distancias = np.zeros([len(lista),len(lista)],dtype=np.float32)
	for i in range(0, len(lista)):
		for j in range(i+1, len(lista)):
			distancia = math.sqrt(math.pow(lista[i][0]-lista[j][0],2) + math.pow(lista[i][1]-lista[j][1],2) + math.pow(lista[i][2]-lista[j][2],2))
			distancias[i][j] = distancia
			distancias[j][i] = distancia
	return distancias

def getExclusions(top):

	archivo = open(top,"r")
	found = False
	for line in archivo:
	
		if found:
			if (not "[" in line ):
				linea = line.split()
				if not(len(linea) == 0):
					continue
			else: 
				break

		if "exclusions" in line:
			found = True
		

def getAtomParameters(top):

	atomtypes = []
	archivo = open(top,"r")
	
	atomtypes_found = False
	atoms_found = False
	for line in archivo:
		
		if atomtypes_found:
			if (not "[" in line ):
				linea = line.split()
				if not(len(linea) == 0 ) and not(linea[0].startswith(";")):
					atomtypes.append([linea[0],float(linea[5]),float(linea[6])])

			else: 
				atomtypes_found = False
				continue
		if "atomtypes" in line:
			atomtypes_found = True
		
		if "atoms" in line:
			atoms_found = True

		
		elif atoms_found:
			if(not "[" in line):
				linea = line.split()
				if not(len(linea) == 0 ) and not(linea[0].startswith(";")):
					for i in atomtypes:
						if (i[0] == linea[1]) and not (len(i) == 4) :
							i.append(float(linea[6]))
							break
			else:
				break		





	return atomtypes
	
num_atoms = getCoords("sys.gro")[0]
coordinates = getCoords("sys.gro")[1]
atom_types = getCoords("sys.gro")[2]
print num_atoms
print coordinates
print atom_types
distancias = calcularDistancias(coordinates)
print distancias
atomParameters = getAtomParameters("sys.top")
print atomParameters
exclusions = getExclusions("sys.top")
print exclusions
