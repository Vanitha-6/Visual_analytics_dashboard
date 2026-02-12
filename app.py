import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("📊 Sales Analytics Dashboard")
st.markdown("Region-Wise Sales and Customer Insights")

# Load Dataset
df = pd.read_csv("C:\\Users\\Vanitha_V\\Downloads\\Data_Analytics\\Sample - Superstore.csv", encoding='latin1')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

df_filtered = df[
    (df['Region'].isin(region_filter)) &
    (df['Category'].isin(category_filter))
]

# KPI Section
total_sales = df_filtered['Sales'].sum()
total_profit = df_filtered['Profit'].sum()
total_orders = df_filtered['Order ID'].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

st.markdown("---")

# Region-wise Sales
region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
fig1 = px.bar(region_sales, x='Region', y='Sales',
              title="Region-wise Sales",
              color='Region')
st.plotly_chart(fig1, use_container_width=True)

# Monthly Sales Trend
df_filtered['Month'] = df_filtered['Order Date'].dt.to_period('M').astype(str)
monthly_sales = df_filtered.groupby('Month')['Sales'].sum().reset_index()

fig2 = px.line(monthly_sales, x='Month', y='Sales',
               title="Monthly Sales Trend")
st.plotly_chart(fig2, use_container_width=True)

# Category-wise Sales
category_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index()
fig3 = px.pie(category_sales, names='Category', values='Sales',
              title="Category-wise Sales Distribution")
st.plotly_chart(fig3, use_container_width=True)

# Top 10 Customers
top_customers = df_filtered.groupby('Customer Name')['Sales'].sum() \
    .sort_values(ascending=False).head(10).reset_index()

fig4 = px.bar(top_customers,
              x='Customer Name',
              y='Sales',
              title="Top 10 Customers",
              color='Sales')

st.plotly_chart(fig4, use_container_width=True)

