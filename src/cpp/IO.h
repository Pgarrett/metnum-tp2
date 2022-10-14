#include <string>
#include <vector>
#include "Matrix.h"
#include "Eigenpair.h"

using namespace std;

namespace IO {
void writeOutEigenPairs(vector<eigenPair> &pairs, string file);
void writeEigenVectorsAsColumns(ofstream &file, vector<eigenPair> &results);
void writeOutMatrix(const matrix &m, const string filename);
} // namespace IO
