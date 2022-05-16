from re import T
import turtle
from PyQt5 import QtWidgets,uic
from cgitb import text
from email.mime import base
import math
import click
from matplotlib.pyplot import title
from sympy import *
import sympy
from sympy.parsing.sympy_parser import parse_expr 
import numpy as np
from numpy.polynomial import Polynomial as P
from tabulate import tabulate
from scipy.misc import derivative
#from CALCULADORA.Graficador import funcion
from numpy.random import uniform as unif

import Graficador,CalcTrapecio,Rectangulo,calculadora_newton,simpson38,Determinante,Transpuesta,Inversa,Rango,Multiplicacion,Elevado




#iniciar app
app = QtWidgets.QApplication([])

#link archivos .iu
Main = uic.loadUi("Main.ui")
Quienes = uic.loadUi("Quienes.ui")
Choose = uic.loadUi("Choose.ui")
Bases = uic.loadUi("Bases.ui")
Binario = uic.loadUi("Binario.ui")
Octal = uic.loadUi("Octal.ui")
Decimal = uic.loadUi("Decimal.ui")
Hexadecimal = uic.loadUi("Hexadecimal.ui")
Ieee = uic.loadUi("IEEE.ui")
IeeeBits = uic.loadUi("IEEE_32y64.ui")
IeeeReverse = uic.loadUi("IEEE_Reverse.ui") 
IeeeReverse64 = uic.loadUi("IEEE_Reverse64.ui") 
Biseccion = uic.loadUi("Biseccion.ui")
ReglaFake = uic.loadUi("RelgaFake.ui")
Newton = uic.loadUi("Newton.ui")
Derivadas = uic.loadUi("Derivadas.ui")
Secante = uic.loadUi("Secante.ui")
Raices = uic.loadUi("Raices.ui")
Trapecio = uic.loadUi("Trapecio.ui")
Simpson13 = uic.loadUi("Simpson1_3.ui")
Simpson38 = uic.loadUi("Simpson3_8.ui")
Graficadora = uic.loadUi("Graficador.ui")
Montecarlo = uic.loadUi("Montecarlo.ui")
Rectangulos = uic.loadUi("Rectangulo.ui")
MatrixSimple = uic.loadUi("MatrisesSimple2x2.ui")
MatrixSimple3x3 = uic.loadUi("MatrisesSimple3x3.ui")
ChooseMatriz = uic.loadUi("MatricesChoose.ui")
MatricesChooseLong = uic.loadUi("MatricesChooseLong.ui")
#FUNCIONES  

    #Funcion para separar Entero y Fraccional
def parte_entera(numero):
    fraccion,entero = math.modf(numero)
    return int(entero)

def parte_fraccional(numero):
  fraccion,entero = math.modf(numero)
  return round(fraccion,10)

#funciones extra de emergencia
def parte_entera_a_binario(numero):
    entero = parte_entera(numero)
    binario = format(entero, '0b')
    return binario

def parte_fraccional_a_binario(numero):
  fraccional=parte_fraccional(numero)
  binario=""
  contador=0
  while contador != 12:
    multiplicacion = fraccional * 2
    binario=binario+str(parte_entera(multiplicacion))
    fraccional=parte_fraccional(multiplicacion)
    contador = contador + 1
  return binario

def decimal_a_binario(numero):
  binario=parte_entera_a_binario(numero)+"."+parte_fraccional_a_binario(numero)
  return binario

#EMERGENCIA EMERGENCIA EMERGENCIA EMERGENCIA

def base_entero_a_decimal(binario,base):
    entero = str(parte_entera(binario))
    decimal=0
    for posicion, digito_string in enumerate(entero[::-1]):
        decimal += int(digito_string) * base ** posicion

    return decimal

def base_fraccional_a_decimal(binario,base):
    fraccional = parte_fraccional(binario)
    entero_fraccional=""
    while parte_fraccional(fraccional) !=0:
        fraccional = fraccional * 10
        entero_fraccional += str(parte_entera(fraccional))
    fraccional= str(int(fraccional))


    decimal=0
    posicion =1
    for posicion, digito_string in enumerate(fraccional):
        decimal += float(digito_string) * (float(base ** 
        ((-posicion-1))))
    
    return decimal

def base_a_decimal(binario,base):
  decimal=str(float(base_entero_a_decimal(binario,base)+base_fraccional_a_decimal(binario,base)))
  return decimal

#EMERGENCIA EMERGENCIA EMERGENCIA EMERGENCIA



  #funcion para decimales
def CambioDecimalBinario():
    DigitoIngresado = float(Decimal.DecimalEntry.toPlainText())
    Digito = DigitoIngresado

    entero = int((parte_entera(Digito)))
    fraccional = parte_fraccional(Digito)
    binarioEntero = format(entero, '0b')
    binarioFraccional=""
    contador=0
    repeticiones = 12

    Decimal.ResultBinario.setText(str(binarioEntero))

    while contador != repeticiones:
        multiplicacion = fraccional *2
        binarioFraccional = binarioFraccional + str(parte_entera(multiplicacion))
        fraccional = parte_fraccional(multiplicacion)
        contador = contador +1

    ResultadoFinal = str(binarioEntero)+"."+str(binarioFraccional)
    Decimal.ResultBinario.setText(str(ResultadoFinal))

def CambioDecimalOctal():
    DigitoIngresado = float(Decimal.DecimalEntry.toPlainText())
    Digito = DigitoIngresado

    entero = int((parte_entera(Digito)))
    fraccional = parte_fraccional(Digito)
    octalEntero = format(entero, '0o')
    octalFraccional=""
    contador=0
    repeticiones = 12

    while contador != repeticiones:
        multiplicacion = fraccional * 8
        octalFraccional = octalFraccional + str(parte_entera(multiplicacion))
        fraccional = parte_fraccional(multiplicacion)
        contador = contador +1

    ResultadoFinal = str(octalEntero)+"."+str(octalFraccional)
    Decimal.ResultOctal.setText(str(ResultadoFinal))

