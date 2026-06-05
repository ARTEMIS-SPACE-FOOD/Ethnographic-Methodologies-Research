import pandas as pd
import os


def load_participant_data(participant_id, base_path="data/cgmacros"):

    file_path = os.path.join(base_path, f"{participant_id}.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Missing file: {file_path}")

    df = pd.read_csv(file_path)

    # Standardize timestamp if present
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df
