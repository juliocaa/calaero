import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("[Visita mi canal de YouTube](https://www.youtube.com/@AutoIngenium-fj8ss)")

# Carga y muestra el logotipo
image = Image.open("mi_logotipo.png")
st.image(image, caption="AUTOINGENIUM", use_column_width=True)

st.markdown("[VIDEO TUTORIAL](https://www.youtube.com/watch?v=gLxunTcgm1I)")

# Function to calculate the aerodynamic consumption
def aerodynamic_consumption(cx, frontal_area, speed):
    # Assuming air density at sea level and 15°C is 1.225 kg/m³
    rho = 1.225
    # Aerodynamic power consumption in kW
    power = 0.5 * rho * speed**2 * frontal_area * cx
    # Convert power to kWh/100km
    consumption = power * speed / 1000
    return consumption

# Function to calculate the battery consumption based on temperature
def battery_consumption(temperature, use_climate_control):
    # Base consumption at optimal temperature (20°C)
    base_consumption = 5.5
    # Adjust consumption based on temperature
    if temperature != 20:
        efficiency_change = 0.3 * (1 - abs(temperature - 20) / 20)
        temperature_consumption = base_consumption / (1 - efficiency_change)
    else:
        temperature_consumption = base_consumption
    
    # Adjust for climate control
    climate_control_consumption = 0
    if use_climate_control:
        if temperature < 20:
            climate_control_consumption = 0.7 * (20 - temperature) / 14
        elif temperature > 20:
            climate_control_consumption = 0.7 * (temperature - 20) / 20
    
    total_consumption = temperature_consumption + climate_control_consumption
    return total_consumption

# Streamlit app
def app():
    st.title('Electric Car Consumption Calculator')

    # Input fields with default values
    cx = st.number_input('Coefficient of drag (Cx)', min_value=0.0, value=0.22)
    frontal_area = st.number_input('Frontal Area (m²)', min_value=0.0, value=2.22)
    temperature = st.number_input('Outside Temperature (°C)', value=20)
    speed = st.number_input('Speed (km/h)', min_value=0.0, value=100.0)
    use_climate_control = st.checkbox('Climate Control', value=False)

    # Calculate button
    if st.button('Calculate'):
        aero_consumption = aerodynamic_consumption(cx, frontal_area, speed)
        battery_consumption = battery_consumption(temperature, use_climate_control)
        total_consumption = aero_consumption + battery_consumption

        # Output
        st.subheader('Results')
        st.write(f'Aerodynamic Consumption: {aero_consumption:.2f} kWh/100km')
        st.write(f'Battery Consumption: {battery_consumption:.2f} kWh/100km')
        st.write(f'Total Consumption: {total_consumption:.2f} kWh/100km')

if __name__ == "__main__":
    app()
