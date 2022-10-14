//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Matrix.h"

#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "Constants.h"
#include "Matrix.h"
#include "Vector.h"

using namespace std;
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
matrix read(string filename) {
  ifstream file(filename.c_str());
  matrix res;
  string line, temp;
  // build matrix
  while (getline(file, line)) {
    vector<double> row;
    list<string> linkList = split(line, ' ');
    auto current = linkList.begin();
    auto last = linkList.end();
    while (current != last) {
      const string &ref = *current;
      row.push_back(stoi(ref));
      current = std::next(current, 1);
    }
    res.push_back(row);
  }
  return res;
}

matrix buildLaplacianMatrix(const matrix &a) {
  matrix D;
  for (int i = 0; i < a.size(); i++) {
    vector<double> row(a.size());
    double degree = 0;
    for (int j = 0; j < a.size(); j++) {
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
    int firstRowDimension = m[1].size();
    for (int i = 0; i < m.size(); ++i) {
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
  for (int i = 0; i < m.size(); ++i) {
    vector<double> row = m[i];
    double resi = 0;
    for (int j = 0; j < row.size(); ++j) {
      resi += row[j] * v[j];
    }
    result.push_back(resi);
  }

  return result;
}

eigenPair powerMethod(const matrix &m, int iterations, double epsilon) {
  assert(m.size() != 0);

  cout << "about to apply power method to matrix: " << endl;
//  printMatrix(m);

  vector<double> initialVector = randomVector(m[1].size());
  eigenPair p;
  vector<double> previousVector = initialVector;

  for (int i = 0; i < iterations; ++i) {
    vector<double> multipliedVector = multiplyMatrixByVector(m, previousVector);
    p.eigenvector = scale(1 / norm2(multipliedVector), multipliedVector);
    if (euclideanDistance(p.eigenvector, previousVector) < epsilon) {
      break;
    }
    previousVector = p.eigenvector;
  }

  normalize(p.eigenvector);
  p.eigenvalue = dotProduct(p.eigenvector, multiplyMatrixByVector(m, p.eigenvector));
  return p;
}

void substract(matrix &a, const matrix &b) {
  for (int i = 0; i < a.size(); i++) {
    for (int j = 0; j < a.size(); j++) {
      a[i][j] = a[i][j] - b[i][j];
    }
  }
}

void scaleMatrix(matrix &m, double c) {
  for (int i = 0; i < m.size(); i++) {
    for (int j = 0; j < m.size(); j++) {
      m[i][j] = m[i][j] * c;
    }
  }
}

matrix outerProduct(vector<double> &u, vector<double> &v) {
  matrix result;
  for (int i = 0; i < u.size(); i++) {
    vector<double> row;
    for (int j = 0; j < u.size(); j++) {
      row.push_back(u[i] * v[j]);
    }
    result.push_back(row);
  }
  return result;
}

double innerProduct(vector<double> &u, vector<double> &v) {
    assert(u.size() == v.size());
    double result = 0;
    for (double i = 0; i < u.size(); ++i) {
        result += u[i] * v[i];
    }
    return result;
}

matrix similarityMatrix(const matrix &a) {
    vector<double> rowOf0(a.size(), 0);
    matrix similarity(a.size(), rowOf0);

    for (double i = 0; i < a.size(); ++i) {
        for (double j = 0; j < a.size(); ++j) {
            vector<double> iVector = a[i];
            vector<double> jVector = a[j];
            double innerProductIJ = innerProduct(iVector, jVector);
            similarity[i][j] = innerProductIJ;
        }
    }
    return similarity;
}

void deleteMaxEigenValue(matrix &m, double a, vector<double> v) {
  matrix subtrahend = outerProduct(v, v);
  scaleMatrix(subtrahend, a);
  substract(m, subtrahend);
}

vector<eigenPair> deflationMethod(const matrix m, int iterations, double epsilon) {
  matrix A = m;
  vector<eigenPair> result;
  eigenPair p;
  for (int i = 0; i < m.size(); i++) {
    p = powerMethod(A, iterations, epsilon);
    result.push_back(p);
    deleteMaxEigenValue(A, p.eigenvalue, p.eigenvector);
  }
  return result;
}
} // namespace MatrixOperator

namespace MatrixPrinter {
void printMatrix(const matrix &m) {
  cout << "matrix: " << endl;
  for (int i = 0; i < m.size(); ++i) {
    cout << "[";
    vector<double> row = m[i];
    for (int j = 0; j < row.size(); ++j) {
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
