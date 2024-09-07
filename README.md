<div align="center">
<img height="180" alt="Sentinel Logo" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/logo.png?token=GHSAT0AAAAAACUXVD5PS2OG2TWFS5JTCPQSZWVD4SA">

# Sentinel

---

📘 [Documentation - Under Construction]()

</div>

---

## Why does Sentinel exist?

💡 **Sentinel** is a minimalist testing library for Python designed to simplify test writing with a clear and intuitive syntax, allowing developers to create and run tests quickly and efficiently without unnecessary complications.

</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> High **isolation** level per file<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> **Performant** and **lightweight**<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> **Fully typed** library<br />

---

## Quickstart

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> Install


```zsh
$ pip install sentinel
```

Or with [poetry](https://python-poetry.org/docs/)

```zsh
poetry add sentinel -G dev
```

---

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> Test

<table>
<tr>
<td>
<blockquote>tests/test_file1.py</blockquote>
</td>
</tr>
<tr>
<td width="1200">

```py
from sentinel.modules.essentials.affirm import affirm


affirm.equal(1, 1, "My first test with sentinel")
```

</td>
</tr>
</table>

---

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> Run


```bash
sentinel # or poetry run sentinel
```

Or defining the directory where the tests are:

```bash
sentinel --dir tests
```

---

## Features

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/c86802a982bebe45ac32c6dc2a42159ae7cc04f7/.github/assets/readme/check.svg?token=A2BPUWMPOQ5JOPYKMTBF2LDG2UIX2"> Main

| Function                                               | Description                               |
|--------------------------------------------------------|-------------------------------------------|
| [affirm](#affirm)                                      | 🔍 Test assertion.                        |
| [it](#it)                                              | 🤹🏻‍♀️ Isolate tests.                         |
| [describe](#describe)                                  | 🤹🏻‍♀️ Grouping tests.                        |
| [before_each • after_each](#before-each--after-each)   | 🃏 Functions for test setup and teardown. |


#### Affirm

The `affirm` is used to create tests that validate whether the behavior of your code is as expected, checking the correspondence between values ​​and triggering errors if there are discrepancies.

```python
from sentinel import affirm
```

| Function                                   | Description                                  |
|--------------------------------------------|----------------------------------------------|
| [ok](#ok)                                  | Checks if a value is truthy.                 |
| [equal](#equal)                            | Compares if two values are equal.            |
| [not_equal](#not_equal)                    | Verifies if two values are different.        |
| [match_re](#match_re)                      | Checks if a string matches a regex.          |
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