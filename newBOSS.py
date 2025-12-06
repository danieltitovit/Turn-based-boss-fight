#-------------------------------------------------------------------------------------------------------------------------------------------------------------
HeroClass = 'NONE'
Answer = 'NONE'
choices = 0
checkBossHP = True
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
HeroHP = 100
BossHP = 300
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
BossDamage = 10
normalHeroDamage = 25
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
swordHeroDamage = 20
daggerHeroDamage = 10
greataxeHeroDamage = 30
# ------------------------------------------------------------------------------------------------------------------------
def chosenHeroClass():
    global normalHeroDamage
    global HeroClass
    if HeroClass == '2':
        global swordHeroDamage
        normalHeroDamage = swordHeroDamage
        return normalHeroDamage
    elif HeroClass == '1':
        global daggerHeroDamage
        normalHeroDamage = daggerHeroDamage
        return normalHeroDamage
    elif HeroClass == '3':
        global greataxeHeroDamage
        normalHeroDamage = greataxeHeroDamage
        return normalHeroDamage
    
def bossChallenges():
    # 1. Attack
    # 2. Block
    # 3. Dodge
    # 4. Critical attack
    import random
    global BossHP
    global HeroHP
    global choices
    global checkBossHP
    global HeroClass
    if checkBossHP == True:
        choices = random.randint(1, 4)
        if choices == 1:
            print('SIGGA sprints towards you and launches an attack!')
            HeroOptions()
            if HeroClass == '1':
            #dagger
                if Answer == '1':
                    print('Both his sword and your dagger clash! However Sigga manages to put pressure to you, resulting in you sustaining 3.5 chip damage!')
                    HeroHP = HeroHP - 3.5
                elif Answer == '2':
                    print('As you try to block his attack, you are pushed back, you only sustain 1 damage!')
                    HeroHP = HeroHP - 1
                elif Answer == '3':
                    print('You dodge his attack really easily!')
                elif Answer == '4':
                    print('You stand there.. waiting and then unleash an counter attack hitting the center of his body! He takes',normalHeroDamage * 1.25,'damage!')
                    BossHP = BossHP - normalHeroDamage * 1.25
            elif HeroClass == '2':
            #sword
                if Answer == '1':
                    print('Both of your swords clash! Both of you sustain 2.5 chip damage!')
                    HeroHP = HeroHP - 2.5
                    BossHP = BossHP - 2.5
                elif Answer == '2':
                    print('You block his attack, he however deals',1,'chip damage!')
                    HeroHP = HeroHP - 1
                elif Answer == '3':
                    print('As you dodge his attack, he sees an opening and goes for it, though he only manages to graze you with',3,'damage!')
                    HeroHP - HeroHP - 3
                elif Answer == '4':
                    print('You make an stance and wait.. then strike as you see an opening! You deal',normalHeroDamage * 1.425,'damage!')
                    BossHP = BossHP - normalHeroDamage * 1.425
            elif HeroClass == '3':
            #greataxe
                if Answer == '1':
                    print('You charge in and begin to attack, though he manages to dodge and strike an hit on you dealing',7.5,'damage!')
                    HeroHP = HeroHP - 7.5
                elif Answer == '2':
                    print('You manage to block the attack sustaining no injury!')
                elif Answer == '3':
                    print('You attempt to dodge the attack but he manages to strike an critical hit on you dealing',BossDamage * 1.35,'damage!')
                    HeroHP = BossDamage * 1.35
                elif Answer == '4':
                    print('You unleash an spinning attack, it breaks his guard and you deal',normalHeroDamage * 1.725,'damage!')
                    BossHP = normalHeroDamage * 1.725
        elif choices == 2:
            print('SIGGA stands on guard ready to take any of your hits!')
            HeroOptions()
            if HeroClass == '1':
                if Answer == '1':
                    print('You launch consecutive attacks on him however he parries it all, you fall back and make distance out of panic.')
                elif Answer == '2':
                    print('You wait.. nothing happens as you two look at each other dumbfounded.')
                elif Answer == '3':
                    print('..As you move he just watches at you, focused.')
                elif Answer == '4':
                    print('You focus on his legs, you then dash forward and make an light slash in great speeds! You manage to make an huge cut dealing',normalHeroDamage * 1.15,'damage!')
                    BossHP = BossHP - normalHeroDamage * 1.15
            elif HeroClass == '2':
                if Answer == '1':
                    print('You attack him with some slashes, you deal some',5,'chip damage!')
                    BossHP = BossHP - 5
                elif Answer == '2':
                    print('You make the same blocking stance as him, you two just stand there doing nothing at that point,')
                elif Answer == '3':
                    print('You begin.. running around to find an opening.')
                elif Answer == '4':
                    print('You unleash an critical attack, you manage to break his posture somehow, you deal',normalHeroDamage * 1.325,'damage!')
                    BossHP = BossHP - normalHeroDamage * 1.325
            elif HeroClass == '3':
                if Answer == '1':
                    print('You rush him and perform an heavy slash, it breaks his guard! You deal',10,'damage!')
                    BossHP = BossHP - 10
                elif Answer == '2':
                    print('You both stand there doing nothing, just looking at each other.')
                elif Answer == '3':
                    print('You begin walking slowly, focusing on your opponent.')
                elif Answer == '4':
                    print('You leap and unleash an heavy hit aimed at him, you send him flying, dealing',normalHeroDamage * 2,'damage!')
        elif choices == 3:
            print('SIGGA drops his guard, he taunts you, however he seems very focused.')
            HeroOptions()
            if HeroClass == '1':
                if Answer == '1':
                    print('You launch an attack at him.. he then counters at you, dealing you',BossDamage * 1.15)
                    HeroHP = HeroHP - BossDamage * 1.15
                elif Answer == '2':
                    print('You two look at each other, nothing happens.')
                elif Answer == '3':
                    print('You run around, perhaps you are trying to confuse him?')
                elif Answer == '4':
                    print('You leap forwards and unleash an critical blow aimed at his head, he dodges and manages to graze you dealing',BossDamage / 1.5,'damage!')
                    HeroHP = HeroHP - BossDamage / 1.5
            elif HeroClass == '2':
                if Answer == '1':
                    print('As you try to attack him he counters you dealing',BossDamage * 1.225,'damage!')
                    HeroHP = HeroHP - BossDamage * 1.225
                elif Answer == '2':
                    print('You make an guard stance, just standing there waiting, nothing happens.')
                elif Answer == '3':
                    print('You beging running, dude, why?')
                elif Answer == '4':
                    print('You launch an critical attack, focusing everything on attacking rather than guarding. He finds an opening and deals an critical blow dealing',BossDamage * 1.35,'damage!')
                    HeroHP = HeroHP - BossDamage * 1.35 
            elif HeroClass == '3':
                if Answer == '1':
                    print('The moment you attempt to attack he lowers his stance and counters you with an devastating blow that deals',BossDamage * 1.5,'damage!')
                    HeroHP = HeroHP - BossDamage * 1.5
                elif Answer == '2':
                    print('You two stand there doing nothing.')
                elif Answer == '3':
                    print('You begin walking around in circles doing nothing but staring at him.')
                elif Answer == '4':
                    print('You unleash an critical attack, charging at him, though he dodges it and takes some distance.')
        elif choices == 4:
            print('SIGGA leaps infront of you, with his charged attack, it seems like it is going to be a very big hit right now!')
            HeroOptions()
            if HeroClass == '1':
                if Answer == '1':
                    print('Without thinking about it, you just.. rush at him too mindlessly, you however do manage to graze him though you are hit with an devastating blow.')
                    BossHP = BossHP - normalHeroDamage / 2
                elif Answer == '2':
                    print('You block his attack, you manage to halve the damage somehow but he still manages to score a hit on you dealing',BossDamage * 1.425,'damage!')
                    HeroHP = HeroHP - BossDamage * 1.425
                elif Answer == '3':
                    print('You successfully dodged his attack!')
                elif Answer == '4':
                    print('As you launch your counter, out of sudden both your blade yet his clash, you both deal 5 chip damage to each other!')
                    HeroHP = HeroHP - 5
                    BossHP = BossHP - 5
            elif HeroClass == '2':
                if Answer == '1':
                    print('You try to attack, though both of your blades clash, you are then pushed back, your back hitting the wall causing you to be flourished with',7.5,'damage!')
                    HeroHP = HeroHP - 7.5
                elif Answer == '2':
                    print('You block the devastating attack, you are pushed away with',3,'chip damage!')
                    HeroHP = HeroHP - 3
                elif Answer == '3':
                    print('You dodge the attack, though he manages to graze you dealing',1.5,'damage!')
                    HeroHP = HeroHP - 1.5
                elif Answer == '4':
                    print('You two exchange critical attacks, your blades hit, you two deal',2,'chip damage to eachother!')
                    HeroHP = HeroHP - 2
                    BossHP = BossHP - 2
            elif HeroClass == '3':
                if Answer == '1':
                    print('You manage to propell the attack and deal him',2,'damage!')
                    BossHP = BossHP - 2
                elif Answer == '2':
                    print('You succesfully block the attack though he manages to score 1 hit on you dealing',2.25,'damage!')
                    HeroHP = HeroHP - 2.25
                elif Answer == '3':
                    print('As you chose to dodge, he finds an opening due to your slow speed, he deals',BossDamage * 1.625,'damage!')
                    HeroHP = BossDamage * 1.625
                elif Answer == '4':
                    print('You unleash an spinning attack, you catch him off-guard and then land an hit on him dealing',normalHeroDamage,'damage!')
                    BossHP = BossHP - normalHeroDamage
    elif BossHP < 0:
        exit(1)

