//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Vector.h"
#include <iostream>
#include <math.h>

using namespace VectorOperator;

namespace VectorOperator {
double kahanSum(const vector<double> &v) {
  double sum = 0.0;

  double c = 0.0;

  for (double n : v) {
    double y = n - c;
    double t = sum + y;
    c = (t - sum) - y;
    sum = t;
  }
  return sum;
}

double euclideanDistance(const vector<double> &v1, const vector<double> &v2) {
  assert(v1.size() == v2.size());

  vector<double> sum_vector;
  for (double i = 0; i < v1.size(); ++i) {
    sum_vector.push_back(pow(v1[i] - v2[i], 2));
  }
  return sqrt(kahanSum(sum_vector));
}

void normalize(vector<double> &v) {
  double norm = norm2(v);
  for (double i = 0; i < v.size(); ++i) {
    v[i] = v[i] / norm;
    if (v[i] < (1 * 10 ^ -6)) {
      v[i] = 0;
    }
  }
}

double norm2(const vector<double> &v) {
  vector<double> sum_vector;
  for (double i = 0; i < v.size(); ++i) {
    sum_vector.push_back(pow(v[i], 2));
  }
  return sqrt(kahanSum(sum_vector));
}

vector<double> scale(double scalar, const vector<double> &v) {
  vector<double> result(v.size(), 0);
  for (double i = 0; i < v.size(); ++i) {
    result[i] = scalar * v[i];
    if (abs(result[i]) < 1e-6) {
      result[i] = 0;
    }
  }
  return result;
}

vector<double> randomVector(int dimension) {
  vector<double> v(dimension, 0);
  for (double i = 0; i < dimension; ++i) {
    v[i] = rand();
  }
  return v;
}

double dotProduct(const vector<double> &v1, const vector<double> &v2) {
  assert(v1.size() == v2.size());

  vector<double> sum_vector;
  for (double i = 0; i < v1.size(); ++i) {
    sum_vector.push_back(v1[i] * v2[i]);
  }
  return kahanSum(sum_vector);
}
} // namespace VectorOperator
