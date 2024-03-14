import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("main_data.csv")
st.title("Dashboard Bike Sharing")
def plot_monthly_counts(data):
    st.write("### Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=data, x="mnth", y="cnt", hue="yr", palette="viridis", marker="o", ax=ax)

    ax.set_ylabel("Jumlah")
    ax.set_xlabel("Bulan")
    ax.set_title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun")
    ax.legend(title="Tahun", loc="upper right")
    ax.set_xticks(data["mnth"])
    ax.set_xticklabels(data["mnth"])
    plt.tight_layout()
    
    st.pyplot(fig)

plot_monthly_counts(data)

def plot_casual_vs_registered(casual_year_counts, reg_year_counts):
    st.write("### Total Casual vs Total Registered by Year")
    fig, ax = plt.subplots(figsize=(8, 6))
    index = casual_year_counts["yr"]
    bar_width = 0.35

    p1 = ax.bar(index, casual_year_counts["total_casual"], bar_width, label="Total Casual", color="b")
    p2 = ax.bar(index + bar_width, reg_year_counts["total_registered"], bar_width, label="Total Registered", color="g")

    ax.set_xlabel("Year")
    ax.set_ylabel("Total Counts")
    ax.set_title("Total Casual vs Total Registered by Year")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(casual_year_counts["yr"])
    ax.legend()
    for p in p1 + p2:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 1, str(int(height)), ha="center")
    plt.tight_layout()
    
    st.pyplot(fig)

casual_year_counts = data.groupby("yr")["casual"].sum()
casual_year_counts = casual_year_counts.reset_index()
casual_year_counts.columns = ["yr", "total_casual"]
reg_year_counts = data.groupby("yr")["registered"].sum()
reg_year_counts = reg_year_counts.reset_index()
reg_year_counts.columns = ["yr", "total_registered"]
# Panggil fungsi plot_casual_vs_registered dengan menggunakan data yang telah Anda siapkan
plot_casual_vs_registered(casual_year_counts, reg_year_counts)

def plot_working_counts(working_counts):
    st.write("### Jumlah total sepeda yang disewakan berdasarkan hari kerja")
    fig, ax = plt.subplots()
    sns.barplot(data=working_counts, x="workingday", y="cnt", hue="yr", palette="viridis")
    ax.set_ylabel("Jumlah")
    ax.set_title("Jumlah total sepeda yang disewakan berdasarkan hari kerja")
    ax.legend(title="Tahun", loc="upper right")
    plt.tight_layout()
    
    st.pyplot(fig)

working_counts = data.groupby(by=["workingday","yr"]).agg({
    "cnt": "sum"
}).reset_index()
# Panggil fungsi plot_working_counts dengan menggunakan data yang telah Anda siapkan
plot_working_counts(working_counts)

def plot_regression(bike_day_df):
    st.write("### Analisis Regresi berdasarkan temperature yang dirasakan tubuh manusia")
    fig, ax = plt.subplots()
    sns.regplot(x=bike_day_df["atemp"], y=bike_day_df["cnt"], ax=ax)
    ax.set_title("Analisis Regresi berdasarkan temperature yang dirasakan tubuh manusia")
    ax.set_xlabel("Temperatur (Celcius)")
    ax.set_ylabel("Total Sepeda yang Disewakan")
    plt.tight_layout()
    
    st.pyplot(fig)

sns.regplot(x=data["temp"], y=data["cnt"])
plt.title("Analisis Regresi berdasarkan Temperatur")
plt.xlabel("Temperatur (Celcius)")
plt.ylabel("Total Sepeda yang Disewakan")
plt.show()
# Panggil fungsi plot_regression dengan menggunakan data yang telah Anda siapkan
plot_regression(data)

def plot_regression(bike_day_df):
    st.write("### Analisis Regresi berdasarkan temperature yang dirasakan tubuh manusia")
    fig, ax = plt.subplots()
    sns.regplot(x=bike_day_df["atemp"], y=bike_day_df["cnt"])
    plt.title("Analisis Regresi berdasarkan temperature yang dirasakan tubuh manusia")
    plt.xlabel("Temperatur (Celcius)")
    plt.ylabel("Total Sepeda yang Disewakan")
    plt.tight_layout()
    
    st.pyplot(fig)

sns.regplot(x=data["atemp"], y=data["cnt"])
plt.title("Analisis Regresi berdasarkan temperature yang dirasakan tubuh manusia")
plt.xlabel("Temperatur (Celcius)")
plt.ylabel("Total Sepeda yang Disewakan")
plt.show()
# Panggil fungsi plot_regression dengan menggunakan data yang telah Anda siapkan
plot_regression(data)

def plot_regression_humidity(bike_day_df):
    st.write("### Analisis Regresi berdasarkan kelembapan")
    fig, ax = plt.subplots()
    sns.regplot(x=bike_day_df["hum"], y=bike_day_df["cnt"])
    plt.title("Analisis Regresi berdasarkan kelembapan")
    plt.xlabel("Kelembapan")
    plt.ylabel("Total Sepeda yang Disewakan")
    plt.tight_layout()
    
    st.pyplot(fig)

sns.regplot(x=data["hum"], y=data["cnt"])
plt.title("Analisis Regresi berdasarkan kelembapan")
plt.xlabel("kelembapan")
plt.ylabel("Total Sepeda yang Disewakan")
plt.show()
# Panggil fungsi plot_regression_humidity dengan menggunakan data yang telah Anda siapkan
plot_regression_humidity(data)