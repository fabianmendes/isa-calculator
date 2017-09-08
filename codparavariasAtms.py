import math

R = 287.00
g = 9.80665  # m/pow(seg,2)

# class Atmosferas:
#     def temp1(self, LAPSE_RATE, t0, deltah,tobtenidas):
#         a = float(LAPSE_RATE)
#         list(tobtenidas)
#         t1 = t0 + a * deltah
#         tobtenidas.append(t1)

# ...realmente no hace falta esto j;


altkm = (0, 11, 20, 32, 47, 51, 71, 84.852, 90, 105)
altitudes = {"11": -0.0065,
             "20": 0,
             "32": 0.001,
             "47": 0.0028,
             "51": 0,
             "71": -0.0028,
             "84.852": -0.002,
             "90": 0,
             "105": 0.004} #alturas MAX
tiniciales = {"0" : 288.15,
             "11": 216.65,
             "20": 216.65,
             "32": 228.65,
             "47": 270.65,
             "51": 270.65,
             "71": 214.65,
             "84.852": 186.95,
             "90": 186.95} #temperaturas MIN

while True:  # para la hMAX
    try:
        h1 = float(input("Ingrese su Altura, o Altitud, FINAL [mETROS]: "))
        h1 = abs(h1)
        if h1 > int(150000):
            print("Uy. Eso está pasando la 'Mesopause' (por allá en la Thermosphera o incluso más allá)"
                  "\n Este programa trabaja básicamente con la International Standar Atmosphere (ISA)"
                  "\n\t Por favor. Intentelo de nuevo, ¡y asegure su de Altitud!")
            continue
        else:
            break
    except: print("Por favor, ingrese únicamente en Números.")
    finally: print("Recuerde que, hasta los momentos, no son aceptadas altitudes que esten por debajo del nivel del mar."
                   "\n\t Altura MÁX a usar \t: ",h1/1000,"km")

h1 = h1

try:  # para la hMIN
    while True:
        h0 = (input("\nAhora. Ingrese su Altura, o Altitud, INICIAL [mETROS]: "))
        h00 = bool(h0)
        if h00 != True:
            h0 = 0
            p0 = 101325  # default
            break
        elif float(h0) >= h1:
            print("Ingrese un valor Distinto y MENOR a su Altitud Final..")
            continue
        else:
            h0 = abs(float(h0))
            p0 = (input("Esta vez: Ingrese su Presión INICIAL [PaSCAL]: "))
            p00 = bool(p0)
            if p00 != True:
                p0 = 101325  # default
                p0 = float(p0)
                break
            else:
                p0 = abs(float(p0))
            break
except: print("Por favor, ingrese únicamente en Números.")
finally: print("Recuerde que, hasta los momentos, no son aceptadas altitudes\n"
               "\t que esten por debajo del nivel del mar.\n","km\n\t Altura MIN a usar \t: ",h0/1000,"km")

h0 = h0
nro = 1
nro1 = 0
tobtenidas = []
pobtenidas = []
while h0 <= h1:
    cond = (1000 * float(altkm[nro]))
    # cond = altura tope (km, altitud MAX) de la list
    try:
        if h0 < cond:
            alt = str(altkm[nro])  # key con la altura para hayar 'a'
            LAPSE_RATE = altitudes[alt]  # 'a' correspondiente
            if nro1 == 0:
                t0 = float(tiniciales.get(str(altkm[nro1])))  # temperatura MIN de la list
            else:
                t0 = T
            cond1 = cond - h1
            if cond1 <= 0:
                deltah = cond - h0
            else:
                deltah = h1 - h0
            a = float(LAPSE_RATE)
            list(tobtenidas)
            t1 = t0 + a * deltah
            tobtenidas.append(t1)
            T = tobtenidas[-1]
            if LAPSE_RATE == 0:
                exponente = -g / (T * R)  # 'T = tobtenidas(-1)'
                p1 = p0 * pow(math.e, exponente * deltah)
                pobtenidas.append(p1)
            else:
                exponente = -g / (LAPSE_RATE * R)
                ctteT = T / t0
                p1 = p0 * pow(ctteT, exponente)
                pobtenidas.append(p1)
            p0 = p1
            h0 = cond
        else:
            pass
    finally:
        nro += 1
        nro1 += 1

P = pobtenidas[-1]
den1 = P/(R*T)
print("\t\t AQUÍ TIENE SUS VALORES:"
     "\n Temperatura a", str(h1/1000),"km \t= ", T, "K"  #unsupported operand type(s) for +: 'float' and 'str'
     "\n Presión a dicha Altitud \t= ", P, "Pa"
     "\n Densidad en dicho punto \t= ", den1, "kg/(m^3)")
