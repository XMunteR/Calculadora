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

import Graficador,CalcTrapecio,Rectangulo,calculadora_newton,simpson38,Determinante,Transpuesta,Inversa,Rango,Multiplicacion,Elevado,GausJordan,CalcMatrizEcuaLinea,montecarlo,AjusteCurvas




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
MatrixSimple2x3 = uic.loadUi("MatrisesSimple2x3.ui")
MatrixSimple3x2 = uic.loadUi("MatrisesSimple3x2.ui")
MatrixSimple3x3 = uic.loadUi("MatrisesSimple3x3.ui")
MatrixGauss = uic.loadUi("MatrisesGauss.ui")
MatrixGauss2x2 = uic.loadUi("MatrisesGauss2x2.ui")
MatrixGauss3x3 = uic.loadUi("MatrisesGauss3x3.ui")
MatrixGauss4x4 = uic.loadUi("MatrisesGauss4x4.ui")
MatrixGauss5x5 = uic.loadUi("MatrisesGauss5x5.ui")
MatrixGauss6x6 = uic.loadUi("MatrisesGauss6x6.ui")
MatrixGauss7x7 = uic.loadUi("MatrisesGauss7x7.ui")
OpMatrixSimple3x3 = uic.loadUi("OpMatrisesSimple3x3.ui")
ChooseMatriz = uic.loadUi("MatricesChoose.ui")
MatricesChooseLong = uic.loadUi("MatricesChooseLong.ui")
AjusteDeCurvas = uic.loadUi("ajusteDcurvas.ui")




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

def Fmontecarlo():
    Funcion = str (Montecarlo.FuncionEntry.toPlainText())
    a       = float(Montecarlo.ExtIzqEntry.toPlainText())
    b       = float(Montecarlo.ExtDerEntry.toPlainText())
    n       = int(Montecarlo.ParticionesEntry.toPlainText())

    montecarlo.f(Funcion)
    montecarlo.MFuncion(a,b,n)
    Montecarlo.ResultIntegral.setText(str(montecarlo.resultado))

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

def MatrixGauss2():
    num1 = float(MatrixGauss2x2.num1Entry.toPlainText())
    num2 = float(MatrixGauss2x2.num2Entry.toPlainText())
    num4 = float(MatrixGauss2x2.num4Entry.toPlainText())
    num5 = float(MatrixGauss2x2.num5Entry.toPlainText())
    ind1 = float(MatrixGauss2x2.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss2x2.ind2Entry.toPlainText())
    
    GausJordan.GaussJordan2x3(num1,num2,num4,num5,ind1,ind2)
    MatrixGauss2x2.ResultMatrix.setText(str(GausJordan.result2x2))

def MatrixGauss3():
    num1 = float(MatrixGauss3x3.num1Entry.toPlainText())
    num2 = float(MatrixGauss3x3.num2Entry.toPlainText())
    num3 = float(MatrixGauss3x3.num3Entry.toPlainText())
    num4 = float(MatrixGauss3x3.num4Entry.toPlainText())
    num5 = float(MatrixGauss3x3.num5Entry.toPlainText())
    num6 = float(MatrixGauss3x3.num6Entry.toPlainText())
    num7 = float(MatrixGauss3x3.num7Entry.toPlainText())
    num8 = float(MatrixGauss3x3.num8Entry.toPlainText())
    num9 = float(MatrixGauss3x3.num9Entry.toPlainText())
    ind1 = float(MatrixGauss3x3.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss3x3.ind2Entry.toPlainText())
    ind3 = float(MatrixGauss3x3.ind3Entry.toPlainText())
    
    GausJordan.GaussJordan3x4(num1,num2,num3,num4,num5,num6,num7,num8,num9,ind1,ind2,ind3)
    MatrixGauss3x3.ResultMatrix.setText(str(GausJordan.result3x3))

