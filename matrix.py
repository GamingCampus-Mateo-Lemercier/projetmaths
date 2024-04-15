from __future__ import annotations

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
    
    def __pow__( self, iPower: int ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
        if ( iPower < -1 ): raise ValueError
        
        if ( iPower == -1 ):
            pass
        
        newMatrix: Matrix = Matrix.identity( 3 )
        for _ in range( iPower ):
            newMatrix *= self
        return newMatrix
    
    
    
    def det( self ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError
    
    def com( self ) -> Matrix:
        if ( not ( self.iRows == self.iColumns ) ): raise ValueError



M1: Matrix = Matrix([
    [  0, -3, -2 ],
    [  1, -4, -2 ],
    [ -3,  4,  1 ]
])
M2: Matrix = Matrix([
    [  4, -5, -2 ],
    [  5, -6, -2 ],
    [ -8,  9,  3 ]
])
print( M1*M2 )