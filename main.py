




with open ("books/frankenstein.txt") as f:
    file_contents = f.read()
    def sort_on(dict):
         return dict["num"]
    letter_counts = {}
    lower_case = file_contents.lower()
    letters_only = [char for char in lower_case if char.isalpha()]

    for char in letters_only:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
                letter_counts[char] = 1
    
    
    length_hint = len(file_contents.split())  
        ## word count
    
    sorted_letters = sorted(letter_counts.items(),
                             key=lambda item: item[1]
                            , reverse=True)

print("--- Begin report of books/frankenstein.txt --- \n",
      length_hint, "words found in the document \n")

for letter, count in sorted_letters:
     print(f"The '{letter}' character was found {count} times")

print("--- End report ---")