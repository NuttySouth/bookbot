file_name = "frankenstein.txt"
with open(f"./books/{file_name}") as f:
    file_contents = f.read()
    words = file_contents.split()
    print(f"--- Begin report of books/{file_name} ---")
    print(f"{len(words)} words found in the document")
    print("")
    letter_dic = {}
    for word in words:
        for letter in word:
            if letter.lower() in letter_dic:
                letter_dic[letter.lower()] += 1
            else:
                letter_dic[letter.lower()] = 1
    
    alphabet = list(letter_dic.keys())
    alphabet.sort()
    for letter in alphabet:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_dic[letter]} times")
print("--- End report ---")
