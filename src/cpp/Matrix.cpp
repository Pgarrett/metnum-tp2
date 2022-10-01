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
#include "Vector.h"

using namespace std;
using namespace MatrixOperator;
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
      const string &ref = *current; // take a reference
      std::cout << ref;
      row.push_back(stoi(ref));
      current = std::next(current, 1);
    }
    res.push_back(row);
  }
  return res;
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

  p.eigenvalue =
      dotProduct(p.eigenvector, multiplyMatrixByVector(m, p.eigenvector));
  return p;
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
