#if !defined(GIGASECOND_H)
#define GIGASECOND_H
#include "boost/date_time/posix_time/posix_time.hpp"

namespace gigasecond {
  using namespace boost::posix_time;
  const ptime advance(const ptime start) { return start + seconds(1e9); }
}

#endif

