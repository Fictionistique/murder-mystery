import random

male_names = [
    'Aaron', 'Abraham', 'Adam', 'Adrian', 'Alex', 'Alexander', 'Andrew', 'Anthony', 'Austin', 'Benjamin',
    'Blake', 'Bradley', 'Brandon', 'Brian', 'Caleb', 'Cameron', 'Carl', 'Carter', 'Charles', 'Christian',
    'Christopher', 'Cole', 'Connor', 'Daniel', 'David', 'Dennis', 'Dominic', 'Dylan', 'Edward', 'Elijah',
    'Elliot', 'Ethan', 'Evan', 'Felix', 'Frank', 'Gabriel', 'George', 'Grant', 'Gregory', 'Harrison',
    'Henry', 'Hudson', 'Hunter', 'Ian', 'Isaac', 'Jack', 'Jacob', 'James', 'Jason', 'Jeffrey',
    'Jeremy', 'John', 'Jonathan', 'Jordan', 'Joseph', 'Joshua', 'Justin', 'Kevin', 'Kyle', 'Liam',
    'Logan', 'Lucas', 'Luke', 'Marcus', 'Mark', 'Mason', 'Matthew', 'Max', 'Michael', 'Nathan',
    'Nicholas', 'Noah', 'Oliver', 'Oscar', 'Owen', 'Patrick', 'Paul', 'Peter', 'Philip', 'Raymond',
    'Richard', 'Robert', 'Ryan', 'Samuel', 'Scott', 'Sean', 'Simon', 'Stephen', 'Steven', 'Thomas',
    'Timothy', 'Tyler', 'Victor', 'Vincent', 'Walter', 'William', 'Wyatt', 'Zachary'
]

indian_male_names = [
    "Veerendra", "Ishaan", "Madhav", "Anirudh", "Bhupendra", "Parth", "Shravan", "Rambilas", "Bhaskar", "Vibhor"
]

indian_last_names = [
    'Sharma', 'Patel', 'Gupta', 'Singh', 'Reddy', 'Iyer', 'Desai', 'Joshi', 'Kumar', 'Chopra'
]


female_names = [
    'Abigail', 'Adele', 'Adeline', 'Alexa', 'Alice', 'Alicia', 'Allison', 'Alyssa', 'Amanda', 'Amber',
    'Amelia', 'Amy', 'Anastasia', 'Andrea', 'Angela', 'Angelica', 'Anna', 'Anne', 'Ariana', 'Ariel',
    'Ashley', 'Audrey', 'Aurora', 'Autumn', 'Ava', 'Bailey', 'Barbara', 'Beatrice', 'Bella', 'Bethany',
    'Bianca', 'Briana', 'Brianna', 'Camila', 'Carla', 'Carmen', 'Caroline', 'Cassandra', 'Catherine', 'Cecilia',
    'Charlotte', 'Chloe', 'Christina', 'Claire', 'Clara', 'Courtney', 'Daisy', 'Dana', 'Danielle', 'Daphne',
    'Delilah', 'Diana', 'Dorothy', 'Eden', 'Edith', 'Eleanor', 'Elena', 'Eliana', 'Elise', 'Elizabeth',
    'Ella', 'Ellen', 'Ellie', 'Eloise', 'Emily', 'Emma', 'Erin', 'Esme', 'Eva', 'Evelyn',
    'Faith', 'Fiona', 'Gabriella', 'Genesis', 'Genevieve', 'Georgia', 'Giselle', 'Grace', 'Hailey', 'Hannah',
    'Harper', 'Hazel', 'Heather', 'Heidi', 'Holly', 'Isabel', 'Isabella', 'Ivy', 'Jade', 'Jasmine',
    'Jennifer', 'Jessica', 'Jocelyn', 'Josephine', 'Julia', 'Juliana', 'Juliet', 'June', 'Katherine', 'Kayla'
]

gnc_names = [
    'Alex', 'Avery', 'Blake', 'Cameron', 'Casey', 'Dakota', 'Emery', 'Finley', 'Harper', 'Jaden',
    'Jordan', 'Kai', 'Kendall', 'Logan', 'Mackenzie', 'Morgan', 'Quinn', 'Reese', 'River', 'Rowan', 'Taylor'
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson",
    "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner",
    "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy", "Cook",
    "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos",
    "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza",
    "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes", "Gonzales",
    "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham", "Reynolds",
    "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson", "Ellis", "Tran", "Medina",
    "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens", "Harrison", "Fernandez", "McDonald", "Woods",
    "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen", "Freeman", "Webb", "Tucker", "Guzman", "Burns",
    "Crawford", "Olson", "Simpson", "Porter", "Hunter", "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon",
    "Munoz", "Hunt", "Hicks", "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar",
    "Fox", "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens", "Soto",
    "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins", "Arnold", "Pierce", "Vazquez",
    "Hansen", "Peters", "Santos", "Hart", "Bradley", "Knight", "Elliott", "Cunningham", "Duncan", "Armstrong", "Hudson",
    "Carroll", "Lane", "Riley", "Andrews", "Alvarado", "Ray", "Delgado", "Berry", "Perkins", "Hoffman", "Johnston",
    "Matthews", "Peña", "Richards", "Contreras", "Willis", "Carpenter", "Lawrence", "Sandoval", "Guerrero", "George",
    "Chapman", "Rios", "Estrada", "Ortega", "Watkins", "Greene", "Nuñez", "Wheeler"
]

def set_names():
    richguy_firstname = random.choice(male_names)
    richguy_lastname = random.choice(last_names)
    butler_firstname = random.choice(indian_male_names)
    butler_lastname = random.choice(last_names)
    female_servant_firstname = random.choice(female_names)
    female_servant_lastname = random.choice(last_names)
    kid_firstname = random.choice(male_names)
    kid_lastname = female_servant_lastname
    male_servant_firstname = random.choice(indian_male_names)
    male_servant_lastname = random.choice(indian_last_names)
    enby_servant_firstname = random.choice(gnc_names)
    enby_servant_lastname = random.choice(last_names)
    list1 = [0, 1, 2]
    sidekick_gender = random.choice(list1)
    if sidekick_gender == 0:
        sidekick_firstname = random.choice(male_names)
    elif sidekick_gender == 1:
        sidekick_firstname = random.choice(female_names)
    else:
        sidekick_firstname = random.choice(gnc_names)
    sidekick_lastname = random.choice(last_names)
    richguy = richguy_firstname + ' ' + richguy_lastname
    butler = butler_firstname + ' ' + butler_lastname
    female_servant = female_servant_firstname + ' ' + female_servant_lastname
    kid = kid_firstname + ' ' + kid_lastname
    male_servant = male_servant_firstname + ' ' + male_servant_lastname
    enby_servant = enby_servant_firstname + ' ' + enby_servant_lastname
    sidekick = sidekick_firstname + ' ' + sidekick_lastname
    character_list = [richguy, butler, female_servant, kid, male_servant, enby_servant, sidekick, sidekick_gender]
    return character_list