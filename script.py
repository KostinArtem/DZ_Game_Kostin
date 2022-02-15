print(" Игра крестики нолики")

grid = list(range(1,10))

def full_grid(grid):
   print("-" * 13)
   for i in range(3):
      print("|", grid[0+i*3], "|", grid[1+i*3], "|", grid[2+i*3], "|")
      print("-" * 13)

def input_value(nominal_hero):
   logic = False
   while not logic:
      hero_value = input("Ставим значение " + nominal_hero + "=")
      try:
         hero_value = int(hero_value)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if hero_value >= 1 and hero_value <= 9:
         if(str(grid[hero_value-1]) not in "XO"):
            grid[hero_value-1] = nominal_hero
            logic = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(grid):
   link_win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in link_win:
       if grid[each[0]] == grid[each[1]] == grid[each[2]]:
          return grid[each[0]]
   return False

def main(grid):
    counter = 0
    win = False
    while not win:
        full_grid(grid)
        if counter % 2 == 0:
           input_value("X")
        else:
           input_value("O")
        counter += 1
        if counter > 4:
           tmp = check_win(grid)
           if tmp:
              print(tmp, "Выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    full_grid(grid)
main(grid)

input("Нажмите Enter для Выхода!")
