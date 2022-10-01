//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Vector.h"
#include <math.h>

using namespace std;
using namespace VectorOperator;

namespace VectorOperator {
    double euclideanDistance(const vector<double> &v1, const vector<double> &v2) {
        assert(v1.size() == v2.size());

        double sum = 0;
        for (int i = 0; i < v1.size(); ++i) {
            sum += pow(v1[i] - v2[i], 2);
        }
        return sqrt(sum);
    }

    double norm2(const vector<double> &v) {
        double sum = 0;
        for (int i = 0; i < v.size(); ++i) {
            sum += pow(v[i], 2);
        }
        return sqrt(sum);
    }

    vector<double> scale(double scalar, const vector<double> &v) {
        vector<double> result(v.size(), 0);
        for (int i = 0; i < v.size(); ++i) {
            result[i] = v[i] * scalar;
        }
        return result;
    }

    vector<double> randomVector(int dimension) {
        vector<double> v(dimension, 0);
        for (int i = 0; i < dimension; ++i) {
            v[i] = rand();
        }
        return v;
    }

    double dotProduct(const vector<double> &v1, const vector<double> &v2) {
        assert(v1.size() == v2.size());

        double sum = 0;
        for (int i = 0; i < v1.size(); ++i) {
            sum += v1[i] * v2[i];
        }
        return sum;
    }
}