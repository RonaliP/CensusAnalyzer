import pandas as pd
from com.bridgelabz.CensusAnalyzer.IndiaCensusCSV import IndiaCensusCSV
from com.bridgelabz.CensusAnalyzer.censusAnalyzerError import censusAnalyzererror
class CSVLoader:
  def __init__(self,path):
    self.path=path
  def record_counter(self):
    try:
      columns_headers=repr(IndiaCensusCSV()).split(",")
      print(columns_headers)
      data=pd.read_csv(self.path,usecols=columns_headers)
      return len(data)

    except FileNotFoundError:
      raise censusAnalyzererror("CheckFilePath")
    except ValueError:
      raise censusAnalyzererror("wrong delimeters or invalid columns name")

# if __name__ == '__main__':
#   csv=CSVLoader(r"D:\PycharmProjects\CensusAnalyzer\CensusData.csv")
#   print(csv.record_counter())