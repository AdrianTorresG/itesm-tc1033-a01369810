def llenar_diccionario():
    ciudades = {}
    meses = {}
    with open("datos_vuelos.csv", "r") as vuelos:
        filas = vuelos.readlines()
        for i in filas():
            vuelos = i.split(",")
            matricula = vuelos[1]
            salida = vuelos[2]
            llegada = vuelos[3]
            pasajeros = vuelos[4]
        if "D" in matricula:
            matricula = "Alemania"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "PP" in matricula:
            matricula = "Brasil"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "CF" in matricula:
            matricula = "Canada"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "A7" in matricula:
            matricula = "Catar"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "CC" in matricula:
            matricula = "Chile"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "B" in matricula:
            matricula = "China"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "OY" in matricula:
            matricula = "Dinamarca"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "HC" in matricula:
            matricula = "Ecuador"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "A6" in matricula:
            matricula = "Emiratos Arabes"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "EC" in matricula:
            matricula = "España"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "N" in matricula:
            matricula = "Estados Unidos"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "PK" in matricula:
            matricula = "Indonesia"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "JA" in matricula:
            matricula = "Japon"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "XA" in matricula:
            matricula = "Mexico"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "9V" in matricula:
            matricula = "Singapur"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "HS" in matricula:
            matricula = "Tailandia"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}

        if "D"or"PP"or"CF"or"A7"or"CC"or"B"or"OY"or"HC"or"A6"or"EC"or"N"or"PK"or"JA"or"XA"or"9V"or"HS" not in matricula:
            matricula = "Otro"
            if matricula not in ciudades.keys():
                ciudades[matricula] = {}


        if "1801" in salida:
            salida = "Enero"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1802" in salida:
            salida = "Febrero"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1803" in salida:
            salida = "Marzo"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1804" in salida:
            salida = "Abril"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1805" in salida:
            salida = "Mayo"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1806" in salida:
            salida = "Junio"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1807" in salida:
            salida = "Julio"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1808" in salida:
            salida = "Agosto"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1809" in salida:
            salida = "Septiembre"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1810" in salida:
            salida = "Octubre"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1811" in salida:
            salida = "Noviembre"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1
        if "1812" in salida:
            salida = "Diciembre"
            if matricula not in meses.keys():
                meses[salida] = {}
                meses[salida] = 1
            meses[salida] += 1

        def contar_vuelos(mes, lista):
            vuelos = 0
            for i in lista:
                if mes == i:
                    vuelos += 1
            return vuelos

        T_E=contar_vuelos("Enero", meses)
        T_F=contar_vuelos("Febrero", meses)
        T_Mr=contar_vuelos("Marzo", meses)
        T_Ab=contar_vuelos("Abril", meses)
        T_My=contar_vuelos("Mayo", meses)
        T_Jn=contar_vuelos("Junio", meses)
        T_Jl=contar_vuelos("Julio", meses)
        T_Ag=contar_vuelos("Agosto", meses)
        T_S=contar_vuelos("Septiembre", meses)
        T_Oc=contar_vuelos("Octubre", meses)
        T_Nv=contar_vuelos("Noviembre", meses)
        T_D=contar_vuelos("Diciembre", meses)

        for ciudades in meses:
            if ciudades[:] not in meses[salida].keys():
                ciudades[matricula] = 0
            else:
                ciudades[matricula] += 1
