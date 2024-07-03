from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.aeroporti = DAO.getAllAirports()
        self.dicAerop = {}
        self.aeroportiDizionario()
        self.grafo = nx.Graph()
        self.edges = []
        self.ap = []
        self.ad = []
    def creaGrafo(self):
        self.grafo.add_nodes_from(self.ap)
        self.grafo.add_nodes_from(self.ad)
        for arco in self.edges:
            self.grafo.add_edge(arco[0],arco[1])
            self.grafo.add_edge(arco[1],arco[0])
        print(self.grafo.edges)
        print(self.grafo.number_of_nodes())
        print(self.grafo.nodes)
    def archiTotali(self,numero):
        for elemento in DAO.getFlightsDestination(numero):
            self.ad.append(elemento)
        for elemento in DAO.getFlightsOrigin(numero):
            self.ap.append(elemento)
        for elemento in DAO.getFlights():
            self.edges.append(elemento)
    def aeroportiDizionario(self):
        for a in self.aeroporti:
            self.dicAerop[a.__hash__()] = a

    def cercaPercorso(self, np, nd):
        self.nodoFinale = nd
        self.percorso = []
        visited = {np}
        trovato = self.ricorsione(np, [], visited)
        if trovato:
            return True, self.percorso
        return False, []

    def ricorsione(self, np, parziale, visited):
        print(np)
        print(parziale)
        vicini = list(self.grafo.neighbors(np))
        if self.nodoFinale in vicini:
            parziale.append((np, self.nodoFinale))
            self.percorso = parziale[:]
            return True  # Percorso trovato, terminare la ricorsione
        for nodo in vicini:
            if nodo in visited:
                continue
            parziale.append((np, nodo))
            visited.add(nodo)
            if self.ricorsione(nodo, parziale, visited):
                return True  # Percorso trovato, esci dalla ricorsione
            parziale.pop()
            visited.remove(nodo)
        return False  # Nessun percorso trovato






