# Diberikan contoh sebuah kalimat, silahkan cari kata terpanjang dari kalimat tersebut, 
# jika ada kata dengan panjang yang sama silahkan ambil salah satu

def longest(sentence):
    words = sentence.split(' ')
    longest_word = ""
    longest_word_len = 0

    for word in words:
        word_len = len(word)
        if(word_len > longest_word_len):
            longest_word = word
            longest_word_len = word_len

    return f"{longest_word}: {longest_word_len} character"

sentence = "Saya sangat senang mengerjakan soal algoritma"
longest_word = longest(sentence)
print(longest_word)