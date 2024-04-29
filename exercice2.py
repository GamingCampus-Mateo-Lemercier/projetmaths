import matplotlib.pyplot as plot
from matrix import Matrix
from vector import Vector

r2 = 2 ** 0.5
r3 = 3 ** 0.5
r6 = 6 ** 0.5
s1 = r6 - r2
s2 = r6 + r2
pi = 22 / 7

circlePoints = [
    [     1 , 0 ,  0    ], # 0 : 0
    [  s2/4 , 0 ,  s1/4 ], # 1 : p/12
    [  r3/2 , 0 ,  1/2  ], # 2 : p/6
    [  r2/2 , 0 ,  r2/2 ], # 3 : p/4 ( D )
    [   1/2 , 0 ,  r3/2 ], # 4 : p/3
    [  s1/4 , 0 ,  s2/4 ], # 5 : 5p/12
    [     0 , 0 ,  1    ], # 6 : p/2
    [ -s1/4 , 0 ,  s2/4 ], # 7 : 7p/12
    [  -1/2 , 0 ,  r3/2 ], # 8 : 2p/3
    [ -r2/2 , 0 ,  r2/2 ], # 9 : 3p/4 ( A )
    [ -r3/2 , 0 ,  1/2  ], # 10 : 5p/6
    [ -s2/4 , 0 ,  s1/4 ], # 11 : 11p/12
    [    -1 , 0 ,  0    ], # 12 : p | -p
    [ -s2/4 , 0 , -s1/4 ], # 13 : -11p/12
    [ -r3/2 , 0 , -1/2  ], # 14 : -5p/6
    [ -r2/2 , 0 , -r2/2 ], # 15 : -3p/4 ( B )
    [  -1/2 , 0 , -r3/2 ], # 16 : -2p/3
    [ -s1/4 , 0 , -s2/4 ], # 17 : -7p/12
    [     0 , 0 , -1    ], # 18 : -p/2
    [  s1/4 , 0 , -s2/4 ], # 19 : -5p/12
    [   1/2 , 0 , -r3/2 ], # 20 : -p/3
    [  r2/2 , 0 , -r2/2 ], # 21 : -p/4 ( C )
    [  r3/2 , 0 , -1/2  ], # 22 : -p/6
    [  s2/4 , 0 , -s1/4 ], # 23 : -p/12
]
wheelPoints: list[ Vector ] = []
basketPoints: list[ Vector ] = []

xlim: list[ float ] = [ -10, 0, 30 ]
zlim: list[ float ] = [ -5, 0, 25 ]



