import streamlit as st

# Define los valores por defecto para el Tesla Model 3
DEFAULT_COEFICIENTE_DRAG = 0.22
DEFAULT_AREA_FRONTAL = 2.2
DENSIDAD_AIRE = 1.225  # en kg/m^3

# Título de la calculadora
st.title('Calculadora de consumo de energía debido a la resistencia aerodinámica')

# Entradas del usuario
velocidad_kmh = st.number_input('Introduzca la velocidad en km/h:', min_value=0.0, value=120.0)
coeficiente_drag = st.number_input('Coeficiente aerodinámico del vehículo:', min_value=0.0, value=DEFAULT_COEFICIENTE_DRAG)
area_frontal = st.number_input('Área frontal del vehículo (en m²):', min_value=0.0, value=DEFAULT_AREA_FRONTAL)

# Conversión de velocidad a m/s
velocidad_ms = velocidad_kmh / 3.6

# Cálculo de la potencia necesaria en vatios
potencia_w = 0.5 * DENSIDAD_AIRE * area_frontal * coeficiente_drag * velocidad_ms**2
potencia_kw = potencia_w / 1000  # Conversión de vatios a kilovatios

# Muestra la potencia necesaria para superar la resistencia del aire
st.write(f'La potencia necesaria para superar la resistencia aerodinámica a {velocidad_kmh} km/h es: {potencia_kw:.2f} kW')

