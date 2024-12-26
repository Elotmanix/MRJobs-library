from mrjob.job import MRJob
from mrjob.step import MRStep

class WomenClothingCashByCity(MRJob):
    
    def mapper(self, _, line):
        fields = line.split('\t')
        if len(fields) == 6:
            city = fields[2]
            category = fields[3]
            payment = fields[5].strip()  # strip() pour enlever les espaces/newlines
            if category == "Women's Clothing" and payment == "Cash":
                try:
                    amount = float(fields[4])
                    yield city, amount
                except ValueError:
                    pass
    
    def reducer(self, city, amounts):
        yield None, (sum(amounts), city)  # None comme clé pour regrouper tous les résultats
    
    def reducer_find_max(self, _, city_amounts):
        yield max(city_amounts)  # Retourne le tuple avec le montant le plus élevé
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  reducer=self.reducer),
            MRStep(reducer=self.reducer_find_max)
        ]

if __name__ == '__main__':
    WomenClothingCashByCity.run()