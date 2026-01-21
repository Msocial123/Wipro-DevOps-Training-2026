import logging
import os


import pdb #python debugger

# -----------------------------------------
# CONFIGURE LOGGING (WRITE TO auth.log FILE)
# -----------------------------------------

logging.basicConfig(
    filename="auth.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------------------
# CUSTOM ERROR CLASSES
# -----------------------------------------

class InvalidCredentials(Exception):
    pass

class UserBlocked(Exception):
    pass

# -----------------------------------------
# AUTHENTICATION SYSTEM
# -----------------------------------------

class AuthSystem:
    
    def __init__(self, db_file="users.txt"):
        self.db_file = db_file
        self.failed_attempts = {}

    def load_users(self):
        logging.debug("Loading user database from file")
        pdb.set_trace() #break point
        if not os.path.exists(self.db_file):
            logging.critical("User database file missing!")
            raise FileNotFoundError("Database file not found")

        users = {}
        with open(self.db_file, "r") as f:
            for line in f:
                if ":" in line:
                    username, pwd = line.strip().split(":")
                    users[username] = pwd # meaning  uers= username , pwd=pwd

        logging.info("User database loaded successfully")
        return users

    def authenticate(self, username, password):

        logging.info(f"Login attempt for username: {username}")
        logging.debug(f"Checking if '{username}' exists in system")
       

        users = self.load_users()

        if username not in users:
            logging.warning(f"Username '{username}' does not exist")
            raise InvalidCredentials("Invalid username or password")

        if self.failed_attempts.get(username, 0) >= 3:
            logging.error(f"User '{username}' is blocked due to multiple failures")
            raise UserBlocked("User account blocked!")

        if users[username] != password:
            logging.error("Incorrect password entered")
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1

            if self.failed_attempts[username] == 3:
                logging.critical(f"User '{username}' is now blocked!")
                raise UserBlocked("Too many failed attempts. User blocked.")

            raise InvalidCredentials("Invalid username or password")

        logging.info(f"User '{username}' logged in successfully")
        self.failed_attempts[username] = 0
        return True


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

auth = AuthSystem()

print("=== LOGIN SYSTEM ===")
username = input("Enter username: ")
password = input("Enter password: ")

try:
    if auth.authenticate(username, password):
        print("Login Successful!")

except InvalidCredentials as e:
    print("Login Failed:", e)

except UserBlocked as e:
    print("Access Denied:", e)

except Exception as e:
    logging.critical(f"Unexpected system failure: {e}")
    print("System Error:", e)

finally:
    logging.info("Login operation completed")
    print("Process complete. Check auth.log for details.")
