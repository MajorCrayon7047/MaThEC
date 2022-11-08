from nextcord.ext import commands
import nextcord
from nextcord import File, ButtonStyle, Embed, Color, SelectOption, Intents, Interaction, SlashOption, Member
from sympy import *
from pylab import *
from numpy import arange
import json

intents = Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="m!",intents = intents, help_command=None)

@bot.command()
async def help(ctx, command=""):
    command = command.lower()
    if command=="":
        embed2 = Embed(
            title = "Help || MaThEC",
            description = "Este es un bot para poder utilizar metodos matematicos a necesidad del usuario, desarrollado en la ETEC por Nicolas Perez, Lucas Perinetti y Calogero Nicolli. Este es el [GitHub](https://github.com/MajorCrayon7047/MaThEC) del proyecto\n\nPara utilizar el bot se puede usar el prefijo **`m!`** al principio de cada comando o tambien se puede utilizar con **`/`**. Puede encontrar una explicacion mas detallada de cada comando utilizando `m!help <comando>`",
        )
        embed2.add_field(name="__Comandos__", value="**`m!derivar <funcion>`** - Deriva una funcion\n**`m!factorisar <funcion|expresion>`** - Factorisa una expresion|funcion\n**`m!graph <funcion>`** - grafica una funcion\n**`m!limite <funcion> <limite>`** - encuentra el limite de la funcion\n**`m!integrar <funcion>`** - Integra una funcion\n**`m!resolve <termino|funcion>`** - Resuelve calculos generales")
        embed2.set_footer(text=f"{ctx.message.author}", icon_url=ctx.message.author.display_avatar)
    elif command == "der" or command == "derivada" or command == "derivadas" or command == "derivar":
        embed2 = Embed(
            title= "Help || Derivadas",
            description="Es un comando para poder **derivar** una vez la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!der <funcion>`**\n- **`/der <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `der` como el termino `derivar`"
        )
    elif command == "factorisar" or command == "fac":
        embed2 = Embed(
            title= "Help || Factorisar",
            description="Es un comando para poder **factorisar** a su minima expresion la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!fac <funcion>`**\n- **`/fac <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `fac` como el termino `factorisar`"
        )
    elif command == "graph" or command == "graficar":
        embed2 = Embed(
            title= "Help || Graficar",
            description="Es un comando para poder **graficar** la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!fac <funcion> <punto inicial=0(opcional)> <rango=100(opcional)> <negativo=True(opcional)>`**\n- **`/fac <funcion> <punto inicial=0(opcional)> <rango=100(opcional)> <negativo=True(opcional)>`**\n\nEste comando se puede llamar usando tanto el termino `graph` como el termino `graficar`"
        )
    elif command == "limite" or command == "lim":
        embed2 = Embed(
            title= "Help || Limite",
            description="Es un comando para poder **sacar el limite** de la funcion que le demos y el limite que le especifiquemos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!lim <funcion> <LIMITE>`**\n- **`/limite <funcion> <LIMITE>`**\n\nEste comando se puede llamar usando tanto el termino `lim` como el termino `limite`"
        )
    elif command == "inte" or command == "integrar":
        embed2 = Embed(
            title= "Help || Integrar",
            description="Es un comando para poder **integrar** una vez la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!inte <funcion>`**\n- **`/integrar <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `inte` como el termino `integrar`"
        )
    elif command == "resolve" or command == "resolver":
        embed2 = Embed(
            title= "Help || Resolver",
            description="Es un comando para poder **resolver** la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!resolve <funcion>`**\n- **`/resolve <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `resolve` como el termino `resolver`"
        )
    elif command == "help":
        await ctx.send("https://www.youtube.com/watch?v=IPOwCwAFG4Y")
        return
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
    await bot.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.watching, name = "pruebas"))


