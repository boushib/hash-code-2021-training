def readFile(file):
  print(f'==> Reading {file}.in ..')
  f = open(f'input/{file}.in', 'r')
  content = [x.strip() for x in f.readlines()]
  f.close()
  return content


def writeFile(file, deliveries):
  print(f'==> Writing {file}.out ..')
  f = open(f'output/{file}.out', 'w')
  f.write(f'{len(deliveries)}\n')  # OK
  f.write('\n'.join(deliveries))
  f.close()


def processFileContent(content):
  stats = content[0].split()
  teams = {
    2: int(stats[1]),
    3: int(stats[2]),
    4: int(stats[3]),
  }
  pizzas = content[1:]
  pizzas = [
    {'id': i, 'ingredients': pizza.split()}
      for i, pizza in enumerate(pizzas)
  ]
  numberOfPizzas = len(pizzas)
  numberOfPizzasNeeded = teams[2] * 2 + teams[3] * 3 + teams[4] * 4

  # sort pizzas by number of ingredients
  pizzas.sort(key=lambda pizza: len(pizza['ingredients']), reverse=True)

  # create deliveries
  """
  1. Start with teams of 4, then 3 then 2
  2. start with pizzas with most of ingredients
  """
  deliveries = []

  while(numberOfPizzas >= 2 and numberOfPizzasNeeded > 0):
    print(f'pizzas needed: {numberOfPizzasNeeded}!')
    print(f'pizzas available: {numberOfPizzas}!')
    deliverySize = 0
    # 4 -> 3 -> 2
    for i in range(4, 1, -1):
      if(teams[i]):
        deliverySize = i
        teams[i] -= 1
        break
    # brute force, non optimised solution
    delivery = f'{deliverySize} '

    for i in range(deliverySize):
      delivery += f'{pizzas[0]["id"]} '
      pizzas.pop(0)
      numberOfPizzas -= 1
      numberOfPizzasNeeded -= 1
    deliveries.append(delivery)

  return deliveries


def processFile(file):
  content = readFile(file)
  deliveries = processFileContent(content)
  writeFile(file, deliveries)


inFiles = ['a_example', 'b_little_bit_of_everything',
           'c_many_ingredients', 'd_many_pizzas', 'e_many_teams']

for file in inFiles:
  processFile(file)
