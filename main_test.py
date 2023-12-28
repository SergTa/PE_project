from streamlit.testing.v1 import AppTest #Импорт тест-клиента

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("main_project.py").run()
    
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"



from main_translater import app           #Импорт объекта арр из файла main

client = TestClient(app)  #Создание клиента тестирования


def test_read_main():   # Функция проверки ответа на гет-запрос в корневой каталог
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_1():   # Функция проверки ответа на пост-запрос варианта перевода
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Я люблю машинное обучение!'


def test_predict_2(): # Функция проверки ответа на пост-запрос другого варианта перевода
    response = client.post("/predict/",
                           json={"text": "We hate testing!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['translation_text'] == 'Мы ненавидим тесты!'