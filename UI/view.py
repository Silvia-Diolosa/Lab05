import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self.menùCorsi = ft.Dropdown(label="Corso", width=500)
        self._controller.mostraCorsi()
        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.cercaIscritti)

        row1 = ft.Row(controls=[self.menùCorsi, self.btnCercaIscritti], alignment=ft.MainAxisAlignment.CENTER)


        #ROW2
        self.matricola = ft.TextField(label="Matricola")
        self.nome = ft.TextField(label="Nome", read_only=True)
        self.cognome = ft.TextField(label="Cognome", read_only=True)

        row2 = ft.Row(controls=[self.matricola, self.nome, self.cognome], alignment=ft.MainAxisAlignment.CENTER)


        #ROW3
        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.cercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.cercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.iscrivi)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi], alignment=ft.MainAxisAlignment.CENTER)


        self._page.add(row1, row2, row3)

        # List View where the reply is printed
        self.lvOut = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.lvOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
