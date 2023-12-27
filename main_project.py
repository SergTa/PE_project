from transformers import pipeline
from transformers import AutoTokenizer
import torch
import tensorflow
import streamlit as st
import io
#from pydantic import BaseModel    # импорт ограничителя ввода данных
from googletrans import Translator

#text = 'I can fly'
st.title("Переводчик текстов на русский")

# Функиця get_data() предоставляет пользователю ввести текст в предложенное поле
def get_data():
  text = st.text_area("Введите текст")
  # Проверка введенного текста на принадлежность к английскому языку
  detector = Translator()
  dec_lan = detector.detect(text)
  
  return text, dec_lan



            
@st.cache_resource
def tr_model(text):
  translator = pipeline("translation", 
                        model = "Helsinki-NLP/opus-mt-en-ru")
  transed = translator(text )[0]
  return transed 


def main():
  # обрабатываем исключение
  try:
     
    # Вызов функции для загрузки данных - текстового файла или ввода с клавиатуры. Результат сохраняется в переменной content
    content = get_data() 
       
    result = st.button('Перевести на русский')
    if result:
        translated = tr_model(content) 
        
        st.write('*Результаты перевода:*')
        st.write(translated ["translation_text"])
        st.write (dec_lan)


  # Если в процессе выполнения программы возникает ValueError вследствие получения None Type - обрабатываем исключение
  except ValueError:
    st.write("Не удалось осуществить перевод, пожалуйста, повторите попытку")
    return

# Запуск программы()
main() 
