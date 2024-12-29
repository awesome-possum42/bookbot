




with open ("books/frankenstein.txt") as f:
    file_contents = f.read()
    length_hint = len(file_contents.split())  
print(length_hint)