# SWIG_TEST

A simple test for creating Python wrapper for C++  using SWIG

## Description

In here, a Python wrapper (example.py) for the example.cpp and example.h codes is created. The folder also contains an interface file (example.i). The example cpp and header is to calculate the area and perimeter of a circle or square.
By utilizing [SWIG](https://www.swig.org/) (Simplified Wrapper and Interface Generator) and setuptools (setup.py) inside Visual Studio 2022, three files of example_wrap.cpp, example.py, and _example.cp311-win_amd64.pyd were generated.


## Getting Started

### Dependencies

* Python 3.8 or above
* SWIG 4.1.1
* OS: Windows 10, 11
* Visual Studio 2022

### Executing program

* Simply run runme.py

## Expected output!

A print of:
- "Creating some objects:
    Created circle <example.Circle; proxy of <Swig Object of type 'Circle *' at 0x000001FD20A05A10> >
    Created square <example.Square; proxy of <Swig Object of type 'Square *' at 0x000001FD20A05980> >

A total of 2 shapes were created

Here is their current position:
    Circle = (20.000000, 30.000000)
    Square = (-10.000000, 5.000000)

Here are some properties of the shapes:
    <example.Circle; proxy of <Swig Object of type 'Circle *' at 0x000001FD20A05A10> >
        area      = 314.1592653589793
        perimeter = 62.83185307179586
    <example.Square; proxy of <Swig Object of type 'Square *' at 0x000001FD20A05980> >
        area      = 100.0
        perimeter = 40.0

Guess I'll clean up now
0 shapes remain
Goodbye"

## Authors

Contributors names and contact info
- [Omid Jahanmahin](https://github.com/ozj1)

## Version History

* 0.1
    * Initial Release

## License

## Acknowledgments

