#include <iostream>

#include "Matrix.h"

using namespace MatrixOperator;
using namespace MatrixPrinter;
using namespace EigenPairPrinter;

int main(int argc, char *argv[]) {
  if (argc < 3) {
    std::cerr << "Formato de entrada: " << argv[0]
              << "<archivo> <iteraciones> <tolerancia>" << std::endl;
    return 1;
  }

  // lectura parametros:
  std::string input = argv[1];
  int iterations = std::atof(argv[2]);
  double tolerance = std::atof(argv[3]);

  std::cout << "Resolviendo matriz: " << input << std::endl;

  matrix M = read(input);

  // matrix m{{1, -1, 0}, {-2, 4, -2}, {0, -1, 1}};
  printMatrix(M);
  eigenPair p = powerMethod(M);
  printEigenPair(p);

  return 0;
}
