//
// Created by Fernando N. Frassia on 10/1/22.
//

#include <vector>
#include "Eigenpair.h"

using namespace std;

typedef vector<vector<double>> matrix;

namespace MatrixOperator {
    vector<double> multiplyMatrixByVector(const matrix &m, const vector<double> &v);
    eigenPair powerMethod(const matrix &m);
}

namespace MatrixPrinter {
    void printMatrix(const matrix &m);
}