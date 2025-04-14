# Python 3.10.9
# Assignment 1
def main():
    #reverse words but not spaces or punctuation or other characters.
    #a word is made up of letters or numbers.
    
    #test case given in assignment
    test_str_1 = "String; 2be reversed..."
    test_str_1_ans = "gnirtS; eb2 desrever..."
    #test case for null
    test_str_2 = ""
    test_str_2_ans = ""
    #test case for input ending in alphanumeric character
    test_str_3 = "The quick brown fox"
    test_str_3_ans = "ehT kciuq nworb xof"
    #test case with singular letters
    test_str_4 = "T.h.e.e.n.d"
    test_str_4_ans = "T.h.e.e.n.d"
    def reverse_words(astr:str):
        output = ""
        partial = "" #stores a word being built in progress.
        #iterate through every char in the string
        for c in astr:
            if c.isdigit() or c.isalpha():
                partial += c
            else:
                #all other characters are treated as termination characters.
                #upon encountering one,
                #reverse partial,
                #append partial to output,
                #clear partial,
                #continue
                partial = partial[::-1]
                output += partial + c
                partial = ""
        #end step in case for loop ends without appending
        partial = partial[::-1]
        output += partial
        #print(output)
        #print(test_str_1_ans)
        return output
    print(test_str_1, test_str_1_ans, reverse_words(test_str_1) == test_str_1_ans)
    assert reverse_words(test_str_1) == test_str_1_ans
    print(test_str_2, test_str_2_ans, reverse_words(test_str_2) == test_str_2_ans)
    assert reverse_words(test_str_2) == test_str_2_ans
    print(test_str_3, test_str_3_ans, reverse_words(test_str_3) == test_str_3_ans)
    assert reverse_words(test_str_3) == test_str_3_ans
    print(test_str_4, test_str_4_ans, reverse_words(test_str_4) == test_str_4_ans)
    assert reverse_words(test_str_4) == test_str_4_ans
if __name__ == "__main__":
    main()