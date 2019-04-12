import time
from datetime import date
import subprocess

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n


def hms(timer):
    h=(timer*24)
    mi=(h*60)
    sec=(mi*60)
    TT=(h,mi,sec)
    return TT
    

def pregunta(timer): #ESTA FUNCION PREGUNTA SI SE QUIERE INCLUIR AMBAS FECHAS EN EL COMPUTO (VALE PARA "A","B" Y "C").
    AD=ns(input("¿Incluir ambos dias en el computo?: "))
    if AD==("s"):
        timer=timer+1
    return(timer)   
        

def nums(a):
    while a<1 or a>9999:
        a=OKI(input("Año no valido: "))
    return a

def mes(m):#HAN DE SER ENTEROS
    while m>12 or m<1:
        m=OKI(input("Hay 12 meses,(introduce un valor entre 1 y 12 ambos incluidos): "))
    return(m)


def mess(a,m,d):#PARA APLICAR LA FUNCION ESTAS VARIABLES HAN DE SER ENTEROS!!!
    M1=date(a,m,1)
    if a<9999 or m<12: #PARA ESTABLECER EL ÚLTIMO DIA DEL MES EN CUESTIÓN
        if m==12:
            M2=date(a+1,1,1)#ESTO SOLO SI a<9999.
        else:
            M2=date(a,m+1,1)#ESTO PARA m<12.
        MD=abs(M1-M2)
        while d>MD.days or d<1:
            d=OKI(input("La cifra del día está fuera del rango para el mes escogido: "))
    else:
        while d>31:
            d=OKI(input("La cifra del día está fuera del rango para el mes escogido: "))
    return d

