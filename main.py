import pandas
from pandas import DataFrame
import building_energy_data as bed


def main():
    reporter = bed.BuidingEnergyReporter('file.csv')


# Q1
    building_name = reporter.max_number_of_floors()
    print('Name of the building that had the largest NumberOfFloors', building_name)

# Q2
    buildings_with_energyscore = reporter.energy_score_buildings(97)
    total_rows = len(buildings_with_energyscore.index)
    print('There are', total_rows,
          'buildings that had an ENERGYSTARScore of at least 97')

# Q3
    median = reporter.median_SiteEUI_gas()
    print('The median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas is', median)

    # The median
    # is also the number that is halfway into the set. To find the median, the data should be arranged in order from least to greatest.
    # If there is an even number of items in the data set, then the median is found by taking the mean (average) of the two middlemost numbers.
    # Example1: The median of 4, 1, and 7 is 4 because when the numbers are put in order (1 , 4, 7) , the number 4 is in the middle.
    # Example2: 1, 4, 6, 8 -> (4+6)/2 = 5

    # 1. Find buildings that used natural gas -> NaturalGas(therms) NOT 0 and NOT NaN
    # 2. Count median for SiteEUI(kBtu/sf):
    #  2.1 sort from least to greatest;
    #  2.2 define whether the even or odd
    #  2.3 if odd - > Example1 2.4 if even -> Example2

# Q4

    electricity = reporter.ballard_building_used_electricity_more_threshold()
    print('The following buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018 within the Ballard neighborhood: \n', electricity)

# Q5
    not_offices_not_hospitals_more_15_NFL = reporter.buildings_floor_area_more_15_NFL()
    print('The properties that have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals: ',
          not_offices_not_hospitals_more_15_NFL)
    # 1 Find out size of a football field (NFL) and miltiply by 15   --> the total area of an American football field is 57,600 square feet ->  864,000.0
    # 2 Find out column name for property gross floor area -> PropertyGFATotal
    # 3 Filter dataset by larger property gross floor area > 15NFL
    # 4 Find out column name for offices and hospitals  -> PrimaryPropertyType
    # 5 Values: Office; Hospital (General Medical & Surgical)  -> Medical Office???
    # 6 Filter dataset#2  = NOT offices NOT hospitals


if __name__ == '__main__':
    main()
