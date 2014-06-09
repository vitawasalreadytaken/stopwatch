import logging, time

logger = logging.getLogger('stopwatch')


class Stopwatch(object):
	def __init__(self, comment = None):
		self.comment = comment

	def __enter__(self):
		self.T0 = time.time()
		self.elapsed = 0
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.elapsed = time.time() - self.T0
		if self.comment is not None:
			logger.debug('"{:s}" done in {:.3f} seconds.'.format(self.comment, self.elapsed))
