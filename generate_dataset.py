import pandas as pd
import random

careers = {
    "Software Engineer": (80, 100, 50, 70, 50),
    "Data Scientist": (85, 95, 50, 65, 50),
    "Teacher": (60, 80, 80, 70, 60),
    "Graphic Designer": (40, 60, 70, 100, 50),
    "Marketing Manager": (50, 70, 90, 80, 90)
}

data = []

for career, base in careers.items():
    for _ in range(200):  # 200 records per career
        row = [
            random.randint(base[0]-10, base[0]+10),  # Maths
            random.randint(base[1]-10, base[1]+10),  # Programming
            random.randint(base[2]-10, base[2]+10),  # Communication
            random.randint(base[3]-10, base[3]+10),  # Creativity
            random.randint(base[4]-10, base[4]+10),  # Leadership
            career
        ]
        data.append(row)

df = pd.DataFrame(
    data,
    columns=[
        "Maths",
        "Programming",
        "Communication",
        "Creativity",
        "Leadership",
        "Career"
    ]
)

df.to_csv("dataset/career_dataset.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))