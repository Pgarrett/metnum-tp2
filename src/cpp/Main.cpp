#include <iostream>

#include "IO.h"
#include "Matrix.h"

using namespace MatrixOperator;
using namespace MatrixPrinter;
using namespace EigenPairPrinter;
using namespace IO;
using namespace std;

void computeAndWriteOutSimilarityMatrix(const string input) {
    matrix M = read("./examples/" + input + ".txt");
    matrix S = similarityMatrix(M);
    writeOutMatrix(S, "./results/" + input + "_similarityMatrix.csv");
}

int main(int argc, char *argv[]) {
  if (argc < 3) {
    cerr << "Formato de entrada: " << argv[0]
              << "<archivo> <iteraciones> <tolerancia>" << endl;
    return 1;
  }

  // lectura parametros:
  string input = argv[1];
  int iterations = atof(argv[2]);
  double tolerance = atof(argv[3]);

  cout << "Resolviendo matriz: " << input << endl;
  cout << "Con iteraciones: " << to_string(iterations) << endl;
  cout << "Con tolerancia: " << to_string(tolerance) << endl;

  matrix M = read("./examples/" + input + ".txt");
  //matrix L = buildLaplacianMatrix(M);

  computeAndWriteOutSimilarityMatrix(input);

  vector<eigenPair> res = deflationMethod(M, iterations, tolerance);
  writeOutEigenPairs(res, "./results/" + input);

  return 0;
}
