import logging, time

logger = logging.getLogger('stopwatch')


class Stopwatch(object):
	def __init__(self, comment):
		self.comment = comment

	def __enter__(self):
		self.T0 = time.time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		logger.debug('"{:s}" done in {:.3f} seconds.'.format(self.comment, time.time() - self.T0))
