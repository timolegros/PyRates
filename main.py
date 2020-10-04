import sqlite3
import pickle
from pathlib import Path
import copy
from sstate import State

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
    conn = sqlite3.connect('db.sqlite3')
    data = conn.execute("SELECT * FROM UserProfiles")
    return data

def parse(string):
    ans = []
    x = []
    for ch in string:    
        if ch == ';':
            ans.append(copy.copy(x))
            x = []
        x += ch
    ans.append(copy.copy(x))
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
    return hcat

def update_val():
    conn = sqlite3.connect('db.sqlite3')
    sql = '''UPDATE UserProfiles
             SET latest = 0,
             WHERE latest =1'''
    cur = conn.cursor()
    cur.execute(sql, 'UserProfiles')
    conn.commit()

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
            if tmp1 <= tmp2:
                c = tmp1
                tmp1 = tmp2
                tmp2 = c
            pdict[tuple([tmp1,tmp2])] = State([tmp1[0],tmp2[0]],[tmp1[1],tmp2[1]],[tmp1[2],tmp2[2]],[tmp1[3],tmp2[3]],[tmp1[4],tmp2[4]])
    save_obj(pdict, 'policy')

if __name__ == "__main__":
    my_file = Path('procolson.pkl')
    if not my_file.is_file():
        first_it()
    pdict = load_obj('policy')
    data = load_data()
    for rows in data:
        if rows[7] == 1:
            hk = catnhack(rows[3])
            pl = parse(rows[4])
            db = parse(rows[5])
            aoi = parse(rows(6))
            inp = [rows[2], pl, db, aoi, hk]           
    outlist = []
    for row in data:
        hk = catnhack(row[3])
        pl = parse(row[4])
        db = parse(row[5])
        aoi = parse(row(6))
        tmp1 = [row[2], pl, db, aoi, hk]
        if inp <= tmp1:
                c = inp
                inp = tmp1 
                inp = c 
        if pdict[tuple([inp, tmp1])].predict():
            outlist.append(row)
    update_val()
    



    

             
    