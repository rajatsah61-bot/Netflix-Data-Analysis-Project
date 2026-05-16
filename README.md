# 📺 Netflix Data Analysis Project

This project focuses on analyzing Netflix content data using **Python, SQL, and Power BI**. The dataset was cleaned, transformed, and analyzed to discover insights about Netflix movies and TV shows, including trends, content distribution, ratings, and durations.

---

# 📌 Project Objectives

- Clean and preprocess raw Netflix dataset
- Perform exploratory data analysis (EDA)
- Run SQL queries using SQLite
- Generate business insights from the dataset
- Build an interactive Power BI dashboard

---

# 📂 Folder Structure

```bash
netflix-data-analysis/
│
├── data/
│   ├── netflix_titles.xlsx        # Raw Netflix dataset
│   └── CLEANED_DATA.xlsx          # Cleaned dataset
│
├── scripts/
│   ├── clean.py                   # Data cleaning using Python
│   └── clean_using_sql.py         # SQL analysis using SQLite
│
├── database/
│   └── cleaned_data.db            # SQLite database file
│
├── dashboard/
│   └── netflix_dashboard.pbix     # Power BI dashboard
│
└── README.md                      # Project documentation
```

---

# 📊 Key Tasks Performed

## ✅ Data Cleaning
- Handled missing and null values
- Removed duplicate records
- Standardized columns such as:
  - `date_added`
  - `duration`
  - `release_year`
- Converted data types for accurate analysis

---

## ✅ SQL Data Analysis

Used **SQLite** with Python to perform SQL-based analysis.

### Queries Performed:
- Total number of Movies vs TV Shows
- Content added per year
- Top producing countries
- Most common genres
- Duration analysis by content type

---

## ✅ Exploratory Data Analysis (EDA)

Performed analysis using **Pandas** and **Matplotlib** to identify:
- Year-wise content growth
- Distribution of ratings
- Popular genres
- Country-wise content production
- Movie and TV Show trends

---

# 📈 Power BI Dashboard Features

The interactive dashboard includes:

- 🌍 Country-wise content distribution
- 📅 Yearly release trends
- 🎬 Movies vs TV Shows comparison
- ⏱ Duration analysis
- 🎭 Genre-based filtering
- 🔍 Interactive slicers and filters

---

# 🧰 Technologies Used

| Tool / Technology | Purpose |
|-------------------|---------|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation |
| Matplotlib | Data visualization |
| SQLite | SQL querying |
| Power BI | Dashboard creation |
| Excel | Dataset storage |

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/netflix-data-analysis.git
cd netflix-data-analysis
```

## 2️⃣ Install Required Libraries

```bash
pip install pandas matplotlib openpyxl
```

## 3️⃣ Run Data Cleaning Script

```bash
python scripts/clean.py
```

## 4️⃣ Run SQL Analysis Script

```bash
python scripts/clean_using_sql.py
```

## 5️⃣ Open Power BI Dashboard

Open the file:

```bash
dashboard/netflix_dashboard.pbix
```

using Power BI Desktop.

---

# 📌 Sample Insights

- Movies are more frequent than TV Shows on Netflix
- The USA contributes the highest amount of content
- Content addition increased rapidly after 2015
- Drama and Comedy are among the most common genres

---

# 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests.

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Author

Developed by **Sudarshan Kumar**
