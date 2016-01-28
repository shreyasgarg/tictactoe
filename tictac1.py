#+==========================+===========================*=================+==============+
#|					Tic Tac Toe 1    				   |
#|					Shreyas Garg					   |
#|					04/16/13					   |
#|					Period:4					   |
#|											   |
#+==========================+===========================*=================+==============+

def storeDataBaseToFile(fileName, dataBase):
  file1 = open (fileName, 'wb')
  import pickle
  pickle.dump(dataBase, file1)
  file1.close()

def retrieveDataFromBaseFile(fileName):
  file1 = open(filename, 'rb')
  import pickle
  dataBase = pickle.load(file1)
  file1.close()
  return dataBase

def printBoard(board):
  print(' ', board[0], ' |',sep = '', end = '')
  print(' ', board[1], ' |',sep = '', end = '')
  print(' ', board[2])
  print('---+---+---')
  print(' ', board[3], ' |',sep = '', end = '')
  print(' ', board[4], ' |',sep = '', end = '')
  print(' ', board[5])
  print('---+---+---')
  print(' ', board[6], ' |',sep = '', end = '')
  print(' ', board[7], ' |',sep = '', end = '')
  print(' ', board[8])
  
def legalBoard(thing):
    countX = 0
    countO = 0
    for item in thing:
        if item == 'X':
            countX +=1
        elif item == 'O':
            countO +=1
    dif = countX - countO
    if dif < 1:
        dif *= -1
    if dif > 1:
        return False
    #if countX + countO < 5:
        #return False
    #if countX + countO > 8:
        #return False
    if thing[0] == thing[1] == thing[2]:
        return False
    if thing[3] == thing[4] == thing[5]:
        return False
    if thing[6] == thing[7] == thing[8]:
        return False
    if thing[0] == thing[3] == thing[6]:
        return False
    if thing[1] == thing[4] == thing[7]:
        return False
    if thing[2] == thing[5] == thing[8]:
        return False
    if thing[0] == thing[4] == thing[8]:
        return False
    if thing[6] == thing[4] == thing[2]:
        return False
    return True
    
def main():
    board = []
    for i in range(19683):
        a = i
        s = "";
        for j in range(9):
            if a%3 == 0:
                s += "X"
            if a%3 == 1:
                s += "O"
            if a%3 == 2:
                s += "-"
            a = a//3
        board.append(s)
    actual = []
    for thing in board:
        if legalBoard(thing):
            actual.append(thing)
    print(len(actual))
    #count = 0
    #for thing in actual:
      #printBoard(thing)
      #count += 1
      #if count > 24:
        #break
if __name__ == '__main__': main()