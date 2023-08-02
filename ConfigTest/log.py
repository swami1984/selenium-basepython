import logging

logging.basicConfig(filename="C://Users//thipr//PycharmProjects//pythonFrameworkInterview//logss//test.log",
                             format="'%(asctime)s :%(levelname)s : %(name)s :%(message)s''",
                             datefmt= "'%m/%d/%Y %I :%M:%S:%p'" , level=logging.DEBUG
                    )

# class LogGen:
#     @staticmethod
#     def loggen():
#         logger  = logging.getLogger("Test Login")
#         fileHandler  = logging.FileHandler('.\\C:\Users\thipr\PycharmProjects\pythonFrameworkInterview')
#         formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#         fileHandler.setFormatter(formatter)
#         logger.addHandler(fileHandler)
#         logger.setLevel(logging.INFO)
#         return logger