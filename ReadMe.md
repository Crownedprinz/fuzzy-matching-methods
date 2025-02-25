# Fuzzy Matching Methods

This project demonstrates different fuzzy matching methods in Python. The main module ([main.py](main.py)) includes:
  
- **fuzzywuzzy**: Utilizes the [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) library to compare strings with various ratios.
- **rapidfuzz**: Uses the [RapidFuzz](https://github.com/maxbachmann/RapidFuzz) library for similar string comparison functions.
- **difflib**: Leverages Python's built-in `difflib` library to compare two strings using sequence matching.

## How to Run

1. Make sure you have installed the required packages:
   - For `fuzzywuzzy`:  
     ```sh
     pip install fuzzywuzzy
     ```
   - For [rapidfuzz](http://_vscodecontentref_/1):  
     ```sh
     pip install rapidfuzz
     ```

2. Run the main module:
   ```sh
   python main.py