def meses(Fm):
    A=("","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    n=-1
    for i in A:
        n+=1
        if int(Fm[1])==n:
            return i
            break
def semana(n):
    N=-1
    for i in("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"):
        N+=1
        if N==n:
            return(i)
            break


while True:
    print("") 
    print(" _________________________________________")
    print("/_    ____________________________________/")
    print("  /  / __   _________   ______   _______")
    print(" /  / |  | |  _   _  | | =====| |  ----_|")
    print("/__/  |__| |_| |_| |_| |______| |_|  \_\ ")
    print("*********************************************")
    print("")
    print("Escoja una opción:")
    print("A)Calcular el número de días tomando como referencia la fecha actual.")
    print("B)Calcular el número de días entre dos fechas distintas a la actual.")
    print("C)Conocer fecha a partir del número de días.")
    op=input("Introduzca aquí su opción: ")
    while op!=("A") and op!=("B") and op!=("C"):
        op=input("Escriba solo \'A\',\'B\'o\'C\' segun su opción: ")
    today=date.today()
    cal=ns(input("¿Desea ver calendarios?: "))
    if op==("A") or op==("B"):
        segg=ns(input("¿Desea ver el tiempo en horas, minutos y segundos?: "))
    if op==("A"):
        a=nums(OKI(input("Año del suceso: ")))#;a=nums(OKI(a))
        m=mes(OKI(input("Mes del suceso: ")))#;m=mes(OKI(m))
        d=OKI(input("Dia del suceso: "));#d=OKI(d)
        Di=mess(a,m,d)
        D1=date(a,m,Di)
        if D1==(today):
            print("Hoy es",D1)
        timer=abs(D1-today).days
        timer=pregunta(timer)
        if D1>today:
            print("")
            print("Quedan",timer,"dias para la fecha escogida.")
        else:
            print("")
            print("Han transcurrido",timer,"dias desde la fecha escogida.")
        print("("+str(int(timer/7)),"semanas y",timer%7,"dias)")
        if cal==("s"):
            import calendar
            print("")
            CAL=calendar.c.prmonth(a,m)
            print("")
        if segg==("s"):
            tiempo_detall=(hms(timer))
            print(tiempo_detall[0],ER(tiempo_detall[0]),"horas",tiempo_detall[1],ER(tiempo_detall[1]),"minutos y",tiempo_detall[2],ER(tiempo_detall[2]),"segundos")
    if op==("B"):
        a=nums(OKI(input("Año del primer suceso: ")))#;a=nums(OKI(a))
        m=mes(OKI(input("Mes del primer suceso: ")))#;m=mes(OKI(m))
        d=OKI(input("Día del primer suceso: "))#;d=OKI(d)
        Di=mess(a,m,d)
        D1=date(a,m,Di)
        Dist1=abs(D1-today).days
        a2=nums(OKI(input("Año del segundo suceso: ")))#;a2=nums(OKI(a2))
        m2=mes(OKI(input("Mes del segundo suceso: ")))#;m2=mes(OKI(m2))
        d2=OKI(input("Día del segundo suceso: "))#;d2=OKI(d2)
        Dii=mess(a2,m2,d2)
        D2=date(a2,m2,Dii)
        Dist2=abs(D2-today).days
        if (D1<=today and D2<=today) or (D1>=today and D2>=today):
            timer=abs(Dist1-Dist2)
            timer=pregunta(timer)
            if D1<=today and D2<=today:
                print("")
                print("Transcurrieron",timer,"dias entre las dos fechas indicadas.")
            else:
                print("")
                print("Transcurriran",timer,"dias entre las dos fechas indicadas.")
            print("("+str(int(timer/7)),"semanas y",timer%7,"dias)")
            print("")
        else:
            timer=(Dist1+Dist2)
            timer=pregunta(timer)
            print("")
            print("Transcurrirán",timer,"dias entre las dos fechas indicadas.")
            print("("+str(int(timer/7)),"semanas y",timer%7,"dias)")
            print("")
            
        if cal==("s"):
            import calendar
            print("")
            CAL=calendar.c.prmonth(a,m)
            CAL2=calendar.c.prmonth(a2,m2)
            print("")
            
        if segg==("s"):
            tiempo_detall=(hms(timer))
            print(tiempo_detall[0],"horas",tiempo_detall[1],"minutos y",tiempo_detall[2],"segundos")
        
    if op==("C"):
        num=OKI(input("Escriba el número de días: "))
        pas_fut=input("¿Al pasado (\'p\') o al futuro (\'f\'): ")
        while pas_fut!=("p") and pas_fut!=("f"):
            pas_fut=input("Esciba solo \'p\'o\'f\'según su opción: ")
        Dia1=date(1,1,1);HOY=int((today-Dia1).days)+1#SE ESTABLECE EL ORDINAL DE LA FECHA ACTUAL
        Dia_ult=date(9999,12,31);fut_hoy=int((Dia_ult-today).days)#SE ESTABLECE LO QUE FALTA PARA EL ULTIMO DIA
        if pas_fut==("p"):
            while num>HOY:
                print("La cantidad introducida es superior al numero de dias transcurridos, el tope es de",HOY-1,"dias")
                num=OKI(input("Prueba con otro número: "))
            dist=HOY-num
            dateo=date.fromordinal(dist)#RESUMIR
            date_spl=str(dateo).split("-")
            mes_nom=meses(date_spl)
            week_day=(dateo).weekday()
            dia_semana=semana(week_day)
            print("")
            print("Hace",num,"días era",dia_semana,date_spl[2],"de",mes_nom,"de",date_spl[0])
            print("")
        if pas_fut==("f"):
            while num>fut_hoy:
                print("La cantidad introducida es superior al numero de dias restantes, el tope es de",fut_hoy,"dias")
                num=OKI(input("Prueba con otro número: "))
            dist=HOY+num
            dateo=date.fromordinal(dist)#RESUMIR
            date_spl=str(dateo).split("-")
            mes_nom=meses(date_spl)
            week_day=(dateo).weekday()
            dia_semana=semana(week_day)
            print("")
            print("Dentro de",num,"días será",dia_semana,date_spl[2],"de",mes_nom,"de",date_spl[0])
            print("")
        if cal==("s"):
            import calendar
            print("")
            CAL=calendar.c.prmonth(int(date_spl[0]),int(date_spl[1]))
            print("")
    print("")
    c=ns(input("¿Desea continuar?: "))
    if c==("n"):
        break
    try:
        subprocess.call(["cmd.exe","/C","cls"])
    except:
        continue
    
