# pip install translate

from translate import Translator

fr_lang = input('What is the language of the word you want to translate: ')
word = input('Enter the word you want to translate: ')
t_lang = input('Into which language do you want to translate your word to: ')

translator = Translator(from_lang= fr_lang, to_lang = t_lang)
translation = translator.translate(word)
print(translation)
