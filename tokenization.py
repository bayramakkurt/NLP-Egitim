import nltk #Natural Language Toolkit

nltk.download("punkt") #Metni kelime ve cümle bazında tokenlara ayırabilmek için gerekli
nltk.download('punkt_tab')

text = "Hello, World! How are you? Hello, ..."

#Kelime Tokenizasyonu => word_tokenize : Metni kelimelere ayırır
#Noktalama işaretleri ve boşluklar ayrı birer token olarak elde edilecektir.
word_tokens = nltk.word_tokenize(text)
print(f"Kelime Tokenizasyonu: {word_tokens}")

#Cümle Tokenizasyonu => sent_tokenize : Metni cümlelere ayırır. Her bir cümle birer token olur.
sentence_tokens = nltk.sent_tokenize(text)
print(f"Cümle Tokenizasyonu: {sentence_tokens}")