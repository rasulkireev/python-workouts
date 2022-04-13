

def mysum(*args):
  sum = 0
  iterable = iter(args)

  for i in range(len(args)):
    sum += next(iterable)

  return sum


if __name__ == '__main__':
  sum = mysum(1,2,3,4,5,7)
  print(sum)