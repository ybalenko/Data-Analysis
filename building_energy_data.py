import pandas
from pandas import DataFrame


class BuidingEnergyReporter:
    '''
    Before beginning to work on any of the following questions first exclude all rows where:
    * The ENERGYSTARScore is blank.
    * The YearBuilt is less than “1920”.
    * The BuildingName contains “CENTER”.

    QUESTIONS
    Question 1: What was the name of the building that had the largest NumberofFloors?  
    Question 2: How many buildings had an ENERGYSTARScore of at least 97?
    Question 3: What is the median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas?
    Question 4: Within the Ballard neighborhood, which buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018?
    Question 5: Which properties have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals?
    '''

    def __init__(self, filename):
        '''
        Reading initial dataset file and applying the prerequsites.
        '''
        self.original_dataset = pandas.read_csv(filename)
        # ENERGYSTARScore is NOT blank.
        score_not_blank = self.original_dataset['ENERGYSTARScore'].notnull()
        dataset = self.original_dataset[score_not_blank]
        # YearBuilt is greater 1920.
        year_filter = dataset['YearBuilt'] >= 1920
        dataset = dataset[year_filter]
        # BuildingName does NOT contain “CENTER”.
        name_filter = dataset['BuildingName'].str.contains(
            'CENTER', case=True, regex=False)
        invertion = name_filter == False
        self.dataset = dataset[invertion]

    def max_number_of_floors(self):
        '''
        Applying the filter to answer the question #1 "What was the name of the building that had the largest NumberofFloors?".
        '''
        max_floors_filter = self.dataset['NumberofFloors'] == self.dataset['NumberofFloors'].max(
        )
        filtered_dataset = self.dataset[max_floors_filter]
        building_name = filtered_dataset.iloc[0]['BuildingName']
        return building_name

    def energy_score_buildings(self, threshold: int):
        '''
        Applying the filter to answer the question #2 "How many buildings had an ENERGYSTARScore of at least 97?".
        '''
        energy_filter = self.dataset['ENERGYSTARScore'] >= threshold
        energy_filtered_buildings = self.dataset[energy_filter]
        return energy_filtered_buildings

    def median_SiteEUI_gas(self):
        '''
        Applying the filter to answer the question #3
        "What is the median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas?".
        '''
        gas_filter_not_zero = self.dataset['NaturalGas(therms)'] != 0
        gas_filtered_buildings = self.dataset[gas_filter_not_zero]
        gas_filter_not_blank = gas_filtered_buildings['NaturalGas(kBtu)'].notnull(
        )
        gas_filtered_buildings = gas_filtered_buildings[gas_filter_not_blank]
        energy_use_index_median = gas_filtered_buildings['SiteEUI(kBtu/sf)'].median(
        )
        return energy_use_index_median

    def ballard_building_used_electricity_more_threshold(self):
        '''
        Applying the filter to answer the question #4
        "Within the Ballard neighborhood, which buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018?".
        '''
        find_biomed_filter = self.original_dataset['BuildingName'] == 'BIOMED FAIRVIEW RESEARCH CENTER'
        filtered_by_biomed = self.original_dataset[find_biomed_filter]
        row = filtered_by_biomed.iloc[0]
        threshold = row['Electricity(kWh)']
        ballard_neighborhood_filter = self.dataset['Neighborhood'] == 'BALLARD'
        filtered_by_ballard_neighborhood = self.dataset[ballard_neighborhood_filter]
        neighborhood_electricity_filter = filtered_by_ballard_neighborhood[
            'Electricity(kWh)'] > threshold
        filtered_by_neighborhood_electricity = filtered_by_ballard_neighborhood[
            neighborhood_electricity_filter]
        return filtered_by_neighborhood_electricity['BuildingName']

    def buildings_floor_area_more_15_NFL(self):
        '''
        Applying the filter to answer the question #5
        "Which properties have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals?".
        '''
        area_filter = self.dataset['PropertyGFATotal'] > 864000
        filtered_by_area = self.dataset[area_filter]
        property_type_filter = filtered_by_area['PrimaryPropertyType'] != 'Office'
        filtered_by_property = filtered_by_area[property_type_filter]
        property_type_filter = filtered_by_property[
            'PrimaryPropertyType'] != 'Hospital (General Medical & Surgical)'
        filtered_by_property = filtered_by_property[property_type_filter]
        return filtered_by_property['BuildingName']
