import random
import time


alphabet = {'a': '.-', 'b': '-...', 'c': '.-.-', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', 'æ': '.-.-', 'ø': '---.', 'å': '.--.-', ' ': ' |'}
learned = [' ']
alphabet3 = ['e', 't', 'i', 'm', 'a', 'n', 's', 'o', 'd', 'w', 'g', 'u', 'k', 'r', 'h', 'j', 'b', 'p', 'f', 'z','c', 'y', 'f', 'v', 'l', 'x', 'æ', 'ø', 'å', ]
def practise():
   letter = random.choice(list(alphabet))
   while True:
       while True:
           letter = random.choice(list(alphabet))
           if letter not in learned:
               break
           elif letter in learned:
               pass
       print('translate "', letter, '"')
       hints = 0
       while True:
           answer = input()
           if answer == alphabet[letter]:
               print("Correct!")
               print('Will you set "', letter, '" to learned(1) or not(2)')
               learned_or_not = input()
               if learned_or_not == 1:
                   learned.append(letter)
               else:
                   break
               break
           elif answer.lower() == 'menu':
               menu()
           else:
               print('Wrong! Try again(1), get a hint(2) or reveal(3)')
               again_or_hint = input()
               if int(again_or_hint) == 1:
                   print('translate "', letter, '"')
                   pass
               elif int(again_or_hint) == 2:
                   hints = hints + 1
                   print(alphabet[letter][:hints])
               elif int(again_or_hint) == 3:
                   print(alphabet[letter])
               else:
                   break
def learn():
   level = 0
   print('When ever you want you can write "lvl up" to level up')
   while True:
       time.sleep(0.3)
       print(f'Level {level + 1}:')
       time.sleep(0.6)
       print(alphabet3[level], ' = ', alphabet[alphabet3[level]])
       time.sleep(0.5)
       while True:
           letter_learn = alphabet3[random.randint(0, level)]
           time.sleep(0.3)
           print('Translate "', letter_learn, '"')
           answer = input()
           time.sleep(0.3)
           if answer == alphabet[letter_learn]:
               print('Correct!')
           elif answer.lower() == 'lvl up':
               level = level + 1
               break
           else:
               print('Wrong!')
def translate():
   while True:
       translate = input("What do you want to translate? ")
       if translate.lower() == 'stop':
           break
       elif translate.lower() == 'menu':
           menu()
       for i in translate.lower():
           print(alphabet[i], '//', end="")
       print()
def test():
   alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å', ]
   input('Press enter when you are ready! ')
   finish = False
   failed = []
   correct = []
   start_time = time.time()
   while len(alphabet2) != 0:
       letter_test = random.choice(alphabet2)
       answer_test = alphabet[letter_test]
       print('translate "', letter_test, '"')
       user_answer = input()
       if user_answer == answer_test:
           correct.append(letter_test)
           print('correct!')
           alphabet2.remove(letter_test)
       else:
           failed.append(letter_test)
           alphabet2.remove(letter_test)
           print('Wrong!')
   end_time = time.time()
   seconds = end_time - start_time
   print('You are finished! here are your stats: ')
   percentage = len(correct) / 29 * 100
   print(f"{percentage:.2f}%")
   time.sleep(0.2)
   print(f"{seconds:.2f} seconds")
   time.sleep(0.2)
   print('You know these: ', end="")
   time.sleep(0.2)
   for i in correct:
       print(i, ',', end=" ")
       time.sleep(0.01)
   print()
   time.sleep(0.2)
   print('And you struggle with these: ')
   for i in failed:
       print(i, ', ', end=" ")
       time.sleep(0.01)
   print()
   time.sleep(0.2)
   print('Press enter to go back to menu or play again(1)')
   input()
   menu()
def menu():
   translate_or_learn = ":)"
   while translate_or_learn not in [1, 2, 3, 4]:
       translate_or_learn = input("Translate(1), Practice(2), take a test(3) or learn(4) ")
       if translate_or_learn == '1':
           translate()
       elif translate_or_learn == '2':
           practise()
       elif translate_or_learn == '3':
           test()
       elif translate_or_learn == '4':
           learn()
       else:
           pass
menu()


