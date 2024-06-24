class Usuario:
    def __init__(self, nome, email, user_id=None):
        self.id = user_id
        self.nome = nome
        self.email = email

    def salvar(self, db_manager):
        if self.id is None:
            db_manager.add_user(self)
        else:
            db_manager.update_user(self)
    
    def remover(self, db_manager):
        db_manager.delete_user(self)