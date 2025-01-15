#IMPORTAMOS ESTOS PAQUETES AL PROGRAMA PARA PODER LIMPIAR LA PANTALLA, PONER CARACTERES DE COLOR Y TIEMPO DE ESPERA 
import os
import random
from colorama import init, Fore, Back, Style
import time

init()
#CREAMOS LAS VARIABLES Y LISTAS PARA NUESTRO PROGRAMA, COMO MARCAS, ENTRADAS Y BEBIDAS DISPONIBLES, ETC
entradas_disponibles = 200
bebidas_disponibles=150
productos = ["Ron","Vodka", "Whisky", "Ginebra","Mezclas"]
ventas=0
productos_vendidos = []
precios_bebidas = ["10","9","15","12","2"]
precios_entradas = ["25","12","10","20","35"]
modelos_ron = ["Barcelo","Brugal","Diplomático","Negrita", "Cacique"]
modelos_vodka = ["Absolut Vodka","Belvedere ","Sobieski","Finlandia","Ciroc"]
modelos_whisky = ["Johnnie Walker","JB","Ballantines", "Jack Daniels","Jammeson Black Barrel",]
modelos_ginebra = ["Larios","Antonio Nadal","Blue Marine","Gin Eva","La Cantabra"]
modelos_mezclas = ["Coca Cola","Fanta","Monster","7UP","Red Bull"]
modelos_entradas = ["Mae West","G10","DSOKO","Sarao","Domo"]
bebidas_todas=[modelos_ron, modelos_vodka, modelos_whisky, modelos_ginebra,modelos_mezclas]
entradas_vendidas=[]
productos_vendidos=[]
ganancias_totales_productos=0
ganancias_totales=0
ganancias_totales_entradas=0
ganancias_productos=[]
ganancias_entradas=[]

