**Superstore DataFlow: End-to-End ETL Project Analysis**

**Abstract**
This section concisely summarizes the project’s goals, technologies, and outcomes. It should clearly communicate to any reader:

* **Purpose**: Demonstrate a production‑style ETL pipeline on PostgreSQL and Power BI for the Superstore dataset.
* **Scope**: Ingest raw CSV, transform and aggregate data, perform quality checks, and automate daily updates.
* **Key Tools**: Python (Pandas, SQLAlchemy), PostgreSQL, Windows Task Scheduler, Power BI.
* **Business Value**: Real-time analytics for supply chain and sales teams to drive data‑backed decisions.

---

**1. Introduction**
Explain why this pipeline matters in a real‑world context:

* **Business Challenge**: Retail and supply chain operations rely on timely, accurate sales and inventory data. Manual updates lead to stale reports and poor forecasting.
* **Solution Overview**: An automated ETL flow that pulls raw sales data, processes it, ensures quality, and feeds into dashboards for instant insights.
* **Audience**: Data engineers, analysts, and stakeholders who need trustworthy, up‑to‑date metrics.

---

**2. Database & Schema Setup**
Detail how the PostgreSQL environment is prepared:

* **Database Creation**: `etl_demo` established on PostgreSQL 17.
* **User Roles & Permissions**: `etl_user1` granted rights on the `public` schema.
* **Schema Inventory**: Describe use of `information_schema.tables` to confirm presence of:

  * `sales_raw` (raw data landing).
  * `sales_summary` (transformed aggregates).

> *Figure*: pgAdmin screenshot of table list.

---

**3. Table Structure**
Outline the two core tables:

**3.1 sales\_raw**

* **Columns (21)** replicate the Superstore fields: Order ID, Order Date, Region, Product Category, Sales, Quantity, Discount, Profit, etc.
* **Data Types**: Mix of `TEXT`, `DATE`, `NUMERIC`, and integer fields.
* **Purpose**: Landing zone for untransformed CSV rows, preserving full granularity.

**3.2 sales\_summary**

* **Composite Key**: `(year, month)` derived from `order_date`.
* **Metrics**: `total_sales`, `avg_discount`, `total_profit`, `order_count`.
* **Goal**: Provide a summarized layer optimized for analytics and reporting.

---

**4. Data Ingestion using `load_raw.py`**
Walk through the Extract & Load script:

1. **Read CSV**: Load `superstore_clean.csv` via Pandas.
2. **Truncate Table**: Remove stale rows from `sales_raw`.
3. **Bulk Insert**: Use `df.to_sql(..., chunksize=1000, method='multi')` to push data efficiently.
4. **Validation**: Query `COUNT(*)` to confirm row count (\~9,994) and uniqueness of `order_id`.

> *Figure*: Console output of row count and duplicate check.

---

**5. Transformation Logic with `transform_summary.py`**
Explain the Transform step in detail:

1. **Load Raw Data**: Read `sales_raw` into DataFrame.
2. **Derive Time Dimensions**: Extract `year` and `month` via `pd.to_datetime`.
3. **Aggregation**: Group by `(year, month)` and calculate:

   * `total_sales = sum(sales)`
   * `avg_discount = mean(discount)`
   * `total_profit = sum(profit)`
   * `order_count = count(order_id)`
4. **Upsert**: Replace contents of `sales_summary` with new aggregates.

> *Figure*: Preview of aggregated DataFrame and pgAdmin view.

---

**6. Data Quality Checks: `quality_checks.py`**
Describe each validation rule:

* **Null Checks**: No missing `order_id` or critical fields.
* **Uniqueness**: `order_id` must be distinct in `sales_raw`.
* **Value Bounds**: `sales ≥ 0`, `0 ≤ discount ≤ 1` to catch negative or out‑of‑range entries.
* **Summary Non-Empty**: `sales_summary` should contain at least one row.
* **Output**: Script prints "All data quality checks passed" or details failing checks.

---

**7. Advanced SQL Queries**
Highlight analytical queries used for deeper insights:

* **Profit by Region**: `SELECT region, SUM(profit) AS total_profit, AVG(profit) AS avg_profit FROM sales_raw GROUP BY region;`
* **Sales by Shipping Mode**: `SELECT ship_mode, SUM(sales) FROM sales_raw GROUP BY ship_mode;`
* **Use Cases**: These can power specialized dashboard tabs or ad‑hoc queries for logistics and marketing teams.

> *Figure*: Query outputs in pgAdmin.

---

**8. Automation using Windows Task Scheduler**
Explain the scheduling setup:

* **Task Name**: "Superstore ETL".
* **Trigger**: Daily at 2:00 AM local time.
* **Action**: Run `python run_etl.py` (which invokes all three scripts: load, transform, quality).
* **Monitoring**: Task history logged successes and failures for audit.

> *Figure*: Task Scheduler screenshot showing next run and last status.

---

**9. Project Structure**
Map the repository layout to guide collaborators:

```
week1/
├─ data/superstore_clean.csv
├─ scripts/
│  ├─ load_raw.py
│  ├─ transform_summary.py
│  ├─ quality_checks.py
│  ├─ notify.py (email/SMS alerts on failures)
│  └─ run_etl.py (wrapper)
├─ screenshots/ (pgAdmin & Task Scheduler)
└─ README.md
```

---

**10. Dashboard Visualization with Power BI**
Detail the BI layer and visuals:

> *Connection*: Power BI Desktop → PostgreSQL (Server: `127.0.0.1`; DB: `etl_demo`; Credentials: `etl_user1`).

**10.1 Monthly Sales Trend**

* **Type**: Line chart, X=Month, Y=Sum of |total\_sales|.
* **Insight**: Seasonal patterns (holiday spikes), enabling inventory planning.

**10.2 Regional Performance Comparison**

* **Type**: Clustered bar chart with regions on X-axis and metrics (sales, profit, order\_count) as series.
* **Insight**: Quickly spot high-volume but low-margin regions.

**10.3 Profit Heatmap by State**

* **Type**: Filled map keyed by state, color intensity = total\_profit.
* **Insight**: Geographic hotspots for targeted promotions or logistics optimization.

**10.4 Category & Discount Distribution**

* **Type**: Donut chart showing order\_count by product category, with inner ring for discount tiers.
* **Insight**: Balance discount strategies across categories for revenue lift.

---

**11. Conclusion & Next Steps**
Summarize achievements and propose enhancements:

* **Achievements**: Fully automated ETL, robust data validation, interactive dashboard.
* **Business Impact**: Near real-time analytics for supply chain, sales forecasting, and profit monitoring.
* **Future Work**:

  1. **Real-time Streaming**: Incorporate Kafka or Change Data Capture for live updates.
  2. **Cloud Integration**: Migrate to cloud warehouses (e.g., AWS Redshift, Snowflake) for scalability.
  3. **Advanced Analytics**: Add machine learning forecasts and anomaly detection in Python or Power BI.




