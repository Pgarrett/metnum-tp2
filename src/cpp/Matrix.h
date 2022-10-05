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
matrix buildLaplacianMatrix(const matrix &a);
void scaleMatrix(matrix &m, double scalar);
void substract(matrix &a, const matrix &b);
matrix outerProduct(vector<double> u, vector<double> v);
void deleteMaxEigenValue(matrix &m, double a, vector<double> v);
vector<double> multiplyMatrixByVector(const matrix &m, const vector<double> &v);
eigenPair powerMethod(const matrix &m, int iterations, double epsilon);
vector<eigenPair> deflationMethod(const matrix m, int iterations,
                                  double epsilon);
} // namespace MatrixOperator

namespace MatrixPrinter {
void printMatrix(const matrix &m);
}
