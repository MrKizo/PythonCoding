
# Python Basic Data Types

## 1. int
Whole numbers with no decimal point.

- Unlimited size in Python
- Supports: `+`, `-`, `*`, `//`, `%`, `**`

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

**Examples:**
```python
a = True
b = False
c = (5 > 3)  # True
```

---

> **Tip:** Check any variable's type with `type(x)`.