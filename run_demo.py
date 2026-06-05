from src.load_data import load_participant_data
from src.meal_extraction import extract_daily_meals
from src.ethnographic_features import compute_ethnographic_features
from src.biocultural_index import compute_biocultural_index
from src.report_generator import generate_report

PARTICIPANT_ID = "CGMacros-001"
TARGET_DAY = 6


def main():

    # Load dataset
    data = load_participant_data(PARTICIPANT_ID)

    # Extract one-day behavioral slice
    meals, activity, microbiome = extract_daily_meals(data, TARGET_DAY)

    # Compute anthropological features
    features = compute_ethnographic_features(meals, activity)

    # Compute biocultural index
    features["biocultural_index"] = compute_biocultural_index(features, microbiome)

    # Generate outputs
    generate_report(PARTICIPANT_ID, meals, features, microbiome)

    print("✔ Pipeline complete. Outputs saved in /outputs")


if __name__ == "__main__":
    main()
