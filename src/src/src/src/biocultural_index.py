def compute_biocultural_index(features, microbiome):

    alpha_div = 4.0

    if microbiome is not None and not microbiome.empty:
        if "alpha_diversity" in microbiome.columns:
            alpha_div = microbiome["alpha_diversity"].mean()

    score = (
        features["meal_ritual_adherence"] * 0.30 +
        min(features["food_diversity"] / 3, 1) * 0.30 +
        features["meal_completion_rate"] * 0.20 +
        min(alpha_div / 5, 1) * 0.20
    )

    return round(score * 10, 2)
