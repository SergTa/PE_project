from transformers import pipeline
#from transformers import AutoTokenizer
import torch
import tensorflow
import streamlit as st
import io
import chardet #детектор языка и кодировки

#text = 'I can fly'
st.title("Переводчик с английского на русский и наоборот")

# Функиця get_data() предоставляет пользователю ввести текст в предложенное поле
def get_data():
  text = st.text_area("Введите текст на русском или на английском языке")
  return text

# Проверка введенного текста на принадлежность к русскому языку
def dec_lan (text):
  dec_lan = chardet.detect(text.encode('cp1251'))
  
  return dec_lan['language']

            
@st.cache_resource # Декоратор
def tr_model_en_ru(text): # Функция вызова модели переводчика с английского на русский
  translator = pipeline("translation", 
                        model = "Helsinki-NLP/opus-mt-en-ru")
  transed = translator(text )[0]
  return transed 

def tr_model_ru_en(text): # Функция вызова модели переводчика с русского на английский
  translator = pipeline("translation", 
                        model = "Helsinki-NLP/opus-mt-ru-en")
  transed = translator(text )[0]
  return transed 

def main():
  # обрабатываем исключение
  try:
     
    # Вызов функции для загрузки данных с клавиатуры. Результат сохраняется в переменной content
    content = get_data() 
       
    result = st.button('Перевести') # Кнопка Перевести
    if result:
        d_lan = dec_lan (content) # Вызов функции определения языка, внесение введенного текста как аргумента, присвоение результата переменной
        if d_lan == 'Russian': #Проверка не русский ли язык введен. Вызов модели русско-англ переводчика или англ-русского
          translated = tr_model_ru_en(content)
        else:
          translated = tr_model_en_ru(content)
       
        st.markdown('*Результаты перевода:*')# Показать надпись
        st.markdown(translated ["translation_text"])#Показать результат перевода
        


  # Если в процессе выполнения программы возникает ValueError - обрабатываем исключение
  except ValueError:
    st.write("Не удалось осуществить перевод, пожалуйста, повторите попытку")
    return

# Запуск программы()
main() 