def MatrixGauss4():
    num1 = float(MatrixGauss4x4.num1Entry.toPlainText())
    num2 = float(MatrixGauss4x4.num2Entry.toPlainText())
    num3 = float(MatrixGauss4x4.num3Entry.toPlainText())
    num4 = float(MatrixGauss4x4.num4Entry.toPlainText())
    num5 = float(MatrixGauss4x4.num5Entry.toPlainText())
    num6 = float(MatrixGauss4x4.num6Entry.toPlainText())
    num7 = float(MatrixGauss4x4.num7Entry.toPlainText())
    num8 = float(MatrixGauss4x4.num8Entry.toPlainText())
    num9 = float(MatrixGauss4x4.num9Entry.toPlainText())
    num10 = float(MatrixGauss4x4.num10Entry.toPlainText())
    num11 = float(MatrixGauss4x4.num11Entry.toPlainText())
    num12 = float(MatrixGauss4x4.num12Entry.toPlainText())
    num13 = float(MatrixGauss4x4.num13Entry.toPlainText())
    num14 = float(MatrixGauss4x4.num14Entry.toPlainText())
    num15 = float(MatrixGauss4x4.num15Entry.toPlainText())
    num16 = float(MatrixGauss4x4.num16Entry.toPlainText())
    ind1 = float(MatrixGauss4x4.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss4x4.ind2Entry.toPlainText())
    ind3 = float(MatrixGauss4x4.ind3Entry.toPlainText())
    ind4 = float(MatrixGauss4x4.ind4Entry.toPlainText())
    
    GausJordan.GaussJordan4x5(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,
    num11,num13,num12,num14,num15,num16,ind1,ind2,ind3,ind4)
    MatrixGauss4x4.ResultMatrix.setText(str(GausJordan.result4x4))

def MatrixGauss5():
    num1 = float(MatrixGauss5x5.num1Entry.toPlainText())
    num2 = float(MatrixGauss5x5.num2Entry.toPlainText())
    num3 = float(MatrixGauss5x5.num3Entry.toPlainText())
    num4 = float(MatrixGauss5x5.num4Entry.toPlainText())
    num5 = float(MatrixGauss5x5.num5Entry.toPlainText())
    num6 = float(MatrixGauss5x5.num6Entry.toPlainText())
    num7 = float(MatrixGauss5x5.num7Entry.toPlainText())
    num8 = float(MatrixGauss5x5.num8Entry.toPlainText())
    num9 = float(MatrixGauss5x5.num9Entry.toPlainText())
    num10 = float(MatrixGauss5x5.num10Entry.toPlainText())
    num11 = float(MatrixGauss5x5.num11Entry.toPlainText())
    num12 = float(MatrixGauss5x5.num12Entry.toPlainText())
    num13 = float(MatrixGauss5x5.num13Entry.toPlainText())
    num14 = float(MatrixGauss5x5.num14Entry.toPlainText())
    num15 = float(MatrixGauss5x5.num15Entry.toPlainText())
    num16 = float(MatrixGauss5x5.num16Entry.toPlainText())
    num17 = float(MatrixGauss5x5.num17Entry.toPlainText())
    num18 = float(MatrixGauss5x5.num18Entry.toPlainText())
    num19 = float(MatrixGauss5x5.num19Entry.toPlainText())
    num20 = float(MatrixGauss5x5.num20Entry.toPlainText())
    num21 = float(MatrixGauss5x5.num21Entry.toPlainText())
    num22 = float(MatrixGauss5x5.num22Entry.toPlainText())
    num23 = float(MatrixGauss5x5.num23Entry.toPlainText())
    num24 = float(MatrixGauss5x5.num24Entry.toPlainText())
    num25 = float(MatrixGauss5x5.num25Entry.toPlainText())
    ind1 = float(MatrixGauss5x5.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss5x5.ind2Entry.toPlainText())
    ind3 = float(MatrixGauss5x5.ind3Entry.toPlainText())
    ind4 = float(MatrixGauss5x5.ind4Entry.toPlainText())
    ind5 = float(MatrixGauss5x5.ind5Entry.toPlainText())
    
    GausJordan.GaussJordan5x6(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,
    num11,num13,num12,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,
    num24,num25,ind1,ind2,ind3,ind4,ind5)
    MatrixGauss5x5.ResultMatrix.setText(str(GausJordan.result5x5))

