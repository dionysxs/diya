#Story code


import time #Imports a module to add a pause
import random

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


required = ("\nUse only a or b\n") #Cutting down on duplication

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
    print(''' do you want to make pancakes?
    A. yes
    B. no''') 
    choice = input(">>> ") #Here is your first choice.
    if choice.lower() == "a": 
        s1b()
    elif choice.lower() =="b":
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
    OH NO! because you fell asleep you missed the stop and nobody woke you up! you walk out of the now empty train and look around, do you start panicking?
    A. yes
    B. no''')
    choice = input(">>>")
    if choice.lower() == "a":
        s5a()
    elif choice.lower() == "b":
        s5b()


def s4b():
    print('''are you gonna be nice to the people you're sitting with?
    A. yes
    B. no''')
    choice = input(">>>")
    if choice.lower() == "a":
        s6a()
    elif choice.lower() == "b":
        s4a()


def s5a():
    print(''' you start walking in circles while grabbing your head. you're panicking!!! you start to frantially look around and scream for help.
    suddenly you hear something behind you. you look around and see a group of centaurs. they heard you panicking!
    the centaurs tell you that they'll help you if you i give them something in return. what do you give them?
    A. give them home made cookies
    B. give an old sock''')
    choice = input (">>>")
    if choice.lower() == "a":
        s7a()
        s6b()
    elif choice.lower() == "b":
        s7b()


def s6a():
    print(''' you start making conversation with the people you're sitting with when suddenly the trains comes to a sharp halt.
    you look out of the window and see that you're stranded in some forest. you rush out of the train to see how you can get home and THERE!
    there are centaurs helping the students up their back and bringing them to the school. you start running towards them but you're too late, 
    they took off without you. now you're actually stranded.
    do you look for something to get you home?
    A. yes''')
    choice = input (">>>")
    if choice.lower() == "a, yes":
        s8a()


def s5b():
    print(''' you start looking around for something to get you to school while trying to stay calm. you start yelling out help in the hope
    for someone to hear you. suddenly you hear something behind you. you look around and see a group of centaurs. they heard you panicking!
    the centaurs tell you that they'll help you if you i give them something in return. what do you give them?
    A. give them home made cookies
    B. give an old sock''')
    choice = input (">>>")
    if choice.lower() == "a":
        s7a()
        s6b()
    elif choice.lower() == "b":
        s7b()


def s7a():
    print(''' the centaurs accept your offer and pull you on their backs and start running. you feel relief flush over you because finally you're going to school.
    but said relief is short lived as you fall off the back of the centaur but they keep running. now you're lost, again.''')


def s6b():
    print(''' you run in the forest in the hopes to find something but alas, you're completly lost with no way back.
    what do you do?
    A. start walking north in the hope to find a path tot the school.
    B. try to find your way back to the train''')
    choice = input (">>>")
    if choice.lower() == "a":
        s8a()
    elif choice.lower() == "b":
        s8b()

    
def s7b():
    print(''' the centaurs get mad because your offer disrespected them. they start attacking you. 
    what do you do?
    A. fight back
    B. run away''')
    choice = input (">>>")
    if choice.lower() == "a":
        s9a()
    elif choice.lower() == "b":
        s6b()


def s9a():
    print(''' you start fighting back but soon realize that the centaurs are way stronger then you and then SLASH!
    you're injured! the centaurs take pity on you and tell you that they'll bring you to school if you give them something else
     what do you give them?
    A. give them home made cookies
    B. give an old sock''')
    choice = input (">>>")
    if choice.lower() == "a":
        s7a()
        s6b()
    elif choice.lower() == "b":
        s7b()



def s8a():
    print(''' you start walking north and keep walking and walking and walking and walking until you've reached the end of the forest.
    you're standing infront ofa river and hey! there's an old boat floating there! do you use the boat?
    A. yes
    B. no''')
    choice = input(">>>")
    if choice.lower() == "a":
        s9b()
    elif choice.lower() == "b":
        s8b()


def s8b():
    print(''' you walk back, trying to find your way back to the train, but the forest is so clsoed in that you can't find a clear path
    to walk. while walking you trip over something and you fall face first into the ground. after getting up you pick up the object and inspect it.
    it looks like a magic broom! 
    do you use it?
    A. yes
    B. no''')
    choice = input (">>>")
    if choice.lower() == "a":
        print('''you put the broom between your legs and use all your power in making it fly off but you just stand there, like a fool with a broom
        between their legs''')
        s10a()
        s9b()
    elif choice.lower() == "b":
        s10a()
        s9b()

    
