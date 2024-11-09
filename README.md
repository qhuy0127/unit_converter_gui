# Unit Converter

A user-friendly tool for converting between different units of measurement. This tool supports conversions for temperature (Celsius/Fahrenheit), distance (Kilometers/Miles), and weight (Kilograms/Pounds).

## Features

- Convert between multiple unit types:
  - Temperature: Celsius ↔ Fahrenheit
  - Distance: Kilometers ↔ Miles
  - Weight: Kilograms ↔ Pounds
- Two interfaces available:
  - Command-line interface (CLI)
  - Graphical user interface (GUI)
- Error handling and input validation
- Clear and formatted output

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/qhuy0127/unit-converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd unit-converter
   ```
3. Make sure you have Python installed on your system

## Usage

### GUI Version (Recommended for most users)
1. Run the GUI version:
   ```bash
   python unit_converter_gui.py
   ```
2. In the window that appears:
   - Select the conversion category (Temperature/Distance/Weight)
   - Choose the conversion direction
   - Enter your value
   - Click "Convert" to see the result

### Command Line Version
The basic syntax is:
```bash
python unit_converter.py VALUE CONVERSION_TYPE
```

Available conversion types:
- `c2f`: Celsius to Fahrenheit
- `f2c`: Fahrenheit to Celsius
- `km2mi`: Kilometers to Miles
- `mi2km`: Miles to Kilometers
- `kg2lb`: Kilograms to Pounds
- `lb2kg`: Pounds to Kilograms

#### Command Line Examples

1. Convert 25 degrees Celsius to Fahrenheit:
   ```bash
   python unit_converter.py 25 c2f
   ```

2. Convert 10 kilometers to miles:
   ```bash
   python unit_converter.py 10 km2mi
   ```

3. Convert 150 pounds to kilograms:
   ```bash
   python unit_converter.py 150 lb2kg
   ```

## Requirements
- Python 3.x
- tkinter (included with Python)

## Error Handling

Both versions include error handling for:
- Invalid input values
- Incorrect conversion types
- General runtime errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.