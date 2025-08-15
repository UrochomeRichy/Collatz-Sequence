# Collatz Sequence Challenge

This program demonstrates the **Collatz sequence**, also known as the *3n + 1 problem*.

## Task
- Write a function named `collatz()` that has one parameter `number`.
  - If `number` is even, the function should print `number // 2` and return this value.
  - If `number` is odd, the function should print and return `3 * number + 1`.

- Then write a program that:
  1. Prompts the user to type in an integer.
  2. Keeps calling `collatz()` on that number until the function returns `1`.

## Example
```python
Please enter any integer number of your choice.
6
3
10
5
16
8
4
2
1

