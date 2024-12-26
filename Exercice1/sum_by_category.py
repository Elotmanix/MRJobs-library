from mrjob.job import MRJob

class SumByCategory(MRJob):
    def mapper(self, _, line):
        data = line.split("\t")
        if len(data) == 6:
            category = data[3]
            try:
                amount = float(data[4])
                yield category, amount
            except ValueError:
                pass

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    SumByCategory.run()
