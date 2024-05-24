from handlers import UserHandler
from handlers import RolHandler
from handlers import PermissionHandler
import User
class Main:
    @staticmethod
    def execute(user: User):
        usernameH = UserHandler()
        rolH = RolHandler()
        permitH = PermissionHandler()

        usernameH.set_next(rolH).set_next(permitH)
        result = usernameH.handle(user)
        if result is None:
            print("All validations passed")
        else:
            print("Validation failed")

            
if __name__ == "__login__":
    user_success = User(username="john_doe", role="admin", permit="Level 5")
    Main.execute(user_success)
    user_failure = User(username="jane_doe", role="user", permit="Level 1")
    Main.execute(user_failure)
from handlers import UserHandler
from handlers import RolHandler
from handlers import PermissionHandler
import User
class Main:
    @staticmethod
    def execute(user: User):
        usernameH = UserHandler()
        rolH = RolHandler()
        permitH = PermissionHandler()

        usernameH.set_next(rolH).set_next(permitH)
        result = usernameH.handle(user)
        if result is None:
            print("All validations passed")
        else:
            print("Validation failed")

            
if __name__ == "__login__":
    user_success = User(username="john_doe", role="admin", permit="Level 5")
    Main.execute(user_success)
    user_failure = User(username="jane_doe", role="user", permit="Level 1")
    Main.execute(user_failure)
