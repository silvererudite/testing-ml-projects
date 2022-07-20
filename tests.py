def convert_to_int(some_number_str):
  return int(some_number_str)

def test_string_to_int():
  assert convert_to_int("20") == 20

def test_on_string_to_num():
  test_argument = "2081"
  expected = 2081
  actual = convert_to_int(test_argument)
  # Format the string with the actual return value
  message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
  # Write the assert statement which prints message on failure
  assert  convert_to_int(test_argument) == expected, message

