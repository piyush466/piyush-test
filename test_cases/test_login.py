from pageobjects.Loginpage import Login
from Utilities.readproperties import Read
from Utilities.loggeneratefiles import LogGenrate
# from  Utilities.loggeneratefiles import Logge

class Test_001:
    url =  Read.urlread()
    username = Read.usernameread()
    password = Read.passwordread()

    genearte = LogGenrate.logger()

    def test_login1(self,setup):
        self.genearte.info("**********start Login************")
        self.driver = setup
        self.driver.get(self.url)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.genearte.info(f"your username is:-{self.username}")
        self.lp.setpassword(self.password)
        self.genearte.info(f"your password is:-{self.password}")
        self.lp.clicksubmit()
        self.genearte.debug("**********Test End***********")
        self.genearte.info("*******Test pass************")

