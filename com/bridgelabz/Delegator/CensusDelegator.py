from com.bridgelabz.Delegator.CensusAnalyzerError import censusAnalyzererror

import pandas as pd


class CensusDelegator:
    def __init__(self, path, headers):
        self.path = path
        self.headers = headers

    def load_data(self):
        try:
            columns_headers = repr(self.headers).split(",")
            data = pd.read_csv(self.path, usecols=columns_headers)
            return data

        except FileNotFoundError:
            raise censusAnalyzererror("Check File path")
        except ValueError:
            raise censusAnalyzererror("Wrong delimeters or Invalid columns name")

    def count_records(self):
        data = self.load_data()
        return len(data)

    def sort_indiacensusCSV_by_state_and_make_json(self):
        sorted_data = (
            self.load_data()
            .sort_values(by=["State"], axis=0)
            .reset_index(drop=True)
            .to_json()
        )

        if (
            sorted_data["State"][0] != "Andhra Pradesh"
            and sorted_data["State"][28] != "West Bengal"
        ):
            raise censusAnalyzererror("Data is un-sorted")

    def sort_statecodeCSV_by_state_code_and_make_json(self):
        sorted_data = (
            self.load_data()
            .sort_values(by=["StateCode"], axis=0)
            .reset_index(drop=True)
            .to_json()
        )

        if sorted_data["StateCode"][0] != "AD" and sorted_data["StateCode"][37] != "WB":
            raise censusAnalyzererror("Data is un-sorted")
