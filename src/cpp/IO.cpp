#include "IO.h"
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>

using namespace std;

namespace IO {
void writeOutEigenPair(eigenPair &p, string file) {
  ostringstream streamObj;
  streamObj << fixed;
  streamObj << setprecision(2);
  ofstream myfile;
  myfile.open(file);
  streamObj << "eigenvalue: " << p.eigenvalue;
  myfile << streamObj.str() + "\n";
  myfile << "["
         << "\n";
  for (double element : p.eigenvector) {
    myfile << "  " << element << ", \n";
  }
  myfile << "]";
  myfile.close();
}
} // namespace IO
