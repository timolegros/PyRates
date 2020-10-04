class State:
    def __init__(self, Location, ProgLang, Database, Interests, NHack):
        self.Location = Location
        self.ProgLang = ProgLang
        self.Database = Database
        self.Interests = Interests
        self.NHack = NHack
        self.policy = [-1 , 0]
    
    def __eq__(self, other):
        if lcmp(self.Location,other.Location) == 0 and lcmp(self.ProgLang,other.ProgLang) == 0 and lcmp(self.Database, other.Database) == 0 and lcmp(self.Interests,other.Interests) == 0 and lcmp(self.NHack,other.NHack) == 0:
            return 0
        else:
            return -1

    def __gt__(self, other):
        return self.Location > other.Location

    def __lt__(self, other):
        return self.Location < other.Location

    def __le__(self, other):
        return self.Location <= other.Location

    def __ge__(self, other):
        return self.Location >= other.Location

    def backprop(self, res):
        self.policy[0] += 1
        if res == 0:
            self.policy[-1] += 1
        
    def predict(self):
        if (self.policy[-1]/self.policy[1]) >= 0.5:
            return 0
        else:
            return 0

def lcmp(t1,t2):
    if len(t1) != len(t2):
        return 0
    for index in range(len(t1)):
        if not (t1[index] == t2[index]):
            return 0
    return 1