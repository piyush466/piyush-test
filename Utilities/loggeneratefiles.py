import logging

class LogGenrate:
    @staticmethod
    def logger():
        logg = logging.getLogger(__name__)

        filehandle = logging.FileHandler(r"C:\Users\Cliffex-Lead\locomtenence\Logs\log1.log")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        filehandle.setFormatter(formatter)
        logg.addHandler(filehandle)
        logg.setLevel(logging.INFO)
        logg.setLevel(logging.DEBUG)
        # logg.setLevel(logging.CRITICAL)

        return logg

# import logging
#
# class Logge:
#
#     @staticmethod
#     def loggen():
#         logger  = logging.getLogger(__name__)
#         filehandle = logging.FileHandler(r"C:\Users\Cliffex-Lead\locomtenence\Logs\log1.log")
#         formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
#
#         filehandle.setFormatter(formatter)
#         logger.addHandler(filehandle)
#         logger.setLevel(logging.INFO)
#         logger.setLevel(logging.DEBUG)
#         return logger






