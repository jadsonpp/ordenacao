class Person:
    def __init__(self,email,gender,uid,birthdate,height,weight):
        self.email      = email
        self.gender     = gender
        self.uid        = uid
        self.birthdate   = birthdate
        self.height     = height
        self.weight     = weight

    def showData(self):
        print("E-mail: "+self.email)
        print("Gender: "+self.gender)
        print("Uid: "+self.uid)
        print("birthdate: "+self.birthdate)
        print("height: "+self.height)
        print("weight: "+self.weight)
    
    def showUid(self):
        print("uid:"+ self.uid)
        
        

#Compare two classes and return -1 if p1 is lower, 0 if both are equals, 1 if p1 is higher
def compareTo(p1:Person , p2:Person): 
    if(p1.uid > p2.uid):
        return 1
    elif (p1.uid < p2.uid):
        return -1
    #caso não ache.
    return 0

def showUids(persons:list):
    for person in persons:
        person.showUid() 
         


