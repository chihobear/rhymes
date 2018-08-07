"""
   File: rhymes-oo.py
   Author: Chenghao Xiong
   Purpose: Find words with perfect rthymes to a specific word
"""


import sys

class Word:
    def __init__(self, word, pronunciations):
        """Initiate class Word with 'self.__word' and 'self.__pron'
           Paremeters: 'word' is a string
                       'pronunciations' is a list of list
        """
        self.__word = word
        self.__pron = pronunciations

    def __eq__(self, other):
        """Judge if two words are in a perfect rhyme
           Parameters: 'other' is an object of class Word
           Return: When these two word are in a perfect rhyme, return True.
                   Otherwise, return False.
        """
        for lists in self.__pron:
            flag1 = False               #Judge the word that has no stress
            for i in range(len(lists)):
                #there is a stress
                if '1' in lists[i]:
                    stress_pos_self = i
                    #find stress position
                    flag1 = True
                    break;
            if flag1 == False:
            #if the word has no stress
                continue
            
            for lists_other in other._get_pron():
                flag2 = False            #Judge the word that has no stress
                for j in range(len(lists_other)):
                    #there is a stress
                    if '1' in lists_other[j]:
                        stress_pos_other = j
                        #find stress position
                        flag2 = True
                        break;
                if flag2 == False:
                #if the word has no stress
                    continue
                
                if lists[stress_pos_self:] == lists_other[stress_pos_other:]:
                    #if the vowels after the stress are same
                    if stress_pos_self != 0 and stress_pos_other == 0:
                        return True
                    elif stress_pos_self == 0 and stress_pos_other != 0:
                        return True
                    elif stress_pos_self != 0 and stress_pos_other != 0:
                        if lists[stress_pos_self - 1] != lists_other[stress_pos_other - 1]:
                            return True
            return False

    def _get_pron(self):
        return self.__pron

    def _get_word(self):
        return self.__word

    def __str__(self):
        return self.__word + str(self.__pron)
                



class WordMap:
    def __init__(self):
        """Initiate class WordMap with a empty dictionary 'self.__dic'"""
        self.__dic = {}

    def _read_and_map(self):
        """Read in a pronunciation file and set the data into 'self.__dic'
           where keys are words and values are pronunciations of words in a list of list.
        """  
        filename = input()
        dictionary = {}
        try:
            file = open(filename)
            for line in file:
                line_list = line.strip().split()
                assert type(line_list) == list
                word_name = line_list[0]
                if word_name in dictionary:
                    dictionary[word_name].append(line_list[1:])
                else:
                    dictionary[word_name] = [line_list[1:]]
        except(IOError):
            print("ERROR: Could not open file " + filename)
            exit(1)
        file.close()
        for key in dictionary:
            self.__dic[key] = Word(key, dictionary[key])
            #elements in self.__dic are objects of class Word

    def _read_and_print(self):
        """Read the word input by users then print out words in perfect rhymes"""
        word = input().upper()
        if word not in self.__dic:
            print("ERROR: the word input by the user is not in the pronunciation dictionary " + word)
            exit(1)
        else:
            for key in self.__dic:
                if word == key:
                    continue
                #ignore the word itself input by users
                else:
                    if self.__dic[word] == self.__dic[key]:
                        print(key)

    def __str__(self):
        return str(self.__dic)

def main():
    wordmap = WordMap()
    wordmap._read_and_map()
    wordmap._read_and_print()

main()
