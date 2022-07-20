def no_of_letters_in_word(word,given_letter):
    count = 0
    for letter in word:
        if letter == given_letter:
            count = count + 1
    return count

word = input('>> Enter the word: ')
the_letter = input('>> Enter the letter: ')
length_of_string = no_of_letters_in_word(word,the_letter)
print("No of letters",the_letter,"in",word,":",length_of_string)
