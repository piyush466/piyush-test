import logging


class Demo:

    def test_piyush(self):
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('Piyushlogs.log')
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        return logger


