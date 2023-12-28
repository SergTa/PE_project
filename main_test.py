from streamlit.testing.v1 import AppTest #Импорт тест-клиента

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("main_project.py").run()
    at.text_area[0].set_value('I can fly').run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Я могу летать"