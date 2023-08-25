import re

from Logging.logging_config import logger


def validate_input(input_string: str) -> bool:
	logger.debug("Calling validate_input(%s)...", input_string)

	# pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z])$|[\^v!<>-]"
	pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z])$|[\^v!<>-]"
	result = re.fullmatch(pattern, input_string) is not None

	logger.debug("Checked against a regex. result(is it valid?)=%s. Returning.", result)
	return result

# todo Create Unit Test
# Test cases
test_cases = [
	"^",
	"v",
	"P",
	"P_1",
	"P_2",
	"a",
	"a_123",
	"123",
	"@",
	"#",
	"%",
	"A",
	"B_42",
	"C_",  # questionable
	"P^Q",
	"PvQ",
	"P->Q",
	"P<->Q",
	"R_10",
	"X-Y",
	"Z_99",
	"0",
	"5",
	"P@Q",
	"abc",  # No
	"def_",
	"_xyz",
	"<",
	">",
	"R-5",
	"S^6",
	"T_7",
]
