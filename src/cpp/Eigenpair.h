//
// Created by Fernando N. Frassia on 10/1/22.
//

#include <vector>
#include <tuple>

using namespace std;


struct eigenPair {
    double eigenvalue;
    vector<double> eigenvector;
};

namespace EigenPairPrinter {
    void printEigenPair(eigenPair &p);
}

