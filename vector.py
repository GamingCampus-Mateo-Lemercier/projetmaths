from __future__ import annotations

class Vector:
    def __init__( self, lValues: list[ int ] ):
        self.lValues: list[ int ] = lValues
        self.iSize: int = len( lValues )
    
    @staticmethod
    def zero( iSize: int ) -> Vector:
        return Vector( [ 0 for _ in range( iSize ) ] )
    
    @staticmethod
    def one( iSize: int ) -> Vector2:
        return Vector( [ 1 for _ in range( iSize ) ] )
    
    def __repr__( self ) -> str:
        sPrint = "("
        if ( self.iSize > 0 ):
            sPrint += str( self.lValues[ 0 ] )
            for iIndex in range( 1, self.iSize ):
                sPrint += ", " + str( self.lValues[ iIndex ] )
        sPrint += ")"
        return sPrint
    
    def copy( self ) -> Vector:
        return Vector( [ v for v in self.lValues ] )
    
    
    
    def __add__( self, other: Vector | float ) -> Vector:
        newVector = self.copy()
        if isinstance( other, Vector ):
            if ( self.iSize != other.iSize ): raise ValueError
            for iIndex in range( self.iSize ):
                newVector.lValues[ iIndex ] += other.lValues[ iIndex ]
        else:
            for iIndex in range( self.iSize ):
                newVector.lValues[ iIndex ] += other
        return newVector
    
    def __sub__( self, other: Vector | float ) -> Vector:
        newVector = self.copy()
        if isinstance( other, Vector ):
            if ( self.iSize != other.iSize ): raise ValueError
            for iIndex in range( self.iSize ):
                newVector.lValues[ iIndex ] -= other.lValues[ iIndex ]
        else:
            for iIndex in range( self.iSize ):
                newVector.lValues[ iIndex ] -= other
        return newVector
    
    def __mul__( self, other: Vector | float ) -> float | Vector:
        newVector = self.copy()
        if isinstance( other, Vector ):
            if ( self.iSize != other.iSize ): raise ValueError
            fSum: int = 0
            for iSelfValue, iOtherValue in zip( self.lValues, other.lValues ):
                fSum += iSelfValue * iOtherValue
            return fSum
        else:
            for iIndex in range( self.iSize ):
                newVector.lValues[ iIndex ] *= other
        return newVector
    
    
    
    def __bool__( self ) -> bool:
        for iValue in self.lValues:
            if ( iValue ): return True
        return False
    
    def __eq__( self ) -> bool:
        for iIndex in range( self.iSize ):
            if ( self.lValues[ iIndex ] != self.lValues[ iIndex ] ): return False
        return True
    
    def __lt__( self, other: Vector ) -> bool:
        for iIndex in range( self.iSize ):
            if ( self.lValues[ iIndex ] >= other.lValues[ iIndex ] ): return False
        return True
    
    def __le__( self, other: Vector ) -> bool:
        for iIndex in range( self.iSize ):
            if ( self.lValues[ iIndex ] > other.lValues[ iIndex ] ): return False
        return True
    
    def __rt__( self, other: Vector ) -> bool:
        for iIndex in range( self.iSize ):
            if ( self.lValues[ iIndex ] <= other.lValues[ iIndex ] ): return False
        return True
    
    def __re__( self, other: Vector ) -> bool:
        for iIndex in range( self.iSize ):
            if ( self.lValues[ iIndex ] < other.lValues[ iIndex ] ): return False
        return True
    
    
    
    def norm( self ) -> float:
        return ( self * self )**0.5
    
    def normalizeToSelf( self ) -> None:
        norm = self.norm()
        for iIndex in range( self.iSize ):
            self.lValues[ iIndex ] /= norm
    
    def normalizeToNew( self ) -> Vector2:
        newVector: Vector = self.copy()
        newVector.normalizeToSelf()
        return newVector
    
    def distanceTo( self, other: Vector ) -> float:
        return ( other - self ).norm()





