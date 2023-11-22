import streamlit as st

# Título de la aplicación
st.title('Calculadora de Resistencia Aerodinámica')

# Inputs del usuario
st.sidebar.header('Parámetros de entrada')
velocidad_kmh = st.sidebar.number_input('Introduce la velocidad en km/h', min_value=0.0, value=120.0, step=1.0)
coeficiente_aerodinamico = st.sidebar.number_input('Coeficiente aerodinámico', min_value=0.0, value=0.23, step=0.01)
area_frontal = st.sidebar.number_input('Área frontal en m²', min_value=0.0, value=2.2, step=0.1)

# Conversión de la velocidad de km/h a m/s
velocidad_ms = velocidad_kmh / 3.6

# Cálculo de la resistencia aerodinámica
def calcular_resistencia_aerodinamica(velocidad, coef_drag, area_frontal):
    densidad_aire = 1.225  # en kg/m³
    resistencia_aerodinamica = 0.5 * densidad_aire * area_frontal * coef_drag * velocidad ** 2
    return resistencia_aerodinamica

resistencia_aerodinamica = calcular_resistencia_aerodinamica(velocidad_ms, coeficiente_aerodinamico, area_frontal)

# Mostrar el resultado
st.write(f"La resistencia aerodinámica a {velocidad_kmh} km/h es: {resistencia_aerodinamica:.2f} N")

# Mostrar información adicional
st.markdown("""
La fórmula utilizada para calcular la resistencia aerodinámica es:
\[ R = \frac{1}{2} \cdot \rho \cdot A \cdot C_d \cdot v^2 \]
donde:
- \( R \) es la resistencia aerodinámica en Newtons (N).
- \( \rho \) es la densidad del aire (1.225 kg/m³ a nivel del mar).
- \( A \) es el área frontal del vehículo en metros cuadrados (m²).
- \( C_d \) es el coeficiente de resistencia aerodinámica.
- \( v \) es la velocidad en metros por segundo (m/s).
""")
