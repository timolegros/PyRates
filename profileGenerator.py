import sqlite3
import random
import uuid

usernames = open('usernames.txt').read().splitlines()
locations = ["East Coast", "Midwest", "West Coast", "Southern US", "Northern US", "Eastern Canada",
             "Western Canada", "Atlantic Provinces", "Outside US/ Canada"]
programmingLanguages1 = ['C', 'Python', 'Javascript', 'Java', 'C#', 'C++']
databases = ['SQL', 'MongoDB', 'Firebase', 'Oracle', 'Redis']
interests = ["Web Development", "AI", "Product Management", "Big data"]
hackathonChoices = [0, 1, 2, 3, 4]

try:
    sqliteConnection = sqlite3.connect('PyRatesFront/db.sqlite3')
    cursor = sqliteConnection.cursor()

    for i in range(1):
        username = random.choice(usernames).strip()
        location = random.choice(locations)
        programmingLanguages = '; '.join(random.choices(programmingLanguages1))
        database = '; '.join(random.choices(databases))
        interest = '; '.join(random.choices(interests))
        hackathon = random.choice(hackathonChoices)

        sqlite_Query = ("""INSERT INTO UserProfiles('userID', 'username', 'location', 'hackathons', 'progLanguages', 'databases',
                        'interests', 'latest') VALUES (?, ?, ?, ?, ?, ?, ?, ?);""")

        data = [str(uuid.uuid4()), str(username), str(location), int(hackathon), str(programmingLanguages), str(database), str(interest),  0]

        cursor.execute(sqlite_Query, data)
        sqliteConnection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