def CambioDecimalHexadecimal():
    DigitoIngresado = float(Decimal.DecimalEntry.toPlainText())
    Digito = DigitoIngresado

    entero = int((parte_entera(Digito)))
    fraccional =float(parte_fraccional(Digito)) 
    HexadecimalEntero = format(entero, '0x')
    HexadecimalFraccional=""
    contador=0
    repeticiones = 30

    while contador != repeticiones:
        multiplicacion = fraccional * 16
        if parte_entera(multiplicacion)==10:
            valor=str("a")
        elif parte_entera(multiplicacion)==11:
            valor=str("b")
        elif parte_entera(multiplicacion)==12:
            valor=str("c")
        elif parte_entera(multiplicacion)==13:
            valor=str("d")
        elif parte_entera(multiplicacion)==14:
            valor=str("e")
        elif parte_entera(multiplicacion)==15:
            valor=str("f")
        else:
            valor=parte_entera(multiplicacion)

        HexadecimalFraccional=HexadecimalFraccional+str(valor)
        fraccional=parte_fraccional(multiplicacion)
        contador=contador+1
        

    ResultadoFinal = str(HexadecimalEntero)+"."+str(HexadecimalFraccional)
    Decimal.ResultHexadecimal.setText(str(ResultadoFinal))
    
  #Funcion para binario 
def CambioBinarioDecimal():
    DigitoIngresado = float(Binario.BinaryEntry.toPlainText())
    Digito = DigitoIngresado

    entero = str((parte_entera(Digito)))
    fraccional = parte_fraccional(Digito)
    base = 2
    decimalEntero = 0
    decimalFraccional = 0
    enteroFraccional = ""

    #BINARIO A DECIMAL 
    #parte entera a decimal
    exponente = len(entero)
    for  i in range(len(entero)):
        exponente = exponente - 1
        decimalEntero += int(entero[i]) * (base ** exponente)
    
    #parte fraccional a decimal
    while parte_fraccional(fraccional) != 0:
        fraccional = fraccional *10
        enteroFraccional += str(parte_fraccional(fraccional))
    fraccional = str(int(fraccional))


    for i in range(len (fraccional)):
        exponentefraccional = (i+1)*-1
        decimalFraccional += float(fraccional[i]) * base ** exponentefraccional    
    
    DecimalFinal = float(decimalEntero)+float(decimalFraccional)
    Binario.ResultDecimal.setText(str(DecimalFinal))   

    #BINARIO A OCTAL
    enteroBOctal = int((parte_entera(DecimalFinal)))
    fraccionalBOctal = parte_fraccional(DecimalFinal)
    octalEntero = format(enteroBOctal, '0o')
    octalFraccional=""
    contadorBOctal=0
    repeticiones = 12

    while contadorBOctal != repeticiones:
        multiplicacion = fraccionalBOctal * 8
        octalFraccional = octalFraccional + str(parte_entera(multiplicacion))
        fraccionalBOctal = parte_fraccional(multiplicacion)
        contadorBOctal = contadorBOctal +1

    ResultadoBinarioOctalFinal = str(octalEntero)+"."+str(octalFraccional)
    Binario.ResultOctal.setText(str(ResultadoBinarioOctalFinal))

    #BINARIO A HEXADECIMAL 
    enteroBHex = int((parte_entera(DecimalFinal)))
    fraccionalBHex =float(parte_fraccional(DecimalFinal)) 
    HexadecimalEntero = format(enteroBHex, '0x')
    HexadecimalFraccional=""
    contadorBHex=0
    repeticiones = 12

    while contadorBHex != repeticiones or parte_fraccional(fraccionalBHex) !=0:
        multiplicacionBHex = fraccionalBHex * 16
        if parte_entera(multiplicacionBHex)==10:
            valor=str("a") 
        elif parte_entera(multiplicacionBHex)==11:
            valor=str("b")
        elif parte_entera(multiplicacionBHex)==12:
            valor=str("c")
        elif parte_entera(multiplicacionBHex)==13:
            valor=str("d")
        elif parte_entera(multiplicacionBHex)==14:
            valor=str("e")
        elif parte_entera(multiplicacionBHex)==15:
            valor=str("f")
        else:
            valor=parte_entera(multiplicacionBHex)

        HexadecimalFraccional=HexadecimalFraccional+str(valor)
        fraccionalBHex=parte_fraccional(multiplicacionBHex)
        contadorBHex=contadorBHex+1
        

    ResultadoFinalBHex = str(HexadecimalEntero)+"."+str(HexadecimalFraccional)
    Binario.ResultHexadecimal.setText(str(ResultadoFinalBHex))

    #FUNCION PARA OCTAL
def CambioOctal():
    DigitoIngresado = float(Octal.OctalEntry.toPlainText())
    Digito = DigitoIngresado

    #Octal a Decimal
    entero = str((parte_entera(Digito)))
    fraccional = parte_fraccional(Digito)
    base = 8
    decimalEntero = 0
    OctalFraccional = 0
    enteroFraccional = ""

    exponente = len(entero)
    for  i in range(len(entero)):
        exponente = exponente - 1
        decimalEntero += int(entero[i]) * (base ** exponente)
    
    #parte fraccional a decimal
    while parte_fraccional(fraccional) != 0:
        fraccional = fraccional *10
        enteroFraccional += str(parte_fraccional(fraccional))
    fraccional = str(int(fraccional))


    for i in range(len (fraccional)):
        exponentefraccional = (i+1)*-1
        OctalFraccional += float(fraccional[i]) * base ** exponentefraccional    
    
    OctalFinal = float(decimalEntero)+float(OctalFraccional)
    Octal.ResultDecimal.setText(str(OctalFinal)) 

    #Octal a BInario
    enteroOBin = int((parte_entera(OctalFinal)))
    fraccionalOBin = parte_fraccional(OctalFinal)
    binarioEnteroOBin = format(enteroOBin, '0b')
    binarioFraccionalOBin=""
    contador=0
    repeticiones = 12

    while contador != repeticiones:
        multiplicacion = fraccionalOBin *2
        binarioFraccionalOBin = binarioFraccionalOBin + str(parte_entera(multiplicacion))
        fraccionalOBin = parte_fraccional(multiplicacion)
        contador = contador +1

    ResultadoFinal = str(binarioEnteroOBin)+"."+str(binarioFraccionalOBin)
    Octal.ResultBinary.setText(str(ResultadoFinal))

    #Octal a Hexadecimal
    enteroOHex = int((parte_entera(OctalFinal)))
    fraccionalOHex =float(parte_fraccional(OctalFinal)) 
    HexadecimalEntero = format(enteroOHex, '0x')
    HexadecimalFraccional=""
    contadorOHex=0
    repeticiones = 12

    while contadorOHex != repeticiones:
        multiplicacionOHex = fraccionalOHex * 16
        if parte_entera(multiplicacionOHex)==10:
            valor=str("a")
        elif parte_entera(multiplicacionOHex)==11:
            valor=str("b")
        elif parte_entera(multiplicacionOHex)==12:
            valor=str("c")
        elif parte_entera(multiplicacionOHex)==13:
            valor=str("d")
        elif parte_entera(multiplicacionOHex)==14:
            valor=str("e")
        elif parte_entera(multiplicacionOHex)==15:
            valor=str("f")
        else:
            valor=parte_entera(multiplicacionOHex)

        HexadecimalFraccional=HexadecimalFraccional+str(valor)
        fraccionalOHex=parte_fraccional(multiplicacionOHex)
        contadorOHex=contadorOHex+1
        

    ResultadoFinal = str(HexadecimalEntero)+"."+str(HexadecimalFraccional)
    Octal.ResultHexadecimal.setText(str(ResultadoFinal))

    #FUNCION PARA HEXADECIMAL 
