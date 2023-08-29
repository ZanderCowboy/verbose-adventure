import re

from Logging.logging_config import logger


def validate_input(input_string: str) -> bool:
	# todo Add docs
	"""

	:param input_string:
	:return:
	"""
	logger.debug("Calling validate_input(%s)...", input_string)

	# pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z])$|[\^v!<>-]"
	# pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z_])$|[\^v!<>-]"
	pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z])$|[\^v!<>-]"
	result = re.fullmatch(pattern, input_string) is not None

	logger.debug("Checked against a regex. result(is it valid?)=%s.", result)
	return result
