

class User_account_details:

    def __init__(self, username, digest_password, account_created, acount_last_login ):
        self.username = username ,
        self.digest_password = digest_password,
        self.account_created = account_created ,
        self.account_last_login = acount_last_login

    @property
    def data(self):
        return {
            'username': self.username[0],
            'digest_password': self.digest_password[0],
            'account_created': self.account_created[0],
            'account_last_login': self.account_last_login[0]
        }