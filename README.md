# Exercise 6.2 Stack

A stack is a data structure that you can add to and take from. Always to the top of it or from the top.

##  Adding to the Stack and Checking Emptiness

Create a `Stack` class that has a list of strings as an instance variable. Add the following methods to the class:

- `is_empty()` - returns a `boolean`-type value (true or false) that tells whether or not the stack is empty.

- `add(self, value)` - Adds the value given as a parameter to the top of the stack.

- `values()` - returns the values ​​contained in the stack as a list.

You can test your class with the following code:

```python
Stack s = Stack()
print(s.is_empty())
print(s.values())
s.add("Value")
print(s.is_empty())
print(s.values())
```

```plaintext
true
[]
false
[Value]
```

## Taking from the Stack

Add to the `Stack` class a `def take()` method, which returns the topmost value (i.e., the last value added to the deque) and removes it from the stack.

```python
s = Stack()
print(s.is_empty())
print(s.values())
s.add("Value")
print(s.is_empty())
print(s.values())
String taken = s.take()
print(s.is_empty())
print(s.values())
print(taken)
```

```plaintext
true
[]
false
[Value]
true
[]
Value
```

```python
s = Stack()
s.add("1")
s.add("2")
s.add("3")
s.add("4")
s.add("5")

while (not s.is_empty()):
    print(s.take())
```

```plaintext
5
4
3
2
1
```

Tip! When a value is added to a list, it goes to the end of the list. As such, the most recently added value is in the last index of the list - the `length` method provided by the list is useful for finding the last index. You can remove an element from a particular index using the `pop` method provided by the list.
