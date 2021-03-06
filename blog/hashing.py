from passlib.context import CryptContext

pwd_cwt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    
    def bcrypt(password: str):
        return pwd_cwt.hash(password)

    def verify(plain_password, hashed_password):
        return pwd_cwt.verify(plain_password, hashed_password)

