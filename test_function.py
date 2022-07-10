#!/usr/bin/python3

def string_is_unique(word):
    debug = 1

    for char in word:
        print(char)

def recommend_word(word_list):
    debug = 1

    print("recommend try")

    if(len(word_list) == 1):
        print("choice is easy : ", end="")
        print(word_list)
        return()
    
    for word in word_list:
        string_is_unique(word)

#end of recommend_word

def main():
    print("helper")
    debug = 1

    word_list = ['berth', 'betel', 'beget', 'befit', 'beret']

    short_list = ['berth']

    recommend_word(word_list)

    print('-'*10)

    #recommend_word(short_list)

if __name__ == "__main__":
    main()
#end