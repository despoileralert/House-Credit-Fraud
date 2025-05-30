import logging

src_logger = logging.getLogger('SRC_Logger')
src_logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(filename = 'running_logs.log', mode = 'a')
fh.setlevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

src_logger.addHandler(fh)
src_logger.addHandler(ch)
