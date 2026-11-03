from database.corso_DAO import DAO

class Model:
    def __init__(self):
        pass

    def getCorsi(self):
        return DAO.getCorsi()

    def getStudenti(self, codins):
        return DAO.getStudenti(codins)

    def cercaStudente(self, matricola):
        return DAO.cercaStudente(matricola)

    def corsiStud(self, matricola):
        return DAO.corsiStud(matricola)