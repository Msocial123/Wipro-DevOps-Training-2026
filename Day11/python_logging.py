
import logging
import os
# logging.basicConfig(level=logging.DEBUG)

# logging.debug("this is a debug message ")
# logging.info(" Application started ")
# logging.warning("low memory waring")
# logging.error("failed to procvess file")
# logging.critical("system crashes ")

#logging in to files :
# logging.basicConfig(filename="app.log",level=logging.WARNING,format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug("this is a debug message ")
# logging.info(" Application started ")
# logging.warning("low memory waring")
# logging.error("failed to procvess file")
# logging.critical("system crashes ")
#logging multiple handlers
# logger=logging.getLogger("devops")
# logger.setLevel(logging.DEBUG)

# #file handler
# fh=logging.FileHandler("devops.log")
# fh.setLevel(logging.DEBUG)

# #console handler
# ch=logging.StreamHandler()
# ch.setLevel(logging.INFO)
# #format
# formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# logger.addHandler(fh)
# logger.addFilter(ch)
# logger.info("pipeline started")
# logger.error("Devployemt failed ")
os.mkdir("logging modules")