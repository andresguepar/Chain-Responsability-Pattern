from handlers import UserHandler
from handlers import RolHandler
from handlers import PermissionHandler
import User
class Main:
    @staticmethod
    def execute(user: User):
        usernameH = UserHandler.UserHandler()
        rolH = RolHandler.RolHandler()
        permitH = PermissionHandler.PermissioHandler()

        print("======================================")
        usernameH.set_next(rolH).set_next(permitH)
        result = usernameH.handle(user)

        if result is None:
            print("All validations passed")
            print("--------------------------------")
        else:
            print("Validation failed")
            print("--------------------------------")

            
if __name__ == "__main__":
    user_success = User.User("john_doe","admin","Level 5")
    print("======================================")
    print(user_success)
    Main.execute(user_success)
    user_failure = User.User("jane_doe","user","Level 1")
    print("======================================")
    print(user_failure)
    Main.execute(user_failure)
