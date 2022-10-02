#include <string>
#include <vector>

#include "Eigenpair.h"

using namespace std;

namespace IO {
void writeOutEigenPairs(vector<eigenPair> &pairs, string file);
void writeEigenVectorsAsColumns(ofstream &file, vector<eigenPair> &results);
} // namespace IO
