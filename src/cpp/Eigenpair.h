//
// Created by Fernando N. Frassia on 10/1/22.
//
#ifndef Eigenpair
#define Eigenpair

#include <tuple>
#include <vector>

using namespace std;

struct eigenPair {
  double eigenvalue;
  vector<double> eigenvector;
};

namespace EigenPairPrinter {
void printEigenPair(eigenPair &p);
}

#endif
