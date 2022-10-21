//
// Created by Fernando N. Frassia on 10/1/22.
//

#pragma once

#include <list>
#include <vector>

#include "Eigenpair.h"
#include "string"

#include "Eigen/Sparse"

using namespace std;
using namespace Eigen;

typedef vector<vector<double>> matrix;

namespace MatrixOperator {

SparseMatrix<double> read(string filename);
eigenPair power_iteration(const Matrix<double, Dynamic, Dynamic, RowMajor> &X, unsigned iterations, double epsilon);
vector<eigenPair> deflationMethod(const Matrix<double, Dynamic, Dynamic, RowMajor> &m, int iterations, double epsilon);
}

namespace MatrixPrinter {
void printMatrix(const matrix &m);
}
