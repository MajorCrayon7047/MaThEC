import discord
from discord.ext import commands
from discord import File
from sympy import *
from pylab import *
from numpy import arange
import json

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="m!",intents = intents, help_command=None)

@bot.command()
async def help(ctx, command=""):
    if command=="":
        embed = discord.Embed(
            title = f"La ayuda ya llego {ctx.message.author.name}",
            description = "Para tener una descripcion mas extensa de cada comando utilize m!help <comando>",
            color = 0xAF33FF)
        embed.add_field(name = "Funcionalidad:", value="- Derivar\n- Factorizar\n- Graficar\n- Limite")
        embed.add_field(name = "Comando a usar:", value="m!der <funcion>\nm!fac <funcion/expresion>\nm!graph <funcion> <raiz>\nm!lim <funcion> <limite>")
        embed.add_field(name= "CMD ALT:", value="[der | derivar]\n[fac | factorisar]\n[graph | graficar]\n[lim | limite]")
        embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/821538238355210271/1034544524783014009/unknown.png")
        embed2 = discord.Embed(
            title = "Help || MaThEC",
            description = "Este es un bot para poder utilizar metodos matematicos a necesidad del usuario, desarrollado en la ETEC por Nicolas Perez, Lucas Perinetti y Calogero Nicolli. Este es el [GitHub](https://github.com/MajorCrayon7047/MaThEC) del proyecto\n\nPara una explicacion mas detallada de cada comando utilize `m!help <comando>`",
        )
        embed2.add_field(name="__Comandos__", value="**m!derivar** - Deriva una funcion\n**m!factorisar** - Factoriza una expresion/funcion\n**m!graph** - grafica una funcion\n**m!limite** - encuentra el limite de la funcion")
    await ctx.send(embed=embed)
    await ctx.send(embed=embed2)

def funcion(expresion="x"):
    lista = list(expresion)
    for i in range(len(lista)):
        try:
            if lista[i] == "∧" or lista[i] == "‸" or lista[i] == "^": lista[i] = "**"
            if lista[i].isdigit() == false and lista[i].isnumeric()  == false and lista[i].isalnum():
                if lista[i] == "X": lista[i] = "(x)"
                elif lista[i] == "x": lista[i] = "(x)"
                if lista[i] == "Y": lista[i] = "(y)"
                elif lista[i] == "y": lista[i] = "(y)"
                if lista[i] == "Z": lista[i] = "(z)"
                elif lista[i] == "z": lista[i] = "(z)"
                if i>0 and lista[i-1].isdigit(): lista[i-1]+="*"
                if i<len(lista) and lista[i+1].isdigit(): lista[i]+="*"
        except:
            pass
    a = "".join(lista)
    return a

#def funcion(expresion="x"):
#    lista1 = list(expresion)
#    lista2=[]
#    for i in range(len(lista1)):
#        print("posicion: "+str(i)+" "+str(lista1[i]) + " es digito: " + str(lista1[i].isdigit()) + " es numerico: "+ str(lista1[i].isnumeric()) + " es alfanum: "+ str(lista1[i].isalnum()))
#        try:
            
#            if lista1[i].isdigit()==false  and lista1[i].isnumeric() == false  and  lista1[i].isalnum(): 
#                print("entro")
#                if i > 0:
#                    print("entro1")
#                    if lista1[i-1].isdigit():
#                        print("entro2") 
#                        lista2.append(str("*") )  
#                lista2.append(str("(x)"))
#                if i < len(lista1):
#                    if lista1[i+1].isdigit():
#                        print("entro2") 
#                        lista2.append(str("*")) 
#            else:
#                 lista2.append(str(lista1[i]) )  
#                 print("entro3")
#        except:
#            pass
#    print(lista2)
#    a=""
#    for u in range(len(lista2)):
#        a = str(a) + str(lista2[u])
#    print(a)
#    return str(a)

def graficadormixto(gfuncion ,tipo:str,idisc): # graficador usado para graficar 2 o mas funciones
    xinicio:int = -100
    xfin:int = 100
    dominio = []
    imagen = []
    xinicio , xfin = int(xinicio) , int(xfin)
    dominioDeseadoRep = [xinicio,xfin]
    step = (dominioDeseadoRep[1] - dominioDeseadoRep[0]) / 35

    precision = len(str(step)) - len(str(trunc(step))) -1
    if ( precision<= 0 ):
        precision = 0

    for x in arange(dominioDeseadoRep[0], dominioDeseadoRep[1] + step, step):
        x = round(x , precision)
        dominio.append(x)
        imagen.append(eval(str(gfuncion))) #entre los parentesis va la funcion 
        if True != isfinite(imagen[len(imagen) - 1]) and 0.0 !=imagen[len(imagen) - 1]:
            pass #aca podes poner print(x) para saber donde no se cualculo la funcion por no ser posibles          
    plot(dominio , imagen , label=tipo)   
    grid(visible=True)
    legend()
    savefig(str(idisc) + ".png")

    return   
        
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print("Joined {}".format(guild.name))

    print(f'Logueado como {bot.user}')
    await bot.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = "pruebas"))

