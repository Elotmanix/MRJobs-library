from mrjob.job import MRJob

class SumByCityPayment(MRJob):
    def mapper(self, _, line):
        data = line.split("\t")
        if len(data) == 6:
            city = data[2]
            payment_method = data[5]
            try:
                amount = float(data[4])
                if city == "San Francisco":
                    yield payment_method, amount
            except ValueError:
                pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SumByCityPayment.run()
