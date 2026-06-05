import pandas as pd
import os


def generate_report(pid, meals, features, microbiome):

    os.makedirs("outputs", exist_ok=True)

    output_path = "outputs/one_day_artemis_demo.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:

        meals.to_excel(writer, sheet_name="Meals", index=False)
        pd.DataFrame([features]).to_excel(writer,
                                           sheet_name="Ethnographic_Features",
                                           index=False)

        if microbiome is not None:
            microbiome.to_excel(writer,
                                sheet_name="Microbiome",
                                index=False)

    print(f"✔ Report saved: {output_path}")