def CambioHexadecimal():
    DigitoIngresado = Hexadecimal.HexaEntry.toPlainText()
    Digito =str(DigitoIngresado)   

    auxentero = ""  
    auxfrac = ""
    contentero = 0
    contfrac = 0
    flag = True

    for i in range(len(Digito)-1):
        if Digito[i] == '.':
            flag = False
        if flag == True:
            auxentero += Digito[i]
            contentero += 1
        
        elif flag == False:  
         auxfrac += Digito[i+1]
         contfrac += 1
    entero = 0
    fracc = 0

    contentero = contentero -1 

    for i in range(len(auxentero)):
        if auxentero[i] == "a" or auxentero[i] == "A":
            entero += 10 *16 ** contentero
        elif auxentero[i] == "b" or auxentero[i] == "B":
            entero +=11*16 ** contentero
        elif auxentero[i] == "c" or auxentero[i] == "C":
            entero +=12 *16 **contentero
        elif auxentero[i] == "d" or auxentero[i] == "D":
          entero += 13 * 16 ** contentero
        elif auxentero[i] == "e" or auxentero[i] == "E":
            entero += 14 * 16 ** contentero
        elif auxentero[i] == "F" or auxentero[i] == "F":
             entero += 15 * 16 ** contentero
        else:
            entero += int(auxentero[i]) * 16 ** contentero

        contentero = contentero -1

    conta = -1
    for i in range(len(auxfrac)):
        if auxfrac[i] == "a" or auxfrac[i] == "A":
            fracc += 10 * 16 ** (conta)
        elif auxfrac[i] == "b" or auxfrac[i] == "B":
            fracc += 11 * 16 ** (conta)
        elif auxfrac[i] == "c" or auxfrac[i] == "C":
            fracc += 12 * 16 ** (conta)
        elif auxfrac[i] == "d" or auxfrac[i] == "D":
            fracc += 13 * 16 ** (conta)
        elif auxfrac[i] == "e" or auxfrac[i] == "E":
            fracc += 14 * 16 ** (conta)
        elif auxfrac[i] == "f" or auxfrac[i] == "F":
            fracc += 15 * 16 ** (conta)
        else:
            fracc += int(auxfrac[i]) * 16 ** (conta)
        conta=conta-1

    resultado = float(entero) + float(fracc)
    Hexadecimal.ResultDecimal.setText(str(resultado))

    #Hexadecimal a Binario
    enteroHBin = int((parte_entera(resultado)))
    fraccionalHBin = parte_fraccional(resultado)
    HexaEntero = format(enteroHBin, '0b')
    HexaFraccional=""
    contadorHexa=0
    repeticiones = 12

    while contadorHexa != repeticiones:
        multiplicacionHBin = fraccionalHBin *2
        HexaFraccional = HexaFraccional + str(parte_entera(multiplicacionHBin))
        fraccionalHBin = parte_fraccional(multiplicacionHBin)
        contadorHexa = contadorHexa +1

    ResultadoFinal = str(HexaEntero)+"."+str(HexaFraccional)
    Hexadecimal.ResultBinary.setText(str(ResultadoFinal))

    #Hexadecimal a Octal
    enteroHOct = int((parte_entera(resultado)))
    fraccionalHOct = parte_fraccional(resultado)
    octalEnteroHOct = format(enteroHOct, '0o')
    octalFraccionalHOct=""
    contadorHOct=0
    repeticiones = 12

    while contadorHOct != repeticiones:
        multiplicacion = fraccionalHOct * 8
        octalFraccionalHOct = octalFraccionalHOct + str(parte_entera(multiplicacion))
        fraccionalHOct = parte_fraccional(multiplicacion)
        contadorHOct = contadorHOct +1

    ResultadoFinal = str(octalEnteroHOct)+"."+str(octalFraccionalHOct)
    Hexadecimal.ResultOctal.setText(str(ResultadoFinal))    

#IEEE 32 Y 64 
def IEEE32():
    DigitoIngresado  = IeeeBits.IeeeEntry.toPlainText()
    Digito = (DigitoIngresado)
    
    numero = ""
    #Signo
    signo = 0

    for i in range(len(Digito)):
        if Digito[i] == '-':
            signo = 1
        else: 
            numero += Digito[i]
    
    numero = float(numero)

    contComa = 0

    binario = parte_entera(numero)
    binario = format(binario, '0b')
    
    flag = True
    while flag == True:
        binario = float(binario)/float(10)
        if parte_entera(binario)==1:
            flag = False
        contComa += 1
    
    suma = contComa + 127
    suma2= contComa + 1023
    exponente=parte_entera_a_binario(suma)
    exponente2 = parte_entera_a_binario(suma2)

    binario2 = float(decimal_a_binario(numero))
    while parte_entera(binario2) != 1:
        binario2 = float(binario2/10)
    mantisa = parte_fraccional(binario2)
    contador2 = 0
    while parte_fraccional(mantisa)!=0:
        mantisa = mantisa*10
        contador2 = contador2+1
    
    faltante = 23 - contador2
    faltante2 = 52 - contador2
    mantisa = int(mantisa)
    mantisa2 = int(mantisa)
    for i in range(0,faltante-1):
        mantisa=str(mantisa)+str(0)
    for i in range(0,faltante2-1):
        mantisa2=str(mantisa2)+str(0)    
    
    
    ResultadoFinal = str(signo)
    IeeeBits.Signo32.setText(ResultadoFinal)
    IeeeBits.Signo64.setText(ResultadoFinal)

    IeeeBits.ResultExp.setText(str(exponente))
    IeeeBits.ResultExp2.setText(str(exponente2))

    IeeeBits.ResultMants.setText(str(mantisa))
    IeeeBits.ResultMants2.setText(str(mantisa2))



    
    #  FUncion IEEE Reverso 
