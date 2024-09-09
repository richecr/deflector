<div align="center">
<img height="180" alt="deflector Logo" src="https://raw.githubusercontent.com/richecr/deflector/main/.github/assets/readme/logo.png">

# Deflector

---

📘 [Documentation - Under Construction]()

</div>

---

## Why does Deflector exist?

💡 **Deflector** is a minimalist testing library for Python designed to simplify test writing with a clear and intuitive syntax, allowing developers to create and run tests quickly and efficiently without unnecessary complications.

</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> High **isolation** level per file<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> **Performant** and **lightweight**<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> **Fully typed** library<br />

---

## Quickstart

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> Install


```zsh
$ pip install deflector
```

Or with [poetry](https://python-poetry.org/docs/)

```zsh
poetry add deflector -G dev
```

---

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> Test

<table>
<tr>
<td>
<blockquote>tests/test_file1.py</blockquote>
</td>
</tr>
<tr>
<td width="1200">

```py
from deflector import affirm


affirm.equal(1, 1, "My first test with deflector")
```

</td>
</tr>
</table>

---

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> Run


```bash
deflector # or poetry run deflector
```

Or defining the directory where the tests are:

```bash
deflector --dir tests
```

---

## Features

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/deflector/91367ebe4c1d82e3d86c92647b391fd1840d6c13/.github/assets/readme/check.svg"> Main

| Function                                               | Description                               |
|--------------------------------------------------------|-------------------------------------------|
| [affirm](#affirm)                                      | 🔍 Test assertion.                        |
| [it](#it)                                              | 🤹🏻‍♀️ Isolate tests.                         |
| [describe](#describe)                                  | 🤹🏻‍♀️ Grouping tests.                        |
| [before_each • after_each](#before-each--after-each)   | 🃏 Functions for test setup and teardown. |


#### Affirm

The `affirm` is used to create tests that validate whether the behavior of your code is as expected, checking the correspondence between values ​​and triggering errors if there are discrepancies.

```python
from deflector import affirm
```

| Function                                   | Description                                  |
|--------------------------------------------|----------------------------------------------|
| [ok](#ok)                                  | Checks if a value is truthy.                 |
| [equal](#equals)                           | Compares if two values are equal.            |
| [not_equal](#not-equals)                   | Verifies if two values are different.        |
| [match_re](#match-regex)                   | Checks if a string matches a regex.          |
| [does_not_match_re](#does-not-match-regex) | Verifies if a string does not match a regex. |

##### Ok

```python
affirm.ok(value, message)
```

```python
affirm.ok(True, "Ok")
```

##### Equals

```python
affirm.equal(value, expected, message)
```

```python
affirm.equal(1 + 2, 3, "Equal: Sum 1+2=3")
```

##### Not Equals

```python
affirm.not_equal(value, expected, message)
```

```python
affirm.not_equal(1 + 2, 4, "Not Equal: Sum 1+2!=4")
```

##### Match Regex

```python
affirm.match_re(value, reg_exp, message)
```

```python
affirm.match_re("acab", "ab", "Match Regex: ab in acab")
```

##### Does Not Match Regex

```python
affirm.does_not_match_re(value, reg_exp, message)
```

```python
affirm.does_not_match_re("ab", "abc", "Does Not Match Regex: ab not in a")
```

#### It

```python
from deflector import affirm, it

@it("It Test 1")
def test_1() -> None:
    affirm.ok(True, "Ok")
    affirm.equal(1 + 1, 2, "Equal")
    affirm.not_equal(1 + 2, 1, "Not Equal")
    affirm.match_re("acab", "ab", "Match Re")
    affirm.does_not_match_re("a", "ab", "Does Not Match Re")
```

#### Describe

```python
from deflector import affirm, describe, it

@describe("Main 1")
def describe_main() -> None:
    @it("It Test 1")
    def test1() -> None:
        affirm.equal(1 + 1, 2, "Equal 1+1=2")

    @it("It Test 2")
    def test2() -> None:
        affirm.match_re("acab", "ab", "Match Re")
```

#### Before Each • After Each

```python
from deflector import affirm, describe, it

@describe("Main 1")
def describe_main() -> None:
    x = 1

    @before_each()
    async def start() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x += 1
        return True

    @after_each()
    async def end_() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x = 1
        return True

    @it("It Test 1")
    def test1() -> None:
        affirm.equal(x, 2, "Equal Before Each")
        affirm.equal(1 + 1, 2, "Equal 1")
        affirm.equal(1 + 1, 2, "Equal 2")

    @it("It Test 2")
    def test2() -> None:
        affirm.equal(x, 2, "Equal After Each")
        affirm.equal(1 + 1, 2, "Equal")
        affirm.not_equal(1 + 1, 1, "Not Equal")
        affirm.ok(True, "Ok")
        affirm.match_re("acab", "ab", "Match Re")
        affirm.does_not_match_re("a", "ab", "Does Not Match Re")
```