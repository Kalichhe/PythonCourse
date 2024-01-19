
# Liskov's Substitution Principle

class Ave:
    def poner_huevos(self):
        print("Poniendo huevos...")
    
    def alimentarse(self):
        print("Alimentándose...")

class AveVoladora(Ave):
    def volar(self):
        print("Volando...")

class AveNadadora(Ave):
    def nadar(self):
        print("Nadando...")
        
# Este principio nos dice que una clase derivada debe poder sustituirse por su clase base sin que se altere el comportamiento del programa. Es decir, que una clase derivada debe ser completamente sustituible por su clase base.