def IEEEReverse():
      
      Signo = int (IeeeReverse.SignoEntry.toPlainText())
      Exponente =int(IeeeReverse.ExpEntry.toPlainText())
      Mantisa = int(IeeeReverse.MantsEntry.toPlainText())
      
      binario = base_entero_a_decimal(Exponente, 2)

      cantComas = binario - 127

      contador = 0
      aux = Mantisa

      while aux >0:
        aux //=10
        contador += 1

      division = int(contador) - (cantComas)

      agregado = str(1)+str(Mantisa)

      for i in range(0,division):
        agregado = float(agregado) / float(10)
    

      reverso = base_a_decimal(float(agregado), 2)
  
      if Signo==1:
        reverso = float(reverso)*float(-1)
      
      IeeeReverse.ResultRev.setText(str(reverso))

def IEEEReverse64():
      
      Signo = int (IeeeReverse64.SignoEntry.toPlainText())
      Exponente =int(IeeeReverse64.ExpEntry.toPlainText())
      Mantisa = int(IeeeReverse64.MantsEntry.toPlainText())
      
      binario = base_entero_a_decimal(Exponente, 2)

      cantComas = binario - 1023

      contador = 0
      aux = Mantisa

      while aux >0:
        aux //=10
        contador += 1

      division = int(contador) - (cantComas)

      agregado = str(1)+str(Mantisa)

      for i in range(0,division):
        agregado = float(agregado) / float(10)
    

      reverso = base_a_decimal(float(agregado), 2)
  
      if Signo==1:
        reverso = float(reverso)*float(-1)
      
      IeeeReverse64.ResultRev.setText(str(reverso))

#Bisseccion

def f(x):
    Funcion = str(Biseccion.FuncionEntry.toPlainText())
    return eval(Funcion)

def GraficarBiseccion():
    x=sympy.symbols('x')
    Funcion = str(Biseccion.FuncionEntry.toPlainText())
    sympy.plot(Funcion,(x,-10,10),title = 'LA RAIZ ES', aspect_ratio = 'auto')

    

def Bisseccion():
    Funcion = str(Biseccion.FuncionEntry.toPlainText())
    Tolerancia = float(Biseccion.ToleranciaEntry.toPlainText())
    LimiteIncial = float(Biseccion.LimInfEntry.toPlainText())
    LimiteSuperior = float(Biseccion.LimSupEntry.toPlainText())
    
    Tupla = []
    Arreglo = () 
    
    Interacciones = 1
    F_c = 99999

    contIter = int(0)

    while abs(F_c)>=Tolerancia:
        contIter += 0
        puntoMedio = (LimiteIncial + LimiteSuperior)/2
        F_Li = f(LimiteIncial)
        F_Ls = f(LimiteSuperior)
        F_c = f(puntoMedio)

        Interacciones +=1
        
        Tupla.append([str(Interacciones-1),str(F_Li),str(F_Ls),str(F_c)])
        Arreglo = Tupla[0:Interacciones]

                  
           

        if(F_Li * F_c)<0:
            LimiteSuperior = puntoMedio
        elif (F_Ls * F_c)<0:
            LimiteIncial = puntoMedio

        if abs(F_c)<Tolerancia:
            break

    result = tabulate(Tupla, headers=[" Inter "," F(a) "," F(b) "," Error " ])
    Biseccion.ResultInter.setText(str(result))
    Biseccion.ResultRaiz.setText(str(puntoMedio))
    

#REGLA FALSA
def f_f(x):
    Ecuacion = str(ReglaFake.FunEntry.toPlainText()) 
    funcion = sympy.sympify(Ecuacion)
    b = funcion.free_symbols
    var = b.pop()
    valor = funcion.evalf(subs = {var:x})
    return valor

def GraficaReglaFalsa():
    x=sympy.symbols('x')
    Funcion = str(ReglaFake.FunEntry.toPlainText()) 
    sympy.plot(Funcion,(x,-10,10),title = 'LA RAIZ ES', aspect_ratio = 'auto')

def ReglaFalsa():
    Ecuacion = str(ReglaFake.FunEntry.toPlainText()) 
    ExtremoInferior = str(ReglaFake.PtoIniEntry.toPlainText()) 
    ExtremoSuperior = str(ReglaFake.PtoFinEntry.toPlainText()) 
    Tolerancia = float(ReglaFake.ErrorEntry.toPlainText()) 
    
    Tupla = [[]]
    Arreglo = () 
    
    x,y = sympy.symbols('x y')
    error = 10.0

    if (f_f(ExtremoInferior) * f_f(ExtremoSuperior)<0):
        Interacciones = 1

        
        while error > Tolerancia and Interacciones < 200:

            fa = float(f_f(ExtremoInferior))
            fb = float(f_f(ExtremoSuperior))
            m = ((float(ExtremoInferior) * float(fb)) - (float(ExtremoSuperior) * float(fa)))/(fb - fa)
            fm = f_f(m)

            Tupla.append([str(Interacciones-1),str(fa),str(fb),str(m)])
            Arreglo = Tupla[0:Interacciones]  

            if fm == 0:
                raiz = m
                break
            elif fa * fm <0:
                ExtremoSuperior = m
            else:
                ExtremoInferior = m
            raiz = m
            error = abs(fm)

            Interacciones += 1
        result = tabulate(Tupla, headers=[" Inter "," F(a) "," F(b) "," Error " ])
        ReglaFake.ResultFake.setText(str(result))
        ReglaFake.ResultRaiz.setText(str(raiz))
        ReglaFake.ResultError.setText(str(error))
    else:
        ReglaFake.ResultRaiz.setText(str("No hay raiz"))

#Calculadora de Derivadas
def Derivada():
    x = symbols('x')
    Funcion = Derivadas.FunEntry.toPlainText()
    f=str(Funcion)
       
    derivada = diff(f,x)
    derivada2 = diff(derivada)
    derivada3 = diff(derivada2)
    derivada4 = diff(derivada3)
    integral = integrate(f,x)
    
    
    Derivadas.ResultPderiv.setText(str(derivada))
    Derivadas.ResultSderiv.setText(str(derivada2))
    Derivadas.ResultTderiv.setText(str(derivada3))
    Derivadas.ResultCderiv.setText(str(derivada4))
    Derivadas.ResultInteg.setText(str(integral))

    
#newtan
def NewtonRapshon():
    XInicial = Derivadas.FunEntry.toPlainText()
    Iteraciones = Derivadas.FunEntry.toPlainText()

    def NRf(XInicial):
        Funcion = Derivadas.FunEntry.toPlainText()
        f = eval(Funcion)
        return f
    def NRdf(XInicial):
        Funcion = Derivadas.FunEntry.toPlainText()
        df = np.diff(Funcion)
        return df 
    
    for intercept in range(1, Iteraciones):
        i = x - (NRf(x)/NRdf(x))
        x = i
    ReglaFake.ResultFake.setText(str(x)) #x
    ReglaFake.ResultFake.setText(str(Iteraciones)) #iteraciones
     
    
