import pandas as pd
import matplotlib.pyplot as plt

weather_df = pd.read_csv("../data/weather_data.csv")
print(weather_df.head())

weather = {
    "temp": [55, 34, 80, 75, 53],
    "weather": ["windy", "cloudy", "sunny", "rain", "sunny"],
}

df_weather = pd.DataFrame.from_dict(weather)
print(df_weather)

df_weather["weather_encoded"] = df_weather["weather"].map(
    {"windy": 0, "cloudy": 1, "sunny": 2, "rain": 3}
)
print(df_weather)

print(pd.get_dummies(weather_df["weather"]))

# plot: pie chart
weather_df["weather"].value_counts().plot.pie(autopct="%1.1f%%")
plt.ylabel("")
plt.show()
# plot: bar chart
weather_df["weather"].value_counts().plot.bar()
plt.show()


# city-weather
city_weather = (
    weather_df.groupby(["weather", "city"])["weather"].count().unstack("city")
)
city_weather = city_weather.fillna(0)
print(f"\n{city_weather}")

# plot
city_weather.plot(kind="bar", stacked=True)
plt.show()

student = {
    "name": ["Alice", "Bob", "Carol", "Dan", "Eli", "Fran"],
    "sex": ["female", "male", "female", "male", "male", "female"],
    "class": ["FY", "SO", "SR", "SO", "JR", "SR"],
    "gpa": [90, 93, 97, 89, 95, 92],
    "num_classes": [4, 3, 4, 4, 3, 2],
}

student_df = pd.DataFrame.from_dict(student)
print(student_df)

# as sex is categorical attribute, values can be binary
student_df["female_flag"] = student_df["sex"] == "female"
student_df.drop("sex", axis=1, inplace=True)
print(f"\n{student_df}")
