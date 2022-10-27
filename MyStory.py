#Story code


import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


required = ("\nUse only A, B, C, yes or no\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
    print ('''You hear the faint sound of your alarm blairing against your ear.
Annoyed you slam your hand down on it. you hate waking up early but today you have too.
It's the first day at your new school, hogwarts, after all.
You look at the time. It's 6 in the morning, 2 hours until your train leaves

Will you:''')
    time.sleep(1)

    print ('''A. get up immediately
B. lay a bit longer in bed
''')
    
    choice = input(">>> ") #Here is your first choice.

    if choice.lower() == "a":
        s1a()
    elif choice.lower() == "b":
        s1b()

def s1a():
    print(''' do you want to make pancakes?''') 
    choice = input(">>> ") #Here is your first choice.
    if choice.lower() == "yes": 
        s1b()
    elif choice.lower() =="no":
        print(''' you calmly walk out of the house, knowing you're gonna be on time. as you walk up the train station you see alot of people around you.''')
        s2b()

def s1b():
    print(''' you're late! because you didn't immediately get ready, you're late for your train.
    you run out of the house and rush to the train station and OH NO! the train is almost leaving!
    do you:
    A. run faster
    B. start crying on the ground
  ''')
  
    choice = input(">>>")
    if choice.lower() == "a":
        s3a()
        s2b()
    elif choice.lower() == "b":
        s3b()
        s2b()

def s2b():
    print(''' you start walking into the train. okay, now it's time to pick a cabin.
    do you want to sit alone or with other people?
    A. sit alone
    B. sit with other people''')
    choice = input(">>>")
    if choice.lower() == "a":
        s4a()
    elif choice.lower() == "b":
        s4b()

def s3a():
    print(''' you start running like you've never ran before. you run harder and harder and harder and OH! you're catching up to the train?!
    you can see the entrance of the train. YES! someone left the door open. you keep running and then grab the side of the entrance and pull yourself in
    YOU MADE IT!!!''')

def s3b():
    print(''' you lay on the ground and start crying and wailing, putting your whole heart into the sobs, until someone pats your shoulder.
    you look up, it's a witch! she asks you why you're crying and you tell her everything. she feels bad for you and tells you to get behind her on her broom.
    she's gonne fly you to the train! as you twof ly to the train you see that someone left the train door open. YES!
    the witch flies close enough to the door so you can grab onto the side and pull yourself in, and then BAM! you fall in the train but you made it!''')

def s4a():
    print(''' the soft wobbling and sound of the train lulled you to sleep.
    OH NO! because you fell asleep you missed the stop and nobody woke you up! you walk out of the now empty train and look around, do you start panicking?''')
    choice = input(">>>")
    if choice.lower() == "yes":
        s5a()
    elif choice.lower() == "no":
        s5b()

def s4b():
    print('''are you gonna be nice to the people you're sitting with?''')
    choice = input(">>>")
    if choice.lower() == "yes":
        s6a()
    elif choice.lower() == "no":
        s4a()

def s5a():
    print(''' you start walking in circles while grabbing your head. you're panicking!!! you start to frantially look around and scream for help.
    suddenly you hear something behind you. you look around and see a group of centaurs. they heard you panicking!
    the centaurs tell you that they'll help you if you i give them something in return. what do you give them?
    A. give them home made cookies
    B. give an old sock
    C. give a fancy pen''')
    choice = input (">>>")
    if choice.lower() == "a, c":
        s7a()
    elif choice.lower() == "b":
        s7b()

def s6a():
    print(''' you start making conversation with the people you're sitting with''')
    


print(required)
print (intro())