from mrjob.job import MRJob
from mrjob.step import MRStep

class TopPaymentMethods(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_category_amount,
                   reducer=self.reducer_category_total),
            MRStep(mapper=self.mapper_filter_top_categories,
                   reducer=self.reducer_top_payment_methods)
        ]

    def mapper_category_amount(self, _, line):
        data = line.split("\t")
        if len(data) == 6:
            category = data[3]
            payment_method = data[5]
            try:
                amount = float(data[4])
                yield category, (payment_method, amount)
            except ValueError:
                pass

    def reducer_category_total(self, key, values):
        total_amount = 0
        payment_data = []
        for payment_method, amount in values:
            total_amount += amount
            payment_data.append((payment_method, amount))
        if total_amount > 50000:
            for payment_method, amount in payment_data:
                yield payment_method, 1

    def mapper_filter_top_categories(self, key, count):
        yield key, count

    def reducer_top_payment_methods(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    TopPaymentMethods.run()