#Polinomios
def Polinomios():
    P = np.zeros([5])

    P[0] = Raices.Entry4.toPlainText() #cuadratico
    P[1] = Raices.Entry3.toPlainText() #lineal
    P[2] = Raices.Entry2.toPlainText() #independiente
    P[3] = Raices.Entry1.toPlainText() #independiente
    P[4] = Raices.Entry0.toPlainText() #independiente

    Resultado=str(np.roots(P))
    Raices.ResultRaices.setText(Resultado)

def GraficaPolinomios():
    x=sympy.symbols('x')
  
    Term4 = (Raices.Entry4.toPlainText())
    Term3 = (Raices.Entry3.toPlainText())
    Term2 = (Raices.Entry2.toPlainText())
    Term1 = (Raices.Entry1.toPlainText())
    Term  = (Raices.Entry0.toPlainText())

    Ecuacion =float(Term4)*x**4+float(Term3)*x**3+float(Term2)*x**2+float(Term1)*x+float(Term)
    Funcion = sympy.sympify(Ecuacion)
    sympy.plot(Funcion,(x,-10,10),aspect_ratio = 'auto' )
    


 
#SECANTES
x = symbols('x')
def S_f(x):
    Funcion = str(Secante.FunEntry.toPlainText())
    return eval(Funcion)

def GraficarSecante():
    Funcion = str(Secante.FunEntry.toPlainText())
    sympy.plot(Funcion,(x,-10,10),aspect_ratio = 'auto' )
def Secantes():
      
    SX1 =float(Secante.PtoIniEntry.toPlainText())
    SX2 =float(Secante.PtoFinEntry.toPlainText())
    Tolerancia = float(Secante.TolEntry.toPlainText())
    

    error = 99999
    n = 0
    SX3 = 0
    
    while float(error) > Tolerancia:
        SX3 = SX1 - ((SX2-SX1)/(S_f(SX2)-      
        S_f(SX1)))*S_f(SX1)
        SX1 = SX2
        SX2 = SX3
        error = abs(S_f(SX3))
        n += 1

    Secante.ResultError.setText(str(SX3))
    Secante.ResultInterSec.setText(str(n))

#Newton-Rhapson
def Ff(x):
   Ecuacion = Newton.FunEntry.toPlainText()
   Funcion = sympy.sympify(Ecuacion)
   b = Funcion.free_symbols
   var = b.pop()
   valor = Funcion.evalf(subs = {var:x})
   return valor

def Dff(x):
    Ecuacion = Newton.FunEntry.toPlainText()
    Funcion = sympy.sympify(Ecuacion)
    b = Funcion.free_symbols
    var = b.pop()
    valor = Funcion.evalf(subs = {var:x})
    return valor


def NewtonRapshon():

    PtoInicial =float  (Newton.PtoIniEntry.toPlainText())
    Tolerancia = float (Newton.TolEntry.toPlainText())

    contador = 0
    result3 =  ()
    result2 = [[]]

    result1 = " "

    while (abs(Ff(PtoInicial))> Tolerancia and contador <199):

        x1 = PtoInicial - Ff(PtoInicial) / Dff(PtoInicial)
        PtoInicial = x1

        result2.append([PtoInicial])
        contador += 1
    if (contador==199):
        Newton.ResultRaizNewton.setText(str("No se logro encontrar la raiz"))
    else:
        Newton.ResultRaizNewton.setText(str(PtoInicial))
        Newton.ResultRaizNewton_2.setText(str(abs(Ff(PtoInicial))))
        

        
        result3 =(result2[0:3])
        result = tabulate(result3, headers=[" Inter "," F(a) "," F(b) "," Error " ])
        Newton.ResultInterNewton.setText(str(result))
        print(result3)

def GraficarNewton():
    Funcion = str(Newton.FunEntry.toPlainText())
    Ecuacion =sympy.sympify(Funcion)
    sympy.plot(Ecuacion, (x,-10,10))




def CTrapecio():
    ''' x = symbols('x')
    fx =  lambda x: np.sqrt(x) * np.sin(x) '''
    Funcion      = str(Trapecio.FuncionEntry.toPlainText())
    a            = int(Trapecio.ExtIzqEntry.toPlainText())
    b            = int(Trapecio.ExtDerEntry.toPlainText()) 
    Particiones  = int(Trapecio.ParticionesEntry.toPlainText())
    CalcTrapecio.ecuacion(Funcion,a,b,Particiones)
    Trapecio.ResultIntegral.setText(str(CalcTrapecio.area))
    Trapecio.ResultError.setText(str(CalcTrapecio.error))
    

def CalcRectangulo():
    funcion = str(Rectangulos.FuncionEntry.toPlainText())
    a       = int(Rectangulos.ExtIzqEntry.toPlainText())
    b       = int(Rectangulos.ExtDerEntry.toPlainText())
    n       = int(Rectangulos.ParticionesEntry.toPlainText())  
    Rectangulo.ecu(funcion,a,b,n)
    Rectangulos.ExtIzqReect.setText(str(Rectangulo.left_riemann_sum))
    Rectangulos.ProMediorect.setText(str(Rectangulo.midpoint_riemann_sum))
    Rectangulos.ExtDerReect.setText(str(Rectangulo.right_riemann_sum))


def evaluacion (x):
    funcion = list(Simpson13.FuncionEntry.toPlainText())
    copia = funcion.copy()
    for j in range (len(copia)):
        if copia [j] == "x":
             copia [j] == x
    return eval("".join(copia))

def CSimpson13():

    funcion = list(Simpson13.FuncionEntry.toPlainText())
    a       = float(Simpson13.ExtIzqEntry.toPlainText())
    b       = float(Simpson13.ExtDerEntry.toPlainText())
    n       = int  (Simpson13.ParticionesEntry.toPlainText())

    expr = "".join(funcion)
    f = sympify(expr)
    derivada1 = sympy.diff(f)
    derivada2 = sympy.diff(derivada1)
    
    h = (b-a)/n 
    total = 0

    for i in range (1,n):
        x = a + (i*h)
        if (i%2==0):
            total+=2*evaluacion(x)
        else:
            total+=4*evaluacion(x)
    total +=evaluacion(a)+evaluacion(b)
    total = total*((1/3)*h)

    error = 0
    k = np.random.uniform (a,b+1)
    z = float(a+(k*a-b))
    error = -(((h)**3/12)*(derivada2*(z)))

    Simpson13.ResultIntegral.setText(str(total))
    Simpson13.ResultError.setText(str(error))