def s10a():
    print(''' you continue walking in the forest. your legs are getting sore but you have no choice but to walk you keep and keep walking
    until you stop by a river with the old boat again. this time you do use the boat.''')


def s9b():
    print(''' you step into the boat, it creaks but you ignore it, hoping the boat won't fall apart.
    how are you gonna sail away?
    A. use your hands
    B. use a long stick you found''')
    choice = input (">>>")
    if choice.lower() == "a":
        s10b()
    elif choice.lower() == "b":
        s10b()


def s10b():
    print(''' you realize you're not moving no matter what you do. so now you only have two options left
    A. swim
    B. jump on the backs of the alligators in the water''')
    choice = input (">>>")
    if choice.lower() == "a":
        s11a()
    elif choice.lower() == "b":
        print (''' you start jumping only to immediatly fall off and almost get eaten by an aligator.
        i guess you have to swim now.''')
        s11a()


def s11a():
    print(''' you start swiming. it's a tough challenge but you're pushing yourself. you have to make it.
    finally after what felt like hours you've crossed the lake. 
    do you keep walking?
    A. yes
    B. no''')
    choice = input (">>>")
    if choice.lower() == "a":
        s12a()
    elif choice.lower() == "b":
        s11b


def s11b():
    print(''' do you make a campfire to keep you warm?
    A. yes
    B. no''')
    choice = input (">>>")
    if choice.lower() == "a":
        print(''' you start grabbing wood and sticks and making a small pile for the fire, only to realize that you don't know
        how to make a campfire''')
        s12a()
    elif choice.lower() == "b":
        s12a()


def s12a():
    print(''' you keep walking and after an eternity you see the school. you start screaming and crying of joy.
    do you run or walk to the school?
    A. run
    B. walk''')
    choice = input(">>>")
    if choice.lower() == "a":
        print(''' you start running at full speed towards the school only to see that the fence is closed shut''')
        s12b()
    elif choice.lower() == "b":
        print(''' you slowly walk to the school because you've used up all your energy by just getting to this point but alas, 
        you find out that the gate is closed''')
        s12b()


def s12b():
    print(''' do climb over the fence?
    A. yes
    B. no''')
    choice = input (">>>")
    if choice.lower() == "a":
        print(''' you walk back and then you take a big leap up the fence, you grab the top of the fence and pull yourself up. YOU DID IT- oh,
    you fell flat on your face but hey, at least you made it''')
        s14a()
    elif choice.lower() == "b":
        print(''' you look for another way inside and hey! there's a tiny hole in de side of the fence. you
        shawiggle your way in, ti was a tight fit but you made it.''')
        s14a()
    


def s14a():
    print(''' you rush into the school but oh no, you're still drenched.
    do you walk in like this or grab someone's bag in the hope for clothes?
    A. walk ik like this
    B. take someone's bag''')
    choice = input(">>>")
    if choice.lower() == "a":
        s13b()
    elif choice.lower() == "b":
        s13a()


def s13a():
    print(''' you snatch someone's bag before anyone notices. you look into the bag but there are no clothes in it and
    for the cherry on top, a teacher caught you and asks what you're doing.
    do you lie to the teacher?
    A. yes
    B. no''')
    choice = input(">>>")
    if choice.lower() == "a":
        print(''' the teacher looks at you with a "are you serious?" face. the teacher just shakes his head and
        drags you into the great hall right as your name it called. time for you to get sorted.''')
        s15a()
    elif choice.lower() == "b":
        print(''' the teacher just shakes his head and drags you into the great hall right as your name is called.
        it's time for you to get sorted''')
        s15a()


def s13b():
    print(''' you walk into the great hall right as your name is called.
    it's time for you to get sorted''')


def s15a():
    number = random.randint(1,4)
    if number == 1: print ("you got sorted in Slytherin WOOOOOO")

    elif number == 2: print ("you got sorted in griffendor WOOOOO")

    elif number == 3: print ("you got sorted in ravenclaw WOOOO")
    
    elif number == 4: print ("you got sorted in huffelpuff WOOOOO")




print(required)
print (intro())