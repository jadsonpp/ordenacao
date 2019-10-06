class Person:
    def __init__(self,email,gender,uid,birthday,height,weight):
        self.email      = email
        self.gender     = gender
        self.uid        = uid
        self.birthday   = birthday
        self.height     = height
        self.weight     = weight

    def showData(self):
        print("E-mail: "+self.email)
        print("Gender: "+self.gender)
        print("Uid: "+self.uid)
        print("birthday: "+self.birthday)
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
         


#p1 = Person('saodasd@gmail.com','M','123123b123a','1992-10-10',192,78)
#p2 = Person('saodasda@gmail.com','M','123123b123b','1992-10-10',192,77)
#print(compareTo(p1,p2))