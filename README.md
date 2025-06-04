# bioio-imageio

[![Build Status](https://github.com/bioio-devs/bioio-imageio/actions/workflows/ci.yml/badge.svg)](https://github.com/bioio-devs/bioio-imageio/actions)
[![PyPI version](https://badge.fury.io/py/bioio-imageio.svg)](https://badge.fury.io/py/bioio-imageio)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python 3.10–3.13](https://img.shields.io/badge/python-3.10--3.13-blue.svg)](https://www.python.org/downloads/)

A BioIO reader plugin for reading [all these formats](https://imageio.readthedocs.io/en/stable/formats/index.html) using `imageio`

---


## Documentation

[See the full documentation on our GitHub pages site](https://bioio-devs.github.io/bioio/OVERVIEW.html) - the generic use and installation instructions there will work for this package.

Information about the base reader this package relies on can be found in the `bioio-base` repository [here](https://github.com/bioio-devs/bioio-base)

## Installation

**Stable Release:** `pip install bioio-imageio`<br>
**Development Head:** `pip install git+https://github.com/bioio-devs/bioio-imageio.git`

## Example Usage (see full documentation for more examples)

Install bioio-imageio alongside bioio:

`pip install bioio bioio-imageio`


This example shows a simple use case for just accessing the pixel data of the image
by explicitly passing this `Reader` into the `BioImage`. Passing the `Reader` into
the `BioImage` instance is optional as `bioio` will automatically detect installed
plug-ins and auto-select the most recently installed plug-in that supports the file
passed in.
```python
from bioio import BioImage
import bioio_imageio

img = BioImage("my_file.mp4", reader=bioio_imageio.Reader)
img.data
```
## TwoDWriter

Import the writer:

```python
from bioio_imageio.writers import TwoDWriter
```

The `TwoDWriter` writes 2D (YX) or 3D (YXS) image data via `imageio`.

### Examples from Tests

```python
import numpy as np
from bioio_imageio.writers import TwoDWriter

# RGB image, inferred YXS
image = np.zeros((100, 100, 3), dtype=np.uint8)
TwoDWriter.save(image, "output.png")
```

```python
# Channels-first array (S,Y,X) with explicit dim_order
image = np.zeros((3, 100, 100), dtype=np.uint8)
TwoDWriter.save(image, "output.bmp", "SYX")
```

---

## TimeseriesWriter

Import the writer:

```python
from bioio_imageio.writers import TimeseriesWriter
```

The `TimeseriesWriter` writes 3D (T,Y,X) or 4D (T,Y,X,S) data as animated formats via `imageio`.

### Examples from Tests

```python
import numpy as np
from bioio_imageio.writers import TimeseriesWriter

# Grayscale GIF (T,Y,X)
image = np.zeros((30, 100, 100), dtype=np.uint8)
TimeseriesWriter.save(image, "output.gif")
```

```python
# Custom dim_order (S,Y,T,X) for GIF
image = np.zeros((3, 100, 30, 100), dtype=np.uint8)
TimeseriesWriter.save(image, "output.gif", "SYTX")
```

```python
# MP4 output for 30 frames of 112x112
image = np.zeros((30, 112, 112), dtype=np.uint8)
TimeseriesWriter.save(image, "output.mp4")
```


## Issues
[_Click here to view all open issues in bioio-devs organization at once_](https://github.com/search?q=user%3Abioio-devs+is%3Aissue+is%3Aopen&type=issues&ref=advsearch) or check this repository's issue tab.


## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.
