import pandas
from pandas import DataFrame
import building_energy_data as bed


def main():
    reporter = bed.BuidingEnergyReporter('file.csv')

# Q1: What was the name of the building that had the largest NumberofFloors?
    building_name = reporter.max_number_of_floors()
    print('Question 1: Name of the building that had the largest NumberOfFloors', building_name)

# Q2: How many buildings had an ENERGYSTARScore of at least 97?
    buildings_with_energyscore = reporter.energy_score_buildings(97)
    total_rows = len(buildings_with_energyscore.index)
    print('Question 2: There are', total_rows,
          'buildings that had an ENERGYSTARScore of at least 97')

# Q3: What is the median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas?
    median = reporter.median_SiteEUI_gas()
    print('Question 3: The median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas is', median)


# Q4: Within the Ballard neighborhood, which buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018?
    electricity = reporter.ballard_building_used_electricity_more_threshold()
    print('Question 4: The following buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018 within the Ballard neighborhood: \n', electricity)

# Q5: Which properties have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals?
    not_offices_not_hospitals_more_15_NFL = reporter.buildings_floor_area_more_15_NFL()
    print('Question 5: The properties that have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals: ',
          not_offices_not_hospitals_more_15_NFL)


if __name__ == '__main__':
    main()
