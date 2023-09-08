import json
import numpy as np
from sklearn.tree import DecisionTreeClassifier

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

answered_features = set()
confidence_threshold = 0.4
predicted_character = None
while True:
    uncertain_feature_indices = [i for i in range(len(all_traits)) if i not in answered_features]
    if not uncertain_feature_indices:
        break

    min_sum_proba = float('inf')
    uncertain_feature_index = None

    for idx in uncertain_feature_indices:
        yes_proba_sum = 0
        no_proba_sum = 0

        for character_idx in range(len(X)):
            X_copy = X.copy()
            X_copy[character_idx][idx] = 1
            proba = model.predict_proba([X_copy[character_idx]])[0]

            if y[character_idx] == predicted_character:
                yes_proba_sum += proba[character_idx]
            else:
                no_proba_sum += proba[character_idx]

        if yes_proba_sum + no_proba_sum < min_sum_proba:
            min_sum_proba = yes_proba_sum + no_proba_sum
            uncertain_feature_index = idx

    uncertain_feature_name = list(all_traits)[uncertain_feature_index]

    answer = input(f"Ваш персонаж {uncertain_feature_name}? (да/нет): ").lower()

    X_copy = X.copy()
    if answer == 'да':
        for i in range(len(X_copy)):
            X_copy[i][uncertain_feature_index] = 1
        answered_features.add(uncertain_feature_index)
    elif answer == 'нет':
        for i in range(len(X_copy)):
            X_copy[i][uncertain_feature_index] = 0
        answered_features.add(uncertain_feature_index)
    else:
        print("Пожалуйста, отвечайте только 'да' или 'нет'.")

    max_proba = 0
    for i in range(len(X_copy)):
        proba = model.predict_proba([X_copy[i]])[0]
        if max(proba) > max_proba:
            max_proba = max(proba)
            predicted_character = model.classes_[np.argmax(proba)]

    if max_proba >= confidence_threshold:
        answer = input(f"Я думаю, что ваш персонаж - {predicted_character} (Вероятность: {max_proba:.2f}) Я прав?: ")
        if answer == "да":
            break

if max_proba < confidence_threshold:
    print("Я не смог угадать персонажа.")