def MatrixGauss6():
    num1 = float(MatrixGauss6x6.num1Entry.toPlainText())
    num2 = float(MatrixGauss6x6.num2Entry.toPlainText())
    num3 = float(MatrixGauss6x6.num3Entry.toPlainText())
    num4 = float(MatrixGauss6x6.num4Entry.toPlainText())
    num5 = float(MatrixGauss6x6.num5Entry.toPlainText())
    num6 = float(MatrixGauss6x6.num6Entry.toPlainText())
    num7 = float(MatrixGauss6x6.num7Entry.toPlainText())
    num8 = float(MatrixGauss6x6.num8Entry.toPlainText())
    num9 = float(MatrixGauss6x6.num9Entry.toPlainText())
    num10 = float(MatrixGauss6x6.num10Entry.toPlainText())
    num11 = float(MatrixGauss6x6.num11Entry.toPlainText())
    num12 = float(MatrixGauss6x6.num12Entry.toPlainText())
    num13 = float(MatrixGauss6x6.num13Entry.toPlainText())
    num14 = float(MatrixGauss6x6.num14Entry.toPlainText())
    num15 = float(MatrixGauss6x6.num15Entry.toPlainText())
    num16 = float(MatrixGauss6x6.num16Entry.toPlainText())
    num17 = float(MatrixGauss6x6.num17Entry.toPlainText())
    num18 = float(MatrixGauss6x6.num18Entry.toPlainText())
    num19 = float(MatrixGauss6x6.num19Entry.toPlainText())
    num20 = float(MatrixGauss6x6.num20Entry.toPlainText())
    num21 = float(MatrixGauss6x6.num21Entry.toPlainText())
    num22 = float(MatrixGauss6x6.num22Entry.toPlainText())
    num23 = float(MatrixGauss6x6.num23Entry.toPlainText())
    num24 = float(MatrixGauss6x6.num24Entry.toPlainText())
    num25 = float(MatrixGauss6x6.num25Entry.toPlainText())
    num26 = float(MatrixGauss6x6.num26Entry.toPlainText())
    num27 = float(MatrixGauss6x6.num27Entry.toPlainText())
    num28 = float(MatrixGauss6x6.num28Entry.toPlainText())
    num29 = float(MatrixGauss6x6.num29Entry.toPlainText())
    num30 = float(MatrixGauss6x6.num30Entry.toPlainText())
    num31 = float(MatrixGauss6x6.num31Entry.toPlainText())
    num32 = float(MatrixGauss6x6.num32Entry.toPlainText())
    num33 = float(MatrixGauss6x6.num33Entry.toPlainText())
    num34 = float(MatrixGauss6x6.num34Entry.toPlainText())
    num35 = float(MatrixGauss6x6.num35Entry.toPlainText())
    num36 = float(MatrixGauss6x6.num36Entry.toPlainText())
    ind1 = float(MatrixGauss6x6.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss6x6.ind2Entry.toPlainText())
    ind3 = float(MatrixGauss6x6.ind3Entry.toPlainText())
    ind4 = float(MatrixGauss6x6.ind4Entry.toPlainText())
    ind5 = float(MatrixGauss6x6.ind5Entry.toPlainText())
    ind6 = float(MatrixGauss6x6.ind6Entry.toPlainText())
    
    GausJordan.GaussJordan6x7(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,
    num11,num13,num12,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,
    num24,num25,num26,num27,num28,num29,num30,num31,num32,num33,num34,num35,num36,
    ind1,ind2,ind3,ind4,ind5,ind6)
    MatrixGauss6x6.ResultMatrix.setText(str(GausJordan.result6x6))

