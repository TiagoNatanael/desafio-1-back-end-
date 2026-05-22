import random
import math
class ponto_de_entrega:
    def __init__(self, id_ponto, x, y):
        self.id = id_ponto;
        self.x = x;
        self.y = y;
    def calcular_distancia(self, outro_ponto):
            return math.hypot( self.x - outro_ponto.x, self.y - outro_ponto.y)      
    def __repr__(self):
            return f"Point (id={self.id}, x={self.x}, y={self.y})"
class Caminho:
    def __init__(self, pontos):
        self.ponto_inicial = self.ponto_atual = pontos[0];
        self.pontos_nao_visitados = pontos[1:];
        self.rota = [self.ponto_inicial.id];  
        self.distancia_total = 0.0; 
    def inicar_rota(self):
        while self.pontos_nao_visitados:
            proximo_ponto = min(self.pontos_nao_visitados, key=self.ponto_atual.calcular_distancia);
            self.distancia_total += self.ponto_atual.calcular_distancia(proximo_ponto);
            self.rota.append(proximo_ponto.id);
            self.ponto_atual = proximo_ponto;
            self.pontos_nao_visitados.remove(proximo_ponto);
        self.distancia_total += self.ponto_atual.calcular_distancia(self.ponto_inicial);
        self.rota.append(self.ponto_inicial.id);
        return{
            "rote": self.rota,
            "total distance": round(self.distancia_total, 2)
        }
if __name__ == "__main__":
    pontos = [ponto_de_entrega(i, random.randint(1,10), random.randint(1,10)) for i in range(random.randint(1,10))]
    print("points generated:");
    print(*pontos, sep="\n");

    rota = Caminho(pontos);
    resultado = rota.inicar_rota();
    print("\n-- FINAL RESULTS --")
    print(f"Rote: {resultado['rote']}")
    print(f"Total distance: {resultado['total distance']} km")                 