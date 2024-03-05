from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import sys


# logging.info("Welcome to the Project")

try: 
    a = 7 / '9'

except Exception as e:
    raise SignException(e, sys)