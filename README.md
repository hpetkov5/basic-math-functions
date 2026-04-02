# basic-math-functions

MyMath is a Python class that performs basic arithmetic operations (addition, subtraction, multiplication, division) and showing how Python operators behave for different data types. It supports multiple built-in types such as numbers, strings, lists, tuples, and booleans.

## Installation

### Requirements
- Python 3.11 or higher

### Install locally

Clone the repository and install the package.

## Usage

First, import the `MyMath` class.

Then create an instance of the class and call the functions.

### Addition

Supports work with integers, floats, strings, lists and booleans.

### Subtraction

Supports work with integers, floats and booleans.

### Multiplication

Supports work with integers, floats, booleans.
Can be used to repeat strings, lists and tuples.

### Division

Supports work with integers, floats and booleans.

## Testing

This project uses unittest for unit testing.

### Running the unittests

Make sure dependencies are installed, then run:
```bash
python -m unittest test/test_my_math.py 
```
### Coverage

Make sure dependencies are installed, then run:
```bash
coverage run -m pytest -s
```
For HTML report run:
```bash
coverage html
```
Last coverage report was ran on 2026-04-02 and is available in the `htmlcov/` directory.
Open `index.html` in a browser to view it.

