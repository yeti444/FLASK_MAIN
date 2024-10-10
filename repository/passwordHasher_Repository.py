import bcrypt

def hashPassword(password):
    byte_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return hashed_password

def checkPassword(password, hashed_password):
    byte_password = password.encode('utf-8')
    return bcrypt.checkpw(byte_password, hashed_password)