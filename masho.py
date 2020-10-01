"""
author: Bryson Rogers
Masho game:
This is a cute little game that pretends to predict your future.
"""
# These functions are a series of prompts that group answers by topic.
# Gets names of persons of interest.
def getSuitors():
    one = str(input("Who do you have a crush on? "))
    two = str(input("Who is your best friend? "))
    three = str(input("Who do you despise? "))
    four = str(input("Who was your childhood crush? "))
    return [one, two, three, four]

# Gets Job ideas.
def getJobs():
    one = str(input("What was your favorite job? "))
    two = str(input("What is your current job? "))
    three = str(input("what is your dream job? "))
    four = str(input("what was your worst job? "))
    return [one, two, three, four]

# Gets interesting pets.
def getAnimals():
    one = str(input("What is your favorite animal? "))
    two = str(input("What is your second favorite animal? "))
    three = "Dog"
    print("Your third animal entry is a dog!(hopefully you didn't put that down as your favorite animal)")
    four = str(input("What is the scariest animal you can think of? "))
    
# Should hopefully get some interesting numbers for kids.
def getKids():
    one = str(input("What is your favorite number? "))
    two = str(input("How many rooms are in your home? "))
    two = str(input("What is your ideal number of work days in a week? "))


    return [one, two, three, "a healthy dozen"]

# A make shift random number number generator.
def getRandomNumber():
    from datetime import datetime
    now = datetime.now()
    seconds = now.strftime("%S")
    num = int(seconds)
    one = num % 4
    two = num % 5
    return [one, two]

# Display's users predicted future
def showPrediction(name, home, marry, work, pet, chaos):
    print (name, " will live in a ", home ," and be married to ", marry, ".")
    print ("They will have ", chaos, "children, and a pet ", pet, ".")
    print (name, " will support all this by working as a ", work, ".")

    
# main prompts for users name, gets a random residence, calls prompts,
# then displays the users predicted future.
def main():
    name = input("What is your name? ")
    masho = ["Mansion", "Apartment", "Shack", "House", "Outhouse"]
    num = getRandomNumber()
    home = masho[num[1]]
    suitors = getSuitors()
    num = getRandomNumber()
    marry = suitors[num[0]]
    jobs = getJobs()
    num = getRandomNumber()
    work = jobs[num[0]]
    pets = getAnimals()
    num = getRandomNumber()
    pet = pets[num[0]]
    children = getKids()
    num = getRandomNumber()
    chaos = children[num[0]]

    showPrediction(name, home, marry, work, pet, chaos)
    



if __name__ == "__main__":
    main()