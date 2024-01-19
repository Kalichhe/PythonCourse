
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