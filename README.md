# Expanding Nebula

This project presents a solution to the "Expanding Nebula" challenge from Google's Foobar, a series of coding challenges used by Google to identify potential recruits. The challenge involves analyzing a 2D grid representing the current state of a nebula and determining the number of possible previous states that could have led to this configuration.

## Challenge Description

You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies. However, one of the escape pods has flown into a nearby nebula, causing you to lose track of it. You start monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. However, you do find that the gas of the steadily expanding nebula follows a simple pattern, meaning that you should be able to determine the previous state of the gas and narrow down where you might find the pod.

From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, so you can model it as a 2D grid. You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, specifically:

1. That cell
2. The cell below it
3. The cell to the right of it
4. The cell below and to the right of it

If, in the current state, exactly one of those four cells in the 2x2 block has gas, then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.

For example, consider the previous state of the grid (p) as:


```
.O..
..O.
...O
O...
```


To see how this grid will change to become the current grid (c) over the next time step, consider the 2x2 blocks of cells around each cell. Applying the transformation rules, the resulting current state (c) would be:


```
O.O
.O.
O.O
```


Note that the resulting output will have one fewer row and column, since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.

## Solution Approach

The solution involves analyzing the transformation rules and determining all possible previous states that could result in the given current state. This requires generating potential 2x(n+1) grids and checking if the resulting 1xn row matches any row in the input grid. By iterating through all possible configurations and applying the transformation rules, the solution counts the number of valid previous states.

## Repository Contents

- **Solution.py**: Contains the implementation of the solution algorithm.
- **Tests.py**: Includes test cases to validate the correctness of the solution.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SecCodeSmith/Expanding-Nebula.git
   cd Expanding-Nebula
   ```


2. **Run the Solution**:
   ```bash
   python Solution.py
   ```


3. **Run the Tests**:
   ```bash
   python Tests.py
   ```


For more details, visit the [Expanding-Nebula GitHub repository](https://github.com/SecCodeSmith/Expanding-Nebula).
