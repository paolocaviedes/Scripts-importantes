def latitudGPRMCdegrees(latitud,direccion):
	auxiliar=float(latitud)/100.0
	auxiliar=int(auxiliar)
	auxiliar2=(float(latitud)-(auxiliar*100))/60.0
	latitude=auxiliar+auxiliar2
	if direccion=="S":
		return latitude*-1
	else:
		return latitude

def longitudGPRMCdegrees(longitud,direccion):
	auxiliar=float(longitud)/100.0
	auxiliar=int(auxiliar)
	auxiliar2=(float(longitud)-(auxiliar*100))/60
	longitude=auxiliar+auxiliar2
	if direccion=="W":
		return longitude*-1
	else:
		return longitude

#print latitudGPRMCdegrees(2029.49050,"N")
#print longitudGPRMCdegrees(10316.32055,"W")