def MatrixGauss7():
    num1 = float(MatrixGauss7x7.num1Entry.toPlainText())
    num2 = float(MatrixGauss7x7.num2Entry.toPlainText())
    num3 = float(MatrixGauss7x7.num3Entry.toPlainText())
    num4 = float(MatrixGauss7x7.num4Entry.toPlainText())
    num5 = float(MatrixGauss7x7.num5Entry.toPlainText())
    num6 = float(MatrixGauss7x7.num6Entry.toPlainText())
    num7 = float(MatrixGauss7x7.num7Entry.toPlainText())
    num8 = float(MatrixGauss7x7.num8Entry.toPlainText())
    num9 = float(MatrixGauss7x7.num9Entry.toPlainText())
    num10 = float(MatrixGauss7x7.num10Entry.toPlainText())
    num11 = float(MatrixGauss7x7.num11Entry.toPlainText())
    num12 = float(MatrixGauss7x7.num12Entry.toPlainText())
    num13 = float(MatrixGauss7x7.num13Entry.toPlainText())
    num14 = float(MatrixGauss7x7.num14Entry.toPlainText())
    num15 = float(MatrixGauss7x7.num15Entry.toPlainText())
    num16 = float(MatrixGauss7x7.num16Entry.toPlainText())
    num17 = float(MatrixGauss7x7.num17Entry.toPlainText())
    num18 = float(MatrixGauss7x7.num18Entry.toPlainText())
    num19 = float(MatrixGauss7x7.num19Entry.toPlainText())
    num20 = float(MatrixGauss7x7.num20Entry.toPlainText())
    num21 = float(MatrixGauss7x7.num21Entry.toPlainText())
    num22 = float(MatrixGauss7x7.num22Entry.toPlainText())
    num23 = float(MatrixGauss7x7.num23Entry.toPlainText())
    num24 = float(MatrixGauss7x7.num24Entry.toPlainText())
    num25 = float(MatrixGauss7x7.num25Entry.toPlainText())
    num26 = float(MatrixGauss7x7.num26Entry.toPlainText())
    num27 = float(MatrixGauss7x7.num27Entry.toPlainText())
    num28 = float(MatrixGauss7x7.num28Entry.toPlainText())
    num29 = float(MatrixGauss7x7.num29Entry.toPlainText())
    num30 = float(MatrixGauss7x7.num30Entry.toPlainText())
    num31 = float(MatrixGauss7x7.num31Entry.toPlainText())
    num32 = float(MatrixGauss7x7.num32Entry.toPlainText())
    num33 = float(MatrixGauss7x7.num33Entry.toPlainText())
    num34 = float(MatrixGauss7x7.num34Entry.toPlainText())
    num35 = float(MatrixGauss7x7.num35Entry.toPlainText())
    num36 = float(MatrixGauss7x7.num36Entry.toPlainText())
    num37 = float(MatrixGauss7x7.num37Entry.toPlainText())
    num38 = float(MatrixGauss7x7.num38Entry.toPlainText())
    num39 = float(MatrixGauss7x7.num39Entry.toPlainText())
    num40 = float(MatrixGauss7x7.num40Entry.toPlainText())
    num41 = float(MatrixGauss7x7.num41Entry.toPlainText())
    num42 = float(MatrixGauss7x7.num42Entry.toPlainText())
    num43 = float(MatrixGauss7x7.num43Entry.toPlainText())
    num44 = float(MatrixGauss7x7.num44Entry.toPlainText())
    num45 = float(MatrixGauss7x7.num45Entry.toPlainText())
    num46 = float(MatrixGauss7x7.num46Entry.toPlainText())
    num47 = float(MatrixGauss7x7.num47Entry.toPlainText())
    num48 = float(MatrixGauss7x7.num48Entry.toPlainText())
    num49 = float(MatrixGauss7x7.num49Entry.toPlainText())
    ind1 = float(MatrixGauss7x7.ind1Entry.toPlainText())
    ind2 = float(MatrixGauss7x7.ind2Entry.toPlainText())
    ind3 = float(MatrixGauss7x7.ind3Entry.toPlainText())
    ind4 = float(MatrixGauss7x7.ind4Entry.toPlainText())
    ind5 = float(MatrixGauss7x7.ind5Entry.toPlainText())
    ind6 = float(MatrixGauss7x7.ind6Entry.toPlainText())
    ind7 = float(MatrixGauss7x7.ind7Entry.toPlainText())
    
    
    GausJordan.GaussJordan7x8(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,
    num11,num13,num12,num14,num15,num16,num17,num18,num19,num20,num21,num22,num23,
    num24,num25,num26,num27,num28,num29,num30,num31,num32,num33,num34,num35,num36,
    num37,num38,num39,num40,num41,num42,num43,num44,num45,num46,num47,num48,num49,
    ind1,ind2,ind3,ind4,ind5,ind6,ind7)
    MatrixGauss7x7.ResultMatrix.setText(str(GausJordan.result7x7))

