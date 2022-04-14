
def run_timing():
  timings = []

  while True:
    user_input = input("How long it took for you to run 10km (in minutes)?")
    if user_input == "":
      num_of_runs = len(timings)
      average = sum(timings) / num_of_runs
      print(f"Average of {average}, over {num_of_runs} runs.")
      break

    timings.append(float(user_input))


def better_run_timing():
  number_of_runs = 0
  total_time = 0

  while True:
    one_run = input('Enter 10 km run time: ')

    if not one_run:
      break

    number_of_runs += 1
    total_time += float(one_run)

  average_time = total_time / number_of_runs
  print(f'Average of {average_time}, over {number_of_runs} runs')


if __name__ == '__main__':
  run_timing()