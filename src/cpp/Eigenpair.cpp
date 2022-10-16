//
// Created by Fernando N. Frassia on 10/1/22.
//

#include "Eigenpair.h"
#include <iostream>

using namespace std;
using namespace EigenPairPrinter;

namespace EigenPairPrinter {
void printVector(vector<double> &v, string msg) {
  cout << msg << "[";
  for (int i = 0; i < v.size(); ++i) {
    cout << v[i];
    if (i < v.size() - 1) {
      cout << ", ";
    } else {
      cout << "]" << endl;
    }
  }
}

void printEigenPair(eigenPair &p) {
  cout << "eigenvalue: " + to_string(p.eigenvalue) + ", ";
  printVector(p.eigenvector, "eigenvector: ");
}
} // namespace EigenPairPrinter
