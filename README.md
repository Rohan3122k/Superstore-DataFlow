
# Superstore DataFlow: End-to-End ETL Project Using PostgreSQL & Power BI

**Project by:** Rohan Verma  
**GitHub Repository:** [Your Repository URL]

---

## Description  
This repository contains a complete data engineering pipeline that ingests, transforms, validates, and automates processing of Superstore sales data using PostgreSQL and Python, with a Power BI dashboard layered on top for real-time analytics. It simulates a production-ready ETL workflow suitable for supply chain analytics, sales forecasting, and inventory optimization. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## Tech Stack  
- **Database:** PostgreSQL  
- **Scripting:** Python (Pandas, SQLAlchemy)  
- **Automation:** Windows Task Scheduler  
- **Visualization:** Power BI  
- **Version Control:** Git / GitHub

---

## Features  
- **Raw Data Ingestion:** Load cleaned CSV into `sales_raw`.  
- **Transformation:** Aggregate monthly metrics into `sales_summary`.  
- **Data Quality:** Automated checks for nulls, duplicates, and value ranges.  
- **Automation:** Daily ETL run via Windows Task Scheduler at 2 AM.  
- **Dashboard:** Interactive Power BI report with key sales and profit visuals.

---

## Table of Contents  
1. [Prerequisites](#prerequisites)  
2. [Installation & Setup](#installation--setup)  
3. [Running the ETL Pipeline](#running-the-etl-pipeline)  
4. [Project Structure](#project-structure)  
5. [Scripts Overview](#scripts-overview)  
6. [Power BI Dashboard](#power bi-dashboard)  
7. [Contributing](#contributing)  
8. [License](#license)

---

## Prerequisites  
- Python 3.8+  
- PostgreSQL 17 (or compatible)  
- Power BI Desktop  
- Windows (for Task Scheduler automation)  

---

## Installation & Setup  
1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
````

2. **Create and configure PostgreSQL database**

   ```sql
   -- In psql or pgAdmin:
   CREATE DATABASE etl_demo;
   CREATE USER etl_user1 WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE etl_demo TO etl_user1;
   ```
3. **Install Python dependencies**

   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```
4. **Place the cleaned Superstore CSV**

   ```text
   week1/data/superstore_clean.csv
   ```

---

## Running the ETL Pipeline

1. **Load raw data**

   ```bash
   python scripts/load_raw.py
   ```
2. **Transform & summarize**

   ```bash
   python scripts/transform_summary.py
   ```
3. **Run data quality checks**

   ```bash
   python scripts/quality_checks.py
   ```
4. **Run full pipeline**

   ```bash
   python scripts/run_etl.py
   ```
5. **Automate daily runs**

   * Open **Task Scheduler** → **Create Task**
   * Name: `Superstore ETL`
   * Trigger: Daily at 2:00 AM
   * Action: `python C:\path\to\run_etl.py`

---

## Project Structure

```
week1/
├── data/
│   └── superstore_clean.csv
├── scripts/
│   ├── load_raw.py          # Extract & Load
│   ├── transform_summary.py # Transform & aggregate
│   ├── quality_checks.py    # Data validation
│   ├── notify.py            # (Optional) Alerts on failure
│   └── run_etl.py           # Wrapper to run all steps
├── screenshots/             # pgAdmin & Task Scheduler images
└── README.md
```

---

## Scripts Overview

* **load\_raw\.py**

  * Reads CSV
  * Truncates & loads into `sales_raw` (9994 rows)
* **transform\_summary.py**

  * Extracts `year`, `month`
  * Aggregates metrics: `total_sales`, `avg_discount`, `total_profit`
  * Loads into `sales_summary`
* **quality\_checks.py**

  * Verifies: no nulls/duplicates, `sales ≥ 0`, `0 ≤ discount ≤ 1`, non-empty summary
* **run\_etl.py**

  * Executes the above three scripts in sequence

---

## Power BI Dashboard

1. **Connecting**

   * **Get Data → PostgreSQL**
   * Server: `127.0.0.1`, Database: `etl_demo`
   * Auth: `etl_user1` / `your_password`&#x20;
2. **Key Visuals**

   * **Monthly Sales Trend:** Line chart of `total_sales` by month
   * **Regional Comparison:** Clustered bar of sales, orders, profit by region
   * **Profit Heatmap:** Filled map of `total_profit` by state
   * **Category & Discount:** Donut chart showing order count by category and discount brackets
3. **Styling**

   * Corporate blue theme, dark page background
   * Date & region slicers for interactive filtering
4. **Export**

   * Save as `Superstore_Dashboard.pbit` for inclusion in repo

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add new ETL step'`
4. Push branch: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**Rohan Verma**
Graduate Student, Data Analytics Engineering
Northeastern University

```

Feel free to copy–paste this `README.md` directly into your repository.
```