def evaluacion1 (x):
    funcion = list(Simpson38.FuncionEntry.toPlainText())
    copia = funcion.copy()
    for j in range (len(copia)):
        if copia [j] == "x":
             copia [j] == x
    return eval("".join(copia))


def CSimpson38():

    funcion = str (Simpson38.FuncionEntry.toPlainText())
    a       = float(Simpson38.ExtIzqEntry.toPlainText())
    b       = float(Simpson38.ExtDerEntry.toPlainText())
    n       = int  (Simpson38.ParticionesEntry.toPlainText())
    simpson38.ecuacion(funcion,a,b,n)
    Simpson38.ResultIntegral.setText(str(simpson38.suma))
    Simpson38.ResultError.setText(str(simpson38.errorporcent))

def montecarlo():
    Funcion = list (Montecarlo.FuncionEntry.toPlainText())
    a       = float(Montecarlo.ExtIzqEntry.toPlainText())
    b       = float(Montecarlo.ExtDerEntry.toPlainText())
    n       = int(Montecarlo.ParticionesEntry.toPlainText())

    e = np.linspace(a,b,0.1)
    x = unif(a,b,n) 
    

    expr = "".join(Funcion)
    f = sympify(expr)
    suma = 0

    

    for i in range(n):
        evalu = x[i]
        suma = suma + f.evalf(subs = {"e" : evalu})

    resultado = (b-a)*suma/n 

    Montecarlo.ResultIntegral.setText(str(resultado))

def MatrixDeterminante():
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
  
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
   
    Determinante.matricesDeterminante2x2(num1,num2,num4,num5)
    MatrixSimple.ResultMatrix.setText(str(Determinante.result1))

def MatrixDeterminante3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    Determinante.matricesDeterminante3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9)
    
    MatrixSimple3x3.ResultMatrix.setText(str(Determinante.result2))

def MatrixTranspuesta():
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
  
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
   
    Transpuesta.matricesTranspuesta2x2(num1,num2,num4,num5)
    MatrixSimple.ResultMatrix.setText(str(Transpuesta.result1))

def MatrixTranspuesta3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    Transpuesta.matricesTranspuesta3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9)
    
    MatrixSimple3x3.ResultMatrix.setText(str(Transpuesta.result2))

def MatrixInversa():
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
  
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
   
    Inversa.matricesInversa2x2(num1,num2,num4,num5)
    MatrixSimple.ResultMatrix.setText(str(Inversa.result1))

def MatrixInversa3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    Inversa.matricesInversa3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9)
    
    MatrixSimple3x3.ResultMatrix.setText(str(Inversa.result2))

def MatrixRango():
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
  
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
   
    Rango.matricesRango2x2(num1,num2,num4,num5)
    MatrixSimple.ResultMatrix.setText(str(Rango.result1))

def MatrixRango3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    Rango.matricesRango3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9)
    
    MatrixSimple3x3.ResultMatrix.setText(str(Rango.result2))

def MatrixMult():
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
    Mult = float (MatrixSimple.MultiEntry.toPlainText())
   
    Multiplicacion.matricesMult2x2(num1,num2,num4,num5,Mult)
    MatrixSimple.ResultMatrix.setText(str(Multiplicacion.result2))

def MatrixMult3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    Mult = float (MatrixSimple3x3.MultiEntry.toPlainText())
   
    Multiplicacion.matricesMult3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9,Mult)
    MatrixSimple3x3.ResultMatrix.setText(str(Multiplicacion.result1))

def MatrixElev():
    
    num1 = float(MatrixSimple.num1Entry.toPlainText())
    num2 = float(MatrixSimple.num2Entry.toPlainText())
    num4 = float(MatrixSimple.num4Entry.toPlainText())
    num5 = float(MatrixSimple.num5Entry.toPlainText())
    elev = int(MatrixSimple.ElevEntry.toPlainText())
   
    Elevado.matricesElevado2x2(num1,num2,num4,num5,elev)
    MatrixSimple.ResultMatrix.setText(str(Elevado.result2))

def MatrixElev3x3():
    num1 = float(MatrixSimple3x3.num1Entry.toPlainText())
    num2 = float(MatrixSimple3x3.num2Entry.toPlainText())
    num3 = float(MatrixSimple3x3.num3Entry.toPlainText())
    num4 = float(MatrixSimple3x3.num4Entry.toPlainText())
    num5 = float(MatrixSimple3x3.num5Entry.toPlainText())
    num6 = float(MatrixSimple3x3.num6Entry.toPlainText())
    num7 = float(MatrixSimple3x3.num7Entry.toPlainText())
    num8 = float(MatrixSimple3x3.num8Entry.toPlainText())
    num9 = float(MatrixSimple3x3.num9Entry.toPlainText())
    elev = int(MatrixSimple3x3.ElevEntry.toPlainText())
    Elevado.matricesElevado3x3(num1,num2,num3,num4,num5,num6,num7,num8,num9,elev)
    MatrixSimple3x3.ResultMatrix.setText(str(Elevado.result1))


















#BOTONES

    #Main Buttons
def gui_Start():
    Main.close()
    Choose.show()

def gui_WhoBtn():
    Main.close()
    Quienes.show()

def gui_BackWho():
    Quienes.close()
    Main.show()
    
def gui_Close():
    Choose.close()

def gui_BackAll():
    Choose.show()

    #Choose Window
def gui_Bases():
    Choose.close()
    Bases.show()

    #Bases Window
def gui_BackBtnBases():
    Bases.close()
    Choose.show()

def gui_Binary():
    Bases.close()
    Binario.show()

def gui_BackBtnBinary():
    Binario.close()
    Bases.show()

def Btn_BinaryCalculate():
    CambioBinarioDecimal()
    

def gui_Octal():
    Bases.close()
    Octal.show()

def gui_BackBtnOctal():
    Octal.close()
    Bases.show()

def Btn_OctalCalculate():
    CambioOctal()
    

def gui_Decimal():
    Bases.close()
    Decimal.show()

def gui_BackBtnDecimal():
    Decimal.close()
    Bases.show()

def Btn_DecimalCalculate():
    CambioDecimalBinario()
    CambioDecimalOctal()
    CambioDecimalHexadecimal()

def gui_Hexaecimal():
    Bases.close()
    Hexadecimal.show()

def gui_BackBtnHexadecimal():
    Hexadecimal.close()
    Bases.show()

def Btn_HexadecimalCalculate():
    CambioHexadecimal()
    
    

    #IEEE Window
def gui_IEEE():
    Choose.close()
    Ieee.show()

def gui_BackBtnIEEE():
    Ieee.close()
    Choose.show()

