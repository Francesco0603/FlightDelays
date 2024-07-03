import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_name = ft.TextField(
            label="name",
            width=200,
            hint_text="Insert a your name"
        )
        # button for the "hello" reply
        self.btn_hello = ft.ElevatedButton(text="Hello", on_click=self._controller.handle_hello)"""


        # textfield numero compagnie minimo
        self.txtCompagnie = ft.TextField(
            label="# compagnie minimo",
            width=400
        )
        # btn analisi
        self.btnAnalisi = ft.ElevatedButton(
            text="Analizza Aereoprti",
            on_click=self.controller.handle_analisi,
            width=200
        )
        # prima riga
        row1 = ft.Row([self.txtCompagnie,self.btnAnalisi],
                      width=600,
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # dropdown aereoporti di partenza
        self.ddPartenza = ft.Dropdown(
            label="Aereoporti di partenza",
            width=400
        )
        # seconda riga
        row2 = ft.Row([ft.Container(self.ddPartenza,width=400),
                       ft.Container(ft.Text(""),width=200)],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # dropdown aereoporti di arrivo
        self.ddArrivo = ft.Dropdown(
            label="Aereoporti di arrivo",
            width=400
        )
        # btn test connessione
        self.btnTest = ft.ElevatedButton(
            text="Test Connessione",
            on_click=self.controller.handle_test,
            width=200
        )
        # terza riga
        row3 = ft.Row([self.ddArrivo, self.btnTest],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
