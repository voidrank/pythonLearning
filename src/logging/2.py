import logging

logging.basicConfig(level=logging.INFO,
	format="%(asctime)s %(filename)s[line:%(lineno)d] \
%(levelname)s %(levelname)s %(message)s",
	datefmt="%a, %m %b %Y %H:%M:%S",
	filename="myapp.log",
	filemode="w",
)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")


'''
	filename: as name
	filemode: "a" (add), "w" (write)
	levelname: logging under the level will not be printed
	fotmat: specify the format and logging content
	%(levelno)s: print the numberical value of the logging level
	%(levelname)s: print level name
	%(pathname)s: print the path of current running program's path
	%(filename)s: print the name of current running program's path
	%(funcName)s: print the name of current function's name
	%(lineno)s: print the lineno 
	%(asctime)s: print the current time
	%(thread)s: print the id of current thread
	%(threadName): print the name of current threadName
	%(process): print the id of the process
	%(message)s: print the logging message
	datefmt: specify the time format, like time.strftime()
	level: set the threshold value
	stream: set the output stream, if set stream and filename at the same time, it will ignore stream
'''
