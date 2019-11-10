#There are 8 prison cells in a row, and each cell is either occupied or vacant.

#Each day, whether the cell is occupied or vacant changes according to the following rules:

#If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
#Otherwise, it becomes vacant.
#(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

#We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

#Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

def prisonAfterNDays(states, days):
    # WRITE YOUR CODE HERE
    outArr = states[:]

    while days > 0:
        previousstatue = outArr[:]
        for pointer, num in enumerate(previousstatue):
            if pointer == 0:
                if previousstatue[pointer + 1] == 0:
                    outArr[pointer] = 0
                else:
                    outArr[pointer] = 1
            elif pointer == len(previousstatue) -1:
                if previousstatue[pointer - 1] == 0:
                    outArr[pointer] = 0
                else:
                    outArr[pointer] = 1
            else:
                if previousstatue[pointer + 1] == previousstatue[pointer - 1]:
                    outArr[pointer] = 0
                else:
                    outArr[pointer] = 1
        days-=1
    return outArr

print prisonAfterNDays([1,1,1,0,1,1,1,1],2)