time.sleep(1)
#MOSTRANDO LOGO DE LA TIENDA
time.sleep(1)
intrologo= (Fore.LIGHTBLUE_EX + '''

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%@@%%%%%%%+%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%#*%%%%%%%#.:#@+=@%::#@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%%%@@@..#@-@%%%%%%%%%%%%%%%%%%%%:.=+@@@@@@@.=@@@@@@%*#-:@%%%%+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%@-=%++##*%@@%%%%%%%.%%%@%%%.:*%%%%%%%%@#-:.-:+*@@%%%%%%%#+-@%%@%%%*%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@%%%%%%%%@@%+++#*%##@%%%%%%%%@@%%:*@%%%%%%%#:%%%@%:---@@%%%:#%%%%%%%%#-%%@%%%%%%@+@@@@@%%%%%%%%%%%%%%%%%
@%%%%%%%%%@+##++##%@@@%%%%=%@%@*@%@@@%%%%%%%%%%%@.*@@@+@%%%%%%%%%%%@%%@@:@%%%*@@@:-.+*@@%%%%%%%%%%%%%%@%
@%%%%%%%%%%@**@@@#%@@%%%%%%-:@%.:.:#@%@%%%%-%%%%@@%%%%@@%%%%:%%%%@.:..=++@@#-%%@@%@@@#@%%%%%%%%%%%%%%%%%
@%%%%%%%%%%@@@@@@:**@@%%%@.@@@.-...-=%@@%%%%%%%%@@@@@@@@@%%%%%%%@.==::*##%@%@#-@.=:=+*@%%%%%%%%%%%%%%%%%
@%%%%%%%%%%%%%@@..-@...@@@@%%%-==::++@*@%%%%@@+.*#######.=@@%%%%@#*=*#*%%@@%%@@@.-.**@@%%%%%%%%%@%%%%%%%
@%%%%%%%%%%%%%%%....:.-...@%%@.##@+%#@%@%%@%.#*#@......@%#*-%@%%@=#@@@%@%%@%%%@@@@@@#@%%%#%%%%%%%%%%%%%%
@%%%%%%%%%%%%%@.-.:.:=--@..@%%@@.*###@@%@@.###@..#-...#..@###+@@%@@*%@%%@@%%%@@:...**@%%%#@%%%%%%%%%%%%@
@%%@%%%%%%%%%@...::+.----%:#@%%%%%@@%%%@.:###@..=#######..@####*@@%%@@@%%%@@@%@...-=@@%%%%%%%%%%%%%%%@@@
@%@@%%%%%%%%%@.-+=::.:.*-**#@@%%%%@%%@@.#####@-.##..-.*#.:@#####+@@%%@@@%%-@%@:...-=@@@%%%%%%%%%%%%@@@@@
@%@@@@%%%%%%#@@#=**++%:#**+@%%%%%%%%@::######@*:%......%:+@######*+@%%@%%@@@%..-.---=@@@@-%%=%%%%%%@@@@@
@%@@@@%%%%%%@%@@=*+=*=+=++@%@@@@@%@@.#######%%@%=:::---:+@%%#######%@@%%%@@..-..---=:-@@%=@%=-%%%%%@@@@@
@@@@@@@%%%%%%%+%@@@*++*@@@%=--=-@@.#####%%%@@@@@@@%++%@@@@@@%@%%#####%@%%.@..-----===+:@@#=%%%@%%@@@@@@@
@@@@%%%%%%%@=%%%%%@@@%:---:@---:@.###%%@%@@###************##%@@@@%%##%%@.#.----======+*:@@@@@@*%%%@@@@@@
@%@@@%%%%#%@%+@%:----*@.....@--#@%%%%%@@###++*:...:--:...:+*+##%@@%%%%%@.@.--========++@@%@@#%%@%%@@@@@@
@@@@@@%%%%+@@-@*----.........:-#@@%%@@####%@@@@@@@####@@@@@@@%#%#%@@%%@@:@=--====%@@@=%@@@@@@@@@@@@@@@@@
@@@@@@@@%@@%%%@@.--=@......*@--##@@@@@@@+++@@*@@@+++++=@@@#@@+++@@@@@@@#:%*@@@=:#+#@@@@@@@@@@@@@%%@@@@@@
@%@@@@@%%#%@@@@@@--***@*----.#%..@%#@@@@++++..:+@@::::@@++..+=++@@@@##@%.##:@@=*@@@@@@@@=......*@@@@@@@@
@@@@@@@%%@%%%@@@@.----.=@.-#..#+#@:.@@@@::::.+@:@@.:::@@=@=.::::@@@@::@@@@@@@@*@@@#@*@@=-...%*.@@@@@@@@@
@@@@@@@%+@%@%@@@%.@:..#+#-..+...*@+%@@@@-:::.=@@@@.:::@@@@=..::.@@@@@*@@@%@@@%@-@-@@@@@@*.#@:..@@@@@@@@@
@@@@@@%@@@@.*-.:@@@.@.-.%:.@...-=@++@@@%::::.-=@@@%..*@@@*+.::::-@@@++@@@+-@@@@@@@#*#%@+=:%...=@%@@@@@@@
@@@@@@@@@....=#.=#.@+..=@#...@.-#@@++@-:::@@.:.@:......:@...@@::::@++@@@@@@@-#*:+@@@#*%=.=+==.@@%@@@@@@@
@@@@@@@@@@...@%++.*@@......+::.=%%@@+@:::@@@@@@-........=@@@@@@:::@+@@-+-:@@@@*+=-=*+@+=...:..@@@@@@@@@@
@@@@@@@@@@...@-@#%+@::::+:@#%:@%@@%@@@+::@@@@@@+=:::::.=+@@@@@@::+@@@@@@:=:========%+@@=.%%..+@@@@@@@@@@
@@@@@@@@@@@..:-%@#-:::::::+%:::::@@@@@%+::@@@@@@++=--=++@@@@@@::+*@@@%:@==========*#-@%.:@#..@@@@@@@@@@@
@@@@@@@@@@@+:::.::::+%:::-.@@@@%##%@%=@=++::@@@@@@@@@@@@@@@@::++=@@%@#=#==========*+#@@@@....@@@@@@@@@@@
@@@@@@@@@@@@::*#.=:::@@@@%%##@+.----=##@@+++::-@@@@@%@@@@-::+++%@%%%@.@.==========**@@@%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@::@@@@**@@@------------**##%@%++++-:::--::::++++#@@%%=@@.@:=========+%=@@@@@@@=%@@@@@@@@@@@
@@@@@@@@@@@@@+@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*@@@@@@@@@@@@
@@@@@@@@@@@@@@@.....@=+.::::::::::::::::::::-:::::::::::::::::::::::::--:::-::--.=+@.....@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@.=..*@..............................................................%@..::@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@.=:*@.....####..####:....######@.###=...######@##@%%%%%%%###:##@...%@.:-@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@:-*@.::::####@##%##:::::*#@:-##:####:::##::###:::::##@:::####@:::.%@::@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@-*@.:#--##:####:##:::::#####%.#####%::##@##@::::::##@::::##@--#:.%@-@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@.-*@.:---##--##=:##-----##@---##@::##@:##--##@---:-%#@----##@----.%@-+@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@.--*@+*=--------------------------------------------------------+*+@@--+@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@+====@**====+=+==++++=+++++===++====++++++++++++===+======+++=+===##@*===%@@@@@@@@@@@@@@@
@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@+@@@@@@@@@@@.+@@@@@@@@@@@*%@@@@@#@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=*@@@@%@@%@@@@@@@@@*..:+--+@@@%%@@@@@@=%@@@@@=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*#@@@@%%=%*@@@@@%@@.--+@@@@@@@%=%-@@%@@%==@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*=+%@@@@@@@@@@@#=@@=+@@@@@%@@@@@%%=+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-=#%@@@@@@@@@@@@@@@@@@%@--+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=-==------==--*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


''')
#MOSTRAMOS LOGO DE LA TIENDA Y PONEMOS UNA PAUSA DE 3 SEGUNDOS
for i in intrologo:
    print(i, end="", flush=True)
    time.sleep(0.00001)