def SaveMatrices():
    if(OpMatrixSimple3x3.num1Entry.toPlainText()!=""):
        num1 = float(OpMatrixSimple3x3.num1Entry.toPlainText())
    else:
        num1= set()

    if(OpMatrixSimple3x3.num2Entry.toPlainText()!=""):
        num2 = float(OpMatrixSimple3x3.num2Entry.toPlainText())
    else:
        num2 = set()
    
    if(OpMatrixSimple3x3.num3Entry.toPlainText()!=""):
        num3 = float(OpMatrixSimple3x3.num3Entry.toPlainText())
    else:
        num3= set()
    
    if(OpMatrixSimple3x3.num4Entry.toPlainText()!=""):
        num4 = float(OpMatrixSimple3x3.num4Entry.toPlainText())
    else:
        num4= set()

    if(OpMatrixSimple3x3.num5Entry.toPlainText()!=""):
        num5 = float(OpMatrixSimple3x3.num5Entry.toPlainText())
    else:
        num5 = set()
    
    if(OpMatrixSimple3x3.num6Entry.toPlainText()!=""):
        num6 = float(OpMatrixSimple3x3.num6Entry.toPlainText())
    else:
        num6 = set()
    
    if(OpMatrixSimple3x3.num7Entry.toPlainText()!=""):
        num7 = float(OpMatrixSimple3x3.num7Entry.toPlainText())
    else:
        num7 = set()
    
    if(OpMatrixSimple3x3.num8Entry.toPlainText()!=""):
        num8 = float(OpMatrixSimple3x3.num8Entry.toPlainText())
    else:
        num8 = set()
    
    if(OpMatrixSimple3x3.num9Entry.toPlainText()!=""):
        num9 = float(OpMatrixSimple3x3.num9Entry.toPlainText())
    else:
        num9 = set()
    
    opcion = str(OpMatrixSimple3x3.comboBox.currentText())
    if(opcion == "A"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.A))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.A))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.A))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.A))

    if(opcion == "B"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.B))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.B))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.B))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.B))

    if(opcion == "C"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.C))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.C))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.C))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.C))

    if(opcion == "D"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.D))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.D))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.D))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.D))

    if(opcion == "E"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.E))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.E))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.E))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.E))

    if(opcion == "F"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.F))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.F))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.F))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.F))

    if(opcion == "G"):
        if((not bool(num1)==False or num1==0) and (not bool(num4)==False or num4==0) and (not bool(num2)==False or num2==0) and (not bool(num5)==False
            or num5==0) and not bool(num3)==True and not bool(num6)==True and not bool(num7)==True and not bool(num8)==True and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,0,0,0,"2x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.G))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False or num3==0) and (not bool(num4)==False or num4==0) and (not bool(num5)==False or num5==0) 
        and (not bool(num6)==False or num6==0) and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and (not bool(num9)==False or num9==0)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,num7,num8,num9,"3x3")
            OpMatrixSimple3x3.ResultMatriMatrix.setText(str(CalcMatrizEcuaLinea.G))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and (not bool(num3)==False) or num3==0 and (not bool(num4)==False or num4==0) and
        not bool(num5)==False or num5==0 and (not bool(num6)==False or num6==0) and (not bool(num7)==True) and (not bool(num8)==True) and (not bool(num9)==True)):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,num3,num4,num5,num6,0,0,0,"2x3")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.G))
        elif((not bool(num1)==False or num1==0) and (not bool(num2)==False or num2==0) and not bool(num3)==True and (not bool(num4)==False or num4==0) and
        (not bool(num5)==False or num5==0) and not bool(num6)==True and (not bool(num7)==False or num7==0) and (not bool(num8)==False or num8==0) and not bool(num9)==True):
            CalcMatrizEcuaLinea.matrices(opcion,num1,num2,0,num4,num5,0,num7,num8,0,"3x2")
            OpMatrixSimple3x3.Matrix.setText(str(CalcMatrizEcuaLinea.G))

