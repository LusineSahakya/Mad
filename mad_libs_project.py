import random

choosed_number = input("Enter the number from 1 to 3: ")
if choosed_number == 4:
    choosed_number = random.randint(1, 3)
if choosed_number == "1": 
    number = input("Enter a Number: ") 
    measure_of_time = input("Enter the Measure of time: ")
    mode_of_transportation = input("Enter Mode of Transportation: ") 
    adjective = input("Enter Adjective: ") 
    adjective2 = input("Enter Adjective2: ") 
    noun = input("Enter Noun: ") 
    color = input("Enter Color: ") 
    part_of_body = input("Enter Part of the Body: ") 
    verb = input("Enter Verb: ") 
    number2 = input("Enter Number2: ") 
    noun2 = input("Enter Noun2: ") 
    noun3 = input("Enter Noun3: ") 
    part_of_body2 = input("Enter Part of the Body 2: ") 
    noun4 = input("Enter Noun4: ") 
    adjective3 = input("Enter Adjective3: ") 
    sillyWord = input("Enter Silly Word: ")
    print( "It was about " + number + measure_of_time + " ago when I arrived at the hospital in " + mode_of_transportation + ". The hospital is a/an " + adjective + " place, there are a lot of " + adjective2 + " " + noun + " here. There are nurses here who have " + color + " " + part_of_body + ". If someone wants to come into my room I told them that they have to " + verb + """ first. I've decorated my room with """ + number2 + " " + noun2 + "․ Today I talked to a doctor and they were wearing a " + noun3 + " on their " + part_of_body2 + " I heard that all doctors " + verb + " " + noun4 + " every day for breakfast. The most " + adjective3 + " thing about being in the hospital is the " + sillyWord + " " + noun + "!")
elif choosed_number == "2":
    proper__noun = input("""Enter Proper Noun (Person's Name)։ """)
    noun = input("Enter Noun: ") 
    adjective = input("Enter Adjective (Feeling): ") 
    verb = input("Enter Verb: ") 
    adjective2 = input("Enter Adjective2 (Feeling): ") 
    animal = input("Enter a(n) animal: ")
    verb2 = input("Enter Verb2: ") 
    color = input("Enter Color: ") 
    verb3 = input("Enter Verb (ending in ing): ") 
    adverb = input("Enter Adverb (ending in ly): ") 
    number = input("Enter Number: ") 
    measure_of_time = input("Enter the Measure of time։ ")
    sillyWord = input("Enter Silly Word: ") 
    noun2 = input("Enter Noun2: ")
    print(" This weekend I am going camping with " + proper__noun + ". I packed my lantern, sleeping bag, and " + noun + ". I am so " + adjective + " to " + verb + " in a tent. I am " + adjective2 + " we might see a(n) " + animal + """, I hear they’re kind of dangerous. """ + """While we’re camping, we are going to hike, fish, and """ + verb2 + ". I have heard that the " + color + " lake is great for " + verb3 + ". Then we will " + adverb + " hike through the forest for " + number + measure_of_time + ". If I see a " + color + " " + animal + " while hiking, I am going to bring it home as a pet! At night we will tell " + number + " " + sillyWord + " stories and roast " + noun2 + " around the campfire!!")
elif choosed_number == "3": 
    proper_noun = input("""Enter Proper Noun (Person's Name): """) 
    adjective = input("Enter Adjective (Feeling): ") 
    color = input("Enter Color: ") 
    animal = input("Enter a(n) animal: ") 
    place = input("Enter Place: ") 
    adjective2 = input("Enter Adjective2 (Feeling): ") 
    magical_creature = input("Enter Magical Creature (Plural): ") 
    adjective3 = input("Enter Adjective3: ") 
    magical_creature2 = input("Enter Magical Creature2 (Plural): ") 
    room = input("Enter Room in a House: ") 
    noun = input("Enter Noun: ") 
    noun2 = input("Enter Noun: ") 
    noun3 = input("Enter Noun(Plural)3: ") 
    adjective4 = input("Enter Adjective4: ") 
    noun4 = input("Enter Noun(Plural)4: ") 
    number = input("Enter Number: ") 
    measure_of_time = input("Enter the Measure of time։ ")
    verb = input("Enter Verb (ending in ing): ") 
    adjective5 = input("Enter Adjective5: ") 
    noun5 = input("Enter Noun5: ")
    print ( "Dear " + proper_noun + ", I am writing to you from a " + adjective + " castle in an enchanted forest. I found myself here one day after going for a ride on a " + color + " " + animal + " in "+ place + ". There are "+ adjective2 + " " + magical_creature + " and " + adjective3 + " " + magical_creature2 + " here! In the "+ room + " there is a pool full of " + noun + ". I fall asleep each night on a " + noun2 + " of " + noun3 + "and dream of" + adjective4 + " " + noun4 + ". It feels as though I have lived here for "+ number + " " + measure_of_time + ". I hope one day you can visit, although the only way to get here now is " + verb + " on a " + adjective5 + " " + noun5 + "!!")