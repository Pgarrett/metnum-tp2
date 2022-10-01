//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Matrix.h"
#include "Vector.h"
#include "Constants.h"
#include <iostream>
#include <cassert>
#include <cstdlib>

using namespace std;
using namespace MatrixOperator;
using namespace VectorOperator;
using namespace Constants;

namespace MatrixOperator {
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

    bool matrixColumnsAreTheSameDimensionAsVector(const matrix &m, const vector<double> &v) {
        return m[1].size() == v.size();
    }

    bool matrixVectorMultiplicationIsPossible(const matrix &m, const vector<double> &v) {
        return allRowsHaveTheSameDimension(m) && matrixColumnsAreTheSameDimensionAsVector(m, v);
    }

    vector<double> multiplyMatrixByVector(const matrix &m, const vector<double> &v) {
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

    eigenPair powerMethod(const matrix &m) {
        assert(m.size() != 0);

        vector<double> initialVector = randomVector(m[1].size());
        eigenPair p;
        vector<double> previousVector = initialVector;

        for (int i = 0; i < powerMethodIterations; ++i) {
            vector<double> multipliedVector = multiplyMatrixByVector(m, previousVector);
            p.eigenvector = scale(1/norm2(multipliedVector), multipliedVector);
            if (euclideanDistance(p.eigenvector, previousVector) < powerMethodEpsilon) {
                break;
            }
            previousVector = p.eigenvector;
        }

        p.eigenvalue = dotProduct(p.eigenvector, multiplyMatrixByVector(m, p.eigenvector));
        return p;
    }
}

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
}