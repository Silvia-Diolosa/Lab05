# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


class DAO:


    @staticmethod
    def getCorsi():
        cnx = DBConnect.getConnection() #connesione al database

        cursor = cnx.cursor(dictionary=True)  # Crea un cursore: oggetto che permette di inviare i comandi SQL al database e di scorrere i risultati ottenuti.

        query = "SELECT * FROM `corso`"
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getStudenti(codins):
        cnx = DBConnect.getConnection()  # connesione al database

        cursor = cnx.cursor(dictionary=True)  # Crea un cursore: oggetto che permette di inviare i comandi SQL al database e di scorrere i risultati ottenuti.

        query = """SELECT s.*
                FROM studente s, iscrizione i
                WHERE s.matricola = i.matricola
                  and i.codins = %s"""
        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(
                matricola=row["matricola"],
                cognome=row["cognome"],
                nome=row["nome"],
                CDS=row["CDS"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def cercaStudente(matricola):
        cnx = DBConnect.getConnection()  # connesione al database

        cursor = cnx.cursor(
            dictionary=True)  # Crea un cursore: oggetto che permette di inviare i comandi SQL al database e di scorrere i risultati ottenuti.

        query = """SELECT *
                            FROM studente s
                            WHERE s.matricola = %s"""
        cursor.execute(query, (matricola,))

        row = cursor.fetchone()

        cursor.close()
        cnx.close()

        if row is None:
            return None
        return Studente(
        matricola=row["matricola"],
        cognome=row["cognome"],
        nome=row["nome"],
        CDS=row["CDS"])


    @staticmethod
    def corsiStud(matricola):
        cnx = DBConnect.getConnection()  # connesione al database

        cursor = cnx.cursor(
            dictionary=True)  # Crea un cursore: oggetto che permette di inviare i comandi SQL al database e di scorrere i risultati ottenuti.

        query = ("""SELECT c.*
                    FROM iscrizione i, corso c
                    WHERE i.codins = c.codins
                    AND i.matricola = %s""")
        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]))

        cursor.close()
        cnx.close()
        return res
