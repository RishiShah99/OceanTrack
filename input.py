import pandas as pd
import joblib

def load_models(lat_model_path, lon_model_path):
    """
    Loads the trained models for latitude and longitude.
    """

    model_lat = joblib.load(lat_model_path)
    model_lon = joblib.load(lon_model_path)
    return model_lat, model_lon

def predict_new_location(model_lat, model_lon, input_data):
    """
    Predicts the new latitude and longitude based on the input data.
    """

    delta_lat_pred = model_lat.predict(input_data)
    delta_lon_pred = model_lon.predict(input_data)
    return delta_lat_pred[0], delta_lon_pred[0]

def predict(lat, lon, sst, slp):
    example_input = pd.DataFrame({
        "latitude": lat,
        "longitude": lon,
        "sst": sst,
        "slp": slp
    })

    model_lat, model_lon = load_models("models/latitude_model.pkl", "models/longitude_model.pkl")

    delta_lat, delta_lon = predict_new_location(model_lat, model_lon, example_input)

    delta_lat = f"{(float(str(delta_lat)[:2])):.2f}"
    delta_lon = f"{(float(str(delta_lon)[:2])):.2f}"

    return delta_lat, delta_lon