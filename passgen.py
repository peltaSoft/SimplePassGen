import random
import string

def GetPassword(length):
    password = ''.join([random.choice(string.ascii_letters + string.digits  ) for n in range(length)])
    return password

def GetDigitPassword(length):
    password = ''.join([random.choice(string.digits) for n in range(length)])
    return password

def GetLetterPassword(length):
    password = ''.join([random.choice(string.ascii_letters) for n in range(length)])
    return password
