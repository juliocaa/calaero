import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("[Visita mi canal de YouTube](https://www.youtube.com/@AutoIngenium-fj8ss)")

# Carga y muestra el logotipo
image = Image.open("mi_logotipo.png")
st.image(image, caption="AUTOINGENIUM", use_column_width=True)

st.markdown("[VIDEO TUTORIAL](https://www.youtube.com/watch?v=gLxunTcgm1I)")

import streamlit as st

# Constants for air density and other calculations
rho = 1.225  # Air density in kg/m³

# Function to calculate the aerodynamic consumption including temperature effect
def aerodynamic_consumption(cx, frontal_area, speed_kmh, temperature):
    # Convert speed from km/h to m/s for the formula
    speed_ms = speed_kmh / 3.6
    # Aerodynamic power in W
    power_w = 0.5 * rho * speed_ms**3 * frontal_area * cx
    # Convert power to kWh and then to kWh/100km
    consumption_aero_kwh_per_100km = (power_w * (100 / speed_kmh)) / 1000
    # Adjust for temperature
    temp_factor = 1 + 0.3 * (abs(temperature - 20) / 20)
    consumption_aero_kwh_per_100km *= temp_factor
    return consumption_aero_kwh_per_100km

# Function to calculate the base consumption based on temperature
def base_consumption(temperature):
    # Base consumption at 20°C is 5.5 kWh/100km
    consumption = 5.5
    # Adjust for temperature
    temp_factor = 1 + 0.3 * (abs(temperature - 20) / 20)
    consumption *= temp_factor
    return consumption

# Function to calculate the influence of the climate control
def climate_control_influence(temperature):
    # Climate control consumption at 20°C is 0 kWh/100km
    # Adjust for temperature: 0.7 kWh/100km for every 6 degrees of deviation from 20°C
    consumption_climate_control = (abs(temperature - 20) / 6) * 0.7
    return consumption_climate_control

# Streamlit app
def electric_car_consumption_app():
    st.title('Electric Car Consumption Calculator')

    # Input fields with default values
    cx = st.number_input('Drag Coefficient (Cx)', value=0.22)
    frontal_area = st.number_input('Frontal Area (m²)', value=2.22)
    temperature = st.number_input('Outside Temperature (°C)', value=20)
    speed = st.number_input('Speed (km/h)', value=100)
    use_climate_control = st.checkbox('Consider Climate Control', value=False)

    # Calculate button
    if st.button('Calculate Consumption'):
        # Calculate aerodynamic consumption including temperature effect
        aero_consumption = aerodynamic_consumption(cx, frontal_area, speed, temperature)
        # Calculate base consumption based on temperature
        base_temp_consumption = base_consumption(temperature)
        # Calculate climate control influence if checked
        climate_control_consumption = climate_control_influence(temperature) if use_climate_control else 0
        # Sum up all consumptions
        total_consumption = aero_consumption + base_temp_consumption + climate_control_consumption

        # Display the results
        st.subheader('Results')
        st.write(f'Aerodynamic Consumption: {aero_consumption:.2f} kWh/100km')
        st.write(f'Base Temperature Consumption: {base_temp_consumption:.2f} kWh/100km')
        st.write(f'Climate Control Influence: {climate_control_consumption:.2f} kWh/100km')
        st.write(f'Total Consumption: {total_consumption:.2f} kWh/100km')

# Run the app function
if __name__ == "__main__":
    electric_car_consumption_app()
