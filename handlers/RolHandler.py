from handlers.AbstractHandler import AbstractHandler

class RolHandler(AbstractHandler):
    def handle(self, user) -> str:
        if not user.rol == "admin":
            print("Username doesn't have access to admin.")
            return False
        print("Username have access, please continue permission validation.")
        return super().handle(user)