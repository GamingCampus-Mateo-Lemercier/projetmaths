from matrix import Matrix

def WhichTransformation( matrix: Matrix ) -> str:
    if ( not matrix.isSquare() ): return "Pas une isométrie vectorielle"
    if ( not matrix.isOrthogonal() ): return "Pas une isométrie vectorielle"
    
    if ( matrix == Matrix.identity( matrix.iRows ) ): return "Transformation identité"
    if ( matrix == Matrix.identity( matrix.iRows ) * -1 ): return "Symétrie par rapport à l'origine"
    
    det: float = matrix.det()
    
    if ( matrix.isSymetric() ):
        if ( det == 1 ): return "Symétrie par rapport à une droite"
        elif ( det == -1 ): return "Symétrie par rapport à un plan"
    else:
        if ( det == 1 ): return "Rotation par rapport à une droite"
        elif ( det == -1 ): return "Anti-rotation par rapport à une droite"