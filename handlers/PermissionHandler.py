from handlers.AbstractHandler import AbstractHandler


class PermissioHandler(AbstractHandler):
    def handle(self, user) -> str:
        if not user.permit == "Level 5":
            print("Username doesn't have access to Lelel 5.")
            return False
        print("Username have access to Level 5, final validation succeed.")
        return super().handle(user)