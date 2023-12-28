from streamlit.testing.v1 import AppTest #Импорт тест-клиента


def test_run_App():
    
    at = AppTest.from_file("main_project.py").run(timeout=30) # Запуск приложения с удлиненным таймаутом

    assert not at.exception # Проверка, что приложение запустилось
       
    at.text_area[0].set_value('I can fly').run(timeout=30) # Вставка в поле текста на английском
    at.button[0].click().run(timeout=30) # Нажатие на кнопку "перевести"
    assert at.markdown[0].value == "*Результаты перевода:*" # Сравнение надписи над переводом
    assert at.markdown[1].value == "Я умею летать." or at.markdown[1].value == "Не удалось осуществить перевод, пожалуйста, повторите попытку"# Сравнение результата перевода на русский
    
    at.text_area[0].set_value('Я умею летать').run(timeout=30) # Вставка в поле текста на русском
    at.button[0].click().run(timeout=30) # Нажатие на кнопку "перевести"
    assert at.markdown[0].value == "*Результаты перевода:*" # Сравнение надписи над переводом
    assert at.markdown[1].value == "I know how to fly." or at.markdown[1].value == "Не удалось осуществить перевод, пожалуйста, повторите попытку"# Сравнение результата перевода на английский

