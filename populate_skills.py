from apployment_site.models import Skill

# read in text file
ins = open("t1.txt")
    array = []
    for line in ins:
        x = line.replace("\n", "")
        if x[0].isalpha():
            x = x[0].upper() + x[1:]
        skill = Skill(skill=x)
        skill.save()
