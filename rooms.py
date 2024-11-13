from mechanics import *

visitedRoom = {'visitedBedroom' : False, 'visitedServantsQuarters' : False, 'visitedLawn' : False, 'visitedBathroom' : False, 'inJudgementCall' : False}
seenChecks = {'seenRichGuy' : False, 'seenButler' : False, 'seenFemaleServant' : False, 'seenKid' : False, 'seenMaleServant' : False, 'seenEnbyServant' : False}
chapterNum = 0
detectivePath = "Unknown"
resiliencePath = "Unknown"
murderWeapon = "Not Found"
yName = ""

# List of characters
# 0 - RichGuy
# 1 - Butler
# 2 - FemaleServant
# 3 - Kid
# 4 - MaleServant
# 5 - EnbyServant
# 6 - Sidekick
# 7 - SidekickGender

char_list = characters_randomizer.set_names()

clues = {}
for i in char_list[:7]:
    clues[i] = []

if (char_list[7] == 0):
    sidekickPronouns1 = 'HE'
    sidekickPronouns2 = 'HIM'
    sidekickPronouns3 = 'HIS'
elif (char_list[7] == 1):
    sidekickPronouns1 = 'SHE'
    sidekickPronouns2 = 'HER'
    sidekickPronouns3 = 'HER'
else:
    sidekickPronouns1 = 'THEY'
    sidekickPronouns2 = 'THEM'
    sidekickPronouns3 = 'THEIR'

split_char_list = [name.split() for name in char_list[:7]]

#Living Room - Cold Open


