# Matrices

Matrices contains many Python functions to manipulate vectors and matrices, representing concepts learned in M340L (Matrices in Linear Algebra) at UT Austin

## Creator
Wajih Ahmed (UT EID: wa4432)

## Usage

```python
from vector import *
from matrix import *
from operations import *

# Creates vector
vec = Vector( 3 )
vec.createVector( [1 , 2 , 3] )

# Creates matrix
mat = Matrix( 3 , 2 )
v1 = Vector( 3 )
v1.createVector( [4 , 5 , 6] )
v2 = Vector( 3 )
v2.createVector( [7 , 8 , 9] )
mat.createMatrix( [v1 , v2] )

# Prints product of matrix and vector
print( multiplyMatrixVector( mat , vec )
```

## Current Status
Updated periodically with new functions to represent more concepts involving matrices.
