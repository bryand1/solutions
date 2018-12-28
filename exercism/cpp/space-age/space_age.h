#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H
namespace space_age {
    class space_age {
    private:
        double _seconds;
        double _earth_years;
    public:
        space_age(long s) {
            _seconds = (double)s;
            _earth_years = _seconds / 31557600.0;
        }
        long seconds() const { return _seconds; }
        double on_earth() const { return _earth_years; }
        double on_mercury() const { return _earth_years / 0.2408467; }
        double on_venus() const { return _earth_years / 0.61519726; }
        double on_mars() const { return _earth_years / 1.8808158; }
        double on_jupiter() const { return _earth_years / 11.862615; }
        double on_saturn() const { return _earth_years / 29.447498; }
        double on_uranus() const { return _earth_years / 84.016846; }
        double on_neptune() const { return _earth_years / 164.79132; }
    };
}
#endif
