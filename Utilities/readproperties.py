import configparser
cong = configparser.RawConfigParser()
cong.read(r"C:\Users\Cliffex-Lead\locomtenence\configuration'\config.ini")

class Read:
    @staticmethod
    def urlread():
        url = cong.get('common info', 'url')
        return url

    @staticmethod
    def usernameread():
        username = cong.get('common info', 'username')
        return username

    @staticmethod
    def passwordread():
        password = cong.get('common info', 'password')
        return password
