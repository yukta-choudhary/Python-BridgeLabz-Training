# Problem 9: Abstract Data Pipeline

from abc import ABC, abstractmethod

class DataPipeline(ABC):

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass


class CSVDataPipeline(DataPipeline):

    def extract(self):
        print("Extracting CSV data...")

    def transform(self):
        print("Transforming data...")

    def load(self):
        print("Loading data into database...")


p = CSVDataPipeline()

p.extract()
p.transform()
p.load()