time.sleep(3)

#CREAMOS UN BUCLE PARA TODO EL PROGRAMA
while True:
    os.system('cls')
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.YELLOW)
    print('''

%@@@@@@@@@@++-.....................................................................................+#%@@@@@@@@@@@#
@@........@=+=.+---==============================---=--=======================--================+-.=*+@........@@@
@@:=....=@@=+=.....................................................................................=++@@+....-:@@@
@@@:=...+@@.......*****:...-****#.......-*****+:.....***-.....*******-...***#+************#...***#:...:@%...=:@@@@
@@@@:-..+@@.......#####%...######:......=###%####%..-####.....###%%#####.###@#%%%%%%%%%:###@.###%.....-@%..=:@@@@@
@@@@@:-:+@@.::::::######@.#######:::::::=**#...###@:#####@.:::###@.::###@:::::::+##%:::::######@::::..-@%.-:@@@@@@
@@@@@@--*@@.:##:::###=###-###+###:::::::=#############@###@:::#########%::::::::+##%::::::####@::-##:.-@#--@@@@@@@
@@@@@@%-*@@.:-=:--###++#####*+###:::::::+###%##%%:*##**#*##-::###@=###@:::::::::*##%::::::+###:---=--.-@#-%@@@@@@@
@@@@@@--*@@.------###*:####@-+###:::::::+###:::::-##%%%%%##%::###%:=###@:::::#::*##%::::::*###:-----:.=@#--@@@@@@@
@@@@@---*@@====---@@@+--@@@--*@@@-------+@@@:----@@@#----@@@@:@@@#--#@@@@----#--*@@@------*@@@:---=====@#---@@@@@@
@@@@----+@@%%+=-----------------------------------------------------------------------------------+%%%@@#----@@@@@
@@@==---==@***==---------------------------------------------------------------------------------=+#*#@**---==@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

''')
    #MOSTRAMOS LAS OPCIONES DISPONIBLES
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
    
    print("\t\t\t\t\t TIENDA DE ALCOHOL, BEBIDAS Y ENTRADAS")
    
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
    if bebidas_disponibles > 0:
        print(Fore.LIGHTCYAN_EX + "\t\t\t1-" + Fore.YELLOW + "VENTA DE BEBIDAS\n")
    else:
        print(Fore.LIGHTCYAN_EX + "\t\t\t1-" + Fore.YELLOW + "VENTA DE BEBIDAS", Fore.RED + " AGOTADO\n")
    if entradas_disponibles > 0:
        print(Fore.LIGHTCYAN_EX + "\t\t\t2-" + Fore.YELLOW + "VENTA DE ENTRADAS\n")
    else:
        print(Fore.LIGHTCYAN_EX + "\t\t\t2-" + Fore.YELLOW + "VENTA DE ENTRADAS", Fore.RED + " AGOTADO\n")
    print(Fore.LIGHTCYAN_EX + "\t\t\t3-" + Fore.YELLOW + "INVENTARIO DE LA TIENDA\n")
    print(Fore.LIGHTCYAN_EX + "\t\t\t4-" + Fore.YELLOW + "REGISTRO DE VENTAS REALIZADAS\n")
    print(Fore.LIGHTRED_EX + "\t\t\t0-" + Fore.LIGHTRED_EX + "SALIR\n")
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "\t\t\tSELECCIONAR OPCION(1-4): \n")
    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
    #PEDIMOS AL USUARIO UNA OPCION PARA ACCEDAR A X PARTE DEL MENU
    opcion = input("OPCION DESEADA: ")
    
    #VENTA DE BEBIDAS
    if opcion == "1":
        #LIMPIAMOS PANTALLA
        os.system('cls')
         #SI HAY BEBIDAS DISPONIBLES MOSTRAMOS LOS TIPOS DE BEBIDA DISPONIBLES(RON,VODKA,WHISKY...)
        if bebidas_disponibles > 0:
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            print("\t\t\t\t\t VENTA DE BEBIDAS")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            cont = 1
            for i in productos:
                print(f"\t\t\t\t{cont}- {i}\n")
                cont += 1
            print(Fore.RED + f"\t\t\t\tOTRO- SALIR\n")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            print("\t\t\t\t\t ELIGE UN TIPO DE BEBIDA")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            #PEDIMOS UN TIPO DE BEBIDA AL USUARIO
            option = input("\t\t\t\t\t OPCION DESEADA (1-5)")
            if option != "":
                option=int(option)
                if 0 < option < 6:
                    #MOSTRAMOS LAS MARCAS DEL TIPO DE BEBIDA ELEGIDO
                    cont = 1
                    os.system('cls')
                    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
                    print("\t\t\t\t\t MARCAS DISPONIBLES")
                    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
                    for i in bebidas_todas[option - 1]:
                        print(f"\t\t\t\t{cont}- {i}\n")
                        cont += 1
                    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
                    print("\t\t\t\t\t ELIGE MARCA")
                    print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
                    #PEDID¡MOS AL USUARIO UNA MARCA
                    marca=input("\t\t\t\t\t MARCA DESEADA (1-5)")
                    if marca != "":
                        marca=int(marca)
                        if 0 < marca < 6:
                            #MOSTRAMOS LA MARCA DESEADA CON SU PRECIO 
                            print(Fore.RESET + f"\t\t\t\tBEBIDA SELECCIONADA: {option - 1}\n")
                            print(Fore.RESET + f"\t\t\t\tTIPO DE BEBIDA: " + Fore.LIGHTYELLOW_EX + f"{productos[option - 1]}\n")
                            print(Fore.RESET + "\t\t\t\tBEBIDA SELECCIONADA: " + Fore.MAGENTA + f"{bebidas_todas[option - 1][marca - 1]}")
                            print(Fore.RESET + "\t\t\t\tPRECIO: " + Fore.YELLOW + f"{precios_bebidas[option-1]} €\n")
                            precio=int(precios_bebidas[option-1])
                            print(Fore.GREEN + "\t\t\t\t1-ACEPTAR")
                            print(Fore.RED + "\t\t\t\t2-RECHAZAR\n")
                            #PEDIMOS AL USUARIO CONFIRMAR LA COMPRA
                            confirm = input(Fore.YELLOW + "CONFIRMAR VENTA? (1-2): ")
                            if confirm == "1":
                                #EN CASO DE CONFIRMAR LA COMPRA SE AGREGARA ESTA A ALGUNAS LISTAS CON SU PRECIO, SUBIRAN LAS VENTAS Y GANANCIAS
                                ganancias_totales_productos=ganancias_totales_productos+precio
                                ganancias_totales=ganancias_totales+precio
                                ventas=ventas+1
                                bebidas_disponibles = bebidas_disponibles - 1
                                ganancias_productos.append(precios_bebidas[option-1])
                                productos_vendidos.append(bebidas_todas[option - 1][marca - 1])
                                print(Fore.GREEN + "\t\t\t\tBEBIDA VENDIDA CON ÉXITO, GRACIAS POR SU COMPRA")
                                print(Fore.BLUE + "\t\t\t\tPD: Y TEN CUIDAICO CON EL ALCOHOL QUE LUEGO NO SABES NI DONDE ESTAS, NO NOS HACEMOS RESPONSABLES :)")
                                print(Fore.RED + """\t\t                                             
                 ####           --==*+-      
           ############         -=-+*+:      
          ###########=-         -==+++-      
        ############+...        -==+++-      
      ##############=..+*       -==+**+      
     ###############==-+##     .=....::      
   ########################  .-#*+###+*#-    
%%%###########%##%%%#**##%% -##=======++*=   
%%%%%%%%%%%%%%%*++=+=+-==+  *%+===--===+**=  
 %%%%%%%%%%%%*=-:--:.:-::  :#%+==----#*#**+  
 %%%%%%#%%%%#=:::---+%--=  -#%*=-:-+#%@%#*+  
   %%=:+**#%%*+:-:.#%*--==::+==*++***%@%%#+  
    ::=--+*%%%+--::-*=-:::::****+===*%@%@#+  
     ==:::=*+==-*##%*==--:::**++*+*+*%#+%#+  
    #####++===--+#%@@%%+====*#***+-:=%%%%#*  
     ##%%%%*+====###%%@@@##=*+---=#*#%%#%#*  
     ##%#%%%%+==####+***#%%#*#+=========***  
    ##########-+##+=*%%%%   ##+=+=======***  
    ###%#######*=-=**#=+%%%%#%+=========***  
    ##.######*:-******--%%%%*%++=+======***  
    ..--=-==+++*******++   #*#+=========*%#  
    --     .:-+#########    *#*=========*%#  
   -:         .=*##%%%@%%  :=+===---=#*+*%#  
   -:.-:.-:.-..+#%%%%@@@%  :+++===--=%#*#%#  
    ==+-.+-:+++*%%@@@@%%%%%:*%#======+++*#*  
    ##%#*#####  @@@@@%%%%%% +#**+=--=+***+-  
    %%%%%%%%%%      %%%%%%%                  
   %%%%%%%%%       %%%%%%%%%                 
 ##########%%%   %%%%%####%%###              
 %%%%#**++****   %%###%%%##****##            
#####*++++++**  %%%%%%##*******##            
#####****+****  %%%%%######**###%            
*###########**  %%%%%%%%%%%%%%%%             
 *****++++***   %%%%%%%%#***##%              """)
                                #PEDIMOS AL USUARIO VOLVER AL INICIO
                                input(Fore.RESET + "\t\t\t\tPULSA " + Fore.GREEN + "ENTER " + Fore.RESET + "PARA VOLVER")
                
                
          #VENTA DE ENTRADAS      
    elif opcion == "2":
        #LIMPIAMOS PANTALLA
        os.system('cls')
        #EN CASO DE HABER ENTRADAS SUFICIENTES SE ACCEDERA AL MENU DE ENTRADAS
        if entradas_disponibles > 0:
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            print("\t\t\t\t\t VENTA DE ENTRADAS")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            cont=1
            #MOSTRAMOS LOS TIPOS DE ENTRADAS QUE SE PUEDEN COMPRAR
            for i in modelos_entradas:
                print(f"\t\t\t\t{cont}- {i}\n")
                cont=cont+1
            print(Fore.RED + f"\t\t\t\tOTRO- SALIR\n")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            print("\t\t\t\t\t ELIGE ENTRADA")
            print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
            #PEDIMOS ENTRADA AL USUARIO
            option = input("\t\t\t\t\tOPCION DESEADA (1-5): ")
            if option != "":
                option=int(option)
                if option != 0 and option < 6:
                    #MOSTRAMOS EL NOMBRE DE ENTRADA Y SU PRECIO POR UNIDAD
                    print(Fore.RESET + f"\t\t\t\tENTRADA SELECCIONADA: {option}\n")
                    print(Fore.RESET + "\t\t\t\tENTRADA SELECCIONADA: " + Fore.MAGENTA + f"{modelos_entradas[option-1]}")
                    print(Fore.RESET + "\t\t\t\tPRECIO POR ENTRADA: " + Fore.YELLOW + f"{precios_entradas[option-1]} €\n")
                    precio=int(precios_entradas[option-1])
                    #PEDIMOS AL USUARIO CONFIRMAR COMPRA
                    print(Fore.GREEN + "\t\t\t\t1-ACEPTAR")
                    print(Fore.RED + "\t\t\t\t2-RECHAZAR\n")
                    confirm = input(Fore.YELLOW + "CONFIRMAR VENTA? (1-2): ")
                    if confirm == "1":
                        #PEDIREMOS AL USUARIO UN NUMERO DE ENTRADAS A COMPRAR (EN CASO DE SER SUPERIOR AL NUMERO DE ENTRADAS DISPONIBLES NO SERA POSIBLE LA COMPRA)
                        num_entradas=int(input(Fore.YELLOW + "\t\t\t\tDIME EL NUMERO DE ENTRADAS QUE VAS A COMPRAR: "))

                        if num_entradas <= entradas_disponibles:
                            #EN CASO DE SER INFERIOR O IGUAL AL NUMERO DE ENTRADAS DISPONIBLES SE AGREGARAN AL REGISTRO DE VENTAS Y SUBIRAN LAS GANANCIAS DE ENTRADAS Y TOTALES
                            for i in range(num_entradas):
                                ganancias_totales_entradas=ganancias_totales_entradas+precio
                                ganancias_totales=ganancias_totales+precio
                                ventas=ventas+1
                                entradas_disponibles = entradas_disponibles - 1
                                ganancias_entradas.append(precios_entradas[option-1])
                                entradas_vendidas.append(modelos_entradas[option-1])
                            print(Fore.GREEN + "\t\t\t\tENTRADA VENDIDA CON ÉXITO, GRACIAS POR SU COMPRA")
                            print(Fore.LIGHTGREEN_EX + """   %#*++++++++++++++++==================#*              
  =*==+*++++++++++++++++++++++++++++++*--+*+            
@*--++==------------------------------=++--=%           
**=#======++==**=#**=+*++*+*++*+=++==+=-=*++#           
=%=#=-===+*#+=*-=%**+**=+=******+*#*=+=--*++*           
@+=#=-==------**=*++=+*++=-+++==-----+=--*+=#           
@*=#==++=======++==++==+=+++=++======+===*+=#           
@+=#==++++***=+#++***+*#*%%++#*=+***+++==*+=#           
@*=#++++++*#+++*++**#****##*+**++***+++++*+=#           
@*-=+++++++++++++++++++++++++++++++++++++=-=%           
  #*-=********************************#=-=*@            
   -#+++++++++++++++++==================*+              
     ....................................               
                       ..                               
                       =:.                              
                      .::-=     ****                    
                    ...:.=*:..*********                 
                   ...::=+::=+**=..-**##                
                   -::=*++-=####++++*###%               
                      -===**%%##****###%%%              
                       *******=*+::=*=+%%%              
                        *****-:*+--+*--#%%              
                         ****+:=+-:++:-#=:              
                          ******-::-+*#+-:              
                           **#%@%##%@@@*                
                           #####*++*#%@                 
                            ###*==+-++   ***            
                             ##%*==*##******#           
                              #%%##%%%####%###          
                              %%#####+*# **##*=         
                              #*-*###+=##+=-:-=.        
                              %#*########%--:.:.        
                               %########%%%+=-.         
                             %%%%%%##%%%%%%%%           
                            %%%%%%%%%%%%%%%%%%%         
                            %%%%%%        %%%%%%%%%     
                           *%%%%%%%         %%%%%%##**  
                          *+++###%%%#        %%%#*++++*#
                          **++**#####        ####*****##
                           #*******##         ##******* """)
                        
                        else:
                            print(Fore.RED + "\t\t\t\tERROR, CANTIDAD INSUFICIENTE DE ENTRADAS")
                        #PEDIMOS AL USUARIO VOLVER AL MENU 
                        input(Fore.RESET + "\t\t\t\tPULSA " + Fore.GREEN + "ENTER " + Fore.RESET + "PARA VOLVER")
    #INVENTARIO DE LA TIENDA        
    elif opcion == "3":
        os.system('cls')
        print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        print("\t\t\t\t\t INVENTARIO DE LA TIENDA")
        print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        #MOSTRAMOS NUMERO DE BEBIDAS RESTANTES
        print(Fore.YELLOW + "BEBIDAS RESTANTES: ", Fore.MAGENTA + f"{bebidas_disponibles}")
        print("")
        print("")
        #MOSTRAMOS TODA LAS MARCAS DE RON
        print(Fore.YELLOW + "MODELOS DE RON: ")
        for i in modelos_ron:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print("")
        print("")
        #MOSTRAMOS TODA LAS MARCAS DE VODKA
        print(Fore.YELLOW + "MODELOS DE VODKA: ")
        for i in modelos_vodka:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print("")
        print("")
        #MOSTRAMOS TODA LAS MARCAS DE WHISKY
        print(Fore.YELLOW + "MODELOS DE WHISKY: ")
        for i in modelos_whisky:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print("")
        print("")
        #MOSTRAMOS TODA LAS MARCAS DE GINEBRA
        print(Fore.YELLOW + "MODELOS DE GINEBRA: ")
        for i in modelos_ginebra:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print("")
        print("")
        #MOSTRAMOS TODA LAS MARCAS DE MEZCLAS
        print(Fore.YELLOW + "MODELOS DE MEZCLAS: ")
        for i in modelos_mezclas:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print("")
        print("")
        #MOSTRAMOS NUMERO DE ENTRADAS RESTANTES
        print(Fore.YELLOW + "ENTRADAS RESTANTES: ", Fore.MAGENTA + f"{entradas_disponibles}")
        print()
        #MOSTRAMOS LOS MODELOS DE ENTRADAS DISPONIBLES
        print(Fore.YELLOW + "ENTRADAS: ")
        for i in modelos_entradas:
            print(Fore.LIGHTGREEN_EX + i, "  |  ", end="", flush=True)
        print()
        #PEDIMOS AL USUARIO VOLVER AL INICIO
        print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        print("\t\t\t\t\t PULSA ENTER PARA VOLVER AL INICIO")
        print(Fore.RED + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        input()
    #REGISTRO DE VENTAS REALIZADAS
    elif opcion == "4":
        os.system('cls')
        print(Fore.GREEN + "-----------------------------------------------------------------------------------------------------------------" + Fore.BLUE)
        print("\t\t\t\t\t REGISTRO DE VENTAS REALIZADAS")
        print(Fore.GREEN + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        print()
        #MOSTRAMOS EN NUMERO TOTAL DE VENTAS
        print(Fore.GREEN +  "NUMERO DE VENTAS REALIZADAS: ", Fore.YELLOW + f"{ventas}")
        print()
        print(Fore.GREEN + "BEBIDAS:")
        print()
        print()
        cont=0
        #MOSTRAMOS CADA BEBIDA VENDIDA CON SU PRECIO
        for i in productos_vendidos:
            print(Fore.LIGHTYELLOW_EX + "\t\t\t\t\t\t Producto: ", Fore.CYAN + f"{i} ----", Fore.LIGHTYELLOW_EX + "precio: ", Fore.CYAN + f"{ganancias_productos[cont]}€")
            cont=cont+1
            print()
            #MOSTRAMOS LAS GANANCIAS TOTALES DE BEBIDAS
        print(Fore.LIGHTYELLOW_EX + "\t\t\t\t\t\t\t\t\t\t Ganancias Totales (Bebidas): ", Fore.CYAN + f"{ganancias_totales_productos}€")

        print(Fore.GREEN + "ENTRADAS:")
        print()
        print()
        cont2=0
        #MOSTRAMOS TODAS LAS ENTRADAS COMPRADAS CON SU CODIGO, TIPO Y PRECIO
        for i in range(0,len(entradas_vendidas),1):
            print(Fore.LIGHTYELLOW_EX + "\t\t\t\t\t\t Codigo Entrada",Fore.CYAN + f"{i}" ,Fore.LIGHTYELLOW_EX + "-Entrada: ", Fore.CYAN + f"{entradas_vendidas[i]} ----", Fore.LIGHTYELLOW_EX + "precio: ", Fore.CYAN + f"{ganancias_entradas[cont2]}€")
            cont2=cont2+1
            print()
            #MOSTRAMOS GANANCIAS TOTALES DE ENTRADAS
        print(Fore.LIGHTYELLOW_EX + "\t\t\t\t\t\t\t\t\t\t Ganancias Totales (Entradas): ", Fore.CYAN + f"{ganancias_totales_entradas}€")
        print()
        print()
        #MOSTRAMOS LAS GANANCIAS TOTALES (ENTRADAS + BEBIDAS)
        print(Fore.LIGHTYELLOW_EX + "\t\t\t\t\t\t\t\t\t\t Ganancias Totales: ", Fore.CYAN + f"{ganancias_totales}€")
        print(Fore.GREEN + "-----------------------------------------------------------------------------------------------------------------" + Fore.BLUE)
        print("\t\t\t\t\t PULSA ENTER PARA VOLVER")
        print(Fore.GREEN + "-----------------------------------------------------------------------------------------------------------------" + Fore.RESET)
        input()
        #SALIR
    elif opcion == "0":
        #AL SALIR MOSTRAOS UN MENSAJE DE DESPEDIDA Y SE CERRARA EL PROGRAMA
        os.system('cls')
        despedida=(Fore.LIGHTBLUE_EX + '''
██╗░░░██╗██╗░░░██╗███████╗██╗░░░░░██╗░░░██╗███████╗  ██████╗░██████╗░░█████╗░███╗░░██╗████████╗░█████╗░
██║░░░██║██║░░░██║██╔════╝██║░░░░░██║░░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗
╚██╗░██╔╝██║░░░██║█████╗░░██║░░░░░╚██╗░██╔╝█████╗░░  ██████╔╝██████╔╝██║░░██║██╔██╗██║░░░██║░░░██║░░██║
░╚████╔╝░██║░░░██║██╔══╝░░██║░░░░░░╚████╔╝░██╔══╝░░  ██╔═══╝░██╔══██╗██║░░██║██║╚████║░░░██║░░░██║░░██║
░░╚██╔╝░░╚██████╔╝███████╗███████╗░░╚██╔╝░░███████╗  ██║░░░░░██║░░██║╚█████╔╝██║░╚███║░░░██║░░░╚█████╔╝
░░░╚═╝░░░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░''')
        for i in despedida:
            print(i, end="", flush=True)
            time.sleep(0.00001)
        time.sleep(3)
        break
    
