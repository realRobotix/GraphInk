# GraphInk

GraphInk is a tool for drawing arbitrary images to your GitHub activity graph.
You can either use it as a library and pass in a Pillow Image object, or use the command line interface to draw an image
from a file.

## Prerequisites

- Python 3.6 or later
- Pillow
- git

## Usage

### CLI

```bash
python main.py path/to/image.png git@github.com:username/repo.git
```

### Library

```python
from graphink import draw_image

draw_image(image, git_repo_path)
```
