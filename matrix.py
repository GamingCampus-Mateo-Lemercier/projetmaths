from __future__ import annotations
from vector import Vector

class Matrix:
    def __init__( self, lliValues: list[ list[ int ] ] ):
        self.lliValues: list[ list[ int ] ] = lliValues
        self.iRows: int = len( lliValues )
        self.iColumns: int = len( lliValues[ 0 ] )
    
    @staticmethod
    def null( iRows: int, iColumns: int ) -> Matrix:
        return Matrix( [ [ 0 for _ in range( iColumns ) ] for _ in range( iRows ) ] )
    
    @staticmethod
    def identity( iSize: int ) -> Matrix:
        newMatrix: Matrix = Matrix( [ [ 0 for _ in range( iSize ) ] for _ in range( iSize ) ] )
        for iRowIndex in range( iSize ):
            for iColumn in range( iSize ):
                if ( iRowIndex == iColumn ):
                    newMatrix[ iRowIndex ][ iColumn ] = 1
        return newMatrix
    
    def __repr__( self ) -> str:
        sFirstRowCharacters = [ "/", "│", "\\" ]
        sLastRowCharacters = [ "\\", "│", "/" ]
        
        repr: str = "\n"
        for iRowIndex in range( self.iRows ):
            iRowCharactersIndex = ( ( iRowIndex + 1 ) // self.iRows ) + bool( iRowIndex )
            repr += sFirstRowCharacters[ iRowCharactersIndex ]
            for iColumnIndex in range( self.iColumns ):
                repr += " " + str( self[ iRowIndex ][ iColumnIndex ] )
            repr += " " + sLastRowCharacters[ iRowCharactersIndex ] + "\n"
        return repr
    
    def copy( self ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.iRows, self.iColumns )
        for iRowIndex in range( newMatrix.iRows ):
            for iColumnIndex in range( newMatrix.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex ][ iColumnIndex ]
        return newMatrix
    
    
    
    def __getitem__( self, iRowIndex: int ) -> list[ int ]:
        return self.lliValues[ iRowIndex ]
    
    def __setitem__( self, iRowIndex: int, iColumnIndex: int, iValue: int ) -> None:
        self.lliValues[ iRowIndex ][ iColumnIndex ] = iValue
    
    
    
    def __add__( self, other: Matrix ) -> Matrix:
        if ( not ( self.iRows == other.iRows and self.iColumns == other.iColumns ) ): raise ValueError
        newMatrix: Matrix = Matrix.null( self.iRows, self.iColumns )
        for iRowIndex in range( newMatrix.iRows ):
            for iColumnIndex in range( newMatrix.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex ][ iColumnIndex ] + other[ iRowIndex ][ iColumnIndex ]
        return newMatrix
    
    def __sub__( self, other: Matrix ) -> Matrix:
        if ( not ( self.iRows == other.iRows and self.iColumns == other.iColumns ) ): raise ValueError
        newMatrix: Matrix = Matrix.null( self.iRows, self.iColumns )
        for iRowIndex in range( newMatrix.iRows ):
            for iColumnIndex in range( newMatrix.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex ][ iColumnIndex ] - other[ iRowIndex ][ iColumnIndex ]
        return newMatrix
    
    def __mul__( self, other: Matrix | float ) -> Matrix:
        if ( isinstance( other, Matrix ) ):
            
            if ( not ( self.iColumns == other.iRows ) ): raise ValueError
            newMatrix: Matrix = Matrix.null( self.iRows, other.iColumns )
            for iRowIndex in range( newMatrix.iRows ):
                for iColumnIndex in range( newMatrix.iColumns ):
                    for x in range( self.iRows ):
                        newMatrix[ iRowIndex ][ iColumnIndex ] += self[ iRowIndex ][ x ] * other[ x ][ iColumnIndex ]
            return newMatrix
        
        else:
            
            newMatrix: Matrix = Matrix.null( self.iRows, self.iColumns )
            for iRowIndex in range( newMatrix.iRows ):
                for iColumnIndex in range( newMatrix.iColumns ):
                    newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex ][ iColumnIndex ] * other
            return newMatrix
    
    def __pow__( self, value: int ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        if ( value < -1 ): raise ValueError
        
        if ( value == -1 ):
            det: float = self.det()
            if ( det == 0 ): raise ValueError
            return self.com().T() * 1/det
        
        newMatrix: Matrix = Matrix.identity( 3 )
        for _ in range( value ):
            newMatrix *= self
        return newMatrix
    
    def __truediv__( self, value: float ) -> Matrix:
        newMatrix: Matrix = self.copy()
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] /= value
        return newMatrix
    
    def __floordiv__( self, value: float ) -> Matrix:
        newMatrix: Matrix = self.copy()
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] //= value
        return newMatrix
    
    def round( self, value: float ) -> Matrix:
        newMatrix: Matrix = self.copy()
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = round( newMatrix[ iRowIndex ][ iColumnIndex ], value ) #! Il faut demander si nous avons le droit d'utiliser la fonction round()
        return newMatrix
    
    
    
    def remove( self, iRow: int, iColumn: int ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.iRows-1, self.iColumns-1 )
        
        iRowSkip: int = 0
        for iRowIndex in range( newMatrix.iRows ):
            if ( iRowIndex == iRow ): iRowSkip += 1
            
            iColumnSkip: int = 0
            for iColumnIndex in range( newMatrix.iColumns ):
                if ( iColumnIndex == iColumn ): iColumnSkip += 1
                
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iRowIndex + iRowSkip ][ iColumnIndex + iColumnSkip ]
        
        return newMatrix
    
    def rotateLeft( self ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.iColumns, self.iRows )
        for iRowIndex in range( newMatrix.iRows ):
            for iColumnIndex in range( newMatrix.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iColumnIndex ][ self.iRows - iRowIndex - 1 ]
        return newMatrix
    
    def rotateRight( self ) -> Matrix:
        newMatrix: Matrix = Matrix.null( self.iColumns, self.iRows )
        for iRowIndex in range( newMatrix.iRows ):
            for iColumnIndex in range( newMatrix.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ self.iColumns - iColumnIndex - 1 ][ iRowIndex ]
        return newMatrix
    
    
    
    def det( self ) -> float:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        
        if ( self.iRows == 2 and self.iColumns == 2 ):
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        
        fSum: float = 0
        for i in range( self.iRows ):
            newMatrix: Matrix = self.remove( i, 0 )
            fSum += (-1)**i * newMatrix.det() * self[ i ][ 0 ]
        
        return fSum
    
    def com( self ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        newMatrix: Matrix = Matrix.null( self.iRows, self.iColumns )
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = (-1)**( iRowIndex + iColumnIndex ) * self.remove( iRowIndex, iColumnIndex ).det()
        return newMatrix
    
    def T( self ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        newMatrix: Matrix = Matrix.null( self.iColumns, self.iRows )
        for iColumnIndex in range( self.iColumns ):
            for iRowIndex in range( self.iRows ):
                newMatrix[ iRowIndex ][ iColumnIndex ] = self[ iColumnIndex ][ iRowIndex ]
        return newMatrix
    
    
    
    def __bool__( self ) -> bool:
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                if ( self[ iRowIndex ][ iColumnIndex ] ): return True
        return False
    
    def __eq__( self, other: Matrix ) -> bool:
        if ( not ( self.iRows == other.iRows and self.iColumns == other.iColumns ) ): return False
        for iRowIndex in range( self.iRows ):
            for iColumnIndex in range( self.iColumns ):
                if ( self[ iRowIndex ][ iColumnIndex ] != other[ iRowIndex ][ iColumnIndex ] ): return False
        return True
    
    def isSquare( self ) -> bool:
        return self.iRows == self.iColumns
    
    def isOrthogonal( self ) -> bool:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        
        newMatrix: Matrix = self.rotateRight()
        lVectors: list[ Vector ] = [ 0 for _ in range( newMatrix.iColumns ) ]
        for iColumnIndex in range( newMatrix.iColumns ):
            lVectors[ iColumnIndex ] = Vector( newMatrix[ iColumnIndex ] )
            if ( round( lVectors[ iColumnIndex ].norm(), 10 ) != 1 ): return False
        
        iLenVectors: int = len( lVectors )
        for iVectorIndex in range( iLenVectors ):
            for iNextVectorIndex in range( iVectorIndex + 1, iLenVectors ):
                if ( lVectors[ iVectorIndex ] * lVectors[ iNextVectorIndex ] != 0 ): return False
        
        return True
    
    def isSymetric( self ) -> bool:
        return ( self == self.T() )