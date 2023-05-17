from assets.project_Logs.test_demo import Demo


class Testing(Demo):

    def test_partner(self,setup):
        log = self.test_piyush()
        log.info(setup[1])
        log.error(setup[3])