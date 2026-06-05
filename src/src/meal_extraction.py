def extract_daily_meals(df, day):

    if "mission_day" not in df.columns:
        raise ValueError("Dataset missing 'mission_day' column")

    day_df = df[df["mission_day"] == day].copy()

    meals = day_df[day_df["event_type"] == "meal"].copy()
    activity = day_df[day_df["event_type"] == "activity"].copy()
    microbiome = day_df[day_df["event_type"] == "microbiome"].copy()

    return meals, activity, microbiome
