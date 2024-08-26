import input

# Example initial lat and lon
lat = 10
lon = 40

# Example initial sea surface temperature (SST) and sea level pressure (SLP)
sst = 30
slp = 1010

# Initialize a list to store latitude and longitude values at each iteration
lat_history = [lat]
lon_history = [lon]

for i in range(3):
    delta_lat, delta_lon = input.predict([lat], [lon], [sst], [slp])
    lat += float(delta_lat)
    lon += float(delta_lon)

    lat_history.append(lat)
    lon_history.append(lon)

# Create a dictionary to store latitude and longitude history
location_history = {"latitude": lat_history, "longitude": lon_history}

# Print the final latitude and longitude compared to the initial values
print(f"Initial Latitude: {lat_history[0]:.2f}")
print(f"Initial Longitude: {lon_history[0]:.2f}")
print("...")
print(f"Final Latitude: {lat_history[-1]:.2f}")
print(f"Final Longitude: {lon_history[-1]:.2f}")


print(location_history)