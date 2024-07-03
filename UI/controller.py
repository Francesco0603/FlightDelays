import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
    def fillDDP(self):
        for ap in self._model.ap:
            self._view.ddPartenza.options.append(ft.dropdown.Option(key=ap,
                                                                        text=self._model.dicAerop[ap].__str__()))
    def fillDDA(self):
        for ad in self._model.ad:
            self._view.ddArrivo.options.append(ft.dropdown.Option(key=ad,
                                                                     text=self._model.dicAerop[ad].__str__()))
    def handle_analisi(self,e):
        numeroMinimo = self._view.txtCompagnie.value
        try:
            nm = int(numeroMinimo)
        except:
            self._view.create_alert("inserire un numero intero, pusillanime!!")
            return
        if nm < 0 or nm > 13:
            self._view.create_alert("Ma quante compagnie inserisci, ti svegli?")
            return
        self._model.archiTotali(nm)
        self.fillDDA()
        self.fillDDP()
        self._model.creaGrafo()
        self._view.update_page()
    def handle_test(self,e):

        nodoP = int(self._view.ddPartenza.value)
        nodoA = int(self._view.ddArrivo.value)
        flag = self._model.cercaPercorso(nodoP,nodoA)[0]
        if flag:
            percorso = self._model.cercaPercorso(nodoP,nodoA)[1]
            self._view.txt_result.controls.append(ft.Text(f"l'aeroporto {self._model.dicAerop[nodoA].__str__()} è raggiungibile, "
                                                          f"un possibile percorso è il seguente:"))
            c = 0
            for arco in percorso:
                c = c+1
                self._view.txt_result.controls.append(ft.Text(f"{c})Da {self._model.dicAerop[arco[0]].__str__()} a {self._model.dicAerop[arco[1]].__str__()};"))

        else:
            self._view.txt_result.controls.append(ft.Text(f"l'aeroporto {self._model.dicAerop[nodoA].__str__()} non è raggiungibile"))
        self._view.update_page()