#----------------------------------PREFIX COMMANDS--------------------------------
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
            #await ctx.send(f"**Expresion:** `{expresion}`\n***SI* tiene limite**!!\n__**LIMITE:**__ `{limite}`\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            print("B")
            embed = Embed(title="LIMITE", description=f"**Expresion:** `{expresion}`\n***SI* tiene limite**!!\n__**LIMITE:**__ `{limite}`\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`", colour=0x60009E)   
            embed.set_footer(text=f"{ctx.message.author}", icon_url=ctx.message.author.display_avatar)
            await ctx.send(embed=embed)
        else:
            #await ctx.send(f"**Expresion:** `{expresion}`\n\n***NO* tiene limite!!**\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            embed = Embed(title="LIMITE", description=f"**Expresion:** `{expresion}`\n\n***NO* tiene limite!!**\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`", colour=0x60009E)   
            embed.set_footer(text=f"{ctx.message.author}", icon_url=ctx.message.author.display_avatar)
            await ctx.send(embed=embed)
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
    await ctx.send( file= File(a, filename=a))
    
@bot.command(pass_context=True, aliases = ["derivar", "ingeayiuda"])
async def der(ctx: commands.Context, funcionaderivar): #funcion que deriva a partir de magia de unicorno
    idisc = ctx.message.author.id
    if "x" in funcionaderivar:
        x = Symbol("x")
        funcionaderivar = funcion(expresion=funcionaderivar)
        graficadormixto(funcionaderivar , "Funcion: " + funcionaderivar,idisc=idisc)
        y = eval(funcionaderivar)
        yprime = y.diff(x)
        graficadormixto(yprime , "Derivada: " + str(yprime),idisc=idisc)
        a = File(str(a:=str(ctx.message.author.id) + ".png"), filename=a)
        b = "Expresion: `F(x)=" + str(funcionaderivar) +"`\nDerivada: `F'(x)=" + str(yprime) + "`"
        clf()
        embed = Embed(title="DERIVADA", description=b, colour=0x60009E)
        embed.set_image(url=f"attachment://{str(ctx.message.author.id)}" + ".png")
        embed.set_footer(text=f"{ctx.message.author}", icon_url=ctx.message.author.display_avatar)
        await ctx.send(embed=embed, file=a)
        #await ctx.send(content=b ,file=a)
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
        imagen = File(a:=str(str(idisc) + ".png"), filename=a)
        respuesta = "`Expresion: f(x)=" + str(funcionaintegrar) +"`\n`Integral: F(x)=" + str(yprime) + "`"
        clf()
        embed = Embed(title="INTEGRAL", description=respuesta, colour=0x60009E)
        embed.set_image(url=f"attachment://{str(ctx.message.author.id)}" + ".png")
        embed.set_footer(text=f"{ctx.message.author}", icon_url=ctx.message.author.display_avatar)
        await ctx.send(embed=embed, file=imagen)
        #await ctx.send(content=respuesta ,file=imagen)
    else:
        await ctx.send(":X:Se require que en la funcincion con x como variable independiente:X:")

