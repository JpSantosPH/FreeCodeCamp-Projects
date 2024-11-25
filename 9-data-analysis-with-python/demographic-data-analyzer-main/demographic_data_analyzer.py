import pandas as pd

def calculate_percentage(series, data):
    if data not in series.values:
        return 0
    counts = series.value_counts()
    return (counts[data]/counts.sum() * 100).round(1)

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('9-data-analysis-with-python\\demographic-data-analyzer-main\\adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df['age'][df['sex'] == 'Male'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = calculate_percentage(df['education'], 'Bachelors')

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    has_higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[has_higher_education]
    lower_education = df[~has_higher_education]

    # percentage with salary >50K
    higher_education_rich = calculate_percentage(higher_education['salary'], '>50K')
    lower_education_rich = calculate_percentage(lower_education['salary'], '>50K')

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = calculate_percentage(min_workers['salary'], '>50K')

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df['native-country'][df['salary'] == '>50K'].value_counts()
    country_rich_percentages = (country_rich_counts/country_counts*100).round(1)

    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = country_rich_percentages.max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df['occupation'][df['native-country'] == 'India'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }