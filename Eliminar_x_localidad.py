import streamlit as st
import pandas as pd
from io import BytesIO

def filtrar_csv(df):
    # Filtrar eliminando las filas donde COD_LOCALIDAD empieza con 13473 o 44430
    df_filtrado = df[~df["COD_LOCALIDAD"].astype(str).str.startswith(("13473", "44430"), na=False)]
    return df_filtrado

def convertir_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    processed_data = output.getvalue()
    return processed_data

st.title("Filtro de CSV por COD_LOCALIDAD")

# Subir archivo
uploaded_file = st.file_uploader("Carga tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, dtype={"COD_LOCALIDAD": str})
    df_filtrado = filtrar_csv(df)
    
    # Mostrar dataframe filtrado
    st.write("Vista previa del archivo filtrado:")
    st.dataframe(df_filtrado)
    
    # Convertir a CSV para descargar
    csv_data = convertir_csv(df_filtrado)
    
    # Obtener el nombre original del archivo
    original_filename = uploaded_file.name
    
    # Botón de descarga
    st.download_button(
        label="Descargar CSV Filtrado",
        data=csv_data,
        file_name=f"filtrado_{original_filename}",
        mime="text/csv"
    )
