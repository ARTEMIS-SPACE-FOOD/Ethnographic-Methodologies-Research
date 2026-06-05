import numpy as np


def ritual_adherence(hour):

    if 6 <= hour <= 9:
        return 1
    if 12 <= hour <= 14:
        return 1
    if 18 <= hour <= 20:
        return 1
    return 0


def food_diversity(food_string):

    if not isinstance(food_string, str):
        return 1

    items = [x.strip() for x in food_string.split(",") if x.strip()]
    n = len(items)

    if n >= 5:
        return 3
    elif n >= 3:
        return 2
    return 1


def compute_ethnographic_features(meals, activity):

    if meals.empty:
        return {
            "meal_ritual_adherence": 0,
            "meal_count": 0,
            "food_diversity": 0,
            "meal_completion_rate": 0
        }

    meals["hour"] = meals["timestamp"].dt.hour
    meals["ritual"] = meals["hour"].apply(ritual_adherence)

    features = {
        "meal_ritual_adherence": float(meals["ritual"].mean()),
        "meal_count": int(len(meals)),
        "food_diversity": meals.get("food_items", pd.Series([""] * len(meals)))
                           .apply(food_diversity)
                           .mean(),
        "meal_completion_rate": meals["completion"].mean()
                                if "completion" in meals.columns else 1.0
    }

    return features
