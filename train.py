import json
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import joblib

with open('characters.json', 'r', encoding='utf-8-sig') as json_file:
    characters_data = json.load(json_file)

all_traits = set()
for character in characters_data:
    traits = character["traits"]
    all_traits.update(traits.keys())

X = np.zeros((len(characters_data), len(all_traits)))
y = [character["name"] for character in characters_data]

for i, character in enumerate(characters_data):
    traits = character["traits"]
    for j, trait_name in enumerate(all_traits):
        X[i][j] = traits.get(trait_name, 0)

model = DecisionTreeClassifier()
model.fit(X, y)

# Сохранение модели в файл
joblib.dump(model, 'character_model.pkl')
