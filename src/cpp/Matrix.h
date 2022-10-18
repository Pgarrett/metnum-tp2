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

struct EP2 {
    double eigenvalue;
    VectorXd eigenvector;
};

namespace MatrixOperator {


//matrix read(string filename);
    SparseMatrix<double> read(string filename);
void scaleMatrix(matrix &m, double scalar);
void substract(matrix &a, const matrix &b);
matrix outerProduct(vector<double> &u, vector<double> &v);
double innerProduct(vector<double> &u, vector<double> &v);
matrix similarityMatrix(const Matrix<double, Dynamic, Dynamic, RowMajor> &a);
void deleteMaxEigenValue(matrix &m, double a, vector<double> v);
vector<double> multiplyMatrixByVector(const matrix &m, const vector<double> &v);
eigenPair power_iteration(const Matrix<double, Dynamic, Dynamic, RowMajor> &X, unsigned iterations, double epsilon);
vector<eigenPair> deflationMethod(const Matrix<double, Dynamic, Dynamic, RowMajor> &m, int iterations, double epsilon);
} // namespace MatrixOperator

namespace MatrixPrinter {
void printMatrix(const matrix &m);
}
