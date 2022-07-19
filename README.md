# LeetCode Submissions
This repository contains all my solutions to the leetcode problems I've solved, I mainly use this to revise, but if this helps you then even better!

## Setup
No setup required, once cloned everything is ready, you can run the unit tests by using `python3 -m unittest` in the terminal

## Structure
The solutions are in the `solutions` package, each file can be run individually and using the provided `.vscode/launch.json` file, you can
simply run it using vscode debug, otherwise you can just use `python3 -m solutions/solution_class.py`

For testing, I created test cases for each class in the `tests` directory, and if you don't want to run the entire suite you can just run the
solution itself and it will run the test cases that correlate to it, and you can mess around in the `if __name__ == '__main__'` block to do whatever you like

## Misc
- For linked lists, I made it easier to test by adding a `ListNode` class which contains several helpful methods, especially a static methods that converts a list to a linked list
- Some files contain more than 1 solution, usually a naive/brute force approach and a more efficient solution.
- I try to be as concise as possible when explaining the solution, but if you find anything confusing please let me know!