import pandas as pd
from com.bridgelabz.CensusAnalyzer.StateCensusCSV import StateCodeCensus
from com.bridgelabz.CensusAnalyzer.censusAnalyzerError import censusAnalyzererror

class StateCodeCSVLoader:
    def __init__(self, path):
     self.path = path


def record_counter(self):
    try:
        columns_headers = repr(StateCodeCensus()).split(",")
        print(columns_headers)
        data = pd.read_csv(self.path, usecols=columns_headers)
        return len(data)

    except FileNotFoundError:
        raise censusAnalyzererror("CheckFilePath")
    except ValueError:
        raise censusAnalyzererror("wrong delimeters or invalid columns name")

# if __name__ == '__main__':
#     csv =StateCodeCSVLoader(r"D:\PycharmProjects\CensusAnalyzer\IndiaStateCode.csv")
#     print(csv.record_counter())


