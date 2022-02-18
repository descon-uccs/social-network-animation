# social-network-animation
Created for CS4/5740 at UCCS; contains several Python functions for creating animations of data that is contained in square grids.

The module `animate_schelling.py` contains several useful functions:

- `create_example()` generates dummy data for an animation; use this to test your setup and to see what format the data needs to be in. This can also dump animation data to disk in JSON format.
- `load_json_file()` loads a pre-generated JSON file with animation data and prepares it for use in animation.
- `display_animation()` actually creates the animation. This can also generate an animated GIF and save it to disk.

Each function has documentation in `animate_schelling.py`, and usage examples in both `usage_example.py` and if you like Jupyter Notebooks, in `Usage Example Notebook.ipynb`.
