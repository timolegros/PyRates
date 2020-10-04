import sqlite3
import pickle
from pathlib import Path
from copy import *

class State:
    def __init__(self, Location, ProgLang, Database, Interests, NHack):
        self.Location = Location
        self.ProgLang = ProgLang
        self.Database = Database
        self.Interests = Interests
        self.NHack = NHack
        self.policy = [0 , 0]
    
    def __eq__(self, other):
        if lcmp(self.Location,other.Location) == 0 and lcmp(self.ProgLang,other.ProgLang) == 0 and lcmp(self.Database, other.Database) == 0 and lcmp(self.Interests,other.Interests) == 0 and lcmp(self.NHack,other.NHack) == 0:
            return 1
        else:
            return 0

    def backprop(self, res):
        self.policy[1] += 1
        if res == 1:
            self.policy[0] += 1
        
    def predict(self):
        if (self.policy[0]/self.policy[1]) >= 0.5:
            return 1
        else:
            return 0

def lcmp(t1,t2):
    if len(t1) != len(t2):
        return 0
    for index in range(len(t1)):
        if not (t1[index] == t2[index]):
            return 0
    return 1

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]
        
def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def load_data():
    conn = sqlite3.connect('procolson.db')
    data = conn.execute("SELECT * FROM info")
    return data

def parse(string):
    ans = []
    x = []
    for ch in string:    
        if ch == ';':
            ans.append(copy(x))
            x = []
        x += ch
    ans.append(copy(x))
    return ans

def catnhack(ha):
    if ha == 0:
            hcat = "0"
    elif ha >= 1 and ha <= 3:
            hcat = "1-3"
    elif ha >= 4 and ha <= 6:
            hcat = "4-6"
    elif ha >= 6 and ha <= 10:
            hcat = "6-10"
    else:
            hcat = "10"

def first_it():
    location = ["East Coast", "Midwest", "West Coast", "Southern US", "Northern US", "Eastern Canada", "Western Canada", "Atlantic Provinces", "Outside US/ Canada"]
    proglang = ["C", "Python", "Javascript", "Java", "C#", "C", "C++"]
    database = ["SQL", "MongoDB", "Firebase", "Oracle", "Redis"]
    areaofinterest = ["Web Development", "AI", "Product Management", "Big data"]
    hackathonsattended = ["0", "1-3", "4-6", "6-10", ">10"]
    plang = list(powerset(proglang))
    pdb = list(powerset(database))
    paoi = list(powerset(areaofinterest))
    pdict = {}
    temp = []
    c = 0
    for l in location:
        for lg in plang:
            for db in pdb:
                for aoi in paoi:
                    for ha in hackathonsattended:
                            temp[c] = [l,lg,db,aoi,ha]
                            c+=1
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            tmp1 = tuple(temp[i])
            tmp2 = tuple(temp[j])
            pdict[tuple([tmp1,tmp2])] = State([tmp1[0],tmp2[0]],[tmp1[1],tmp2[1]],[tmp1[2],tmp2[2]],[tmp1[3],tmp2[3]],[tmp1[4],tmp2[4]])
    save_obj(pdict, 'policy')

if __name__ == "__main__":
    my_file = Path('procolson.pkl')
    if not my_file.is_file():
        first_it()
    pdict = load_obj('policy')
    ###take in input and save to database###       
    data = load_data()
    inp = []

    for rows in data:
        hk = catnhack(rows[5])
        pl = parse(rows[2])
        db = parse(rows[3])
        aoi = parse(rows(4))
        tmp1 = [rows[1], pl, db, aoi, hk]
        if pdict[tuple([inp, tmp1])].predict():
            outlist.append(tmp1)

    ##push output
    outlist = []
    ##take in res
    res = []
    for index in range(len(outlist)):
        pdict[tuple([outlist[index], tmp1])].backprop(res[index])
    save_obj(pdict, 'policy')


    

             
    