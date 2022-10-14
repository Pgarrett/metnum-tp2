#include "IO.h"
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

using namespace std;

namespace IO {
void writeEigenVectorsAsColumns(ofstream &file, vector<eigenPair> &results) {
  vector<vector<double>> transposed(results.size());
  for (eigenPair pair : results) {
    int row = 0;
    for (double v_i : pair.eigenvector) {
      transposed[row].push_back(v_i);
      row++;
    }
  }

  for (int i = 0; i < transposed.size(); i++) {
    // column names
    file << "v_" << i + 1 << ", ";
  }
  file << "\n";

  for (int i = 0; i < transposed.size(); i++) {
    for (double v_i : transposed[i]) {
      file << v_i << ", ";
    }
    file << "\n";
  }
  file.close();
}

void writeOutEigenPairs(vector<eigenPair> &results, string filename) {
  ostringstream streamObj;
  streamObj << fixed;
  streamObj << setprecision(2);
  ofstream eigenValues;
  ofstream eigenVectors;
  eigenValues.open(filename + "_eigenValues.csv");
  if (eigenValues.fail()) {
      cout << "unable to create eigenvalues for: " << filename << endl;
  }

  eigenVectors.open(filename + "_eigenVectors.csv");
  if (eigenVectors.fail()) {
      cout << "unable to create eigenvectors for: " << filename << endl;
  }

  eigenValues << "eigenValues,\n";
  for (eigenPair pair : results) {
    eigenValues << pair.eigenvalue << ",\n";
  }
  writeEigenVectorsAsColumns(eigenVectors, results);
  eigenValues.close();
}

void writeOutMatrix(const matrix &m, const string filepath) {
    ostringstream streamObj;
    streamObj << fixed;
    streamObj << setprecision(2);
    ofstream outputFile;
    outputFile.open(filepath, ios::out);
    if (outputFile.fail()) {
        cout << "unable to write out matrix in filepath: " << filepath << endl;
    }
    for (int i = 0; i < m.size(); ++i) {
        vector<double> row = m[i];
        for (int j = 0; j < row.size(); ++j) {
            outputFile << row[j];
            if (j < row.size() - 1) {
                outputFile << ", ";
            } else {
                outputFile << "\n";
            }
        }
    }
    outputFile.close();
}

} // namespace IO
