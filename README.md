# TemplateGitHub
[![Total Downloads](https://img.shields.io/github/downloads/drbmrp/TemplateGitHub/total.svg)](https://github.com/drbmrp/TemplateGitHub)
[![PypiDownloads](https://img.shields.io/pypi/dm/TemplateGitHub.svg)](https://pypistats.org/packages/templategithub)
[![PypiVersion](https://img.shields.io/pypi/v/TemplateGitHub.svg)](https://pypistats.org/packages/templategithub)
[![PypiFormat](https://img.shields.io/pypi/format/TemplateGitHub.svg)](https://pypistats.org/packages/templategithub)
[![PypiStatus](https://img.shields.io/pypi/status/TemplateGitHub.svg)](https://pypistats.org/packages/templategithub)
[![License](https://img.shields.io/github/license/drbmrp/TemplateGithub.svg)](https://github.com/drbmrp/TemplateGitHub)

Note that this repository is still under development. When performed first release/tag then master branch could be consider as stable.

## Table of content

- [README Style](#readme-style)
  - [Itemize and style](#itemize-and-style)
  - [Add a picture](#add-a-picture)
  - [Code](#code)
- [PIP setup](#pip-setup)
  - [TestPyPi](#testpypi)
  - [PyPi](#pypi)
- [CI](#ci)
  - [UnitTest](#unittest)
- [License](#license)
- [Notes For Developers](#notes-for-developers)
- [Links](#links)

## README Style

### Itemize and style

This is a template repository for future packages developed by drbmrp. The main purpose is:

- This an item with :star: **black** and *italic*
  - This is my second item
    - And my third My local edit

### Add a picture

Adding a picture.
![Logo](Logos/Logo.png)

Adding a gif.
![l](Logos/Logo.gif)

### Code

There are different way to show code in a README.md file. These are some examples of how to print code:

Example of code in a signle line. Also could be used to simply highlight.

`pip install your_package`

Another example of single line code:

```python
python -c "import numpy as np"
```

Python example of code segment:
```python
l = ['it%d' % n for n in range(5)]
for ii,item in enumerate(l):
    print(item,ii)
```

Matlab example of code segment:
```matlab
v = linspace(1,4,100);
res = v .* 0;
for ii = 1:100
    res = v(ii)^ii;
end
```

## Pip setup

### TestPypi

### Pypi



## License
This software is licensed under the terms of the GPL Open Source license and is available for free. However, contact author to use these packages.

## Notes for developers

- Recommended use of vscode extensions for .md files
- This author uses a codying style that deffers from PEP 8.
- Check link for .gitignore, very useful

## Links
https://github.com/DavidAnson/markdownlint/blob/master/doc/Rules.md

https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7

https://shields.io

http://google.github.io/styleguide/pyguide.html

https://github.com/github/gitignore