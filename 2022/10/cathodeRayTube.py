def getSignalStrength(cycle, register):
    signalStrength = 0
    if (cycle % 20 == 0) and ((cycle // 20) % 2 == 1):
        signalStrength = register * cycle
        
    return signalStrength

def renderImage(cycle, register):
    spritePos = register - 1 
    drawingPosition = (cycle-1) % 40
    if drawingPosition >= spritePos and drawingPosition <= spritePos + 2:
        print('#', end='')
    else:
        print('.', end='')
        
    if drawingPosition == 39:
        print()

if __name__ == '__main__':
    register = 1
    cycle = 1
    totalSignalStrength = 0
    with open('instructions.txt', 'r') as f:
        while True:
            instruction = f.readline().strip()
            if instruction == '':
                break

            instruction = instruction.split()
            val = 0
            cycleAmmount = 1
            if instruction[0] != 'noop':
                val = int(instruction[1])
                cycleAmmount = 2
            while cycleAmmount > 0:
                totalSignalStrength += getSignalStrength(cycle, register)       # part 1
                renderImage(cycle, register)                                    # part 2
                
                cycle += 1
                cycleAmmount -= 1
                    
            register += val
    
    print(totalSignalStrength)
            
            