#-------------------------------SLASH COMMANDS--------------------------------------
@bot.slash_command(guild_ids=[818657386004217856])
async def help(ctx: nextcord.Interaction, command: str = SlashOption(name="command", required=False)):
    if command==None:
        embed2 = Embed(
            title = "Help || MaThEC",
            description = "Este es un bot para poder utilizar metodos matematicos a necesidad del usuario, desarrollado en la ETEC por Nicolas Perez, Lucas Perinetti y Calogero Nicolli. Este es el [GitHub](https://github.com/MajorCrayon7047/MaThEC) del proyecto\n\nPara utilizar el bot se puede usar el prefijo **`m!`** al principio de cada comando o tambien se puede utilizar con **`/`**. Puede encontrar una explicacion mas detallada de cada comando utilizando `m!help <comando>`",
        )
        embed2.add_field(name="__Comandos__", value="**`m!derivar <funcion>`** - Deriva una funcion\n**`m!factorisar <funcion|expresion>`** - Factorisa una expresion|funcion\n**`m!graph <funcion>`** - grafica una funcion\n**`m!limite <funcion> <limite>`** - encuentra el limite de la funcion\n**`m!integrar <funcion>`** - Integra una funcion\n**`m!resolve <termino|funcion>`** - Resuelve calculos generales")
        embed2.set_footer(text=f"{ctx.user}", icon_url=ctx.user.display_avatar)
    elif command == "der" or command == "derivada" or command == "derivadas" or command == "derivar":
            embed2 = Embed(
            title= "Help || Derivadas",
            description="Es un comando para poder **derivar** una vez la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!der <funcion>`**\n- **`/der <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `der` como el termino `derivar`"
        )
    elif command == "factorisar" or command == "fac":
        embed2 = Embed(
            title= "Help || Factorisar",
            description="Es un comando para poder **factorisar** a su minima expresion la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!fac <funcion>`**\n- **`/fac <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `fac` como el termino `factorisar`"
        )
    elif command == "graph" or command == "graficar":
        embed2 = Embed(
            title= "Help || Graficar",
            description="Es un comando para poder **graficar** la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!fac <funcion> <punto inicial=0(opcional)> <rango=100(opcional)> <negativo=True(opcional)>`**\n- **`/fac <funcion> <punto inicial=0(opcional)> <rango=100(opcional)> <negativo=True(opcional)>`**\n\nEste comando se puede llamar usando tanto el termino `graph` como el termino `graficar`"
        )
    elif command == "limite" or command == "lim":
        embed2 = Embed(
            title= "Help || Limite",
            description="Es un comando para poder **sacar el limite** de la funcion que le demos y el limite que le especifiquemos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!lim <funcion> <LIMITE>`**\n- **`/limite <funcion> <LIMITE>`**\n\nEste comando se puede llamar usando tanto el termino `lim` como el termino `limite`"
        )
    elif command == "inte" or command == "integrar":
        embed2 = Embed(
            title= "Help || Integrar",
            description="Es un comando para poder **integrar** una vez la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!inte <funcion>`**\n- **`/integrar <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `inte` como el termino `integrar`"
        )
    elif command == "resolve" or command == "resolver":
        embed2 = Embed(
            title= "Help || Resolver",
            description="Es un comando para poder **resolver** la funcion que le demos. El comando se puede utilizar de las 2 siguientes maneras:\n- **`m!resolve <funcion>`**\n- **`/resolve <funcion>`**\n\nEste comando se puede llamar usando tanto el termino `resolve` como el termino `resolver`"
        )
    elif command == "help":
        await ctx.send("https://www.youtube.com/watch?v=IPOwCwAFG4Y")
        return
    await ctx.send(embed=embed2)


@bot.slash_command(guild_ids=[818657386004217856])
async def resolver(ctx: nextcord.Interaction, termino: str):
    try:
        nomehackes=true
        for i in range(len(termino)):
            if termino[i].isalpha():
                nomehackes=false
        if nomehackes:
            await ctx.response.send_message("El resultado es: " + str(eval(termino)))
        else:
            await ctx.response.send_message("El resultado es: tu puta madre")
    except:
        await ctx.response.send_message("Algo salio mal lo lamento, recuerda solo escribir el calculo sin letras")

@bot.slash_command(guild_ids=[818657386004217856])
async def factorisar(ctx: nextcord.Interaction, expresion: str): #funcion que simplemente se encarga de factorisar una funcion
    expresion = expresion.replace("`", "")
    expresion = expresion.replace(" ", "")
    x = symbols("x")
    expresion = funcion(expresion=expresion)
    expresionfactorisada = sympify(expresion)

    await ctx.response.send_message(f"**Expresion Ingresada:** `{expresion}`\n**Expresion extendida/desglozada:** `{expand(expresionfactorisada)}`\n**Expresion comprimida:** `{factor(expresionfactorisada)}`")

@bot.slash_command(guild_ids=[818657386004217856])
async def derivar(ctx: nextcord.Interaction, funcionaderivar: str):
    idisc = ctx.user.id
    if "x" in funcionaderivar:
        x = Symbol("x")
        funcionaderivar = funcion(expresion=funcionaderivar)
        graficadormixto(funcionaderivar , "Funcion: " + funcionaderivar,idisc=idisc)
        y = eval(funcionaderivar)
        yprime = y.diff(x)
        graficadormixto(yprime , "Derivada: " + str(yprime),idisc=idisc)
        a = File(str(a:=str(ctx.user.id) + ".png"), filename=a)
        b = "Expresion: `F(x)=" + str(funcionaderivar) +"`\nDerivada: `F'(x)=" + str(yprime) + "`"
        clf()
        embed = Embed(title="DERIVADA", description=b, colour=0x60009E)
        embed.set_image(url=f"attachment://{str(ctx.user.id)}" + ".png")
        embed.set_footer(text=f"{ctx.user}", icon_url=ctx.user.display_avatar)
        await ctx.response.send_message(embed=embed, file=a)
        #await ctx.send(content=b ,file=a)
    else:
        await ctx.send(":X:Se require que en la funcincion con x como variable independiente:X:")

