import json

characters_data = [
    {
        "name": "Гарри Поттер",
        "description": "Молодой волшебник",
        "traits": {"Умный": 8, "Храбрый": 9, "Лояльный": 7},
        "photo_url": "https://example.com/harry_potter.jpg"
    },
    {
        "name": "Дориан Грей",
        "description": "Художник с вечной молодостью",
        "traits": {"Красивый": 10, "Таинственный": 8, "Эгоцентричный": 7},
        "photo_url": "https://example.com/dorian_gray.jpg"
    },
    { "name": "Пиздабол",
        "description": "Художник с вечной молодостью",
        "traits": {"Еблан": 10, "Таинственный": 4, "Тупой сученок": 10},
        "photo_url": "https://example.com/dorian_gray.jpg"
    },
    {   "name": "Создатель бота",
        "description": "Просто даун, которому скучно было :>",
        "traits": {"тупой хуйлан": 10, "дрочил кабану": 10, "мразота": 10, "харизматичный": 10, "создал бота": 10},
        "photo_url": "https://imgur.com/a/x0TFv6F"
        }
]

with open('characters.json', 'w', encoding='utf-8-sig') as json_file:
    json.dump(characters_data, json_file, indent=4)