def gui_IEEEBits():
    Ieee.close()
    IeeeBits.show()

def gui_BackBtnBits():
    IeeeBits.close()
    Ieee.show()

def Btn_Calculate32():
    IEEE32()


def gui_IEEEReverse():
    Ieee.close()
    IeeeReverse.show()

def gui_BackBtnReverse():
    IeeeReverse.close()
    Ieee.show()

def Btn_CalculateReverse():
    IEEEReverse()

def gui_IEEEReverse64():
    Ieee.close()
    IeeeReverse64.show()

def gui_BackBtnReverse64():
    IeeeReverse64.close()
    Ieee.show()

def Btn_CalculateReverse64():
    IEEEReverse64()

def gui_Newton():
    Choose.close()
    Newton.show()

def gui_BackNewton():
    Newton.close()
    Choose.show()

def Btn_NewtonCalculate():
    ''' NewtonRapshon() '''
    str_ecuacion = Newton.FunEntry.toPlainText()
    puntoInicio =float  (Newton.PtoIniEntry.toPlainText())
    toler = float (Newton.TolEntry.toPlainText())
    calculadora_newton.newtonR(str_ecuacion,puntoInicio,toler)
    Newton.ResultRaizNewton.setText(str(calculadora_newton.raiz))
    Newton.ResultRaizNewton_2.setText(str(calculadora_newton.error))
    Newton.ResultInterNewton.setText(str(calculadora_newton.contador))
    

def gui_Biseccion():
    Choose.close()
    Biseccion.show()

def gui_BackBtnBisec():
    Biseccion.close()
    Choose.show()

def Btn_BisecCalculate():
    Bisseccion()

def Btn_BisecGraficar():
    GraficarBiseccion()


def gui_ReglaFalsa():
    Choose.close()
    ReglaFake.show()

def gui_BackBtnFalsa():
    ReglaFake.close()
    Choose.show()

def Btn_CalculateFalsa():
    ReglaFalsa()

def Btn_FakeGraficar():
    GraficaReglaFalsa()


def gui_Derivadas():
    Choose.close()
    Derivadas.show()

def gui_BackBtnDerivada():
    Derivadas.close()
    Choose.show()

def Btn_CalculateDerivada():
    Derivada()

def gui_Secantes():
    Choose.close()
    Secante.show()

def gui_BackSecantes():
    Secante.close()
    Choose.show()

def Btn_SecantesCalculate():
    Secantes()

def Btn_SecanteGraficar():
    GraficarSecante()

def gui_RaicesPol():
    Choose.close()
    Raices.show()

def gui_BackBtnRaices():
    Raices.close()
    Choose.show()

def Btn_CalculateRaices():
    Polinomios()

def Btn_GraficaPolinomios():
    GraficaPolinomios()

def Btn_GraficaNewton():
    GraficarNewton()

def gui_Trapecio():
    Choose.close()
    Trapecio.show()

def gui_BackBtnTrapecio():
    Trapecio.close()
    Choose.show()

def Btn_CalculateTrapecio():
    CTrapecio()

def gui_Simpson13():
    Choose.close()
    Simpson13.show()

def gui_BackBtnSimpson13():
    Simpson13.close()
    Choose.show()

def Btn_CalculateSimpson13():
    CSimpson13()


def gui_Simpson38():
    Choose.close()
    Simpson38.show()

def gui_BackBtnSimpson38():
    Simpson13.close()
    Choose.show()

def Btn_CalculateSimpson38():
    CSimpson38()

def gui_Graficadora():
    Choose.close()
    Graficadora.show()

def gui_ButtonGraficadora():
    ecuacion=Graficadora.GraphEntry.toPlainText()
    Graficador.funcion(ecuacion)
    

def gui_BackButtonGraficadora():
    Graficadora.close()
    Choose.show()

def gui_Montecarlo():
    Choose.close()
    Montecarlo.show()

def Btn_CalculateMontecarlo():
    montecarlo()

def gui_BackBtnMontecarlo():
    Montecarlo.close()
    Choose.show()

def gui_Rectangulo():
    Choose.close()
    Rectangulos.show()

def Btn_CalculateRectangulo():
    CalcRectangulo()

def gui_BackBtnRectangulo():
    Rectangulos.close()
    Choose.show()

def gui_matrices():
    Choose.close()
    ChooseMatriz.show()

def gui_BackbtnMatriz():
    ChooseMatriz.close()
    Choose.show()

#longitud de matricez
def gui_LongMatrices():
    ChooseMatriz.close()
    MatricesChooseLong.show()

def gui_BackLongMatrices():
    MatricesChooseLong.close()
    ChooseMatriz.show()
    

#abrir matriz 2x2
def Gui_open2x2():
    MatricesChooseLong.close()
    MatrixSimple.show()

def Gui_open3x3():
    MatricesChooseLong.close()
    MatrixSimple3x3.show()


#matrices 2x2
def gui_Matricez1op():
    ChooseMatriz.close()
    MatrixSimple.show()

def gui_backMatricez1op():
    MatrixSimple.close()
    ChooseMatriz.show()

def Btn_1Matricez():
    MatrixDeterminante()

#matriz 3x3
def gui_Matricez3x3():
    ChooseMatriz.close()
    MatrixSimple3x3.show()

def Gui_backMaatriz3x3():
    MatrixSimple3x3.close()
    MatricesChooseLong.show()

def Btn_Matrix3x3():
    MatrixDeterminante3x3()

    



#Main BUtton Link
Main.StartButton.clicked.connect(gui_Start)
Main.WhoButton.clicked.connect(gui_WhoBtn)

#Quienes Button link
Quienes.backButton.clicked.connect(gui_BackWho)

#Choose Buttons Link
Choose.BackButton.clicked.connect(gui_Close)
Choose.BasesButton.clicked.connect(gui_Bases)
Choose.IEEEButton.clicked.connect(gui_IEEE)
Choose.NewtonButton.clicked.connect(gui_Newton)
Choose.BisecButton.clicked.connect(gui_Biseccion)
Choose.FakeButton.clicked.connect(gui_ReglaFalsa)
Choose.DerivadaButton.clicked.connect(gui_Derivadas)
Choose.SecanteButton.clicked.connect(gui_Secantes)
Choose.RaicesButton.clicked.connect(gui_RaicesPol)
Choose.TrapecioButton.clicked.connect(gui_Trapecio)
Choose.Simpson13Button.clicked.connect(gui_Simpson13)
Choose.Simpson38Button.clicked.connect(gui_Simpson38)
Choose.GraphButton.clicked.connect(gui_Graficadora)
Choose.MontecarloButton.clicked.connect(gui_Montecarlo)
Choose.RectanguloButton.clicked.connect(gui_Rectangulo)
Choose.MatrixButton.clicked.connect(gui_matrices)

