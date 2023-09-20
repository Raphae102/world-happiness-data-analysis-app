import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="centered")

st.title("In Search for Happiness")
x_axis = st.selectbox("Select the data for X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for Y-axis", ("GDP", "Happiness", "Generosity"))

# load the data
df = pd.read_csv("happy.csv")

# match the value of the first option
match x_axis:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]

# match the value of the second option
match y_axis:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

# a sub_header above the plot
st.subheader(f"{x_axis} and {y_axis}")

#
figure = px.scatter(x=x_array, y=y_array,
                    labels={"x": x_axis, "y": y_axis})
st.plotly_chart(figure)
