# import logging
# import logging.handlers

# import platform


import logging
# logging.basicConfig(level=logging.DEBUG)
# def get_logger(name):
#     logger = logging.getLogger(name)
#     return logger


# logger = logging.getLogger(__name__)

# import logging.handlers

# formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
# handler.setFormatter(formatter)

PAPERTRAIL_HOST = "logs4.papertrailapp.com"
PAPERTRAIL_PORT =  47944

handler = logging.handlers.SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))



logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    handlers=[handler]
)

def get_logger(name):
    logger = logging.getLogger(name)
    return logger




# logger.debug("This message will be recorded.")
# logger.info("This message will be recorded.")
# logger.warning("This message will be recorded.")
# logger.error("This message will be recorded.")
# logger.critical("This message will be recorded.")

# if platform.system() != "Windows":
#     from logging.handlers import SysLogHandler

# # Initialize logging
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# # Initialize logging
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# # Conditional handler setup
# if platform.system() == "Windows":
#     handler = logging.FileHandler("log.txt")
# else:
#     handler = SysLogHandler(address="/dev/log")

# PAPERTRAIL_HOST =  'logs5.papertrailapp.com'
# PAPERTRAIL_PORT = 25146

# handler = logging.handlers.SysLogHandler(
#     PAPERTRAIL_HOST, PAPERTRAIL_PORT
# )
# # formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")

# # handler.setFormatter(formatter)

# logging.basicConfig(
#     level=logging.DEBUG,
#     format= "%(asctime)s %(levelname)s %(name)s %(message)s",
#     handlers= [handler]
#     )

# def get_logger(name):
#     logger = logging.getLogger(name)
#     return logger