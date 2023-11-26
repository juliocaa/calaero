import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("[Visita mi canal de YouTube](https://www.youtube.com/@AutoIngenium-fj8ss)")

# Carga y muestra el logotipo
image = Image.open("mi_logotipo.png")
st.image(image, caption="AUTOINGENIUM", use_column_width=True)

st.markdown("[VIDEO TUTORIAL](https://www.youtube.com/watch?v=gLxunTcgm1I)")

import streamlit as st

def calculate_aerodynamic_drag(cx, frontal_area, speed):
    # Constante para la densidad del aire a nivel del mar y 15°C
    air_density = 1.225  # en kg/m^3
    # Calcula la fuerza de arrastre aerodinámico
    drag_force = 0.5 * air_density * (speed ** 2) * frontal_area * cx
    # Suponiendo una potencia constante para superar esta fuerza a la velocidad dada
    # Potencia = Fuerza * Velocidad
    # Energía = Potencia * Tiempo
    # Energía en kWh para 100 km
    energy_consumption = drag_force * speed / 3600  # Convertir W a kW y segundos a horas
    return energy_consumption

def calculate_additional_consumption(temperature, include_climate_control):
    optimal_temperature = 20  # Temperatura óptima en grados Celsius
    base_consumption = 5.5  # Consumo base en kWh cada 100 km

    # Ajustar el consumo base en función de la pérdida de eficiencia
    if temperature < optimal_temperature:
        efficiency_loss = (optimal_temperature - temperature) / 20 * 0.3
    else:
        efficiency_loss = (temperature - optimal_temperature) / 20 * 0.3

    adjusted_consumption = base_consumption * (1 + efficiency_loss)

    # Añadir un consumo fijo si se incluye el control climático
    climate_control_consumption = 2 if include_climate_control else 0

    total_additional_consumption = adjusted_consumption + climate_control_consumption

    return total_additional_consumption

def main():
    st.title("Calculadora de consumo de coche eléctrico")

    # Entrada de datos del usuario
    cx = st.number_input('Introduce el coeficiente aerodinámico (Cx):', min_value=0.0, max_value=1.0, step=0.01)
    frontal_area = st.number_input('Introduce la superficie frontal del vehículo (m²):')
    temperature = st.number_input('Introduce la temperatura exterior (°C):')
    speed = st.number_input('Introduce la velocidad a la que calcular el consumo (km/h):')
    include_climate_control = st.checkbox('Incluir climatización del habitáculo')

    if st.button('Calcular consumo'):
        # Convertir la velocidad de km/h a m/s
        speed_m_s = speed * 1000 / 3600
        # Calcular el consumo debido a la resistencia aerodinámica
        aerodynamic_consumption = calculate_aerodynamic_drag(cx, frontal_area, speed_m_s)
        # Calcular el consumo adicional
        additional_consumption = calculate_additional_consumption(temperature, include_climate_control)
        # Calcular el consumo total
        total_consumption = aerodynamic_consumption + additional_consumption

        st.write(f"El consumo total es: {total_consumption:.2f} kWh cada 100 km")

if __name__ == "__main__":
    main()


