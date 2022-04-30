import logging
import sys

class Logger:
    def __init__(self):
        self.logging = logging
        
        handlers=[
            self.logging.FileHandler('./logs/user.log','w'),
            self.logging.StreamHandler(sys.stdout)]

        self.logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            # datefmt='%d/%m/%Y %H:%M:%S',
            handlers=handlers)
        
        logging.info("Initializing logs")

    def get_logger(self,logger_name=""): 
        return self.logging.getLogger(logger_name) if logger_name!="" else self.logging.getLogger()
       
    
if __name__ == "__main__":
    Logger = Logger()
    
    root_logger = Logger.get_logger()
    
    root_logger.debug('Hello World a')
    
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