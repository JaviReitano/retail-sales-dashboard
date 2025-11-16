# 📊 Retail Sales Dashboard – Power BI

Este proyecto presenta un dashboard profesional desarrollado en **Power BI** para analizar el rendimiento de ventas de un negocio retail.  
El informe permite comprender de manera clara las tendencias comerciales, el comportamiento de los clientes y la distribución del revenue por categoría de producto.

---

## 🎯 Objetivos del Dashboard

- Visualizar la evolución del **Total Revenue** y **Units Sold**.
- Analizar las ventas por **categoría de producto**.
- Comprender el comportamiento de los **clientes por edad y género**.
- Facilitar la **toma de decisiones** mediante KPIs claros e intuitivos.
- Presentar una vista ejecutiva y accesible para diferentes niveles de la organización.

---

## 🧠 Tecnologías y herramientas utilizadas

### 🟦 Power BI
- Power Query (transformaciones básicas)
- Modelado de datos (relación Calendar ↔ FactSales)
- DAX avanzado para cálculos:

### 🐍 Python (pandas)
- Limpieza de datos original
- Estandarización de columnas
- Conversión de fechas
- Creación de campos auxiliares (`month`, `year`)
- Preparación del archivo `retail_sales_clean.csv` utilizado por Power BI

### 🟨 Otras herramientas
- CSV como formato de almacenamiento
- GitHub como repositorio y control de versiones

---

## 📄 Contenido del Dashboard

### **Página 1 – Resumen Ejecutivo**
- KPIs:
  - Revenue
  - Units Sold
  - Avg Ticket
  - Customers
  - Revenue MoM (con indicador ↑ ↓)
- Gráfico de Revenue mensual + Running Total
- Distribución del revenue por categoría
- Distribución Ingreso por género

---

### **Página 2 – Categorías**
- Desempeño por categoría
- Participación porcentual (%)
- Tabla comparativa por categoría (Revenue, Units Sold, Avg Ticket)
- Gráfico de unidades vendidas por categoría

---

### **Página 3 – Clientes**
- Clientes únicos
- Revenue por cliente
- Segmentación por grupos de edad (Age Band)
- Distribución por género
- Matriz Edad × Categoría

---

### **Página 4 – Serie Temporal**
- Revenue mensual (YearMonth)
- Units Sold mensual
- Running Total
- Slicer de rango de fechas

---

## 🚀 Próximos pasos (versión 2 del proyecto)

La siguiente versión del proyecto incluirá:

- Automatización en Python para **simular nuevas ventas diarias**
- Pipeline simple:
  - Python → actualización del CSV  
  - Power BI → actualización del dashboard
- Documentación del proceso de actualización automática

---

## 👤 Realizado por:

**Javier Reitano**  
Data Analyst | Power BI | Python  
En transición profesional desde contabilidad hacia análisis de datos.

📩 email: javireitano@gmail.com
---






