from com.bridgelabz.Delegator.CensusDelegator import CensusDelegator


class CSVLoader:
    def __init__(self, path, headers):
        self.delegator = CensusDelegator(path=path, headers=headers)
        # self.delegator_methods = [
        #     f for f in dir(CensusDelegator) if not f.startswith("__")
        # ]

    def count_records(self):
        num_records = self.delegator.count_records()
        return num_records

    def sort_indiacensusCSV_by_state_and_make_json(self):
        self.delegator.sort_indiacensusCSV_by_state_and_make_json()

    def sort_statecodeCSV_by_state_code_and_make_json(self):
        self.delegator.sort_statecodeCSV_by_state_code_and_make_json()

    # def __getattr__(self, func):
    #     def method(*args, **kwargs):
    #         if func in self.delegator_methods:
    #             return getattr(self.delegator, func)(*args, **kwargs)
    #         else:
    #             raise AttributeError

    #     return method
