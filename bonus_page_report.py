import pandas as pd

# Rutas de los archivos
landing_pages_path = "C:\\Users\\ChristianBastidasNie\\Downloads\\landing_pages_search.csv"
bonus_pages_path = "C:\\Users\\ChristianBastidasNie\\Downloads\\Bonus Pages Report.csv"
output_path = "C:\\Users\\ChristianBastidasNie\\Downloads\\Consolidado_Bonus_Pages.xlsx"

# Cargar el archivo de landing pages
landing_df = pd.read_csv(landing_pages_path, encoding='utf-8')

# Filtrar las URLs que contienen "bonus" en la columna D
landing_df = landing_df[landing_df.iloc[:, 3].str.contains("bonus", na=False, case=False)]

# Seleccionar las columnas necesarias incluyendo "Landing Page Data"
landing_df = landing_df[["Description", "Landing Page ID", "Tracking Domain", "Channels", landing_df.columns[3]]]
landing_df.rename(columns={landing_df.columns[4]: "Landing Page Data"}, inplace=True)

# Cargar el archivo Bonus Pages Report
bonus_df = pd.read_csv(bonus_pages_path, encoding='utf-8')

# Renombrar la columna "Landing Page" en bonus_df para que coincida con "Description"
bonus_df.rename(columns={"Landing Page": "Description"}, inplace=True)

# Seleccionar las columnas necesarias en bonus_df
bonus_df = bonus_df[["Description", "Clicks", "Signups", "Signups LIVE", "NDC", "NDC LIVE", "Deposits", "Calculated NGR", "Qualified Players", "Withdrawals"]]

# Hacer merge de los dos DataFrames basados en "Description"
merged_df = landing_df.merge(bonus_df, on="Description", how="left")

# Reorganizar las columnas para que "Landing Page Data" esté en la columna N
merged_df = merged_df[["Description", "Landing Page ID", "Landing Page Data", "Tracking Domain", "Channels", "Clicks", "Signups", "Signups LIVE", "NDC", "NDC LIVE", "Deposits", "Calculated NGR", "Qualified Players", "Withdrawals", "Landing Page Data"]]

# Guardar el resultado en un archivo Excel
merged_df.to_excel(output_path, index=False)

print(f"Archivo consolidado guardado en: {output_path}")
