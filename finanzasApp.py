"""
****Hacer caso omiso a los comentarios, 
ya que fueron intentos pasados***
"""

class Finanzas:
    def __init__(self):
        self.cuentaList = []
        # self.ingresosList = []
        # self.IdIngresos = 0
        # self.egresosList = []
        # self.IdEgresos = 0
        cuentaDict = {"Saldo": 0.0}
        self.cuentaList.append(cuentaDict)

    def addMoney(self, ingreso):
        for cuenta in self.cuentaList:
            cuenta["Saldo"] += ingreso

    def takeMoney(self, egreso):
        for cuenta in self.cuentaList:
            cuenta["Saldo"] -= egreso

    def showMoney(self):
        return self.cuentaList

class Ingresos:
    # def __init__(self):
    #     self = Finanzas.__init__(self)
    def __init__(self):
        self.ingresosList = []
        self.IdIngresos = 0

    def addMoney(self, ingreso):
        self.IdIngresos += 1
        ingresoId = self.IdIngresos
        cuentaDict = {"dinero": 0.0}

        ingresosDict = {"id": ingresoId, "cantidad": ingreso}
        self.ingresosList.append(ingresosDict)

        # self.cuentaList.append(cuentaDict)
        # for cuenta in self.cuentaList:
        #     cuenta["dinero"] += ingreso
        
    def countIngresos(self):
        if (self.ingresosList == []):
            return 0
        else: 
            for ingresos in self.ingresosList:
                return self.ingresosList

class Egresos:
    # def __init__(self):
    #     self = Finanzas.__init__(self)
    def __init__(self):
        self.egresosList = []
        self.IdEgresos = 0

    def takeMoney(self, egreso):
        self.IdEgresos += 1
        egresoId = self.IdEgresos

        egresosDict = {"id": egresoId, "cantidad": egreso}
        self.egresosList.append(egresosDict)

        # for cuenta in self.cuentaList:
        #     cuenta["dinero"] -= egreso

    def countEgresos(self):
        if self.egresosList == []:
            return 0
        else:
            for egresos in self.egresosList:
                return self.egresosList


