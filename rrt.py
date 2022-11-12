import pygame
from rrtbase import RRTGraph
from rrtbase import RRTMap

def main():
    dimensions = (600,1000)
    start = (50,50)
    goal = (510,510)
    obsdim = 50
    obsnum = 50
    iteration = 0

    pygame.init()
    map = RRTMap(start, goal, dimensions, obsdim, obsnum)
    graph = RRTGraph(start, goal, dimensions, obsdim, obsnum)
    
    obstacles = graph.makeobs()

    map.drawMap(obstacles)

    while(not graph.path_to_goal()):
        if iteration%20 == 0:
            X,Y,Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue, (X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
        else:
            X,Y,Parent = graph.expand()
            pygame.draw.circle(map.map,map.grey, (X[-1],Y[-1]),map.nodeRad+2,0)
            pygame.draw.line(map.map,map.Blue, (X[-1],Y[-1]),(X[Parent[-1]],Y[Parent[-1]]),map.edgeThickness)
            
        if iteration%5 == 0:
            pygame.display.update()
        iteration+=1
    map.drawpath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)
    pygame.image.save(map.map, "screenshot.jpeg")




if __name__== '__main__':
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False
