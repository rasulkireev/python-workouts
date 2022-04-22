

def hex_output(hex_string: str) -> int:
  decimal = 0
  for index, str_digit in enumerate(reversed(hex_string)):
    decimal += int(str_digit, 16) * (16 ** index)

  return decimal

if __name__ == '__main__':
  hex_string = input("Enter a hex number to convert: ")

  decimal = hex_output(hex_string)

  print(decimal)