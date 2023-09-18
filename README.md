# bioio-imageio

[![Build Status](https://github.com/bioio-devs/bioio-imageio/workflows/CI/badge.svg)](https://github.com/bioio-devs/bioio-imageio/actions)
[![Documentation](https://github.com/bioio-devs/bioio-imageio/workflows/Documentation/badge.svg)](https://bioio-devs.github.io/bioio-imageio)

A BioIO reader plugin for reading simple image formats using imageio.

This plugin is intended to be used in conjunction with [bioio](https://github.com/bioio-devs/bioio)
---

## Installation

**Stable Release:** `pip install bioio-imageio`<br>
**Development Head:** `pip install git+https://github.com/bioio-devs/bioio-imageio.git`

## Quickstart

```python
from bioio_imageio import Reader 

r = Reader("my-image.ext")
r.dims
```

## Documentation

For full package documentation please visit [bioio-devs.github.io/bioio-imageio](https://bioio-devs.github.io/bioio-imageio).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

**MIT License**
