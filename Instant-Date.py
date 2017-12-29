import datetime
from datetime import date
from VALID import OKI, ER, ns
import subprocess

def año_valido(a):
    if a<0 or a>9999:
        a=año_valido(OKI(input("El año no puede ser menor de 0 ni mayor de 9999: ")))
    return a
    

def dia_valido(año,mes,dia):
    d1=date(año,mes,1)
    if mes==12:
        d2=date(año+1,1,1)
    else:
        d2=date(año,mes+1,1)
    diferencia=d2-d1
    while dia>diferencia.days or dia<1:
        dia=OKI(input("Número de dia no valido: "))
    return dia

def mes_valido(mes):#REVISAR
    while mes<1 or mes>12:
        mes=mes_valido(OKI(input("Mes no valido: ")))
    return mes

def hora_valida():
    while True:
        h=OKI(input("Introduce hora: "))
        if h<0 or h>=24:
            pass
        else:
            break
    return h

def mn_valido(n):#ESTA FUNCION VALE TANTO PARA LOS MINUTOS COMO PARA LOS SEGUNDOS
    while True:#REVISAR
        if n==("m"):
            mn=OKI(input("Introduce minuto: "))
        else:
            mn=OKI(input("Introduce segundo: "))
        if mn<0 or mn>=60:
            pass
        else:
            break
    return mn

def entering_date0(h1,m1,s1,h2,m2,s2):
    D_hora=abs(h2-h1);D_minuto=abs(m2-m1);D_segundo=abs(s2-s1)
    lista=[D_hora,D_minuto,D_segundo]
    return lista

def entering_date(a,m,d,h,mi,s):
    D=datetime.datetime(a,m,d,h,m)
    return D


while True:
    print("""El presente programa calcula las horas, minutos y segundos
entre dos fechas cualesquiera tanto del pasado como del futuro""")
    print("INSTANT DATE")
    print("*********PRIMER SUCESO*********")
    año1=año_valido(OKI(input("Introduce año: ")))
    mes1=mes_valido(OKI(input("Introduce mes: ")))
    dia1=dia_valido(año1,mes1,OKI(input("Introduce día: ")))
    hora1=hora_valida()
    minuto1=mn_valido("m")
    segundo1=mn_valido("s")
    print("*********SEGUNDO SUCESO*********")
    año2=año_valido(OKI(input("Introduce año: ")))
    mes2=mes_valido(OKI(input("Introduce número del mes: ")))
    dia2=dia_valido(año2,mes2,OKI(input("Introduce día: ")))
    hora2=hora_valida()
    minuto2=mn_valido("m")
    segundo2=mn_valido("s")
    
    if año1==año2 and mes1==mes2 and dia1==dia2:
        hms=entering_date0(hora1,minuto1,segundo1,hora2,minuto2,segundo2)
        Horas_totales=hms[0]
        Minutos_totales=(hms[0]*60)+(hms[1])
        Segundos_totales=(Minutos_totales*60)+(hms[2])
        print("HORAS TOTALES:",Horas_totales,ER(Horas_totales),"MINUTOS TOTALES:",Minutos_totales,ER(Minutos_totales),"SEGUNDOS TOTALES:",Segundos_totales,ER(Segundos_totales))
    else:
        D1=entering_date(año1,mes1,dia1,hora1,minuto1,segundo1)
        D2=entering_date(año2,mes2,dia2,hora2,minuto2,segundo2)

        difer=(str(abs(D2-D1))).split(",")
        numero_dias=((difer[0].split(" "))[0])

        tiempo=difer[1].split(":")
        #print(difer)
    
        numero_horas=int(tiempo[0])
        numero_minutos=int(tiempo[1])
        print(numero_minutos)
        numero_segundos=int(tiempo[2])

        Total_horas=(int(numero_dias)*24)+numero_horas
        Total_minutos=((Total_horas*60)+numero_minutos)+minuto2
        Total_segundos=((Total_minutos*60)+numero_segundos)+segundo2
        print("HORAS TOTALES:",Total_horas,ER(Total_horas),"MINUTOS TOTALES:",Total_minutos,ER(Total_minutos),"SEGUNDOS TOTALES:",Total_segundos,ER(Total_segundos))
    preg=ns(input("¿Desea efectuar más calculos?: "))
    if preg==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
