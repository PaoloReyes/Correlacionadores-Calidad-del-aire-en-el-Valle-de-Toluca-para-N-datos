import math

arch = open("Base De Datos Reto.csv", "r")
PM10 = []
PM25 = []
O3 = []
NO2 = []
CO = []
SO2 = []
iteracion = 1
for reg in arch.readlines():
    lista = reg.split(",")
    lista[6] = lista[6][:-1]
    if iteracion == 1:
        PM10titulo = lista[1]
        PM25titulo = lista[2]
        O3titulo = lista[3]
        NO2titulo = lista[4]
        COtitulo = lista[5]
        SO2titulo = lista[6]
    else:
        PM10.append(int(lista[1]))
        PM25.append(int(lista[2]))
        O3.append(int(lista[3]))
        NO2.append(int(lista[4]))
        CO.append(int(lista[5]))
        SO2.append(int(lista[6]))
    iteracion = iteracion+1
arch.close()

ttl = [PM10titulo, PM25titulo, O3titulo, NO2titulo, COtitulo, SO2titulo]
var = [PM10, PM25, O3, NO2, CO, SO2]
estadisticos = ["Covarianza: ", "Coeficiente de Pearson: ", "Coeficiente de Determinacion: "]

arch = open("Correlaciones.csv", "w")
arch.write(estadisticos[0]+","+ttl[0]+","+ttl[1]+","+ttl[2]+","+ttl[3]+","+ttl[4]+","+ttl[5]+","+"\n")
arch.close()
bigCovlist = []
big_rlist = []
bigR2list = []
for i in range(6):
    covlist = []
    rlist = []
    R2list = []
    for j in range(6):
        xp = sum(var[i])/len(var[i])
        yp = sum(var[j])/len(var[i])
        xy = 0
        difX2 = 0
        difY2 = 0
        for k in range(len(var[i])):
            difX = var[i][k]-xp
            difY = var[j][k]-yp
            xy = xy+(difX)*(difY)
            difX2 = difX2+difX*difX
            difY2 = difY2+difY*difY
        cov = xy/(len(var[i])-1)
        ra = xy/math.sqrt(difX2*difY2)
        R2a = ra*ra
        covlist.append(cov)
        rlist.append(ra)
        R2list.append(R2a)
    bigCovlist.append(covlist)
    big_rlist.append(rlist)
    bigR2list.append(R2list)
arch = open("Correlaciones.csv", "a")
for cov in range(len(bigCovlist)):
    arch.write(ttl[cov]+","+str(bigCovlist[cov][0])+","+str(bigCovlist[cov][1])+","+str(bigCovlist[cov][2])+","+str(bigCovlist[cov][3])+","+str(bigCovlist[cov][4])+","+str(bigCovlist[cov][5])+"\n")
arch.write("\n\n")
arch.write(estadisticos[1]+","+ttl[0]+","+ttl[1]+","+ttl[2]+","+ttl[3]+","+ttl[4]+","+ttl[5]+","+"\n")
for r in range(len(big_rlist)):
    arch.write(ttl[r]+","+str(big_rlist[r][0])+","+str(big_rlist[r][1])+","+str(big_rlist[r][2])+","+str(big_rlist[r][3])+","+str(big_rlist[r][4])+","+str(big_rlist[r][5])+"\n")
arch.write("\n\n")
arch.write(estadisticos[2]+","+ttl[0]+","+ttl[1]+","+ttl[2]+","+ttl[3]+","+ttl[4]+","+ttl[5]+","+"\n")
for R2 in range(len(big_rlist)):
    arch.write(ttl[R2]+","+str(bigR2list[R2][0])+","+str(bigR2list[R2][1])+","+str(bigR2list[R2][2])+","+str(bigR2list[R2][3])+","+str(bigR2list[R2][4])+","+str(bigR2list[R2][5])+"\n")
arch.close()