@bot.slash_command(guild_ids=[818657386004217856])
async def integrar(ctx: commands.Context, funcionaintegrar:str): #funcion que deriva a partir de magia de unicorno
    idisc = ctx.user.id
    if "x" in funcionaintegrar:
        funcionaintegrar = funcion(expresion=funcionaintegrar)
        x = Symbol("x")
        graficadormixto( funcionaintegrar , "Funcion: " + funcionaintegrar,idisc)
        y = eval(funcionaintegrar)
        yprime = y.integrate(x)
        graficadormixto(yprime , "Integral: " + str(yprime),idisc) 
        imagen = File(a:=str(str(idisc) + ".png"), filename=a)
        respuesta = "`Expresion: f(x)=" + str(funcionaintegrar) +"`\n`Integral: F(x)=" + str(yprime) + "`"
        clf()
        embed = Embed(title="INTEGRAL", description=respuesta, colour=0x60009E)
        embed.set_image(url=f"attachment://{str(ctx.user.id)}" + ".png")
        embed.set_footer(text=f"{ctx.user}", icon_url=ctx.user.display_avatar)
        await ctx.send(embed=embed, file=imagen)
        #await ctx.send(content=respuesta ,file=imagen)
    else:
        await ctx.send(":X:Se require que en la funcincion con x como variable independiente:X:")


@bot.slash_command(guild_ids=[818657386004217856])
async def limite(ctx: nextcord.Interaction, expresion:str = SlashOption(name="expresion"), LIMITE:float = SlashOption(name="limite")): # funcion que calcula limite
    #LIMITE = float(LIMITE.rstrip("`"))
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
            #await ctx.send(f"**Expresion:** `{expresion}`\n***SI* tiene limite**!!\n__**LIMITE:**__ `{limite}`\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            print("B")
            embed = Embed(title="LIMITE", description=f"**Expresion:** `{expresion}`\n***SI* tiene limite**!!\n__**LIMITE:**__ `{limite}`\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`", colour=0x60009E)   
            embed.set_footer(text=f"{ctx.user}", icon_url=ctx.user.display_avatar)
            await ctx.response.send_message(embed=embed)
        else:
            #await ctx.send(f"**Expresion:** `{expresion}`\n\n***NO* tiene limite!!**\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`")
            embed = Embed(title="LIMITE", description=f"**Expresion:** `{expresion}`\n\n***NO* tiene limite!!**\n**limite por la derecha:** `{limiteD}`\n**limite por la izquierda:** `{limiteI}`", colour=0x60009E)   
            embed.set_footer(text=f"{ctx.user}", icon_url=ctx.user.display_avatar)
            await ctx.response.send_message(embed=embed)
            print("C")

    except Exception as e:
        print(e)
        await ctx.response.send_message(":x: **Ups! Tuve problemas para analizar la funcion, porfavor vuelva a introducir la funcion, verifique que haya especificado el limite o que el denominador de la funcion no sea un cero inamovible** :x:")

@bot.slash_command(guild_ids=[818657386004217856])
async def graficar(ctx: nextcord.Interaction, expresion:str = SlashOption(name="expresion"), LIMITE:int = SlashOption(name="limite", required=False), rango: int = SlashOption(name="rango", required=False), connegativo: bool = SlashOption(name="con_negativo", required=False)): # funcion encargada de graficar una funcion
    if LIMITE==None: LIMITE = 0
    if rango == None: rango = 100
    if connegativo == None: connegativo = True
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
    savefig(a:=str(ctx.user.id) + ".png")
    await ctx.send(f"`f(x)={expresion}`", file= File(a, filename=a))

with open('seguridad.json','r') as f:
        token = json.load(f)

bot.run(token["token"])