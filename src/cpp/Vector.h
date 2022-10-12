//
// Created by Fernando N. Frassia on 10/1/22.
//

#include <vector>

using namespace std;

namespace VectorOperator {
    double euclideanDistance(const vector<double> &v1, const vector<double> &v2);

    void normalize(vector<double> &v);

    double norm2(const vector<double> &v);

    vector<double> scale(double scalar, const vector<double> &v);

    vector<double> randomVector(int dimension);

    double dotProduct(const vector<double> &v1, const vector<double> &v2);
}