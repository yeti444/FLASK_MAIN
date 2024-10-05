from repository.passwordHasherRepository import hashPassword, checkPassword

def hashPassword_service(password):
    return hashPassword(password)

def checkPassword_service(password, hashed_password):
    return checkPassword(password, hashed_password)

