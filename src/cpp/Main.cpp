#include <iostream>
#include "Matrix.h"

using namespace MatrixOperator;
using namespace MatrixPrinter;
using namespace EigenPairPrinter;

int main() {
    matrix m{{1,-1,0},{-2,4,-2},{0,-1,1}};
    printMatrix(m);
    eigenPair p = powerMethod(m);
    printEigenPair(p);

    return 0;
}
