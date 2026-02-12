📊 Sales Data Analysis Dashboard using Streamlit

An interactive and fully functional Sales Data Analysis Dashboard built using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

This project transforms raw sales data into meaningful business insights through interactive visualizations and filters in a browser-based dashboard.

🚀 Project Overview

The Sales Dashboard allows users to:

📍 Analyze Region-wise Sales

📦 Compare Category-wise Performance

📅 View Monthly Sales Trends

💰 Analyze Profit Distribution

📊 Visualize Sales using interactive charts

🔎 Filter data dynamically

The dashboard runs completely in the browser using Streamlit.

🛠️ Tech Stack

Python

Pandas – Data cleaning & aggregation

Matplotlib – Data visualization

Seaborn – Statistical visualization

Streamlit – Web application framework

📂 Project Structure
sales-dashboard/
│
├── app.py                 # Main Streamlit dashboard
├── sales_data.csv         # Dataset used for analysis
├── requirements.txt       # Required Python libraries
└── README.md              # Project documentation

📈 Dashboard Features
1️⃣ Region-wise Sales Analysis

Bar chart showing total sales across different regions.

2️⃣ Category-wise Sales Comparison

Visual comparison of product categories.

3️⃣ Monthly Sales Trend

Line chart showing sales growth over time.

4️⃣ Profit Analysis

Profit distribution across segments/categories.

5️⃣ Interactive Filters

Users can:

Select specific regions

Filter by product category

Dynamically update visualizations

▶️ How to Run This Project
Step 1: Clone the Repository
git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard

Step 2: Install Required Libraries
pip install -r requirements.txt


Or manually install:

pip install streamlit pandas matplotlib seaborn

Step 3: Run the Streamlit Application
streamlit run app.py


After running the command, the dashboard will automatically open in your browser at:

http://localhost:8501

📊 Example Insights Generated

Identify highest performing region

Compare sales between categories

Track monthly growth patterns

Analyze profit contribution

Detect sales distribution trends

🎯 Learning Outcomes

Through this project, I learned:

Data preprocessing and cleaning using Pandas

GroupBy operations and aggregations

Creating visualizations using Matplotlib & Seaborn

Building interactive dashboards using Streamlit

Deploying browser-based data applications

🌍 Future Enhancements

Add KPI Cards (Total Sales, Total Profit, Growth %)

Add CSV download option

Add advanced filtering options

Add Sales Forecasting using Machine Learning

Deploy on Streamlit Cloud

Add authentication and multi-user access
