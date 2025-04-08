import pandas as pd
import sqlite3

conn = sqlite3.connect("chinook.db")
query = """
    SELECT customers.CustomerId, customers.FirstName, customers.LastName, COUNT(invoices.InvoiceId) AS TotalInvoices
    FROM customers
    INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
    GROUP BY customers.CustomerId
"""
df_inner_join = pd.read_sql_query(query, conn)
print("Inner Join (Chinook) Result:")
print(df_inner_join.head())

df_movie = pd.read_csv("movie.csv")
df_director_color = df_movie[["director_name", "color"]]
df_director_reviews = df_movie[["director_name", "num_critic_for_reviews"]]

df_left_join = pd.merge(
    df_director_color, df_director_reviews, on="director_name", how="left"
)
df_full_outer_join = pd.merge(
    df_director_color, df_director_reviews, on="director_name", how="outer"
)

print("\nOuter Join (Movie) Row Counts:")
print("Left Join Rows:", len(df_left_join))
print("Full Outer Join Rows:", len(df_full_outer_join))

df_titanic = pd.read_excel("titanic.xlsx")
df_grouped = (
    df_titanic.groupby("Pclass")
    .agg({"Age": "mean", "Fare": "sum", "PassengerId": "count"})
    .rename(
        columns={
            "Age": "AverageAge",
            "Fare": "TotalFare",
            "PassengerId": "PassengerCount",
        }
    )
    .reset_index()
)
print("\nGrouped Titanic Data:")
print(df_grouped)

df_multi_grouped = (
    df_movie.groupby(["color", "director_name"])
    .agg({"num_critic_for_reviews": "sum", "duration": "mean"})
    .reset_index()
)
print("\nMulti-level Grouped (Movie):")
print(df_multi_grouped.head())


def classify_age(age):
    return "Child" if age < 18 else "Adult"


df_titanic["Age_Group"] = df_titanic["Age"].apply(classify_age)
print("\nTitanic Age Group Example:")
print(df_titanic[["Age", "Age_Group"]].head())

df_employee = pd.read_csv("employee.csv")
df_employee["NormalizedSalary"] = df_employee.groupby("DEPARTMENT")["BASE_SALARY"].transform(
    lambda x: (x - x.mean()) / x.std()
)
print("\nNormalized Employee Salaries:")
print(df_employee.head())


def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"


df_movie["Duration_Class"] = df_movie["duration"].apply(classify_duration)
print("\nMovie Duration Classification:")
print(df_movie[["duration", "Duration_Class"]].head())


def pipeline_titanic(df):
    df = df[df["Survived"] == 1].copy()
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df


df_titanic_pipe = pipeline_titanic(df_titanic)
print("\nTitanic Pipeline Result:")
print(df_titanic_pipe[["Survived", "Age", "Fare_Per_Age"]].head())
