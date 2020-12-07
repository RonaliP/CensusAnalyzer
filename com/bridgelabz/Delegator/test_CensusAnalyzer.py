from com.bridgelabz.Delegator.main import CSVLoader
from com.bridgelabz.Delegator.CensusAnalyzerError import censusAnalyzererror

from com.bridgelabz.Delegator.HeaderProvider import IndiaCensusCSV
from com.bridgelabz.Delegator.HeaderProvider import StateCodeCSV
import pytest

csv_filepath= r"D:\PycharmProjects\CensusAnalyzer\CensusData.csv"
csv_filepath1=r"D:\PycharmProjects\CensusAnalyzer\IndiaStateCode.csv"
csv_wrongfilepath=r"C:\PycharmProjects\CensusAnalyzer\CensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE=r"D:\PycharmProjects\CensusAnalyzer\ModifiedCensus.csv"
CENSUS_CSV_FILE_WRONG_DELIMITER=r"D:\PycharmProjects\CensusAnalyzer\ModifiedCensus.csv"

censusRecordCount = 29
statesRecordCount = 37

#Below two functions will check for record counts of both indiacensus.csv file and statecode.csv

def test_recordcount():
    csv_loader = CSVLoader(path=csv_filepath, headers=IndiaCensusCSV())
    assert csv_loader.count_records() == censusRecordCount

def test_recordcount_for_Statecode():
    csv_loader=CSVLoader(path=csv_filepath1,headers=StateCodeCSV())
    assert csv_loader.count_records()==statesRecordCount


#below two test cases will check for file paths and will raise error if wrong

def test_recordcount_wrongfilepath():
    csv_loader = CSVLoader(path=csv_wrongfilepath, headers=IndiaCensusCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()

def test_recordcount_wrongfilepath_for_Statecode():
    csv_loader = CSVLoader(path=csv_wrongfilepath, headers=StateCodeCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()

#Below two test cases will test for wrong file type and will raise error

def test_record_counter_for_wrong_file_type_IndiaCensus():
    csv_loader = CSVLoader(path=CENSUS_CSV_FILE_WRONG_TYPE , headers=IndiaCensusCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()

def test_record_counter_for_wrong_file_type_IndiaCensus():
    csv_loader = CSVLoader(path=CENSUS_CSV_FILE_WRONG_TYPE , headers=StateCodeCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()



#below two functions will check for delimiters of two csv files and will raise error if wrong


def test_record_counter_for_wrong_delimiter_IndiaCensus():
    csv_loader = CSVLoader(path=CENSUS_CSV_FILE_WRONG_DELIMITER,headers=IndiaCensusCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()


def test_record_counter_for_wrong_delimiter_IndiaCensus():
    csv_loader = CSVLoader(path=CENSUS_CSV_FILE_WRONG_DELIMITER,headers=StateCodeCSV())
    with pytest.raises(censusAnalyzererror):
        csv_loader.count_records()


#Below two functions will check for if two csv files will be sorted and raise error

def test_if_indiacensusCSV_is_sorted_by_state():
    csv_loader = CSVLoader(path=csv_wrongfilepath, headers=IndiaCensusCSV())

    with pytest.raises(censusAnalyzererror):
        csv_loader.sort_indiacensusCSV_by_state_and_make_json()


def test_if_statecodeCSV_is_sorted_by_state_code():
    csv_loader = CSVLoader(path=csv_wrongfilepath, headers=StateCodeCSV())

    with pytest.raises(censusAnalyzererror):
        csv_loader.sort_statecodeCSV_by_state_code_and_make_json()