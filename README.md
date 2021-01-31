# Data-Analysis

This [repository](https://github.com/ybalenko/Data-Analysis) contains samples of data analysis using **Python** and **Pandas** [1] in particular. You've got the dataset which should be transformed and after that you should apply filters to answer the questions.
The dataset, in CSV format was downloaded from [here](https://data.seattle.gov/dataset/2018-Building-Energy-Benchmarking/7rac-kyay). 

>   ```
>   Before beginning it is the requirement to exclude all rows where:
>   * The ENERGYSTARScore is blank.
>   * The YearBuilt is less than “1920”.
>   * The BuildingName contains “CENTER”.
>   
>   QUESTIONS:
>   1. What was the name of the building that had the largest NumberofFloors? 
>   2. How many buildings had an ENERGYSTARScore of at least 97?
>   3. What is the median of the Site Energy Use Index (the SiteEUI(kBtu/sf) column) among all buildings that used natural gas?
>   4. Within the Ballard neighborhood, which buildings used more electricity than BIOMED FAIRVIEW RESEARCH CENTER in 2018?
>   5. Which properties have a larger property gross floor area for their buildings greater than 15 football fields (NFL) and are not offices or hospitals?
>   ```

*NOTES*:

[1] [Pandas]( https://www.python.org) is an open source data analysis and manipulation tool, built on top of the Python programming language.
