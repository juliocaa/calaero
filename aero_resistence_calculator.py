import streamlit as st

# Constantes por defecto para el Tesla Model 3
DEFAULT_CD = 0.22  # Coeficiente de resistencia aerodinámica
DEFAULT_AF = 2.2   # Área frontal en m^2
DENSIDAD_AIRE = 1.225  # Densidad del aire en kg/m^3

# Función para calcular la potencia necesaria para superar la resistencia del aire
def calcular_potencia(cd, af, velocidad):
    velocidad_ms = velocidad / 3.6  # Convertir km/h a m/s
    potencia = 0.5 * DENSIDAD_AIRE * af * cd * velocidad_ms**3
    return potencia / 1000  # Convertir W a kW

# Función para calcular el consumo en kWh cada 100 km
def calcular_consumo(potencia, velocidad):
    horas = 100 / velocidad  # Tiempo para recorrer 100 km
    consumo = potencia * horas  # Consumo en kWh
    return consumo

# Título de la aplicación en Streamlit
st.title('Calculadora de Consumo de Energía por Resistencia Aerodinámica')

# Entradas del usuario
cd_input = st.number_input('Coeficiente de resistencia aerodinámica (Cd)', value=DEFAULT_CD)
af_input = st.number_input('Área frontal (m^2)', value=DEFAULT_AF)
velocidad_input = st.number_input('Velocidad (km/h)', min_value=1.0, value=120.0)

# Calculando la potencia y el consumo
potencia = calcular_potencia(cd_input, af_input, velocidad_input)
consumo = calcular_consumo(potencia, velocidad_input)

# Mostrar la potencia y el consumo
st.write(f"Potencia necesaria a {velocidad_input} km/h: {potencia:.2f} kW")
st.write(f"Consumo de energía cada 100 km debido a la resistencia aerodinámica: {consumo:.2f} kWh")

