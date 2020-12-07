from com.bridgelabz.CensusAnalyzer.CSVLoader import CSVLoader
from com.bridgelabz.CensusAnalyzer.censusAnalyzerError import censusAnalyzererror
import pytest
csv_filepath= r"D:\PycharmProjects\Census_Analyzer\CensusData.csv"
csv_wrongfilepath=r"C:\PycharmProjects\Census_Analyzer\CensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE=r"D:\PycharmProjects\Census_Analyzer\ModifiedCensus.csv"
CENSUS_CSV_FILE_WRONG_DELIMITER=r"D:\PycharmProjects\Census_Analyzer\ModifiedCensus.csv"
def test_recordcount_Indiacensus():
    csv_loader=CSVLoader(csv_filepath)
    assert csv_loader.record_counter()== 29


def test_recordcount_wrongfilepath_IndiaCensus():
    csv_loader=CSVLoader(csv_wrongfilepath)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()

# Check if exception gets raised or not
def test_record_counter_for_wrong_file_type_IndiaCensus():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()


# Check if exception gets raised or not
# NOTE - Change delimiter of the file and save it
def test_record_counter_for_wrong_delimiter_IndiaCensus():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(censusAnalyzererror):
        csv_loader.record_counter()




