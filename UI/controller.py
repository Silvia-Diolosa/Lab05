import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._sceltaCorso = None




    def mostraCorsi(self):
        for c in self._model.getCorsi():
            self._view.menùCorsi.options.append(ft.dropdown.Option(key=c.codins, data=c, text=c.__str__(), on_click=self.selezCorso))
        self._view.update_page()


    def cercaIscritti(self, e):
        self._view.lvOut.controls.clear()

        corso = self._sceltaCorso

        if corso is None:
            (self._view.create_alert("Attenzione, selezionare un corso."))
            self._view.update_page()
            return

        numero_studenti = len(self._model.getStudenti(corso.codins))
        if numero_studenti == 0:
            self._view.lvOut.controls.append(ft.Text("Non ci sono studenti iscritti a questo corso"))
            self._view.update_page()
        else:
            self._view.lvOut.controls.append(ft.Text("Ci sono " + str(numero_studenti) + " iscritti al corso"))
            for studente in self._model.getStudenti(corso.codins):
                self._view.lvOut.controls.append(ft.Text(studente.__str__()))
            self._view.update_page()

    def selezCorso(self,e):
        self._sceltaCorso = e.control.data


    def cercaStudente(self, e):
        self._view.lvOut.controls.clear()
        matricola = self._view.matricola.value
        studente = self._model.cercaStudente(matricola)
        if studente is None:
            (self._view.create_alert("Non c'è nessuno studente con questa matricola"))
            self._view.update_page()
            return

        self._view.nome.value = studente.nome
        self._view.cognome.value = studente.cognome
        self._view.update_page()

    def cercaCorsi(self, e):
        self._view.lvOut.controls.clear()
        matricola = self._view.matricola.value
        studente = self._model.cercaStudente(matricola)
        if studente is None:
            (self._view.create_alert("Non c'è nessuno studente con questa matricola"))
            self._view.update_page()
            return

        corsi = self._model.corsiStud(matricola)
        for corso in corsi:
            self._view.lvOut.controls.append(ft.Text(corso.__str__()))
        self._view.update_page()


    def iscrivi(self):
        pass