def setGraph():
    global xlim; global zlim; global circlePoints; global wheelPoints; global basketPoints
    
    position = [ 1, 0, 1 ] # wheel position
    size = 10 # wheel size
    wheelPoints.append( Vector( [ position[0] * size, 0, position[2] * size ] ) ) # wheel center
    for point in circlePoints:
        wheelPoints.append( Vector( [ ( position[ 0 ] + point[ 0 ] ) * size, 0, ( position[ 2 ] + point[ 2 ] ) * size ] ) ) # wheel
    
    position = [ ( 1 + position[0] ) * size, ( 0 + position[1] ) * size, ( 0 + position[2] ) * size ] # basket position
    size = 4 # basket size
    basketPoints.append( Vector( [ position[0], 0, position[2] ] ) ) # basket center
    for point in circlePoints:
        basketPoints.append( Vector( [ position[ 0 ] + point[ 0 ] * size, 0, position[ 2 ] + point[ 2 ] * size ] ) ) # basket
    
    plot.xlim( xlim[0], xlim[2] )
    plot.ylim( zlim[0], zlim[2] )
    
    wheelRotation: Matrix = Matrix.rotation3( -pi/6, Vector( [ 0, 1, 0 ] ) )
    wheelTranslation: Vector = ( wheelRotation - Matrix.identity( 3 ) ) * Vector( [ -10, 0, -10 ] )
    
    basketRotationAxis: Vector = Vector( [ 0, 0, 1 ] )
    
    wheelPointsTime: list[ list[ Vector ] ] = []
    basketPointsTime: list[ list[ Vector ] ] = []
    
    for aaaa in range( 1000 ):
        
        wheelPointsTime.append( [ *wheelPoints ] )
        basketPointsTime.append( [ *basketPoints ] )
        
        basketRotationAxis = wheelRotation * basketRotationAxis
        
        for iIndex in range( len( wheelPoints ) ):
            wheelPoints[ iIndex ] = wheelRotation * wheelPoints[ iIndex ] + wheelTranslation
        
        for iIndex in range( len( basketPoints ) ):
            basketPoints[ iIndex ] = wheelRotation * basketPoints[ iIndex ] + wheelTranslation    
            basketRotation: Matrix = Matrix.rotation3( -pi/3, basketRotationAxis )
            basketTranslation: Vector = ( basketRotation - Matrix.identity( 3 ) ) * basketPoints[ 0 ] * -1
            basketPoints[ iIndex ] = basketRotation * basketPoints[ iIndex ] + basketTranslation
    
    for iIndex in range( 40 ):
        plot.clf()
        
        wheelPoints = [ *wheelPointsTime[ iIndex ] ]
        basketPoints = [ *basketPointsTime[ iIndex ] ]
        
        trace()
        plot.draw()
        plot.pause( 0.5 )
    
    plot.show()



def trace():
    global xlim; global zlim; global wheelPoints; global basketPoints
    color = [ "blue", "orange" ]
    
    plot.scatter( 0, 0, color="black" ) # origin
    plot.plot( [ xlim[0], xlim[2] ], [ 0, 0 ], color="black" ) # axe x
    plot.plot( [ 0, 0 ], [ zlim[0], zlim[2] ], color="black" ) # axe z
    
    plot.scatter( wheelPoints[0][0], wheelPoints[0][2], color=color[0], marker="D" ) # wheel center
    plot.scatter( basketPoints[0][0], basketPoints[0][2], color=color[1], marker="D" ) # basket center
    
    plot.plot( [ wheelPoints[13][0], wheelPoints[1][0] ], [ wheelPoints[13][2], wheelPoints[1][2] ], color=color[0] )
    plot.plot( [ wheelPoints[19][0], wheelPoints[7][0] ], [ wheelPoints[19][2], wheelPoints[7][2] ], color=color[0] )
    # plot.plot( [ wheelPoints[16][0], wheelPoints[4][0] ], [ wheelPoints[16][2], wheelPoints[4][2] ], color=color[0] )
    # plot.plot( [ wheelPoints[10][0], wheelPoints[22][0] ], [ wheelPoints[10][2], wheelPoints[22][2] ], color=color[0] )
    plot.scatter( [ basketPoints[10][0] ], [ basketPoints[10][2] ], color="#00ff00", label="A" )
    plot.scatter( [ basketPoints[16][0] ], [ basketPoints[16][2] ], color="#00dd00", label="B" )
    plot.scatter( [ basketPoints[22][0] ], [ basketPoints[22][2] ], color="#00aa00", label="C" )
    plot.scatter( [ basketPoints[4][0] ], [ basketPoints[4][2] ], color="#007700", label="D" )
    plot.plot( [ basketPoints[4][0], basketPoints[10][0], basketPoints[16][0], basketPoints[22][0], basketPoints[4][0] ], [ basketPoints[4][2], basketPoints[10][2], basketPoints[16][2], basketPoints[22][2], basketPoints[4][2] ], color="green" ) # seat
    
    figures = [ wheelPoints, basketPoints ]
    for index, figure in enumerate( figures ):
        x, y, z = zip( *figure )
        x, y, z = list( x ), list( y ), list( z )
        x.pop( 0 )
        y.pop( 0 )
        z.pop( 0 )
        plot.plot( [ *x, x[0] ], [ *z, z[0] ], color=color[ index ] )



setGraph()