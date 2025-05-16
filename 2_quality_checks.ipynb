{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c1ccb8e6-df54-475c-9f5e-ddf5dce65452",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ sales_raw quality checks passed\n",
      "✅ sales_summary quality checks passed\n",
      "🎉 All data quality checks passed\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "from urllib.parse import quote_plus\n",
    "\n",
    "# ── CONFIG ──────────────────────────────────────────────────────────\n",
    "user     = 'etl_user1'\n",
    "password = quote_plus('3December2000@')\n",
    "host     = '127.0.0.1'\n",
    "port     = '5432'\n",
    "db       = 'etl_demo'\n",
    "engine   = create_engine(\n",
    "    f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'\n",
    ")\n",
    "\n",
    "def run_checks():\n",
    "    # 1) Raw table checks\n",
    "    df_raw = pd.read_sql(\"SELECT * FROM public.sales_raw\", engine,\n",
    "                         parse_dates=['order_date','ship_date'])\n",
    "    assert df_raw['order_id'].notnull().all(), \"Null order_id found\"\n",
    "    assert df_raw['order_id'].is_unique,      \"Duplicate order_id found\"\n",
    "    assert (df_raw['sales'] >= 0).all(),      \"Negative sales detected\"\n",
    "    assert df_raw['discount'].between(0,1).all(), \"Invalid discount (>1 or <0)\"\n",
    "    print(\"✅ sales_raw quality checks passed\")\n",
    "\n",
    "    # 2) Summary table checks\n",
    "    df_sum = pd.read_sql(\"SELECT * FROM public.sales_summary\", engine)\n",
    "    assert not df_sum.empty,                 \"sales_summary is empty\"\n",
    "    print(\"✅ sales_summary quality checks passed\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    try:\n",
    "        run_checks()\n",
    "    except AssertionError as e:\n",
    "        print(f\"❌ Data quality check failed: {e}\")\n",
    "        sys.exit(1)\n",
    "    print(\"🎉 All data quality checks passed\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ea70f01-d0a3-4aba-88a6-0446f09c7078",
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