def CalcMatrix():
    ecuacion = OpMatrixSimple3x3.EcEntry.toPlainText()
    ecuacionAux = str(ecuacion)
    if(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==False and any(c == "C" for c in ecuacionAux)==False
        and any(c == "D" for c in ecuacionAux)==False and any(c == "E" for c in ecuacionAux)==False and any(c == "F" for c in ecuacionAux)==False
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==False
        and any(c == "D" for c in ecuacionAux)==False and any(c == "E" for c in ecuacionAux)==False and any(c == "F" for c in ecuacionAux)==False
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            B = CalcMatrizEcuaLinea.B
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==True
        and any(c == "D" for c in ecuacionAux)==False and any(c == "E" for c in ecuacionAux)==False and any(c == "F" for c in ecuacionAux)==False
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            B = CalcMatrizEcuaLinea.B
            C = CalcMatrizEcuaLinea.C
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==True
        and any(c == "D" for c in ecuacionAux)==True and any(c == "E" for c in ecuacionAux)==False and any(c == "F" for c in ecuacionAux)==False
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            B = CalcMatrizEcuaLinea.B
            C = CalcMatrizEcuaLinea.C
            D = CalcMatrizEcuaLinea.D
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==True
        and any(c == "D" for c in ecuacionAux)==True and any(c == "E" for c in ecuacionAux)==True and any(c == "F" for c in ecuacionAux)==False
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            B = CalcMatrizEcuaLinea.B
            C = CalcMatrizEcuaLinea.C
            D = CalcMatrizEcuaLinea.D
            E = CalcMatrizEcuaLinea.E
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==True
        and any(c == "D" for c in ecuacionAux)==True and any(c == "E" for c in ecuacionAux)==True and any(c == "F" for c in ecuacionAux)==True
        and any(c == "G" for c in ecuacionAux)==False):
            A = CalcMatrizEcuaLinea.A
            B = CalcMatrizEcuaLinea.B
            C = CalcMatrizEcuaLinea.C
            D = CalcMatrizEcuaLinea.D
            E = CalcMatrizEcuaLinea.E
            F = CalcMatrizEcuaLinea.F
            try:
                resp = eval(ecuacionAux)
                OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
            except Exception as e:
                OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))
    elif(any(c == "A" for c in ecuacionAux)==True and any(c == "B" for c in ecuacionAux)==True and any(c == "C" for c in ecuacionAux)==True
        and any(c == "D" for c in ecuacionAux)==True and any(c == "E" for c in ecuacionAux)==True and any(c == "F" for c in ecuacionAux)==True
        and any(c == "G" for c in ecuacionAux)==True):
        A = CalcMatrizEcuaLinea.A
        B = CalcMatrizEcuaLinea.B
        C = CalcMatrizEcuaLinea.C
        D = CalcMatrizEcuaLinea.D
        E = CalcMatrizEcuaLinea.E
        F = CalcMatrizEcuaLinea.F
        G = CalcMatrizEcuaLinea.F
        try:
            resp = eval(ecuacionAux)
            OpMatrixSimple3x3.ResultMatrix.setText(str(resp))
        except Exception as e:
            OpMatrixSimple3x3.ResultMatrix.setText(str("Error no se puede la operacion, revise las matrices"))

def SaveAjusteCurvas():
    xn = float(AjusteDeCurvas.EntryX.toPlainText())
    yn = float(AjusteDeCurvas.EntryY.toPlainText())

    AjusteCurvas.DeArray(xn,yn)

    AjusteDeCurvas.ArrayX.setText(str(AjusteCurvas.x))
    AjusteDeCurvas.ArrayY.setText(str(AjusteCurvas.y))

def AjustarCuerva():
    AjusteCurvas.AjustarCurva(1)
    AjusteDeCurvas.Grado1Result.setText(str(AjusteCurvas.p))

    AjusteCurvas.AjustarCurva(2)
    AjusteDeCurvas.Grado2Result.setText(str(AjusteCurvas.p))

    AjusteCurvas.AjustarCurva(3)
    AjusteDeCurvas.Grado3Result.setText(str(AjusteCurvas.p))

    AjusteCurvas.AjustarCurva(4)
    AjusteDeCurvas.Grado4Result.setText(str(AjusteCurvas.p))

    AjusteCurvas.AjustarCurva(5)
    AjusteDeCurvas.Grado5Result.setText(str(AjusteCurvas.p))

    AjusteCurvas.AjustarCurva(6)
    AjusteDeCurvas.Grado6Result.setText(str(AjusteCurvas.p))

    
    





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
    Fmontecarlo()

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

#Gauss Jordan 
def gui_openGaus():
    MatrixSimple3x3.close()
    MatrixGauss.show()

def gui_openGaus2():
    MatrixSimple.close()
    MatrixGauss.show()
    
def gui_BackChooseGauss():
    MatrixGauss.close()
    MatricesChooseLong.show()

def gui_openGauss2x2():
    MatrixGauss.close()
    MatrixGauss2x2.show()

def gui_backGauss2x2():
    MatrixGauss.show()
    MatrixGauss2x2.close()

def gui_openGauss3x3():
    MatrixGauss.close()
    MatrixGauss3x3.show()

def gui_backGauss3x3():
    MatrixGauss.show()
    MatrixGauss3x3.close()

def gui_openGauss4x4():
    MatrixGauss.close()
    MatrixGauss4x4.show()

def gui_backGauss4x4():
    MatrixGauss.show()
    MatrixGauss4x4.close()

def gui_openGauss5x5():
    MatrixGauss.close()
    MatrixGauss5x5.show()

def gui_backGauss5x5():
    MatrixGauss.show()
    MatrixGauss5x5.close()

