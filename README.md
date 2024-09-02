<div align="center">
<img height="180" alt="Sentinel Logo" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/logo.png">

# Sentinel

---

📘 [Documentation - Under Construction]()

</div>

---

## Why does Sentinel exist?

💡 **Sentinel** is a minimalist testing library for Python designed to simplify test writing with a clear and intuitive syntax, allowing developers to create and run tests quickly and efficiently without unnecessary complications.

</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> High **isolation** level per file<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> **Performant** and **lightweight**<br />
</span><img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> **Performant** and **lightweight**<br />

---

## Quickstart

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> Install


```zsh
$ pip install sentinel
```

Or with [poetry](https://python-poetry.org/docs/)

```zsh
poetry add sentinel -G dev
```

---

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> Test

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

### <img width="16" height="16" alt="check" src="https://raw.githubusercontent.com/richecr/sentinel/main/.github/assets/readme/check.svg"> Run


```bash
sentinel // or poetry run sentinel
```

Or defining the directory where the tests are:

```bash
sentinel --dir tests
```

---


