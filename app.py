import streamlit as st
import pandas as pd

st.set_page_config(page_title="Project Dashboard", layout="wide")
st.title("📊 Project Dashboard with Filters")

# -----------------------------
# Load data
# -----------------------------
df = pd.read_excel("data.xlsx")
df["date"] = pd.to_datetime(df["date"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

# District filter
district_filter = st.sidebar.selectbox(
    "Select District", options=["All"] + df["district"].unique().tolist()
)

# Activity filter
activity_filter = st.sidebar.selectbox(
    "Select Activity", options=["All"] + df["activity"].unique().tolist()
)

# Status filter
status_filter = st.sidebar.selectbox(
    "Select Status", options=["All"] + df["status"].unique().tolist()
)

# Date range filter
date_min = df["date"].min()
date_max = df["date"].max()
date_filter = st.sidebar.date_input(
    "Select Date Range", value=(date_min, date_max)
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df.copy()

if district_filter != "All":
    filtered_df = filtered_df[filtered_df["district"] == district_filter]

if activity_filter != "All":
    filtered_df = filtered_df[filtered_df["activity"] == activity_filter]

if status_filter != "All":
    filtered_df = filtered_df[filtered_df["status"] == status_filter]

filtered_df = filtered_df[
    (filtered_df["date"] >= pd.to_datetime(date_filter[0])) &
    (filtered_df["date"] <= pd.to_datetime(date_filter[1]))
]

# -----------------------------
# Display Table
# -----------------------------
st.subheader("📄 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# Optional: Download filtered data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    "⬇️ Download Filtered Data",
    data=csv,
    file_name="filtered_data.csv",
    mime="text/csv"
)
