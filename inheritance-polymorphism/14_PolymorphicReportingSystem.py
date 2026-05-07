# Problem 14: Polymorphic Reporting System
# Scenario: Generate different report types
# Task: Override generate() method

class Report:

    def generate(self):
        print("Generating report...")


class PDFReport(Report):

    def generate(self):
        print("Generating PDF report...")


class ExcelReport(Report):

    def generate(self):
        print("Generating Excel report...")


# Creating list of objects
reports = [PDFReport(), ExcelReport()]

# Looping through reports
for r in reports:
    r.generate()