def game():
    def livingroom1():
        global chapterNum
        chapterNum = 0
        chapterNum += 1
        type_effect('Chapter ' + str(chapterNum) + ': Welcome to the life of Private Detective ', newline = False)
        global yName
        yName = get_choice('', partnerThoughts = f"{split_char_list[6][0]}: \"I\'d say John sounds good enough?\"")
        
        #Add more clues
        type_effect('The day was cold as it could be when you reached ' + char_list[0] + '\'s estate. A layer of fog covered the ground. His property looked just like you expected. Gothic architecture, well maintained, and', newline = False)
        type_effect('...', 0.7, False)
        type_effect(' lifeless.\nLuckily, you\'re here with your new apprentice, ' + char_list[6] + '. You assured ' + sidekickPronouns2.lower() + ' that it won\'t take long to be done with this.\n\n' + yName + ': \"The smell\'s the worst part, and they\'ve taken care of the body so we should be fine\"\n'+ sidekickPronouns1.capitalize() +' snorts', newline = False)
        if char_list[7] == 2:
            print('\b', end = '')
        type_effect('. You both walked up to the front door and rang the doorbell. The door creaked open, revealing the Butler ' + char_list[1] + ' standing there, looking as stoic as ever. You eyeballed him, he\'s well dressed. A grim expression on his face. His eyes never meeting yours.\n')
        seenChecks['seenButler'] = True
        type_effect('Butler: \"Good evening, it\'s unfortunate we had to call you under these circumstances. But it is of utmost important for the estate to ensure none of the staff was involved in this incident. Please, come in."')
        type_effect('You and ' + split_char_list[6][0] + ' followed the Butler into the living room. The room was dimly lit, the only light coming from the fireplace. There was a grand staircase, a chandelier, and a large portrait of ' + split_char_list[0][1] + ' hanging above the fireplace. It was a single floor with a very high ceiling. The stairs leading to an overhanging walkway and some balconies. Everyone who worked in the property was there at the edge of the staircase. A common expression of anxiety on everyone\'s faces, except a kid, who looked almost annoyed to be there.\n')
        type_effect('Butler: \"As you\'re aware, with the death -\" Weird emphasis on the word \'death\' \"- of Mr. ' + split_char_list[0][1] +', the property goes to the bank, with no one to heir it. In interest of those who have served Mr. ' + split_char_list[0][1] + ' throughout thick and thin, we require you to conduct your examination of the crime scene -\" Pause before saying crime scene \"- before the state officials desecrate the place.\"')
        clues[char_list[1]].append('Weird emphasis on the word \'death\'')
        clues[char_list[1]].append('Pause before saying \'crime scene\'')
        type_effect(split_char_list[6][0] + ': \"I did some background checks on these people. Most of them seem uninteresting, however the servants '+ char_list[4] + ' and ' + char_list[5] + ' have barely any legal records. Probably worth looking into.\"')
        clues[char_list[4]].append['No legal records']
        clues[char_list[5]].append['No legal records']
        type_effect('Make a choice: Question the servants or move on?',newline = False)
        choice = get_choice('(type \'servants\' or \'move on\'): ')
        print(choice)
        if choice == "servants" :
            seenChecks['seenMaleServant'] = True
            seenChecks['seenEnbyServant'] = True
            type_effect(split_char_list[6][0] + " signals both of them over.\n" + split_char_list[6][0] + ": \"Fine evening we're having folks, right?", newline = False)
            sleep(2)
            type_effect(' Ugh nevermind. I can\'t play coy.\" '+ split_char_list[4][0] + '\'s wearing raggedy clothes. His breath clearly molded by betel and tobacco. He doesn\'t fit this place.' + ' \"Why\'re your names not on any records?\"')
            type_effect(split_char_list[4][0] + ': \"Illegal immigrants.\" He just shrugged.')
            choice = get_choice('Make your choice:\n1. Seems like ' + char_list[0] + ' was quite accepting of you guys. [Risk: 1]\n2. Fair enough. Why did '+ split_char_list[0][0] +' keep you guys around? [Exploration: 1]\n3. I\'ll keep that in mind. [No change]\n (type \'assess\', \'doubt\', or \'accept)\'', partnerThoughts = split_char_list[6][0] + ': \"Not much here. Old guy just liked \'em.\"')
            if choice == 'assess':
                stat_cloud['risk'] += 1
                type_effect(split_char_list[5][0] + ': \"Yes, he was.\" His voice was cold and spiteful. \"May we go back to our duties now?\"')
                type_effect(split_char_list[6][0] + ' nods slightly and turns to you.\n' + split_char_list[6][0] + ': \"Let\'s check with the butler now. What was his name again? Ah, ' + split_char_list[1][0] + '.\"')
            elif choice == 'doubt':
                stat_cloud['exploration'] += 1
                type_effect(split_char_list[5][0] + ': \"He was a good man. Took me in when my family wouldn\'t even look me in the eyes. I owe him a lot. As for ' + split_char_list[4][0] + ', Bossman found him funny.\"\nThey leave.')
            elif choice == 'accept':
                type_effect('You nod and they leave.')
            else:
                type_effect('They leave.')
        
        type_effect('Butler: \"The murder took place two days ago, or yesterday during the night. ' + split_char_list[2][0]+ ', the maid found Mr.' + split_char_list[0][1] + ' on the bed with a stab wound. No murder weapon.\" He\'s saying all this without a single look into your eyes. It\'s disturbing, but he\'s probably doing it as a sign of respect. \"The murder weapon was not found. No one has been in or out of the estate so we doubt it has left the area. Let me tell you about the rooms.\n', newline = False)
        sleep(2)
        type_effect('There\'s a bedroom. Where the murder happened. Looks out to the lawn.\" You hear a voice break. \"The door to your left leads to the servant\'s quarters down the hall. The bath is the oak gate under the mezzanine. ',newline = False)
        if seenChecks['seenMaleServant'] == False:
            type_effect('\b\" There\'s a servant sitting near its gate. Raggedy clothes. Quite clear tobacco stains on his teeth. Probably never settled to rich living. \"',newline = False)
        type_effect('There are a couple of balconies but they\'ve been locked', newline = False)
        type_effect('...', 0.7, False)
        type_effect(' since the incident with Mr. ' + split_char_list[0][1] + '\'s wife, and there are no plans to open them. You will be chauffeured by the staff while you\'re here, they\'ll lock up after you. You\'re free to conduct your investigation now. We thank you for your service.')
        choice = get_choice('Make your choice: (type \'y\' to move to Chapter '+ str(chapterNum+1) +')')
        clear_output()
        type_effect("Switch rooms:\n1. Living Room[Judgement Call]\n2. Bedroom[Fishy Business]\n3. Servants' Quarter[The Reds]\n4. Lawn[A Breathe of Fresh Air]\n5. Bathroom[The Walls Have Ears]")
        choice = get_choice('Make your choice: (type \'judge\' or \'fish\' or \'red\' or \'air\' or \'wall\':)')
        if choice == 'judge':
            type_effect('There\'s no going back. Are you sure you\'ve made a decision and have someone to accuse?')
            choice = get_choice('Make your choice: (type \'y\' to confirm, \'n\' to go back:)')
            if choice == 'n':
                choice = get_choice('Make your choice: (type \'judge\' or \'fish\' or \'red\' or \'air\' or \'wall\':)')
            else:
                livingroom2()

        if choice == 'judge':
            livingroom2()
            return
        if choice == 'fish':
            bedroom()
            return
        if choice == 'red':
            quarter()
            return
        if choice == 'air':
            lawn()
            return
        if choice == 'wall':
            bathroom()
            return
        

            
    def lawn():
        global chapterNum
        clear_output()
        stat_cloud['exploration'] += 1
        type_effect('Exploration +1')
        if not (visitedRoom['visitedBathroom'] == True or visitedRoom['visitedBedroom'] == True or visitedRoom['visitedLawn'] == True or visitedRoom['visitedServantsQuarters'] == True):
            chapterNum += 1
            type_effect("Chapter " + str(chapterNum) + ": A Breathe Of Fresh Air")
            visitedRoom['visitedLawn'] = True
            chapterNum += 1
        type_effect("You head out to the lawn with " + split_char_list[6][0] + ". There's neatly cut grass. Except for a couple of patches around the corners. Someone did a pretty lazy job. The maid " + split_char_list[2][0] + " and her kid join you soon enough.")

       
        type_effect(split_char_list[2][0] + ": \"Mr. " + split_char_list[0][1] + " ", newline = False)
        if visitedRoom['visitedBedroom'] == True:
            type_effect('never really ', newline = False)
            clues[char_list[2]].append('Lied about ' + split_char_list[0][1] + '\'s liking for the lawn')
            global detectivePath
            detectivePath = char_list[2]
        type_effect("had a thing for this place. We had to take care of it as an ode to Mrs. " + split_char_list[0][1] + ". " + split_char_list[3][0] + ", this young man, and I keep things going around here.\"")
        choice = get_choice('Make your choice:\n1. Felt that way about the lawn, you say?\n2. Fair enough. What\'s with the kid looking weird at us?\n3. I\'ll keep that in mind.\n (type \'assess\', \'doubt\', or \'accept)\'', partnerThoughts = split_char_list[6][0] + ': \"The butler\'s voice break seemed to say more than he did.\"')
        if choice == 'assess':
            stat_cloud['risk'] += 1
            type_effect(split_char_list[2][0] + ': \"Yes, -\" Her eyes shift around. \"Would you like to take a look around?\"')
            choice = get_choice('Make your choice:(type \'y\' or \'n\')', partnerThoughts = split_char_list[6][0] + ': \"Doubt there\'s much else we need to know. I say we call her out.\"')
            if choice == 'y':
                stat_cloud['exploration'] += 1
                if visitedRoom['visitedBedroom'] == True:
                    type_effect('You look around. There\'s nothing significant wrong with the place. It\'s cold. You decide to head back inside.')
                else:
                    type_effect('You look around. The wind howls in your ears. There\'s something shining in a patch of glass. A gleam of red dripping down. You\'ve found the knife used to kill ' + char_list[0])
                    global murderWeapon
                    murderWeapon = 'lawn'
                    global resiliencePath
                    resiliencePath = char_list[2]
        elif choice == 'doubt':
            stat_cloud['exploration'] += 1
            type_effect(split_char_list[3][0] + ': \"You got a problem with that pig!?\" That was a scowl if you\'d ever heard one.')
            type_effect(split_char_list[6][0] + ': \"We... aren\'t exactly cops buddy.\" ' + sidekickPronouns1.capitalize() + ' turns')
            if char_list[7] == 2:
                print("\b")
            type_effect(' to you,  \"We should head somewhere else.\"')
        elif choice == 'accept':
            type_effect('You nod and they leave.')
        else:
            type_effect('They leave.')
        type_effect(split_char_list[6][0] + ': Where to next?')
        type_effect("Switch rooms:\n1. Living Room[Judgement Call]\n2. Bedroom\n3. Servants' Quarter\n4. Bathroom")
        if detectivePath == char_list[2]:
            partnerThoughtsInp = split_char_list[6][0] + ': \"I don\'t believe what we search after this matters too much.\"'
        else:
            partnerThoughtsInp = split_char_list[6][0] + ': \"I suggest we check out the bath"'
        choice = get_choice('Make your choice: (type \'judge\' or \'bedroom\' or \'quarter\' or \'bath\':)', partnerThoughtsInp)
        if choice == 'judge':
            livingroom2()
            return
        if choice == 'bedroom':
            bedroom()
            return
        if choice == 'quarter':
            quarter()
            return
        if choice == 'bath':
            bathroom()
            return

    
    #TBD
    def quarter():
        global chapterNum
        clear_output()
        stat_cloud['exploration'] += 1
        type_effect('Exploration +1')
        if not (visitedRoom['visitedBathroom'] == True or visitedRoom['visitedBedroom'] == True or visitedRoom['visitedLawn'] == True or visitedRoom['visitedServantsQuarters'] == True):
            chapterNum += 1
            type_effect("Chapter " + str(chapterNum) + ": The Reds")
            visitedRoom['visitedServantsQuarters'] = True
            chapterNum += 1
        type_effect("This path is being worked upon. Please check the changelogs to know when the update arrives. You are being redirected to the final room. " + split_char_list[5][0] + " is a revolutionary and has radical ideas about social heirarchy. But you don\'t find anything incriminating against them.\n")
        sleep(6)
        livingroom2()
    
    
    def bathroom():
        global chapterNum
        
        clear_output()
        stat_cloud['exploration'] += 1
        type_effect('Exploration +1')
        choice = ""
        if not (visitedRoom['visitedBathroom'] == True or visitedRoom['visitedBedroom'] == True or visitedRoom['visitedLawn'] == True or visitedRoom['visitedServantsQuarters'] == True):
            chapterNum += 1
            type_effect("Chapter " + str(chapterNum) + ": The Walls Have Ears")
            visitedRoom['visitedBathroom'] = True
            chapterNum += 1
            type_effect('As you and ' + split_char_list[6][0] + ' walk towards the oak door. You notice deep red stains on the lower half of the wall outside.\n' + split_char_list[6][0] + ':\"No signs of struggle, right? These folks haven\'t talked about any sounds they heard that night. You think what I\'m thinking?\"')
            choice = get_choice('Make your choice:\n1. You think it\'s blood too?\n2. Can\'t be blood, definitely not here. Let\'s just take a quick look around.\n(type \'believe\' or \'doubt\'):', partnerThoughts= split_char_list[6][0] + ': It\'s a weird place for the struggle to have happened. But we might be on to something.')
            if choice == 'believe':
                type_effect(split_char_list[6][0] + ': \"Definitely. Let\'s check out the inside. I\'ll take a sample on the way out.\"')
            elif choice == 'doubt':
                type_effect(split_char_list[6][0] + ':\" Well. Fair enough. Let\'s see what awaits us inside.\"')
        type_effect('You enter the bath. It\'s tiled with shiny white marble. Clean as a cloud. Tall ceiling and a hanging chandelier. And a waist high mirror from where ' + split_char_list[4][0] + ' looked into your eyes. He\'s got his back towards you. His hands crushing something between them. He turns around. Empties his hands between his teeth and lower lips and walks to the exit.')
        if choice == 'believe':
            type_effect('\nExploration +1', newline = False)
            type_effect(': Idiot Within Me\n', 0.35)
            type_effect('You stand there. Embarrassed at your ignorance. It\'s hard to make a bigger fool of ourselves.')
        type_effect(split_char_list[6][0] + ': \"Not much seems off here. Shall we move on or do you want to hang around a while?\"')
        global resiliencePath
        resiliencePath = char_list[4]
        choice = get_choice('Make your choice:(type \'leave\' or \'wait\')')
        if choice == 'leave':
            choice = get_choice('Make your choice: (type \'judge\' or \'bedroom\' or \'quarter\' or \'lawn\':)', partnerThoughts = split_char_list[6][0] + ': \"I suggest we wait a bit and look around.\"')
            if choice == 'judge':
                livingroom2()
                return
            if choice == 'bedroom':
                bedroom()
                return
            if choice == 'quarter':
                quarter()
                return
            if choice == 'lawn':
                lawn()
                return
        elif choice == 'wait':
            type_effect('You hear some hush voices coming from near the window looking out to the lawn. ' + split_char_list[4][0] + ' seems to be distracted, standing near the door and lost in his own world. You move closer to the window. It sounds like the maid\'s kid is talking to her.\n' + split_char_list[3][0] + ': \"You don\'t have to worry mom. They\'re never tracing it back to ' + split_char_list[5][0] + '.', newline = False)
            if visitedRoom['visitedLawn'] == False:
                type_effect('. I doubt they have half a mind to even look at the place I\'ve shoved it away to.\"')
            type_effect(split_char_list[2][0] + ': \"It\'s not exactly them that I\'m worried about. It\'s you.\"')
            if visitedRoom['visitedLawn'] == True:
                resiliencePath = char_list[3]
                global detectivePath
                detectivePath = char_list[5]
            
            choice = get_choice('Make your choice:(type \'accuse\' or \'explore\')', partnerThoughts = split_char_list[6][0] + ': I suggest we take a look at the servants\' quarters first. Might tell us more about the involvement of '+ split_char_list[5][0] + '.')
            if choice == 'accuse':
                livingroom2()
            elif choice == 'explore':
                choice = get_choice('Make your choice: (type \'judge\' or \'bedroom\' or \'quarter\' or \'lawn\':)', partnerThoughts = split_char_list[6][0] + ': \"I suggest we wait a bit and look around.\"')
                if choice == 'judge':
                    livingroom2()
                    return
                if choice == 'bedroom':
                    bedroom()
                    return
                if choice == 'quarter':
                    quarter()
                    return
                if choice == 'lawn':
                    lawn()
                    return


    #TBD
    def bedroom():
        global chapterNum
        clear_output()
        stat_cloud['exploration'] += 1
        type_effect('Exploration +1')
        if not (visitedRoom['visitedBathroom'] == True or visitedRoom['visitedBedroom'] == True or visitedRoom['visitedLawn'] == True or visitedRoom['visitedServantsQuarters'] == True):        
            chapterNum += 1
            type_effect("Chapter " + str(chapterNum) + ": Fishy Business")
            visitedRoom['visitedBedroom'] = True
            chapterNum += 1
        type_effect("This path is being worked upon. Please check the changelogs to know when the update arrives. You are being redirected to the final room.")
        sleep(4)
        livingroom2()
    
    
    def livingroom2():
        global chapterNum
        global resiliencePath
        global detectivePath
        global yName
        clear_output()
        stat_cloud['exploration'] += 1
        type_effect('Exploration +1')
        type_effect("Chapter " + str(chapterNum) + ": Judgement Call")
        visitedRoom['inJudgementCall'] = True
        type_effect('Everyone gathers around the stairway. Looking intently at you. The same anxiety in everyone\'s eyes. Except for ' + resiliencePath.split()[0] + ' who seems weirdly relaxed.\nButler : \"Well ' + yName + ', have you reached a conclusion?\"')
        type_effect(yName + ': Yes, we\'ve looked over everything we needed to know. ' + char_list[0] + ' was murdered by ', newline = False)
        choice = get_choice('Make your choice:(type \'butler\' or \'maid\' or \'kid\' or ' + split_char_list[4][0] + ' or ' + split_char_list[5][0] + ')')
        if choice == 'butler':
            choice = char_list[1]
        elif choice == 'maid':
            choice = char_list[2]
        elif choice == 'kid':
            choice = char_list[3]
        elif choice == split_char_list[4][0]:
            choice = char_list[4]
        elif choice == split_char_list[5][0]:
            choice = char_list[5] 
        
        type_effect('You hear gasps from the group. The butler\'s expression remains unchanged.\n\nButler: \"And what exactly makes you believe that?\"')
        type_effect('Your clues were: ')
        for i in clues[choice]:
            type_effect('- ' + i + '\n')
        kickOut = ''
        if clues[choice] == []:
            type_effect('Nothing',0.5)
        choice1 = get_choice('Make your choice:(type \'mention clues\' or \'gut feeling\'):')
        if choice1 == 'mention clues' and clues[choice] == []:
            type_effect('Risk +3')
            stat_cloud['risk'] += 3
            type_effect('Butler:\"I couldn\'t have had been more wrong in inviting you here. Please leave and let us be.\"')
            failState()
        else:
            diceRoll = random.randint(1,200)
            if diceRoll == 20:
                lucky = True
            if choice == detectivePath:
                type_effect('Risk +1')
                stat_cloud['risk'] += 1
                type_effect(choice + ': \"You will regret this ' + yName + '!\"\nFor the first time, you see a change in the Butler\'s expressions, as they turn to disappointment.\nButler:\"I apologise in their behalf. Thank you for your service ' + yName + ', we are grateful to you. The authorities will deal with this', newline = False)
                type_effect('...', 0.7, False)
                type_effect(' letdown of a person.')
                type_effect('You and ' + split_char_list[6][0] + ' walk out the mansion.\n' + yName + ': \"Told you, in and out, no time at all.\"\n' + sidekickPronouns1.capitalize() + 'chuckles', newline = False)
                if char_list[7] == 2:
                    print('\b')
                type_effect('\nThe End', 0.35)
                return
            elif choice == resiliencePath:
                type_effect('Risk +2')
                stat_cloud['risk'] += 2
                type_effect(choice.split()[0] + ': \"No! It can\'t be! You\'ve messed up somewhere. I would never do something like that to Mr.' + split_char_list[0][1] + '! Please, you have to listen to me.\"\nButler:\"There isn\'t nothing to listen to.\" There\'s a deep sadness on the Butler\'s face. \"Thank you for your service ' + yName + '. It\'s better if you leave now.\"')
                type_effect('...', 0.7, False)
                type_effect(' Exploration -1: I\'ve won, but at what cost?')
                type_effect('You walk out into the sunset. It\'s all done. But that dots still feel disconnected. Something feels off, you just can\'t tell what it is.')
                type_effect('The End', 0.35)
                return
            elif lucky:
                stat_cloud['lucky'] += 1
                type_effect('You\'ve unlocked a rare ending. Unfortunately, it is currently in progress. Please check the changelogs to know when the update arrives. You are being redirected to a special end scene.')
                sleep(4)
                specialEnd()
                return

    def specialEnd():
        type_effect('As you set your step outside. ' + detectivePath.split()[0] + ' stops you. Everyone else is occupied with themselves, with no idea about what ' + detectivePath.split()[0] + ' is saying.\n' + detectivePath.split()[0] + ':\"Man, I can\'t believe you couldn\'t tell it was me.\" A laughter echoes in your ears as the curtains fall.')
        type_effect('The End', 0.35)
        return
    def failState():
        type_effect('Unfortunately, you have failed. This ending is currently in progress. Please check the changelogs to know when the update arrives. Thank you for playing!')
        sleep(2)
        return()
    livingroom1()