from mrjob.job import MRJob

class CountByCategory(MRJob):
    def mapper(self, _, line):
        data = line.split("\t")
        if len(data) == 6:
            category = data[3]
            yield category, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
    CountByCategory.run()
