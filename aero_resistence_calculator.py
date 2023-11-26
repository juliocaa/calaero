import streamlit as st
import ipywidgets as widgets
from IPython.display import display
import pandas as pd
from PIL import Image

st.markdown("[Visita mi canal de YouTube](https://www.youtube.com/@AutoIngenium-fj8ss)")

# Carga y muestra el logotipo
image = Image.open("mi_logotipo.png")
st.image(image, caption="AUTOINGENIUM", use_column_width=True)

st.markdown("[VIDEO TUTORIAL](https://www.youtube.com/watch?v=gLxunTcgm1I)")

# Define the function to calculate the electric car consumption
def calculate_consumption(cx, frontal_area, external_temp, speed, climate_control):
    # Constants
    air_density = 1.225  # in kg/m^3 at sea level and at 15°C
    drag_coefficient = 0.5  # typical value for a passenger car
    
    # Calculate aerodynamic resistance consumption
    aerodynamic_consumption = (1/2) * air_density * frontal_area * cx * (speed/3.6)**2 / 1000  # Convert speed to m/s and consumption to kWh/100km
    
    # Calculate battery efficiency based on temperature
    temperature_factor = 1 - 0.3 * (abs(external_temp - 20) / 20)
    battery_efficiency_consumption = 5.5 * temperature_factor
    
    # Adjust consumption for climate control if necessary
    if climate_control:
        climate_control_consumption = 2.0  # Assuming an additional 2 kWh/100km for climate control
    else:
        climate_control_consumption = 0.0
    
    # Total consumption
    total_consumption = aerodynamic_consumption + battery_efficiency_consumption + climate_control_consumption
    return total_consumption

# Create interactive widgets
cx_slider = widgets.FloatSlider(min=0.2, max=0.4, step=0.01, value=0.3, description='Coeficiente CX:')
frontal_area_slider = widgets.FloatSlider(min=1.0, max=3.0, step=0.1, value=2.2, description='Superficie Frontal:')
temperature_slider = widgets.IntSlider(min=-20, max=40, step=1, value=20, description='Temperatura Exterior:')
speed_slider = widgets.FloatSlider(min=50, max=200, step=1, value=100, description='Velocidad (km/h):')
climate_control_checkbox = widgets.Checkbox(value=False, description='Climatización')

# A function to update the output when any widget value changes
def update_output(*args):
    consumption = calculate_consumption(cx_slider.value, frontal_area_slider.value, temperature_slider.value, speed_slider.value, climate_control_checkbox.value)
    print(f"Consumo total cada 100 km: {consumption:.2f} kWh")

# Bind the function to changes in widget values
cx_slider.observe(update_output, 'value')
frontal_area_slider.observe(update_output, 'value')
temperature_slider.observe(update_output, 'value')
speed_slider.observe(update_output, 'value')
climate_control_checkbox.observe(update_output, 'value')

# Display the widgets and the initial consumption calculation
display(cx_slider, frontal_area_slider, temperature_slider, speed_slider, climate_control_checkbox)
update_output()  # To display the initial calculation

