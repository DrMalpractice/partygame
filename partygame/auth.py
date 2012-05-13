import hashlib
import os
import datetime
from config import SECRET_KEY

class User:
    def __init__(self, username, userid, admin=False):
        self.name = username
        self.id = userid
        self.admin = admin

def hash_password(password):
    return hashlib.sha256(password+SECRET_KEY.encode('hex')).hexdigest()
        
def login(db, username, password):
    """Logs in as user."""
    
    password_hash = hash_password(password)
    
    cursor = db.cursor()
    rows = cursor.execute('select userid, admin from user where username=? and password_hash=?', [username, password_hash]).fetchall()
    if len(rows) > 0:
        userid, admin = rows[0][0], rows[0][1]
        cursor.execute('update user set lastlogin=datetime(\'now\') where userid=?', [userid])
        db.commit()
        return User(username, userid, bool(admin))
    else:
        return None
        
def change_password(db, userid, password):
    """Changes a user's password."""
    
    password_hash = hash_password(password)
    
    cursor = db.cursor()
    cursor.execute('update user set password_hash=? where userid=?', [password_hash, userid])
    db.commit()
        
def create_user(db, username, password, email):
    """Creates a user."""
    
    password_hash = hash_password(password)
    
    cursor = db.cursor()
    cursor.execute('insert into user(username, password_hash, email) values(?, ?, ?)', [username, password_hash, email])
    db.commit()
    
    return User(username, cursor.lastrowid)
