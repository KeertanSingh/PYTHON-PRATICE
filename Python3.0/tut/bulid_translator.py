def translate(phrase):
    vowel = ["a", "e", "i", "o", "w"]
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter

    return translation


if __name__ == '__main__':
    word = input("Enter phrase here: ")
    ph = translate(word)
    print(ph)
