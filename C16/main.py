import pandas
from pandas import DataFrame
import high_school_graduates_outcome as hsgo


def main():
    reporter = hsgo.HSGOReporter(
        'file.csv')

    building_name = reporter.greatest_number_of_records()
    print('Name of the school (and its achievement level) with the greatest number of records (NumRecords) is', building_name)

    school_and_achievement = reporter.sum_numrecords_for_highestachievement()
    print('The sum NumRecords for HighestAchievement of a "Bachelor\'s or Higher" using the DemographicGrouping "All Students" is ', school_and_achievement)

    median = reporter.median_medianearnings()
    print('The median of the median earnings among students who had a DemographicValue of FRPL and highest level of academic achievement as HS Diploma is ', median)

    difference = reporter.difference_in_earnings_among_male_and_female()
    print('The difference in highest MedianEarnings for students with Bachelor’s or Higher degree between Male and Female students is ', difference)

    districts_with_earnings_greater_than_median_household = reporter.districts_with_medianearnings_more_than_threshold()
    print('The district(s): ', districts_with_earnings_greater_than_median_household)


if __name__ == '__main__':
    main()
