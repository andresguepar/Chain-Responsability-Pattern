

from handlers.AbstractHandler import AbstractHandler


class UserHandler(AbstractHandler):
    def handle(self, user) -> str:
        if not user.username:
            print("Username doesn't exist.")
            return False
        print("Username does exist, please continue with rol valifation.")
        return super().handle(user)
    