### Movie Theater Seating - Walmart

A service for assigning seats within a movie theater to
fulfill reservation requests.

Logic:
- Maintain a preference of rows (middle rows have higher preference)
- Assign seating in preferred rows from left to right
- Earliest requests assigned first.
- All seats are together if possible. Even if seats have to be split, the split groups are assigned together. Together Seating has higher preference over Preferred row seating; until tickets are split.
 
There are 3 files:
- `theater.py`: Contains theater class and methods that implement the algorithm as well as helper functions.
- `main.py`: Entry file for execution that reads and processes input and writes output.
- `test.py`: Unit test file. Can be executed using pytest.

Input Format:
- Input is read from an input file placed in root of repo directory.
- There can be multiple requests in each file. Each request on a newline.
- Requests are of the format {Request ID} {Number of Tickets requested}. For e.g. `R001 4`

Output Format:
- Output is written to `output.txt` created in the root of repo directory. The full path is returned on the terminal.
- Output is of the format {Request ID} {Reserved Tickets}. For e.g. `R001 F1,F2,F3,F4`

How to run: 
- General Execution: `python3 main.py /path/to/input` (Make sure `input.txt` exists)
- Tests: `python3 -m pytest test.py`