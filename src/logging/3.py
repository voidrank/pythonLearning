import logging

logging.basicConfig(
	level=logging.WARNING,
	datefmt="%a, %d %b %Y %H:%M:%S",
	filename="3.log",
	filemode="w"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")

'''
	logging.StreamHandler: output log to sys.stderr or sys.stdout
	logging.FileHandler: output log to file
'''