from math import dist

def updateVisitedTails(visitedTails, tail):
    if not (tail in visitedTails):
        visitedTails.append(tail)
        return True
    else:
        return False

def touching(tail, head):
    return int(dist(tail, head)) <= 1

def nextTail(tail, head):
    x = y = 0
    xt, yt = tail[1], tail[0]
    
    if not touching(tail, head):
        xh, yh = head[1], head[0]
        if xh - xt != 0:    
            x = (xh - xt) // abs(xh - xt)
        if yh - yt != 0:
            y = (yh - yt) // abs(yh - yt)
            
    return (y + yt, x + xt)

def nextHead(head, direction):
    mvs = {
        'L': (-1, 0), 
        'R': (1, 0),
        'U': (0, -1),
        'D': (0, 1)
    }
    
    x1, y1 = head[1], head[0]
    x2, y2 = mvs[direction][0], mvs[direction][1]
    
    return (y1 + y2, x1 + x2)

def challengePart1():
    start = head = tail = (0, 0)
    visitedTails = [start]
    
    with open('headMovements.txt', 'r') as f:
        while True:
            mv = f.readline().strip()
            if mv == '':
                break
            
            mv = mv.split()
            direction = mv[0]
            ammount = int(mv[1])
            
            while ammount > 0:
                tail = nextTail(tail, head)
                updateVisitedTails(visitedTails, tail)
                
                head = nextHead(head, direction)
                ammount -= 1
                
        tail = nextTail(tail, head)
        updateVisitedTails(visitedTails, tail)
                
    print(len(visitedTails))
    
def challengePart2():
    start = head = (0, 0)
    tails = []
    for i in range(0, 9):
        tails.append((0, 0))
    
    visitedLastTails = [start]
    
    with open('headMovements.txt', 'r') as f:
        while True:
            mv = f.readline().strip()
            if mv == '':
                break

            mv = mv.split()
            direction = mv[0]
            ammount = int(mv[1])
            
            while ammount > 0:
                tails[-1] = nextTail(tails[-1], head)
                tailNo = len(tails)
                for i in range(tailNo-2, -1, -1):
                    tails[i] = nextTail(tails[i], tails[i+1])
                    
                    if i == 0:
                        # last tail (9)
                        updateVisitedTails(visitedLastTails, tails[i])
                
                head = nextHead(head, direction)
                ammount -= 1

        tails[-1] = nextTail(tails[-1], head)
        tailNo = len(tails)
        for i in range(tailNo-2, -1, -1):
            tails[i] = nextTail(tails[i], tails[i+1])
            
            if i == 0:
                # last tail (9)
                updateVisitedTails(visitedLastTails, tails[i])
                
    print(len(visitedLastTails))

if __name__ == '__main__':
    challengePart1()
    challengePart2()