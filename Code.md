# Python Data Types & Syntax

---

## 1. int
Whole numbers — no decimal point.

- Unlimited size in Python
- Supports: `+`, `-`, `*`, `//`, `%`, `**`

**Syntax:**
```python
variable_name = whole_number
```

**Examples:**
```python
x = 10
y = -5
z = 1_000_000
```

---

## 2. str
Text — a sequence of characters.

- Immutable (cannot be changed in place)
- Supports indexing, slicing, and f-strings

**Syntax:**
```python
variable_name = "text"
variable_name = 'text'
variable_name = f"Hello {other_var}"
```

**Examples:**
```python
name = "Alice"
msg  = 'hello'
s    = f"Hi {name}"
```

---

## 3. float
Decimal / real numbers (64-bit IEEE 754).

- Supports scientific notation (`1.5e10`)
- Watch out for floating-point rounding errors

**Syntax:**
```python
variable_name = decimal_number
```

**Examples:**
```python
pi   = 3.14159
temp = -0.5
sci  = 1.5e10
```

---

## 4. bool
Logical value — either `True` or `False`.

- Subclass of `int` (`True == 1`, `False == 0`)
- Result of comparisons and logical operations

**Syntax:**
```python
variable_name = True
variable_name = False
variable_name = (expression)  # evaluates to True or False
```

**Examples:**
```python
a = True
b = False
c = (5 > 3)   # True
d = (2 == 5)  # False
```

---

## 5. list
Ordered, mutable collection — allows duplicates.

- Uses square brackets `[ ]`
- Items can be added, removed, or changed

**Syntax:**
```python
variable_name = [item1, item2, item3]
```

**Examples:**
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")     # add to end
fruits.remove("banana")    # remove by value
fruits[0]                  # access by index → "apple"
fruits[1:3]                # slicing → ["cherry", "mango"]
len(fruits)                # length → 3
```

**Common methods:** `.append()` `.remove()` `.sort()` `.pop()` `.insert()`

---

## 6. tuple
Ordered, immutable collection — allows duplicates.

- Uses parentheses `( )`
- Cannot be modified after creation
- Faster than list — good for fixed data

**Syntax:**
```python
variable_name = (item1, item2, item3)
```

**Examples:**
```python
point = (10.5, 20.3)
point[0]              # access by index → 10.5
point[0:2]            # slicing → (10.5, 20.3)
len(point)            # length → 2
# point[0] = 5        # ❌ TypeError: tuple is immutable
```

---

## 7. Syntax
The rules and structure of the Python language.

### if / elif / else — Conditionals
```python
if condition:
    # runs if condition is True
elif other_condition:
    # runs if other_condition is True
else:
    # runs if none of the above are True
```

**Example:**
```python
x = 10
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```

---

### for — Loop over a sequence
```python
for variable in sequence:
    # runs for each item
```

**Example:**
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

### while — Loop while condition is True
```python
while condition:
    # runs as long as condition is True
```

**Example:**
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

### def — Define a function
```python
def function_name(parameters):
    # code block
    return value
```

**Example:**
```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8
```

---

### class — Define a class
```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value

    def method(self):
        # code block
```

**Example:**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

d = Dog("Rex")
d.bark()  # Rex says woof!
```

---

### try / except — Handle errors
```python
try:
    # code that might fail
except ErrorType:
    # what to do if it fails
```

**Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

> **Tip:** Check any variable's type with `type(x)`.

| Type  | Syntax              | Mutable | Example              |
|-------|---------------------|---------|----------------------|
| int   | `x = 1`             | ✅      | `42`, `-7`           |
| str   | `x = "hi"`          | ❌      | `"hello"`            |
| float | `x = 3.14`          | ✅      | `3.14`, `1.5e10`     |
| bool  | `x = True`          | ✅      | `True`, `False`      |
| list  | `x = [1, 2]`        | ✅      | `["apple", "mango"]` |
| tuple | `x = (1, 2)`        | ❌      | `(10.5, 20.3)`       |
| syntax| `if / for / def...` | —       | rules of the language|