'''
 We have a repository of athletes.
 An athlete has a name, height in centimeters, and a profession.

 Typically, there is a clear correlation between being tall and
 playing basketball: If an Athlete is tall (we define being tall as having a height of at least 180)
 then s/he is a basketball player, and if s/he is not tall then
 s/he is not a basketball player. 
 
 In the code below:
 Bob is tall and plays basketball, and Alex is short and plays
 soccer, so they are typical. 
 Frank, Shorty and Jane are rare athletes.
 
 We want to print the names of all the rare athletes.
 
 Unfortunately we have a bug. Please fix it. 
 Use the opportunity to improve the code quality, until you feel comfortable putting your name behind it.
 
 *Do not change the behavior of the function "findAll". For example: When it gets a None value as input, it is expected to throw an TypeError.
'''

def find_rare_athletes(athletes=None):
    if (athletes == None):
          raise TypeError()

    if (len(athletes) < 1):
          return list()
        
    return [athlete[0] for athlete in athletes if is_athlete_rare(athlete)]
               
      

def is_athlete_rare(athlete=None):
     if (athlete == None):
        raise TypeError()
        
     if (athlete[1] >= 180 and athlete[2] != "basketball"):
        return True
     
     if (athlete[1] < 180 and athlete[2] == "basketball"):
        return True
     
     return False
    


athletes = [
       ("Bob", 190, "basketball"),
       ("Alex", 170, "soccer"),
       ("Frank", 130, "basketball"),
       ("Shorty", 175, "basketball"),
       ("Jane", 190, "chess"),
       ("John", 180, "chess")
]

print(find_rare_athletes(athletes))


