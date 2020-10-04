from sstate import State
import sys
import sqlite3
import pickle
from main import load_obj, save_obj, parse, catnhack

def main():
    inp = []
    prof = []
    print(sys.argv)
    for index in range(1, len(sys.argv)):
        inp.append(int(sys.argv[index]))
    conn = sqlite3.connect('db.sqlite3')
    data = conn.execute("SELECT * FROM UserProfiles")
    for row in data:
        if row[0] == inp[0] or row[0] == inp[1]:
            prof.append(row)
    pdict = load_obj('policy')
    ud = []
    for p in prof:
        hk = catnhack(p[3])
        pl = parse(p[4])
        db = parse(p[5])
        aoi = parse(p(6))
        lt = [p[2], pl, db, aoi, hk]
        ud.append(lt)
    if ud[0] <= ud[1]:
        c = ud[0]
        ud[0] = ud[1]
        ud[1] = c
    pdict[tuple(ud[0], ud[1])].backprop(inp[2])
    save_obj(pdict, 'policy')    
            
main()