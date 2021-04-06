import pandas
from pandas import DataFrame


class HSGOReporter:
    """
    BEFORE YOU BEGIN
    Before beginning first include only rows where:

    1. The DistrictTTL is equal to any of the following:
       - “Seattle Public Schools”,
       - “Lake Washington School District”
       - “Bellevue School District”
       - “Mercer Island School District”
       - “Renton School District”
    2. The YearAfterGrad is greater than or equal to 7.
    3. The SchoolTTL does not contain the word “District”

     """

    def __init__(self, filename):
        """
        Reading initial dataset file and applying the prerequsites.
        """
        self.original_dataset = pandas.read_csv(filename)

        """
        DistrictTTL equals to “Seattle Public Schools”, “Lake Washington School District”,
        “Bellevue School District”, “Mercer Island School District”, “Renton School District”
        """
        specific_district_ttl = self.original_dataset['DistrictTTL'].str.contains(
            'Seattle Public Schools|Lake Washington School District|Bellevue School District|Mercer Island School District|Renton School District', regex=True)
        dataset = self.original_dataset[specific_district_ttl]

        """
        The YearAfterGrad is greater than or equal to 7
        """
        year_filter = dataset['YearAfterGrad'] >= 7
        dataset = dataset[year_filter]

        """
        The SchoolTTL does not contain the word “District”
        """
        name_filter = dataset['SchoolTTL'].str.contains(
            'District', case=True, regex=False)
        invertion = name_filter == False
        self.dataset = dataset[invertion]

    # Question1: What is the school (SchoolTTL) and achievement level (HighestAchievement) with the greatest number of records(NumRecords)?

    def greatest_number_of_records(self):
        max_number_of_records_filter = self.dataset['NumRecords'] == self.dataset['NumRecords'].max(
        )
        filtered_dataset = self.dataset[max_number_of_records_filter]
        school_name = filtered_dataset.iloc[0]['SchoolTTL']
        achievement = filtered_dataset.iloc[0]['HighestAchievement']
        return school_name, achievement

    # Question 2: What is the sum NumRecords for HighestAchievement of a "Bachelor's or Higher" using the DemographicGrouping "All Students"?

    def sum_numrecords_for_highestachievement(self):
        all_students = self.dataset['DemographicGrouping'].str.contains(
            'All Students', case=True, regex=False)
        filtered_dataset_all_students = self.dataset[all_students]

        highest_achievement_all_students = filtered_dataset_all_students['HighestAchievement'].str.contains(
            "Bachelor's or Higher", case=True, regex=False)
        filtered_dataset_all_students_bachelors = filtered_dataset_all_students[
            highest_achievement_all_students]
        numrecords_sum = filtered_dataset_all_students_bachelors['NumRecords'].sum(
        )
        return numrecords_sum

    # Question 3: What is the median of the median earnings (the MedianEarnings column) among students who had a DemographicValue of Free or Reduced Price Lunch status ("FRPL") and who’s highest level of academic achievement was "HS Diploma"?

    def median_medianearnings(self):
        demographic_value_frpl = self.dataset['DemographicValue'] == 'FRPL'
        filtered_dataset_by_frpl = self.dataset[demographic_value_frpl]
        students_with_hs_diploma = filtered_dataset_by_frpl['HighestAchievement'].str.contains(
            'HS Diploma', case=True, regex=False)
        filtered_dataset_by_frpl_and_diploma = filtered_dataset_by_frpl[students_with_hs_diploma]
        median = filtered_dataset_by_frpl_and_diploma['MedianEarnings'].median(
        )
        return median

    # Question 4: What is the difference in highest MedianEarnings for students with the highest achievement of "Bachelor’s or Higher" between "Male" and "Female" students?

    def difference_in_earnings_among_male_and_female(self):
        demographic_value_male = self.dataset['DemographicValue'] == 'Male'
        filtered_dataset_men = self.dataset[demographic_value_male]
        men_with_bachelor = filtered_dataset_men['HighestAchievement'].str.contains(
            "Bachelor", case=True, regex=False)
        filtered_dataset_by_men_and_diploma = filtered_dataset_men[men_with_bachelor]

        men_with_highest_earnings = filtered_dataset_by_men_and_diploma[
            'MedianEarnings'] == filtered_dataset_by_men_and_diploma['MedianEarnings'].max()
        filtered_dataset_by_men_and_diploma_earnings = filtered_dataset_by_men_and_diploma[
            men_with_highest_earnings]
        highest_earning_m = filtered_dataset_by_men_and_diploma_earnings.iloc[
            0]['MedianEarnings']

        demographic_value_female = self.dataset['DemographicValue'] == 'Female'
        filtered_dataset_women = self.dataset[demographic_value_female]

        women_with_bachelor = filtered_dataset_women['HighestAchievement'].str.contains(
            "Bachelor", case=True, regex=False)
        filtered_dataset_by_women_and_diploma = filtered_dataset_women[women_with_bachelor]

        women_with_highest_earnings = filtered_dataset_by_women_and_diploma[
            'MedianEarnings'] == filtered_dataset_by_women_and_diploma['MedianEarnings'].max()
        filtered_dataset_by_women_and_diploma_earnings = filtered_dataset_by_women_and_diploma[
            women_with_highest_earnings]
        highest_earning_w = filtered_dataset_by_women_and_diploma_earnings.iloc[
            0]['MedianEarnings']

        difference = int(highest_earning_m) - int(highest_earning_w)
        return abs(difference)

    # Question 5: What school districts had students that had higher MedianEarnings than the "Median household income (in 2019 dollars), 2015-2019 in Washington State according to the US Census Bureau"?

    def districts_with_medianearnings_more_than_threshold(self):
        threshold = 73775
        earnings_more_than_threshold = self.dataset['MedianEarnings'] > threshold
        dataset = self.dataset[earnings_more_than_threshold]
        res = dataset['DistrictTTL'].unique()
        return res
