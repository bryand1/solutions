#if !defined(HAMMING_H)
#define HAMMING_H
#include <string>

namespace hamming {
  // Compute the hamming distance of two DNA strings
  int compute(std::string a, std::string b) {
    if (a.length() != b.length()) {
      throw std::domain_error("Strands are different lengths");
    }
    int distance = 0;
    for (int i = 0; i < a.length(); i++) {
      if (a[i] != b[i]) distance++;
    }
    return distance;
  }
}

#endif