#Bases Buttons Link
Bases.BasesBackButton.clicked.connect(gui_BackBtnBases)
Bases.BinaryButton.clicked.connect(gui_Binary)
Bases.OctalButton.clicked.connect(gui_Octal)
Bases.DecimalButton.clicked.connect(gui_Decimal)
Bases.HexadecimalButton.clicked.connect(gui_Hexaecimal)

Binario.BInaryBackButton.clicked.connect(gui_BackBtnBinary)
Binario.BinaryCalculateButton.clicked.connect(Btn_BinaryCalculate)

Octal.OcatlBackButton.clicked.connect(gui_BackBtnOctal)
Octal.OctalCalculateButton.clicked.connect(Btn_OctalCalculate)
Decimal.DecimalBackButton.clicked.connect(gui_BackBtnDecimal)
Decimal.DecimalCalculateButton.clicked.connect(Btn_DecimalCalculate)


Hexadecimal.HexadecimalBackButton.clicked.connect(gui_BackBtnHexadecimal)
Hexadecimal.HexaCalculateButton.clicked.connect(Btn_HexadecimalCalculate)

#IEEE Buttons link
Ieee.IEEEBackButton.clicked.connect(gui_BackBtnIEEE)
Ieee.IEEEBitsButton.clicked.connect(gui_IEEEBits)
Ieee.IEEEInvButton.clicked.connect(gui_IEEEReverse)
Ieee.IEEEInvButton2.clicked.connect(gui_IEEEReverse64)

IeeeBits.BitsBackButton.clicked.connect(gui_BackBtnBits)
IeeeBits.IEEECalculateButton.clicked.connect(Btn_Calculate32)


IeeeReverse.ReverseBackButton.clicked.connect(gui_BackBtnReverse)
IeeeReverse.RevCalculateButton.clicked.connect(Btn_CalculateReverse)

IeeeReverse64.ReverseBackButton.clicked.connect(gui_BackBtnReverse64)
IeeeReverse64.RevCalculateButton.clicked.connect(Btn_CalculateReverse64)

Biseccion.BisecBackButton.clicked.connect(gui_BackBtnBisec)
Biseccion.BisCalculateButton.clicked.connect(Btn_BisecCalculate)
Biseccion.BisGraficarButton.clicked.connect(Btn_BisecGraficar)

ReglaFake.FakeBackButton.clicked.connect(gui_BackBtnFalsa)
ReglaFake.FakeCalculateButton.clicked.connect(Btn_CalculateFalsa)
ReglaFake.FakeGraficaButton.clicked.connect(Btn_FakeGraficar)

Newton.NewtonBackButton.clicked.connect(gui_BackNewton)
Newton.NewtonCalculateButton.clicked.connect(Btn_NewtonCalculate)
Newton.NewtonGraficaButton.clicked.connect(Btn_GraficaNewton)

Derivadas.FakeBackButton.clicked.connect(gui_BackBtnDerivada)
Derivadas.DerivCalculateButton.clicked.connect(Btn_CalculateDerivada)

Secante.SecanteCalculateButton.clicked.connect(Btn_SecantesCalculate)
Secante.GraficarSecanteButton.clicked.connect(Btn_SecanteGraficar)
Secante.SecanteBackButton.clicked.connect(gui_BackSecantes)

Raices.RaicesBackButton.clicked.connect(gui_BackBtnRaices)
Raices.RaicesCalculateButton.clicked.connect(Btn_CalculateRaices)
Raices.RaicesGraficarButton.clicked.connect(Btn_GraficaPolinomios)

Trapecio.TrapBackButton.clicked.connect(gui_BackBtnTrapecio)
Trapecio.TrapCalculateButton.clicked.connect(Btn_CalculateTrapecio)

Simpson13.simp18BackButton.clicked.connect(gui_BackBtnSimpson13)
Simpson13.Simp13CalculateButton.clicked.connect(Btn_CalculateSimpson13)

Simpson38.simp38BackButton.clicked.connect(gui_BackBtnSimpson38)
Simpson38.Simp38CalculateButton.clicked.connect(Btn_CalculateSimpson38)

Graficadora.GraphBackButton.clicked.connect(gui_BackButtonGraficadora)
Graficadora.GraphButton.clicked.connect(gui_ButtonGraficadora)

Montecarlo.MontCalculateButton.clicked.connect(Btn_CalculateMontecarlo)
Montecarlo.MontBackButton.clicked.connect(gui_BackBtnMontecarlo)

Rectangulos.RecCalculateButton.clicked.connect(Btn_CalculateRectangulo)
Rectangulos.RectBackButton.clicked.connect(gui_BackBtnRectangulo)

ChooseMatriz.ChoseMaBackButton.clicked.connect(gui_BackbtnMatriz)

#longitud de matricez
ChooseMatriz.btnOpSimples.clicked.connect(gui_LongMatrices)
MatricesChooseLong.ChoseMaBackButton.clicked.connect(gui_BackLongMatrices)
MatricesChooseLong.M2x2.clicked.connect(gui_Matricez1op)
MatricesChooseLong.M3x3.clicked.connect(gui_Matricez3x3)


#2x2
MatrixSimple.MatBackButton.clicked.connect(gui_backMatricez1op)
MatrixSimple.DetCalculButton.clicked.connect(Btn_1Matricez)
MatrixSimple.TranCalculButton.clicked.connect(MatrixTranspuesta)
MatrixSimple.InvCalcButton.clicked.connect(MatrixInversa)
MatrixSimple.RanCalcButton.clicked.connect(MatrixRango)
MatrixSimple.MultCalcButton.clicked.connect(MatrixMult)
MatrixSimple.ElevCalcButton.clicked.connect(MatrixElev)

#3x3
MatrixSimple3x3.MatBackButton.clicked.connect(Gui_backMaatriz3x3)
MatrixSimple3x3.DetCalculButton.clicked.connect(Btn_Matrix3x3)
MatrixSimple3x3.TranCalculButton.clicked.connect(MatrixTranspuesta3x3)
MatrixSimple3x3.InvCalcButton.clicked.connect(MatrixInversa3x3)
MatrixSimple3x3.RanCalcButton.clicked.connect(MatrixRango3x3)
MatrixSimple3x3.MultCalcButton.clicked.connect(MatrixMult3x3)
MatrixSimple3x3.ElevCalcButton.clicked.connect(MatrixElev3x3)





#Exectue
Main.show()
app.exec()