class Vector2:
    def __init__( self, x: float, y: float ):
        self.x: float = x
        self.y: float = y
    
    @staticmethod
    def zero() -> Vector2:
        return Vector2( 0, 0 )
    
    @staticmethod
    def one() -> Vector2:
        return Vector2( 1, 1 )
    
    def __repr__( self ) -> str:
        return f"({ self.x }, { self.y })"
    
    def copy( self ) -> Vector2:
        return Vector2( self.x, self.y )
    
    
    
    def __add__( self, other: Vector2 | float ) -> Vector2:
        newVector = self.copy()
        if isinstance( other, Vector2 ):
            newVector.x += other.x
            newVector.y += other.y
        else:
            newVector.x += other
            newVector.y += other
        return newVector
    
    def __sub__( self, other: Vector2 | float ) -> Vector2:
        newVector = self.copy()
        if isinstance( other, Vector2 ):
            newVector.x -= other.x
            newVector.y -= other.y
        else:
            newVector.x -= other
            newVector.y -= other
        return newVector
    
    def __mul__( self, other: Vector2 | float ) -> float | Vector2:
        newVector = self.copy()
        if isinstance( other, Vector2 ):
            return self.x * other.x + self.y * other.y
        else:
            newVector.x *= other
            newVector.y *= other
        return newVector
    
    
    
    def __bool__( self ) -> bool:
        return bool( self.x ) or bool( self.y )
    
    def __lt__( self, other: Vector2 ) -> bool:
        return ( self.x < other.x ) and ( self.y < other.y )
    
    def __le__( self, other: Vector2 ) -> bool:
        return ( self.x <= other.x ) and ( self.y <= other.y )
    
    def __rt__( self, other: Vector2 ) -> bool:
        return ( self.x > other.x ) and ( self.y > other.y )
    
    def __re__( self, other: Vector2 ) -> bool:
        return ( self.x >= other.x ) and ( self.y >= other.y )
    
    
    
    def norm( self ) -> float:
        return ( self * self )**0.5
    
    def normalizeToSelf( self ) -> None:
        norm = self.norm()
        self.x /= norm
        self.y /= norm
    
    def normalizeToNew( self ) -> Vector2:
        return self / self.norm()
    
    def distanceTo( self, other: Vector2 ) -> float:
        return ( other - self ).norm()





class Vector3:
    def __init__( self, x: float, y: float, z: float ):
        self.x: float = x
        self.y: float = y
        self.z: float = z
    
    @staticmethod
    def zero() -> Vector3:
        return Vector3( 0, 0, 0 )
    
    @staticmethod
    def one() -> Vector3:
        return Vector3( 1, 1, 1 )
    
    def __repr__( self ) -> str:
        return f"({ self.x }, { self.y }, { self.z })"
    
    def copy( self ) -> Vector3:
        return Vector3( self.x, self.y, self.z )
    
    
    
    def __add__( self, other: Vector3 | float ) -> Vector3:
        newVector = self.copy()
        if isinstance( other, Vector3 ):
            newVector.x += other.x
            newVector.y += other.y
            newVector.z += other.z
        else:
            newVector.x += other
            newVector.y += other
            newVector.z += other
        return newVector
    
    def __sub__( self, other: Vector3 | float ) -> Vector3:
        newVector = self.copy()
        if isinstance( other, Vector3 ):
            newVector.x -= other.x
            newVector.y -= other.y
            newVector.z -= other.z
        else:
            newVector.x -= other
            newVector.y -= other
            newVector.z -= other
        return newVector
    
    def __mul__( self, other: Vector3 | float ) -> float | Vector3:
        newVector = self.copy()
        if isinstance( other, Vector3 ):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            newVector.x *= other
            newVector.y *= other
            newVector.z *= other
        return newVector
    
    
    
    def __bool__( self ) -> bool:
        return bool( self.x ) or bool( self.y ) or bool( self.z )
    
    def __lt__( self, other: Vector3 ) -> bool:
        return ( self.x < other.x ) and ( self.y < other.y ) and ( self.z < other.z )
    
    def __le__( self, other: Vector3 ) -> bool:
        return ( self.x <= other.x ) and ( self.y <= other.y ) and ( self.z <= other.z )
    
    def __rt__( self, other: Vector3 ) -> bool:
        return ( self.x > other.x ) and ( self.y > other.y ) and ( self.z > other.z )
    
    def __re__( self, other: Vector3 ) -> bool:
        return ( self.x >= other.x ) and ( self.y >= other.y ) and ( self.z >= other.z )
    
    
    
    def norm( self ) -> float:
        return ( self * self )**0.5
    
    def normalizeToSelf( self ) -> None:
        norm = self.norm()
        self.x /= norm
        self.y /= norm
        self.z /= norm
    
    def normalizeToNew( self ) -> Vector3:
        return self / self.norm()
    
    def distanceTo( self, other: Vector3 ) -> float:
        return ( other - self ).norm()