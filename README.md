# Random_Numbers_Generator

## Description / Background
A program that generates a set of random numbers at an interval defined by the user, from initiation until the user requests a stop. The generated numbers are saved in a text file.

## Requirements
- Possibility to:
   - input how many random numbers the user wants to get at the same time (between 1 and 6)
   - define at what interval the random numbers should be generated (in seconds)
   - choose data type for each random number (int or float)
   - to define min & max range for each number
-	All inputs have to be protected against invalid input type (all have to be integers). If a user inputs a string, an error message should be displayed and he should be prompted to give the correct value
-	Generated values have to be saved in a csv file
-	Function can be launched from command line, or via an executable

## Design
### Step-by-step
1)	How many numbers should be generated
2)	At what time interval
3)	For each number, what should be the type of the output (int / float)
4)	For each number, what are min & max values from which the number should be generated

### Workflow

TBD

### Functions
- Generate random numbers
- Input function with formatting
   - The same for all 4 inputs, only command line text changes  function is called with an argument
- Input :how many
- Input: time interval
- Input: data type
- Input: min/max
- If input incorrect
- Write to file

## Limitations
The way the function re-run is handled is probably not what it's supposed to be.
