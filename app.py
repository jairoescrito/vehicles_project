
# Importar librerías
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer el conjunto de datos desde el archivo plano
data = pd.read_csv('vehicles_us.csv')

# Crear título de la aplicación
st.header('Oferta de vehículos')

# Presentar la tabla de datos en formato DataFrame
# Crear un boton para presentar la tabla de datos
df_button = st.button('Presentar la tabla de datos')
if df_button:
    st.write('Tabla de datos de los vehículos ofertados')
    st.dataframe(data)

# Presentar el histograma del precio de venta de los vehículos
# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Histograma con plotly
    # Figura de histograma
    fig = go.Figure(data=[go.Histogram(x=data['price'])])

    # Agregar titulo y nombre de los ejes
    fig.update_layout(title_text='Distribución del Precio de los Vehículos',
                      xaxis_title='Precio ($)',
                      yaxis_title='Número de Vehículos')

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)


# Presentar la relación del precio de venta de los vehículos y su kilometraje
# Crear un botón en la aplicación Streamlit
scatt_button = st.button('Construir un diagrama de dispersión')
if scatt_button:
    st.write('Creación de un gráfico de dispersión para del precio de venta de los vehículos frente a su kilometraje')
    # Scatterplor con plotly
    # Figura de gráfico de dispersión
    fig = go.Figure(
        data=[go.Scatter(x=data['odometer'], y=data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Kilometraje y Precio',
                      xaxis_title='Kilometraje del vehículo',
                      yaxis_title='Precio ($)')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig, use_container_width=True)

# Presentar la comparación de la cantidad de vehículos por tipo y su transmisión
# Crear un checkbox en la aplicación Streamlit
bar_checkbox = st.checkbox('Construir un gráfico de barras')
if bar_checkbox:
    st.write('Creación de un gráfico de barras para comparar la cantidad de vehículos '
             'por tipo y su transmisión')
    type_count = data.groupby(['type', 'transmission']).size().reset_index(
        name='count').sort_values(by='count', ascending=False)

    fig = go.Figure()

    # Generar valores únicos de tipo de transmisión
    transmissions = type_count['transmission'].unique()

    # Graficar de forma separada cada barra por tipo de transmisión
    for transmission in transmissions:
        # Filtrar por tipo de transmisión
        transmission_data = type_count[type_count['transmission']
                                       == transmission]

        fig.add_trace(go.Bar(
            x=transmission_data['type'],
            y=transmission_data['count'],
            name=transmission,  # Crear etiqueta para la leyenda
        ))

        fig.update_layout(
            title_text="Cantidad de vehículos por tipo y por transmisión",
            xaxis_title="Tipo de vehículo",
            yaxis_title="Cantidad",
            barmode='stack'  # Opción para barras apiladas
        )

    st.plotly_chart(fig, use_container_width=True)
    # Mostrar la tabla de resultados graficados en barras apiladas
    st.write('Tabla de datos de cantidades por tipo de vehículo y transmisión')
    st.dataframe(type_count)
