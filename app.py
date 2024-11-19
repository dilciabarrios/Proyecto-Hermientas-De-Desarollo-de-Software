import pandas as pd
import plotly.express as px
import streamlit as st

# Función para cargar los datos
def cargar_datos():
    return pd.read_csv('vehicles_us.csv')

# Función para crear el histograma
def crear_histograma(data, columna):
    return px.histogram(data, x=columna)

# Mostrar título y encabezado en Streamlit
st.title("Análisis de vehículos")  # Título principal
st.header("Histograma de Odometer")  # Encabezado secundario

# Cargar los datos
car_data = cargar_datos()

# Mostrar la tabla en Streamlit
st.write("Tabla con los datos de los vehículos:")
st.dataframe(car_data)  # Mostrar el DataFrame como tabla interactiva

# Crear un botón en Streamlit
hist_button = st.button('Construir histograma')

if hist_button:
    # Mostrar un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear y mostrar el histograma
    fig = crear_histograma(car_data, "odometer")
    st.plotly_chart(fig, use_container_width=True)
    

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Mostrar un mensaje
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    
    # Crear y mostrar el gráfico de dispersión
    fig_scatter = crear_dispersion(car_data, "odometer", "price")
    st.plotly_chart(fig_scatter, use_container_width=True)