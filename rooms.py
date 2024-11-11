import characters_randomizer
from mechanics import *
from IPython.display import clear_output # type: ignore

visitedRoom = {'visitedBedroom' : False, 'visitedServantsQuarters' : False, 'visitedLawn' : False, 'visitedBathroom' : False, 'inJudgementCall' : False}
seenChecks = {'seenRichGuy' : False, 'seenButler' : False, 'seenFemaleServant' : False, 'seenKid' : False, 'seenMaleServant' : False, 'seenEnbyServant' : False}
chapterNum = 0

questioned = False
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
        chapterNum += 1
        type_effect('Chapter ' + str(chapterNum) + ': Welcome to the life of Private Detective', newline = False)
        yName = get_choice('', partnerThoughts = f"{split_char_list[6][0]}: \"I\'d say John sounds good enough?\"")
        
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
        type_effect(split_char_list[6][0] + ': \"I did some background checks on these people. Most of them seem uninteresting, however the servants '+ char_list[4] + ' and ' + char_list[5] + ' have barely any legal records. Probably worth looking into.\"')
        type_effect('Make a choice: Question the servants or move on?',newline = False)
        choice = get_choice('(type \'servants\' or \'move on\'): ')
        print(choice)
        if choice == "servants" :
            seenChecks['seenMaleServant'] = True
            seenChecks['seenEnbyServant'] = True
            type_effect(split_char_list[6][0] + " signals both of them over.\n" + split_char_list[6][0] + ": \"Fine evening we're having folks, right?", newline = False)
            sleep(2)
            type_effect(' Ugh nevermind. I can\'t play coy.'+ split_char_list[4][0] + '\'s wearing raggedy clothes. His breath clearly molded by betel and tobacco. He doesn\'t fit this place.' + ' \"Why\'re your names not on any records?\"')
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
        type_effect('There\'s a bedroom. Where the murder happened. Looks out to the lawn.\" You hear a voice break. \"The door to your left leads to the servant\'s quarters down the hall. The bath is the oak gate under the mezzanine.\"',newline = False)
        if not seenChecks['seenMaleServant']:
            type_effect(' There\'s a servant sitting near its gate. Raggedy clothes. Quite clear tobacco stains on his teeth. Probably never settled to rich living. \"',newline = False)
        type_effect(' There are a couple of balconies but they\'ve been locked', newline = False)
        type_effect('...', 0.7, False)
        type_effect(' since the incident with Mr. ' + split_char_list[0][1] + '\'s wife, and there are no plans to open them. You will be chauffeured by the staff while you\'re here. You\'re free to conduct your investigation now. We thank you for your service.')
        choice = get_choice('(type \'y\' to move to Chapter '+ chapterNum+1 +')')
        chapterNum += 1
        clear_output()
    livingroom1()