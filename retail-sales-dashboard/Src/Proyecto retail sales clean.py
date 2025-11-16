import pandas as pd

df = pd.read_csv(r"C:\Users\Usuario\Desktop\DATA ANALIST\retail-sales-dashboard\Data\retail_sales_dataset.csv")


print(df.columns)

"""print(df)

print(df.shape)
print(df.head())
print(df.info())"""

# Normalización nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convertimos fecha a tipo datetime
df["date"] = pd.to_datetime(df["date"])

# Creamos columna 'month' y 'year'
df["month"] = df["date"].dt.month_name()
df["year"] = df["date"].dt.year

# Agrupamos por categoría y año para KPIs básicos
kpi_summary = df.groupby(["year", "product_category"]).agg(
    total_revenue=("total_amount", "sum"),
    avg_ticket=("total_amount", "mean"),
    units_sold=("quantity", "sum"),
    customers=("customer_id", "nunique")
).reset_index()

kpi_summary["revenue_per_customer"] = kpi_summary["total_revenue"] / kpi_summary["customers"]

print(kpi_summary.head())

# 6. Guardar CSV limpio
df.to_csv("data/retail_sales_clean.csv", index=False)
print("\nArchivo limpio guardado: data/retail_sales_clean.csv")
