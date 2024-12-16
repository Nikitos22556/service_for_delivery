from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__== '__main__':
  app.run(debug=True)
import json

# Создание данных
data = {
    "name": "Никита Госов",
    "age": 16,
    "city": "Москва",
    "skills": ["Python", "Django", "Machine Learning"]
}

# Запись данных в JSON файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Чтение данных из JSON файла
with open('data.json', 'r', encoding='utf-8') as file:
    loaded_data = json.load(file)

print(loaded_data)
