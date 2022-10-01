//
// Created by Fernando N. Frassia on 10/1/22.
//

#include <list>
#include <vector>

#include "Eigenpair.h"
#include "string"

using namespace std;

typedef vector<vector<double>> matrix;

namespace MatrixOperator {
matrix read(string filename);
vector<double> multiplyMatrixByVector(const matrix &m, const vector<double> &v);
eigenPair powerMethod(const matrix &m);
} // namespace MatrixOperator

namespace MatrixPrinter {
void printMatrix(const matrix &m);
}
