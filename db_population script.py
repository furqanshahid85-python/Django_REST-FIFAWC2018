import sqlite3
import csv

# Global constants
FILENAME = '../2018 FIFA World Cup Squads.csv'
DB_NAME = 'db.sqlite3'


def populate_db(filename, cursor):
    """
    This method reads the csv file and passes each row for insert.
    :param filename : name of csv file
    :param cursor: the db cursor object
    :return : None
    """

    with open(filename, 'r', encoding='utf-8') as inputfile:
        csv_reader = csv.reader(inputfile)
        header = 0
        for record in csv_reader:
            if header == 0:
                header += 1
                continue
            Team = record[0]
            Group = record[1]
            Squad_Number = record[2]
            Position = record[3]
            Player = record[4]
            Date_Of_Birth = record[5].replace('/', '-')
            Age = record[6]
            Caps = record[7]
            Goals = record[8]
            Club = record[9]
            insert_record(cursor, Team, Group, Squad_Number, Position,
                          Player, Date_Of_Birth, Age, Caps, Goals, Club)


def insert_record(cursor, team, group, squad_num, position, player_name, dob, age, caps, goals, club):
    """
    This method inserts each row in csv file into the django sqlite3 database.

    :param cursor: db cursor object 
    :param team: name of the country for which the player plays 
    :param group: world cup group
    :param squad_num: squad number of the player
    :param position: playing position of the player
    :param player_name: name of the player
    :param dob: date of birth of the player
    :param age: age of the player
    :param caps: total matches played by a player
    :param goals: goals scored by the player
    :param club: name of the club for which the player plays
    :return : None
    """
    
    values = (team, group, squad_num, position,
              player_name, dob, age, caps, goals, club)
    sql_query = """INSERT INTO Players_Country_squad(Country_Name,WorldCup_Group,Squad_Number,Position,Player_Name,Date_Of_Birth,Age,Caps,Goals,Club) VALUES(?,?,?,?,?,?,?,?,?,?)"""
    
    try:
        cursor.execute(sql_query, values)
    except Exception as error:
        print("couldn't insert into the database, error: ",error)


if __name__ == "__main__":
    try:
        con = sqlite3.connect(DB_NAME)
    except Exception as error:
        print('could not connect,error: ', error)

    cursor = con.cursor()
    populate_db(FILENAME, cursor)
    con.commit()
    con.close()
