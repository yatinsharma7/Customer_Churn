
import csv
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv("//opt/predict/data/Customer_Data2.csv")
a="//opt/predict/data/"

def plot1(a):
    plot1 = sb.boxplot(x="Churn", y="tenure", data=df)
    fig1 = plot1.get_figure()
    fig1.savefig(a+"plot1.png")

def plot2(a):
    plot2 = sb.countplot(x="PaymentMethod", data=df)
    fig2 = plot2.get_figure()
    fig2.savefig(a+"plot2.png")

def plot3(a):
    plot3 = sb.FacetGrid(df, col="gender", row="PhoneService", margin_titles=True)
    plot3.savefig(a+"plot3.png")
    b=plot3.map(sb.plt.scatter, "MonthlyCharges","tenure")
    b.savefig(a+"plot3.png")
def plot4(a):
    Numeric_Data =df[["tenure","MonthlyCharges","TotalCharges"]]
    plot4 = sb.pairplot(Numeric_Data,palette='paired')
    plot4.savefig(a+"plot4.png")



plot1(a)
plot2(a)
plot3(a)
plot4(a)
