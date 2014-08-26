import logging

from logging.handlers import RotatingFileHandler

Rthandler = RotatingFileHandler("4.log", maxBytes=10*1024*1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
Rthandler.setFormatter(formatter)
logging.getLogger("").addHandler(Rthandler)

logging.debug("This is DEBUG message")
logging.info("This is INFO message")
logging.warning("This is WARNING message")


'''
	logging.handlers.BaseRotatingHandler
	logging.handlers.RotatingFileHandler
	logging.handlers.TimedRotatingFileHandler

	logging.handlers.SocketHandler : output log to remote TCP/IP sockets
	logging.handlers.DatagramHandler : output log to remote UDP sockets
	logging.handlers.SMTPHandler : output log to remote email address
	logging.handlers.SysLogHandler : output log to syslog
	/sout{logging.handlers.NTEventLogHandler: output log to Windows NT/2000/XP log system}
	logging.handlers.MemoryHandler : output log to the specified buffer
	logging.handers.HTTPHandler : output log through GET | POST remote HTTP server
'''