class User:
    def __init__(self, username=None, rol=None, permit=None):
        self.username = username
        self.rol = rol
        self.permit = permit
        
    def __str__(self):
        return f"User:\nUsername: {self.username}\nRol: {self.rol}\nPermit: {self.permit}\n"