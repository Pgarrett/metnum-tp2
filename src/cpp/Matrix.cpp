//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Matrix.h"

#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "Constants.h"
#include "Vector.h"

using namespace MatrixOperator;
using namespace MatrixPrinter;
using namespace VectorOperator;
using namespace Constants;

/* Helper function */
list<string> split(string originalString, char delim) {
  list<string> output;
  string current;
  stringstream stream(originalString);

  while (getline(stream, current, delim)) {
    output.push_back(current);
  }

  return output;
}

namespace MatrixOperator {

SparseMatrix<double> read(string filename) {
  ifstream file(filename.c_str());
  matrix res;
  string line, temp;
  // build matrix
  vector<Triplet<double>> inputReader;
  int rowNumber = 0;
  while (getline(file, line)) {
    list<string> linkList = split(line, ' ');
    auto current = linkList.begin();
    auto last = linkList.end();
    int columnNumber = 0;
    while (current != last) {
      const string &ref = *current;
      inputReader.push_back(Triplet(rowNumber, columnNumber, stod(ref)));
      current = std::next(current, 1);
      columnNumber++;
    }
    rowNumber++;
  }
  SparseMatrix<double> result(rowNumber, rowNumber);
  result.setFromTriplets(inputReader.begin(), inputReader.end());
  return result;
}

matrix buildLaplacianMatrix(const matrix &a) {
  matrix D;
  for (double i = 0; i < a.size(); i++) {
    vector<double> row(a.size());
    double degree = 0;
    for (double j = 0; j < a.size(); j++) {
      degree += a[i][j];
    }
    row[i] = degree;
    D.push_back(row);
  }

  substract(D, a);
  return D;
}

bool allRowsHaveTheSameDimension(const matrix &m) {
  if (m.size() > 0) {
    unsigned long firstRowDimension = m[1].size();
    for (unsigned long i = 0; i < m.size(); ++i) {
      if (m[i].size() != firstRowDimension) {
        return false;
      }
    }
  }
  return true;
}

bool matrixColumnsAreTheSameDimensionAsVector(const matrix &m,
                                              const vector<double> &v) {
  return m[1].size() == v.size();
}

bool matrixVectorMultiplicationIsPossible(const matrix &m,
                                          const vector<double> &v) {
  return allRowsHaveTheSameDimension(m) &&
         matrixColumnsAreTheSameDimensionAsVector(m, v);
}

vector<double> multiplyMatrixByVector(const matrix &m,
                                      const vector<double> &v) {
  assert(matrixVectorMultiplicationIsPossible(m, v));

  vector<double> result;
  for (unsigned long i = 0; i < m.size(); ++i) {
    vector<double> row = m[i];
    vector<double> products_vector;
    for (unsigned long j = 0; j < row.size(); ++j) {
      products_vector.push_back(row[j] * v[j]);
    }
    result.push_back(kahanSum(products_vector));
  }

  return result;
}

void substract(matrix &a, const matrix &b) {
  for (unsigned long i = 0; i < a.size(); i++) {
    for (unsigned long j = 0; j < a.size(); j++) {
      a[i][j] = a[i][j] - b[i][j];
    }
  }
}

void scaleMatrix(matrix &m, double c) {
  for (unsigned long i = 0; i < m.size(); i++) {
    for (unsigned long j = 0; j < m.size(); j++) {
      m[i][j] = m[i][j] * c;
    }
  }
}

matrix outerProduct(vector<double> &u, vector<double> &v) {
  matrix result;
  for (unsigned long i = 0; i < u.size(); i++) {
    vector<double> row;
    for (unsigned long j = 0; j < u.size(); j++) {
      row.push_back(u[i] * v[j]);
    }
    result.push_back(row);
  }
  return result;
}

double innerProduct(vector<double> &u, vector<double> &v) {
  assert(u.size() == v.size());
  vector<double> products_vector;
  for (double i = 0; i < u.size(); ++i) {
    products_vector.push_back(u[i] * v[i]);
  }
  return kahanSum(products_vector);
}

matrix similarityMatrix(const SparseMatrix<double> &a) {
  vector<double> rowOf0(a.size(), 0);
  matrix similarity(a.size(), rowOf0);

  for (double i = 0; i < a.size(); ++i) {
    for (double j = 0; j < a.size(); ++j) {
//      vector<double> iVector = a[i];
//      vector<double> jVector = a[j];
//      double innerProductIJ = innerProduct(iVector, jVector);
//      similarity[i][j] = innerProductIJ;
    }
  }
  return similarity;
}

eigenPair power_iteration(const Matrix<double, Dynamic, Dynamic, RowMajor> &m, unsigned int iterations, double epsilon) {
    VectorXd previousVector = VectorXd::Random(m.cols());
    EP2 result;

    for (unsigned int i = 0; i < iterations; i++) {
        VectorXd multipliedVector = m * previousVector;
        multipliedVector = multipliedVector / multipliedVector.norm();
        double cos_angle = multipliedVector.transpose() * previousVector;
        previousVector = multipliedVector;
        if ((1 - epsilon) < cos_angle && cos_angle <= 1) {
            break;
        }
    }

    eigenPair eigenPair;

    eigenPair.eigenvalue = previousVector.transpose() * m * previousVector;
    for (VectorXd::iterator it = previousVector.begin(); it != previousVector.end(); it++) {
        eigenPair.eigenvector.push_back(*it);
    }
    return eigenPair;
}

vector<eigenPair> deflationMethod(const Matrix<double, Dynamic, Dynamic, RowMajor> &m, int iterations, double epsilon) {
    Matrix<double, Dynamic, Dynamic, RowMajor> A = m;
    vector<eigenPair> result;
    double a = 0;
    VectorXd v = VectorXd::Zero(A.rows());
    eigenPair p;
    for (int i = 0; i < m.rows(); i++)
    {
        A = A - (a * v * v.transpose());
        p = power_iteration(A, iterations, epsilon);
        result.push_back(p);
        a = p.eigenvalue;
        vector<double> ev = p.eigenvector;
        v = Eigen::Map<Eigen::VectorXd, Eigen::Unaligned>(ev.data(), ev.size());
    }
  return result;
}
} // namespace MatrixOperator

namespace MatrixPrinter {
void printMatrix(const matrix &m) {
  for (unsigned long i = 0; i < m.size(); ++i) {
    cout << "[";
    vector<double> row = m[i];
    for (unsigned long j = 0; j < row.size(); ++j) {
      cout << row[j];
      if (j < row.size() - 1) {
        cout << ", ";
      } else {
        cout << "]" << endl;
      }
    }
  }
}
} // namespace MatrixPrinter
