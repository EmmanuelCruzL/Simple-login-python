from os import name
from peewee import  *
from  peewee import  Model
import peewee

db = MySQLDatabase("crud", user="ema", password="KILLERDEADKILLER123", host="localhost", port=3306)


class Users(Model):
    id = peewee.AutoField()
    name = peewee.CharField(unique=True)
    pwd = peewee.CharField()

    class Meta:
        database = db



def login(user, pwd):
    try:
        query = (Users
            .select(Users.name, Users.pwd)
            .where(Users.name == user and Users.pwd == pwd))
        if query:
            return True
        else:
            return False
    except Exception as e:
        print("Exception {}".format(type(e).__name__))
        
def get_end_id():
    try:
        query =(Users.select(Users.id))
        count = 0
        for  id in query:
            count +=1
        
        return (count+1);
    except Exception as e:
        print(e)
        print(type(e).__name__)
        return -1
        
def  create_user(user,pwd):
    try:
        insert = Users(name=user,pwd=pwd)
        insert.save()
        return True
    except Exception as e:
        print(type(e).__name__)
        return False

def main():
    try:
        db.connect()
        db.create_tables(Users)
    except Exception as e:
        print(type(e).__name__)

if __name__ == '__main__':
    main()

