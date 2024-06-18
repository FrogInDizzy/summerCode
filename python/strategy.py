from abc import ABC, abstractmethod
import csv
import pandas as pd

class FileReader(ABC):
    @abstractmethod
    def read(self, filepath):
        pass


class TxtReader(FileReader):
    def read(self, filepath):
        with open(filepath, 'r') as file:
            data = file.read()
        return data

class CsvReader(FileReader):
    def read(self, filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
        return data

class XlsxReader(FileReader):
    def read(self, filepath):
        data = pd.read_excel(filepath)
        return data

class FileContext:
    def __init__(self, strategy: FileReader):
        self._strategy = strategy

    def set_strategy(self, strategy: FileReader):
        self._strategy = strategy

    def read_file(self, filepath):
        return self._strategy.read(filepath)

def get_file_reader(file_type):
    if file_type == 'txt':
        return TxtReader()
    elif file_type == 'csv':
        return CsvReader()
    elif file_type == 'xlsx':
        return XlsxReader()
    else:
        raise ValueError("Unsupported file type")
