from time import sleep

stat_cloud = {
    'risk': 0,
    'exploration': 0,
    'resilience': 0,
    'detective': 0,
    'lucky': 0
}
#delay = 0.039
def type_effect(text, delay=0.0, newline=True):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    if newline:
        print()

def get_choice(prompt, partnerThoughts = ""):
    choice = input(prompt)
    if choice == '1':
        print(f"\nPlayer Stats:\nRisk - {stat_cloud['risk']},\tExploration - {stat_cloud['exploration']}")
        choice = get_choice(prompt, partnerThoughts)
    elif choice == '2':
        type_effect(partnerThoughts)
        choice = get_choice(prompt)
    return choice

def guide():
    type_effect("Thankyou for playing Zenevrie : The murder mystery that changes with your choices. During any choice , use 1 to view your current stats, or 2 to ask the thoughts of your partner.")