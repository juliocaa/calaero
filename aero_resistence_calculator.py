import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("[Visita mi canal de YouTube](https://www.youtube.com/@AutoIngenium-fj8ss)")

# Carga y muestra el logotipo
image = Image.open("mi_logotipo.png")
st.image(image, caption="AUTOINGENIUM", use_column_width=True)

st.markdown("[VIDEO TUTORIAL](https://www.youtube.com/watch?v=gLxunTcgm1I)")

import streamlit as st

# Constants for air density
rho = 1.225  # Air density in kg/m³

# Function to calculate the aerodynamic consumption
def aerodynamic_consumption(cx, frontal_area, speed_kmh):
    # Convert speed from km/h to m/s for the formula
    speed_ms = speed_kmh / 3.6
    # Aerodynamic power in W
    power_w = 0.5 * rho * speed_ms**3 * frontal_area * cx
    # Convert power to kWh and then to kWh/100km
    consumption_kwh_per_100km = (power_w * (100 / speed_kmh)) / 1000
    return consumption_kwh_per_100km

# Function to calculate the consumption based on temperature
def temperature_based_consumption(temperature):
    # Base consumption at 20°C is 5.5 kWh/100km
    base_consumption = 5.5
    # Adjust consumption based on temperature
    if temperature != 20:
        efficiency_change = 0.3 * (1 - abs(temperature - 20) / 20)
        consumption = base_consumption / (1 - efficiency_change)
    else:
        consumption = base_consumption
    return consumption

# Function to calculate the influence of the climate control
def climate_control_influence(temperature, use_climate_control):
    # No influence at 20°C, linear increase/decrease outside this temperature
    # At 6°C or 34°C (20±14), the influence is 0.7kWh/100km
    if use_climate_control:
        if temperature != 20:
            influence = 0.7 * abs(temperature - 20) / 14
        else:
            influence = 0
    else:
        influence = 0
    return influence

# Streamlit app
def electric_car_consumption_app():
    st.title('Electric Car Consumption Calculator')

    # Input fields with default values
    cx = st.number_input('Drag Coefficient (Cx)', min_value=0.0, max_value=1.0, value=0.22, step=0.01)
    frontal_area = st.number_input('Frontal Area (m²)', min_value=0.0, max_value=10.0, value=2.22, step=0.01)
    temperature = st.number_input('Outside Temperature (°C)', min_value=-50.0, max_value=50.0, value=20.0, step=0.1)
    speed = st.number_input('Speed (km/h)', min_value=0.0, max_value=300.0, value=100.0, step=1.0)
    use_climate_control = st.checkbox('Consider Climate Control', value=False)

    # Calculate button
    if st.button('Calculate Consumption'):
        # Calculate aerodynamic consumption
        aero_consumption = aerodynamic_consumption(cx, frontal_area, speed)
        # Calculate temperature based consumption
        temp_consumption = temperature_based_consumption(temperature)
        # Calculate climate control influence
        climate_consumption = climate_control_influence(temperature, use_climate_control)
        # Sum up all consumptions
        total_consumption = aero_consumption + temp_consumption + climate_consumption

        # Display the results
        st.subheader('Results')
        st.write(f'Aerodynamic Consumption: {aero_consumption:.2f} kWh/100km')
        st.write(f'Temperature-based Consumption: {temp_consumption:.2f} kWh/100km')
        st.write(f'Climate Control Influence: {climate_consumption:.2f} kWh/100km')
        st.write(f'Total Consumption: {total_consumption:.2f} kWh/100km')

# Run the app function
if __name__ == "__main__":
    electric_car_consumption_app()