def HeroOptions():
    global Answer
    global HeroName
    print('1. Attack')
    print('2. Block / Wait')
    print('3. Dodge')
    print('4. Critical / Counter')
    print('[MAKE A MOVE]')
    Answer = input('-> ')
    print('. . .')
    print('SIGGA :', BossHP)
    print(HeroName,':', HeroHP)
    print('. . .')
        

def bfContinue():
    global BossHP
    global checkBossHP
    checkBossHP = True
    if BossHP > 0:
        checkBossHP = True
        for i in range(0, 100):
            bossChallenges()
            if BossHP == 0 or BossHP < 0:
                print('..You have defeated Sigga.')
                print('[THANKS FOR PLAYING]')
                input('[ENTER TO LEAVE]')
                exit(1)
            if HeroHP == 0 or HeroHP < 0:
                print('...You have been defeated by Sigga.')
                print('[THANKS FOR PLAYING]')
                input('[ENTER TO LEAVE]')
                exit(1)
    elif BossHP < 0:
        checkBossHP = False
        print('..You have defeated Sigga.')
        print('[THANKS FOR PLAYING]')
        exit(1)

def bcHeroAnswer():
    print('BC Hero answer test successful.')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
def hcCheck():
    global HeroClass
    if HeroClass != 'X' or 'x':
        exit(1)
