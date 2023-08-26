class Cars():

    engine = 'EV'
    @staticmethod
    def _statement():
        return 'hi'
        
        
    def __init__(self, brand, year, cost):
        self.brand = brand
        self.year = year
        self.cost = cost

    def add_ons(self, specs):
        self.specs = specs

Tesla = Cars('Tesla', 2020, 65000)
Tesla.add_ons('Self drive')

print(Tesla.specs)

Hyundai = Cars('Prius', 2022, 50000)
Hyundai.add_ons('Fast charge')
print(Hyundai.specs)
print(Hyundai._statement())
print(Tesla._statement())