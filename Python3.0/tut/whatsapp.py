import pyautogui
import time
import random
time.sleep(1)
i = 10
n = 0

with open("joker.txt", "r") as word:
    words = word.read()
    word_list = words.split("\n")
    print(word_list)

# word="""Ishq jehi aasan koi sheh vi nai
# Ishq jeha mushkil te shadeed koi na
# Oye tu andaron ee labh Sartaaj shayra
# Chhad baahron milan di ummeed koi na"""

# word = """Dil Da Nhi C Marra, Oye Sadda Sidhu Moosewala🥰"""

while n < i:
    print(n)
    for word in word_list:
        word = random.choice(word_list)
        pyautogui.write(word)
        pyautogui.press('enter')
    n += 1   
    # pyautogui.write(word)
    
    # pyautogui.press('enter')
    # n += 1  

