import sys

print_beej = 1
halt = 2
print_num = 3
save_to_reg = 4
print_reg = 5
add = 6

memory = [
  'print_beej',
  'print_num',
   17,
  'print_beej',
  'print_beej',
  'print_num',
   32,
   'save_to_reg',
   65,
   2,
  'save_to_reg',
  65,
  2,
  'add'
  2,
  3,
  'print_reg',
  2,
  'halt'
]

register = []

running = True
pc = 0
while running:
  # Execute instructiuons in memory

  command = memory[pc]

  if command == 'print_beej':
    print('Beej')
    pc += 1

  elif command == 'halt':
    running = False

  elif command == 'print_num':
    num = pc + 1
    print(num)
    pc += 2

  else:
    print(f"Error Unknown Command {command}")
    sys.exit()
