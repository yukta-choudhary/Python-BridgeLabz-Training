# Problem 17: Data Export System
# Scenario: Export data in multiple formats
# Task: Override export() method

class Exporter:

    def export(self, data):
        print("Exporting data...")


class CSVExporter(Exporter):

    def export(self, data):
        print("Exporting data as CSV...")


class JSONExporter(Exporter):

    def export(self, data):
        print("Exporting data as JSON...")


class XMLExporter(Exporter):

    def export(self, data):
        print("Exporting data as XML...")


# Creating exporter objects
for e in [CSVExporter(), JSONExporter()]:
    e.export({"name": "Alex"})