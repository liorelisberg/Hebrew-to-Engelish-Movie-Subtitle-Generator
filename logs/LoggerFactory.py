import logging
import sys

class Logger:
    def __init__(self):
        
        handlers=[
            logging.FileHandler('./logs/user.log','w'),
            logging.StreamHandler(sys.stdout)]
        
        # print("path: ",self.logging.FileHandler('./logs/user.log').baseFilename)

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
            # datefmt='%d/%m/%Y %H:%M:%S',
            handlers=handlers)
        
        self.logging = logging
        
    def test_log(self,msg:str,name:str):
        myLogger = Logger()
        logger = myLogger.get_logger(name)
        logger.warning(msg=msg)
        
    def get_logger(self,logger_name=""):
        logger = self.logging.getLogger("test logger")
        logger.info("testing logger")
        
        return self.logging.getLogger(logger_name) if logger_name!="" else self.logging.getLogger()
       
       
# class Logger(): 
#     def get_logger(self):
#         handlers=[
#             logging.FileHandler('./logs/user.log','w'),
#             logging.StreamHandler(sys.stdout)]

#         logging.basicConfig(
#             level=logging.INFO,
#             format='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
#             handlers=handlers)
        
#         logging.setLoggerClass(self.__class__)
          
#         formatter = logging.Formatter("[%(asctime)s.%(msecs)03d][%(levelname)s][%(message)s]", "%H:%M:%S")
#         console = logging.StreamHandler()
#         console.setLevel=logging.INFO
#         console.setFormatter(formatter)
#         sys._kivy_logging_handler = console
        
#         return logging.getLogger()
    
        
if __name__ == "__main__":
    Logger = Logger()
    
    root_logger = Logger.get_logger()
        
    root_logger.info('Initializing project b')
    root_logger.warning('Initializing project c')
    root_logger.error('Initializing project d')
    root_logger.critical('Initializing project e')
    
    logger1 = Logger.get_logger("Example")
    
    logger1.debug('Hello World a')
    
    logger1.info('Initializing project b')
    logger1.warning('Initializing project c')
    logger1.error('Initializing project d')
    logger1.critical('Initializing project e')