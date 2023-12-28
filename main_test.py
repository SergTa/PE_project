from streamlit.testing.v1 import AppTest #Импорт тест-клиента


def test_run_App():
    
    at = AppTest.from_file("main_project.py").run(timeout=10) # Запуск приложения с удлиненным таймаутом

    assert not at.exception # Проверка, что приложение запустилось
       
    at.text_area[0].set_value('I can fly').run(timeout=5) # Вставка в поле текста на английском
    at.button[0].click().run(timeout=15) # Нажатие на кнопку "перевести"
    assert at.markdown[1].value == "Я умею летать." # Сравнение результата перевода на русский
    
    at.text_area[0].set_value('Я умею летать').run(timeout=5) # Вставка в поле текста на русском
    at.button[0].click().run(timeout=15) # Нажатие на кнопку "перевести"
    assert at.markdown[1].value == "I know how to fly." # Сравнение результата перевода на английский