def gui_openGauss6x6():
    MatrixGauss.close()
    MatrixGauss6x6.show()

def gui_backGauss6x6():
    MatrixGauss.show()
    MatrixGauss6x6.close()

def gui_openGauss7x7():
    MatrixGauss.close()
    MatrixGauss7x7.show()

def gui_backGauss7x7():
    MatrixGauss.show()
    MatrixGauss7x7.close()

#OPERACIONES CON MATRICES
def gui_closeOperacionesMatricez():
    ChooseMatriz.show()
    OpMatrixSimple3x3.close()

def gui_openOperacionesMatricez():
    ChooseMatriz.close()
    OpMatrixSimple3x3.show()

#Ajuste de curvas 
def gui_openAjustes():
    Choose.close()
    AjusteDeCurvas.show()

def gui_closeAjustes():
    Choose.show()
    AjusteDeCurvas.close()


    





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
ChooseMatriz.btnOpSimples2.clicked.connect(gui_openOperacionesMatricez)
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
MatrixSimple.GausButton.clicked.connect(gui_openGaus2)




#3x3
MatrixSimple3x3.MatBackButton.clicked.connect(Gui_backMaatriz3x3)
MatrixSimple3x3.DetCalculButton.clicked.connect(Btn_Matrix3x3)
MatrixSimple3x3.TranCalculButton.clicked.connect(MatrixTranspuesta3x3)
MatrixSimple3x3.InvCalcButton.clicked.connect(MatrixInversa3x3)
MatrixSimple3x3.RanCalcButton.clicked.connect(MatrixRango3x3)
MatrixSimple3x3.MultCalcButton.clicked.connect(MatrixMult3x3)
MatrixSimple3x3.ElevCalcButton.clicked.connect(MatrixElev3x3)
MatrixSimple3x3.GausButton.clicked.connect(gui_openGaus)

#Choose Gauss
MatrixGauss.GausBackButton.clicked.connect(gui_BackChooseGauss)
MatrixGauss.GausButton2x2.clicked.connect(gui_openGauss2x2)
MatrixGauss.GausButton3x3.clicked.connect(gui_openGauss3x3)
MatrixGauss.GausButton4x4.clicked.connect(gui_openGauss4x4)
MatrixGauss.GausButton5x5.clicked.connect(gui_openGauss5x5)
MatrixGauss.GausButton6x6.clicked.connect(gui_openGauss6x6)
MatrixGauss.GausButton7x7.clicked.connect(gui_openGauss7x7)



#gauss 2x2
MatrixGauss2x2.GausButton.clicked.connect(MatrixGauss2)
MatrixGauss2x2.GausBackButton.clicked.connect(gui_backGauss2x2)

#gauss 3x3
MatrixGauss3x3.GausButton.clicked.connect(MatrixGauss3)
MatrixGauss3x3.GausBackButton.clicked.connect(gui_backGauss3x3)

#gauss 4x4
MatrixGauss4x4.GausButton.clicked.connect(MatrixGauss4)
MatrixGauss4x4.GausBackButton.clicked.connect(gui_backGauss4x4)

#gauss 5x5
MatrixGauss5x5.GausButton.clicked.connect(MatrixGauss5)
MatrixGauss5x5.GausBackButton.clicked.connect(gui_backGauss5x5)

#gauss 6x6
MatrixGauss6x6.GausButton.clicked.connect(MatrixGauss6)
MatrixGauss6x6.GausBackButton.clicked.connect(gui_backGauss6x6)

#gauss 7x7
MatrixGauss7x7.GausButton.clicked.connect(MatrixGauss7)
MatrixGauss7x7.GausBackButton.clicked.connect(gui_backGauss7x7)

#operaciones con matricez 
OpMatrixSimple3x3.comboBox.activated[str].connect(SaveMatrices)
OpMatrixSimple3x3.CalcButton.clicked.connect(CalcMatrix)
OpMatrixSimple3x3.BackButton.clicked.connect(gui_closeOperacionesMatricez)

#ajustes de curvas
Choose.AjusteButton.clicked.connect(gui_openAjustes)
AjusteDeCurvas.AjustBackButton.clicked.connect(gui_closeAjustes)
AjusteDeCurvas.BtnGuardar.clicked.connect(SaveAjusteCurvas)
AjusteDeCurvas.CalculateButton.clicked.connect(AjustarCuerva)




#Exectue
Main.show()
app.exec()