@bot.command(pass_context=True ,aliases = ["resolver", "mama" , "res"]) # Funcion que simplemente resuelve la cuenta que le pidas
async def resolve(ctx: commands.Context, termino:str):
    try:
        nomehackes=true
        for i in range(len(termino)):
            if termino[i].isalpha():
                nomehackes=false
        if nomehackes:
            await ctx.send("El resultado es: " + str(eval(termino)))
        else:
            await ctx.send("El resultado es: tu puta madre")
    except:
        await ctx.send("Algo salio mal lo lamento, recuerda solo escribir el calculo sin letras")

@bot.command(pass_context=True , aliases = ["factorisar"]) 
async def fac(ctx, *, expresion): #funcion que simplemente se encarga de factorisar una funcion
    expresion = expresion.replace("`", "")
    expresion = expresion.replace(" ", "")
    x = symbols("x")
    expresion = funcion(expresion=expresion)
    expresionfactorisada = sympify(expresion)

    await ctx.send(f"**Expresion Ingresada:** `{expresion}`\n**Expresion extendida/desglozada:** `{expand(expresionfactorisada)}`\n**Expresion comprimida:** `{factor(expresionfactorisada)}`")

@bot.command(pass_context=True ,aliases = ["lim"])
async def limite(ctx, expresion, LIMITE): # funcion que calcula limite
    LIMITE = float(LIMITE.rstrip("`"))
    expresion = funcion(expresion=expresion)
    expresion2 = expresion
    try:
        x = symbols("x")
        expresion2 = sympify(expresion)

        limite = limit(expresion2, x, LIMITE)
        limiteD = limit(expresion2, x, LIMITE, dir='+')
        limiteI = limit(expresion2, x, LIMITE, dir='-')

        if limite == oo:limite="∞"
        elif limite == -oo: limite="-∞"
        else: round(limite, 4)

        if limiteD == oo: limiteD="∞"
        elif limiteD == -oo: limiteD="-∞"
        else: round(limiteD, 4)
        if limiteI == oo: limiteI="∞"
        elif limiteI == -oo: limiteI="-∞"
        else: round(limiteI, 4)
        print("A")
        if limiteI == limiteD:
            await ctx.send(f"**Expresion:** `{expresion}`\n***SI* tiene limite**!!\n__**LIMITE:**__ `{limite}`\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            print("B")        
        else:
            await ctx.send(f"**Expresion:** `{expresion}`\n\n***NO* tiene limite!!**\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            print("C")

    except Exception as e:
        print(e)
        await ctx.send(":x: **Ups! Tuve problemas para analizar la funcion, porfavor vuelva a introducir la funcion, verifique que haya especificado el limite o que el denominador de la funcion no sea un cero inamovible** :x:")
    
@bot.command(pass_context=True , aliases = ["graficar"])
async def graph(ctx, expresion:str, LIMITE:int = 0 ,  rango = 100 , connegativo:bool = True): # funcion encargada de graficar una funcion
    listay = []
    listax = []
    expresion = funcion(expresion=expresion)
    if connegativo==True:
        for x in range(LIMITE-rango, LIMITE+rango, 1):
            listay.append(eval(expresion))
            listax.append(x)
    else:
        a = limite-rango
        if a < 0:
            a = 0
        for x in range(a, LIMITE+rango, 1):
            listay.append(eval(expresion))
            listax.append(x)
    clf()
    plot(listax, listay)
    grid()
    savefig(a:=str(ctx.message.author.id) + ".png")
    await ctx.send( file= discord.File(a, filename=a))
    
@bot.command(pass_context=True ,aliases = ["derivar", "ingeayiuda"])
async def der(ctx: commands.Context, funcionaderivar): #funcion que deriva a partir de magia de unicorno
    idisc = ctx.message.author.id
    if "x" in funcionaderivar:
        x = Symbol("x")
        funcionaderivar = funcion(expresion=funcionaderivar)
        graficadormixto(funcionaderivar , "Funcion: " + funcionaderivar,idisc=idisc)
        y = eval(funcionaderivar)
        yprime = y.diff(x)
        graficadormixto(yprime , "Derivada: " + str(yprime),idisc=idisc)
        a = discord.File(str(a:=str(ctx.message.author.id) + ".png"), filename=a)
        b = "F(x)=" + str(funcionaderivar) +"\nF'(x)=" + str(yprime)
        clf()
        await ctx.send(content=b ,file=a)
    else:
        await ctx.send(":X:Se require que en la funcincion con x como variable independiente:X:")
    
@bot.command(pass_context=True ,aliases = ["integrar"])
async def inte(ctx: commands.Context, funcionaintegrar:str): #funcion que deriva a partir de magia de unicorno
    idisc = ctx.message.author.id
    if "x" in funcionaintegrar:
        funcionaintegrar = funcion(expresion=funcionaintegrar)
        x = Symbol("x")
        graficadormixto( funcionaintegrar , "Funcion: " + funcionaintegrar,idisc)
        y = eval(funcionaintegrar)
        yprime = y.integrate(x)
        graficadormixto(yprime , "Integral: " + str(yprime),idisc) 
        imagen = discord.File(a:=str(str(idisc) + ".png"), filename=a)
        respuesta = "F(x)=" + str(funcionaintegrar) +"\nF'(x)=" + str(yprime)
        clf()
        await ctx.send(content=respuesta ,file=imagen)
    else:
        await ctx.send(":X:Se require que en la funcincion con x como variable independiente:X:")

with open('seguridad.json','r') as f:
        token = json.load(f)

bot.run(token["token"])
