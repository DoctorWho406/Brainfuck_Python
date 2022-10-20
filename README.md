# Brainfuck_Python

Simple implementation of the Brainfuck interpreter.

## Using

Instantiate the class.
```python
from brainfuck import BrainfuckMachine

bf = BrainfuckMachine()
```

It is possible to specify the number of memory registers as a parameter of the class constructor.
```python
bf = BrainfuckMachine(64)
```

Write your brainfuck code and assign it to the code variable.
```python
bf.code='++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.'
```

Run your code and see the result :smile:

```python
bf.run()
```
