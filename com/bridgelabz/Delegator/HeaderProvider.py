class IndiaCensusCSV:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "AreaInSqKm"
        self.density = "DensityPerSqKm"

    def __repr__(self):
        return self.state + "," + self.population + "," + self.area + "," + self.density


class StateCodeCSV:
    def __init__(self):
        self.srno = "SrNo"
        self.state_name = "State Name"
        self.tin = "TIN"
        self.statecode = "StateCode"

    def __repr__(self):
        return f"{self.srno},{self.state_name},{self.tin},{self.statecode}"