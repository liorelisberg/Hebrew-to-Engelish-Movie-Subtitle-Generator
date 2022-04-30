from LoggerFactory import Logger

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