# intro
print('Welcome to the boss fight game!')
print('[DANIEL TITOVS FIRST EVER GAME]')
print('1. Start game')
print('2. End game')
print('3. Tutorial [UNFINISHED]') 
print('4. Credits [UNFINISHED]')
gameStartUp = input('-> ')
if gameStartUp == '2':
    exit(1)
elif gameStartUp == '1':
    print('-------------------------------------------------------------------------------------------')
    print('DAGGER: Low damage, more chances for counter, dodge and parry')
    print('SWORD: Normal, a great balance between the dagger and the greataxe')
    print('GREATAXE: High damage, less chances for counter, dodge and parry but more chances for block')
    print('-------------------------------------------------------------------------------------------')
    print('[YOU MAY NOW CHOOSE YOUR WEAPON, YOUR SELECTED WEAPON WILL ALSO AUTOMATICALLY SELECT YOUR CLASS]')
    print('1. DAGGER')
    print('2. SWORD')
    print('3. GREATAXE')
    HeroClass = input('-> ')
    if HeroClass == '1' or '2' or '3':
        chosenHeroClass()
elif gameStartUp == '3':
    print('3rd option test successfull')
    print('[END? - Y/N]')
    gameStartUp = input('-> ')
    if gameStartUp == 'Y' or 'y':
        exit(1)
elif gameStartUp == '4':
    print('4th option test succesfull')
    print('[END? - Y/N]')
    gameStartUp = input('-> ')
    if gameStartUp == 'Y' or 'y':
        exit(1)

if HeroClass == '1':
    print('[YOU HAVE BEEN GIVEN THE ASSASSIN CLASS]')
elif HeroClass == '2':
    print('[YOU HAVE BEEN GIVEN THE SOLDIER CLASS]')
elif HeroClass == '3':
    print('[YOU HAVE BEEN GIVEN THE BERSERKER CLASS]')
print('[CREATE AN NAME FOR YOUR HERO]')
HeroName = input('-> ')




# bassicaly the start of the game
print('. . . !')
print('You reach the final section of the long hallway that you have ventured, you are then met with an formidable foe.')
print('He clears his throat, then speaks, his words send shivers to your spine.')
print('Sigga, the fiercest one: "It seems that.. he has sent more worms like you to my.. manor, is that it..?" ')
print('Sigga, the fiercest one: "Well.. you know well that I cannot let you pass so eassily, so.." ')
print('Sigga, the fiercest one: "Let us have some fun yeah..?" ')
#
# true fight begins
print(' ! ! ! ')
# scenarios begin
bfContinue()
bossChallenges()

# 
