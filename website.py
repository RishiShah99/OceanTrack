import streamlit as st
import numpy as np
import input  # Custom module for prediction

# Set up the app title
st.title("OceanTracker")

# App description
st.markdown("""
**OceanTrack** is a machine learning tool designed to predict the movement of plastic waste in the ocean.
By analyzing environmental data such as Sea Level Pressure (SLP) and Sea Surface Temperature (SST), 
OceanTrack forecasts the changes in the longitude and latitude of plastic debris over time. 
This helps in mapping out the future journey of plastic waste and identifying areas with a high likelihood 
of accumulation, enabling targeted clean-up efforts and better resource allocation to combat ocean pollution.

**DISCLAIMER:** Don't input parameters that are on land. The model is trained on ocean data and will not work accurately with land data.
""")

# Sidebar for parameter input
st.sidebar.header("Simulation Parameters")
longitude = st.sidebar.slider("Longitude", -180.0, 180.0, 0.0, help="Select the starting longitude")
latitude = st.sidebar.slider("Latitude", -90.0, 90.0, 0.0, help="Select the starting latitude")
sst = st.sidebar.slider("Sea Surface Temperature (SST)", -2.0, 35.0, 15.0, help="Set the sea surface temperature")
slp = st.sidebar.slider("Sea Level Pressure (SLP)", 900.0, 1100.0, 1013.0, help="Set the sea level pressure")
time = st.sidebar.slider("Time (in weeks)", 1, 10, 3, help="Select the number of days to simulate")

# Run the simulation when the button is clicked
if st.sidebar.button("Run Prediction"):
    # Prepare input data for prediction
    input_data = np.array([[longitude, latitude, sst, slp]])

    # Make predictions using the custom prediction function
    predicted_latitude, predicted_longitude = input.predict([latitude], [longitude], [sst], [slp])

    # Ensure the predictions are floating-point numbers
    predicted_latitude = float(predicted_latitude)
    predicted_longitude = float(predicted_longitude)

    # Initialize lists to store latitude and longitude values at each iteration
    lat_history = [latitude]
    lon_history = [longitude]

    # Run multiple iterations to simulate the movement over time
    for i in range(time):
        delta_lat, delta_lon = input.predict([latitude], [longitude], [sst], [slp])
        latitude += float(delta_lat)
        longitude += float(delta_lon)

        lat_history.append(latitude)
        lon_history.append(longitude)

    # Create a dictionary to store the latitude and longitude history
    location_history = {"latitude": lat_history, "longitude": lon_history}

    # Create REAL-TIME map
    st.subheader("Simulation Map")
    st.map(location_history)

    # Display the final latitude and longitude compared to the initial values
    st.subheader("Simulation Results")
    st.write(f"Initial Latitude: {lat_history[0]:.2f}")
    st.write(f"Initial Longitude: {lon_history[0]:.2f}")
    st.write("...")
    st.write(f"Final Latitude: {lat_history[-1]:.2f}")
    st.write(f"Final Longitude: {lon_history[-1]:.2f}")
