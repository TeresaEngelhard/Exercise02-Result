from finanzasApp import Finanzas, Ingresos, Egresos

ingresosAppObj = Ingresos()
egresosAppObj = Egresos() 
finanzasAppObj = Finanzas()

def putMoney():
    print("**Agregar un ingreso**")
    ingreso = float(input("Por favor, escriba la cantidad a agregar: "))
    ingresosAppObj.addMoney(ingreso)
    finanzasAppObj.addMoney(ingreso)

def removeMoney():
    print("**Realizar un egreso**")
    egreso = float(input("Por favor, escriba la cantidad a egresar: "))
    egresosAppObj.takeMoney(egreso)
    finanzasAppObj.takeMoney(egreso)

def showSaldo():
    print("**Monto total de la cuenta**")
    cuentaList = finanzasAppObj.showMoney()
    for cuenta in cuentaList:
        print(cuenta)

def showIngresos():
    noIncome = ingresosAppObj.countIngresos()
    if noIncome == 0:
        print("Usted aún no ha efectuado ningún ingreso")
    else:
        ingresosList = ingresosAppObj.countIngresos()
        print("|Ingresos realizados|:")
        for ingresos in ingresosList:
            print(ingresos)

def showEgresos():
    noOutcome = egresosAppObj.countEgresos()
    if noOutcome == 0:
        print("Usted aún no ha efectuado ningún egreso")
    else:
        egresosList = egresosAppObj.countEgresos()
        print("|Egresos realizados|:")
        for egresos in egresosList:
            print(egresos)

def showTransactions():
    noOutcome = egresosAppObj.countEgresos()
    noIncome = ingresosAppObj.countIngresos()
    if (noIncome == 0) and (noOutcome == 0):
        print("Usted aún no ha realizado ninguna transacción")
    else:
        print("**Reporte de transacciones** \n")
        showIngresos()
        print("")
        showEgresos()
    

while True:
    print("\n Menu: \n")
    print("(0) Salir")
    print("(1) Mostrar el saldo de la cuenta")
    print("(2) Agregar un ingreso")
    print("(3) Realizar un egreso")
    print("(4) Mostrar todos los ingresos realizados")
    print("(5) Mostrar todos los egresos realizados")
    print("(6) Mostrar reporte de todas las transacciones \n")
    option = int(input("opcion: "))

    if option == 0:
        print("termino FinanzasApp\n")
        break
    elif option == 1:
        showSaldo()
    elif option == 2:
        putMoney()
    elif option == 3:
        removeMoney()
    elif option == 4:
        showIngresos()
    elif option == 5:
        showEgresos()
    elif option == 6:
        showTransactions()
    elif option >6:
        print("Opción no existente, por favor elija una opción correcta")