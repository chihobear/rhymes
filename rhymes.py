"""
   File: rhymes.py
   Author: Chenghao Xiong
   Purpose: Find words with perfect rhymes to a specific word.
"""


def init(name):
    """Read the information in a file and put it in a dictionary of list of list.
       The dictionary's key is the word, the value is the word's pronunciation.
       Parameters: name is a name of the file.
       Returns: return the created dictionary.
    """
    dict = {}
    file = open( name, "r" )
    source_in_lines = file.readlines()
    file.close()
    for line in source_in_lines:
        temp = line.strip('\n')
        temp = temp.split()
        list = []
        if temp[0] not in dict:
            list.append(temp[1:])
            dict[temp[0]] = list
        else:
            dict[temp[0]].append(temp[1:])
    return dict

def find_words_step2(dict, word):
    """Sovle the problem of matching the stressed vowel sound. And use the function
       find_words_step1() to judge the phonemes that precede the stressed vowel if are same.
       Paremeters: dict is a dictionary of list of list
                   word is the specific word
       Returns: return a list containing all the required words.
    """
    list = []
    n_list_word = len(dict[word])   #n_list_word records how many pronunciations of the word
    for num in range(n_list_word):
        n = len(dict[word][num])    #n records the length of the pronunciation of the word
        position_word = primary_stress_position(dict[word][num])
        if position_word != None:
            for i in dict:
                if i == word:      #ignore the word itself
                    continue
                else:
                    n_list = len(dict[i])  #n_list records how many pronunciations of each word in the file
                    for k in range(n_list):
                        n_pro = len(dict[i][k]) #n_pro records the length of the pronunciation
                        position = primary_stress_position(dict[i][k])
                        if n_pro > position_word and position != None: #judge if the lengths of the matching pronuciation is greater than the length of stressed part
                            if n_pro - position == n - position_word:  #judge if the lengths of two matching stressed parts are same
                               n_after_stress = n_pro - position
                               for j in range(n_after_stress):
                                   if dict[i][k][position + j] == dict[word][num][position_word + j]:
                                       if j == n_after_stress - 1:
                                           if find_words_step1(dict[i][k], position, dict[word][num], position_word):
                                               list.append(i)
                                   else:
                                       break;
        
    return list

def find_words_step1(list, position, word_list, position_word):
    """Judge if two lists meet the requirement that the phoneme preceding the stressed
       vowel are same
       Parameters: list is the first list
                   position is the position of first list's stressed vowel
                   word_list is the second list
                   position_word is the second list's stressed vowel
       Returns: return True or False
    """
    if position == 0 and position_word == 0:
        return False
    elif position != 0 and position_word != 0:
        if list[position - 1] == word_list[position_word - 1]:
            return False
        else:
            return True
    else:
        return True
    
def primary_stress_position(phoneme_list):
    """Find the position of the stressed vowel of a word
       Parameters: phoneme_list is a list of string
       Returns: return the position of the stressed vowel or None
    """
    n = len(phoneme_list)
    for i in range(n):
        n_string = len(phoneme_list[i])
        if phoneme_list[i][n_string - 1] == '1':
            return i
        elif i == n - 1:
            return None


def main():
    """Use the functions init() and find_words_step2() to print the required words
    """
    file_name = input()
    word = input().upper()
    dict = init(file_name)
    for i in find_words_step2(dict, word):
        print(i)

main()
