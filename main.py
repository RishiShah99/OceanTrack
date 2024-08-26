import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import lightgbm as lgb

# The dataset
file_path = "osmc_30day.csv"

def load_and_preprocess_data(file_path):
    """
    Loads data, preprocesses it, and returns prepared features and target.
    """

    df = pd.read_csv(file_path, skiprows=[1])

    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    df.dropna(subset=["time"], inplace=True)

    df = df.sort_values(by=["platform_code", "time"])

    for col in ["latitude", "longitude", "sst", "slp"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.dropna(subset=["latitude", "longitude"], inplace=True)

    df["delta_latitude"] = df.groupby("platform_code")["latitude"].diff().fillna(0)
    df["delta_longitude"] = df.groupby("platform_code")["longitude"].diff().fillna(0)

    df = df[df["delta_latitude"] != 0]

    df["sst"] = df["sst"].fillna(df["sst"].mean())
    df["slp"] = df["slp"].fillna(df["slp"].mean())

    X = df[["latitude", "longitude", "sst", "slp"]]
    y_lat = df["delta_latitude"]
    y_lon = df["delta_longitude"]

    return X, y_lat, y_lon

def train_and_save_model(X_train, X_test, y_train, y_test, model_path):
    """
    Trains a LightGBM Regressor model and saves it.
    """

    train_data = lgb.Dataset(X_train, label=y_train)
    valid_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

    params = {
        'objective': 'regression',
        'metric': 'rmse',
        'boosting_type': 'gbdt',
        'learning_rate': 0.05,
        'num_leaves': 31,
        'verbose': -1,
        'random_state': 42
    }

    model = lgb.train(
        params,
        train_data,
        num_boost_round=500,
        valid_sets=[train_data, valid_data],
        callbacks=[
            lgb.early_stopping(stopping_rounds=50),
            lgb.log_evaluation(10),
            lgb.reset_parameter(learning_rate=lambda iter: 0.05 * (0.99 ** iter))
        ]
    )

    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    y_pred = model.predict(X_test, num_iteration=model.best_iteration)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    X, y_lat, y_lon = load_and_preprocess_data(file_path)

    # Split the data for latitude prediction
    X_train_lat, X_test_lat, y_train_lat, y_test_lat = train_test_split(X, y_lat, test_size=0.2, random_state=42)

    print("Training model for delta_latitude prediction...")
    train_and_save_model(X_train_lat, X_test_lat, y_train_lat, y_test_lat, "latitude_model.pkl")

    # Split the data for longitude prediction
    X_train_lon, X_test_lon, y_train_lon, y_test_lon = train_test_split(X, y_lon, test_size=0.2, random_state=42)

    print("Training model for delta_longitude prediction...")
    train_and_save_model(X_train_lon, X_test_lon, y_train_lon, y_test_lon, "longitude_model.pkl")