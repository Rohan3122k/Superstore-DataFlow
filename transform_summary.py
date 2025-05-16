{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "356984a2-2eff-43fb-8809-c6bc1ace24eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ sales_summary updated:\n",
      "   year  month  total_sales  total_orders  avg_discount  total_profit\n",
      "0  2014      1     14236.90            32      0.126582       2450.18\n",
      "1  2014      2      4519.92            28      0.176087        862.30\n",
      "2  2014      3     55691.04            71      0.167516        498.72\n",
      "3  2014      4     28295.35            66      0.110000       3488.86\n",
      "4  2014      5     23648.28            69      0.155328       2738.74\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine, text\n",
    "from urllib.parse import quote_plus\n",
    "\n",
    "# ── CONFIG ──────────────────────────────────────────────────────────\n",
    "user     = 'etl_user1'\n",
    "password = quote_plus('3December2000@')  # encode '@' as '%40'\n",
    "host     = '127.0.0.1'\n",
    "port     = '5432'\n",
    "db       = 'etl_demo'\n",
    "\n",
    "engine = create_engine(\n",
    "    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'\n",
    ")\n",
    "\n",
    "# ── 1) Read raw data ─────────────────────────────────────────────────\n",
    "sql_raw = \"SELECT order_date, sales, discount, profit, order_id FROM public.sales_raw;\"\n",
    "df_raw = pd.read_sql(sql_raw, engine, parse_dates=['order_date'])\n",
    "\n",
    "# ── 2) Aggregate by year & month ────────────────────────────────────\n",
    "df_raw['year']  = df_raw['order_date'].dt.year\n",
    "df_raw['month'] = df_raw['order_date'].dt.month\n",
    "\n",
    "summary = (\n",
    "    df_raw\n",
    "    .groupby(['year','month'])\n",
    "    .agg(\n",
    "      total_sales   = ('sales',    'sum'),\n",
    "      total_orders  = ('order_id','nunique'),\n",
    "      avg_discount  = ('discount','mean'),\n",
    "      total_profit  = ('profit',   'sum')\n",
    "    )\n",
    "    .reset_index()\n",
    ")\n",
    "\n",
    "# ── 3) Write into sales_summary ─────────────────────────────────────\n",
    "with engine.begin() as conn:\n",
    "    # clear old data\n",
    "    conn.execute(text(\"TRUNCATE TABLE public.sales_summary;\"))\n",
    "    # bulk insert\n",
    "    summary.to_sql(\n",
    "        'sales_summary',\n",
    "        con=conn,\n",
    "        if_exists='append',\n",
    "        index=False,\n",
    "        method='multi'\n",
    "    )\n",
    "\n",
    "print(\"✅ sales_summary updated:\")\n",
    "print(summary.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52452ecf-3ac8-4099-a062-49627c8dd1a7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0695998b-6469-473f-9d23-bfb2e9b6d9f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
