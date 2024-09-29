import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    # print(df.head(10))
    # print(df.columns)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    # print(race_count)

    # What is the average age of men?
    # print(df['sex'].value_counts())
    male_sex = df[df["sex"] == "Male"]
    # print(male_sex.head(10))
    average_age_men = male_sex["age"].mean()
    # print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    # print(df[(df["education"] == "Bachelors")]['education'].count())
    # print(len(df))
    percentage_bachelors = (
        df[(df["education"] == "Bachelors")]["education"].count() / len(df)
    ) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # make_more_than_50k = df[df["salary"] == ">50K"]
    # print("making more than 50k", make_more_than_50k.shape)
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    # print("higher_education_count : ", higher_education["education"].count())
    # print("higher_education size : ", higher_education.size)
    # print("higher_education shape 0 : ", higher_education.shape)
    # print("total population : ", len(df))
    higher_education_make_more_than_50k = higher_education[
        higher_education["salary"] == ">50K"
    ]
    # print("making more than 50k count", higher_education_make_more_than_50k.count())
    # print("making more than 50k shape", higher_education_make_more_than_50k.shape)

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education_make_more_than_50k = lower_education[
        lower_education["salary"] == ">50K"
    ]

    # percentage with salary >50K
    higher_education_rich = (
        higher_education_make_more_than_50k.shape[0] / higher_education.shape[0]
    ) * 100
    lower_education_rich = (
        lower_education_make_more_than_50k.shape[0] / lower_education.shape[0]
    ) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = (
        num_min_workers[num_min_workers["salary"] == ">50K"].shape[0]
        / num_min_workers.shape[0]
    ) * 100

    # What country has the highest percentage of people that earn >50K?
    filter_salary_more_50K = df[df["salary"] == ">50K"]["native-country"].value_counts()
    # print(filter_salary_more_50K)
    # print(df["native-country"].value_counts())
    filter_by_country = df["native-country"].value_counts()
    highest_earning_percentage = (
        filter_salary_more_50K / df["native-country"].value_counts()
    ) * 100
    # print(highest_earning_percentage.sort_values(ascending=False).head(1))
    highest_earning_country = highest_earning_percentage.idxmax()
    highest_earning_country_percentage = round(highest_earning_percentage[highest_earning_country],2)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().idxmax()
    # .sort_values(ascending=False).index[0] # works
    # .index[0] #works
    # .idxmax() # works

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
