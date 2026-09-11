## Terminal Rotating Cube written in Python
- Small project inspired by [ASMR Programming - Spinning Cube - No Talking [- Code Fiction]](https://youtu.be/p09i_hoFdd0)

## Startup
- run the rotation.py with python ```python ./rotation.py```
- ```Control + C``` to stop the programme

## Todo
1. ~~Rotation smoothening~~
    - constants set
    - future may add a rotation axis, together with noice
2. ~~Arr of "pixels" being brute for now~~
     - less brute, search through rectangle instead of whole arr
3. ~~Rendering logic~~
    - "in-place"
4. ~~Order of face rendering~~
    - order semi-accomplished by sort the max - min x coordinates
        - taking angle between face vec and y-axis will take too much memory