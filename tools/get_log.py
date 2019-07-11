import logging.handlers

class GetLogger():
    logger=None
    @classmethod
    def get_logger(self):
        #获取日志器
        logger=logging.getLogger()
        #设置日志总级别
        logger.setLevel(logging.INFO)
        #获取处理器
        th=logging.handlers.TimedRotatingFileHandler(filename='./log/log.log',
                                                     when='midnight',
                                                     interval=1,
                                                     backupCount=3,
                                                     encoding='utf-8')
        #设置处理器级别
        th.setLevel(logging.INFO)
        #获取格式器


        #