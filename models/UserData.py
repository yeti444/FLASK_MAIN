class UserData:
    def __init__(self, userId, email, firstName, lastName, password, createDate, roleId):
        self.__userId = userId
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName
        self.__password = password
        self.__createDate = createDate
        self.__roleId = roleId
    
    @property
    def userId(self):
        return self.__userId
    
    @property
    def email(self):
        return self.__email
    
    @property
    def firstName(self):
        return self.__firstName
    
    @property
    def lastName(self):
        return self.__lastName
    
    @property
    def password(self):
        return self.__password
    
    @property
    def createDate(self):
        return self.__createDate
    
    @property
    def roleId(self):
        return self.__roleId
    
    def to_dict(self):
        return {
            "userId": self.__userId,
            "email": self.__email,
            "firstName": self.__firstName,
            "lastName": self.__lastName,
            "password": self.__password,
            "createDate": self.__createDate,
            "roleId": self.__roleId
        }