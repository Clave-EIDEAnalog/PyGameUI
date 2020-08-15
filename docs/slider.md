# Slider widget
## class Slider(builtins.object)

### Description
It can be used to select a value from a range from 0 to a maximum value

### Usage
```python
Slider(parent, *, x=0, y=0, orientation='horizontal', length=200, max=100)
```

#### Parameters

`x: int`   
x position in pixels

`y: int`   
y position in pixels

`orientation: str`   
Slider orientation (either `"vertical"` or `"horizontal"`)

`length: int`   
Slider length in pixels.
This number will be increased by 15 to include the pointer

`max: int`   
The maximum number the slider can select.
The slider selects a number in a range from `0` to `max`

---

## Methods
### `get_mark(self)`
#### Description
Return the value marked by the slider

#### Parameters
None

#### Returns
`int`

#### Usage
`Slider.get_mark()`

---

### `move(self, x, y)`
#### Description
Change the widget's position

#### Parameters
`x: int`
Set widget's position along the x axis
`y: int`
Set widget's position along the y axis

#### Returns
None

#### Usage
`Slider.move(200,300)`

---

### `set_bg_color(self, color)`
#### Description
Set the color of the widget's background.

#### Parameters
`color: tuple`
A 3-tuple containing an RGB value

#### Returns
None

#### Usage
`Slider.set_bg_color((34,45,18))`

---

### `set_border_color(self, color)`
#### Description
Set the color of the border around the widget.

#### Parameters
`color: tuple`
A 3-tuple containing an RGB value

#### Returns
None

#### Usage
`Slider.set_border_color((34,45,18))`

---

### `set_border_width(self, width)`
#### Description
Set the width of the border around the widget.
Set to 0 to remove the border entirely.

#### Parameters
width: int
Width in pixels of the border

#### Returns
None

#### Usage
Slider.set_border_width(5)

---

### `set_font(self, font)`
#### Description
Change the font of the widget's label.

#### Parameters
`font: str`
A font name such as "Arial" or a path to a font file '.ttf' or '.otf'.

#### Returns
None

#### Usage
`Slider.set_font("Arial")`

### `set_font_color(self, color=(0, 0, 0)`)
#### Description
Set the color of the widget's label.

#### Parameters
`color: tuple`
A 3-tuple containing an RGB value

#### Returns
None

#### Usage
`Slider.set_font_color((34,45,18))`

---

### `set_font_size(self, size=10)`
#### Description
Set the size of the widget's label font.

#### Parameters
`size: int`
The label font size in pixels.

#### Returns
None

#### Usage
`Slider.set_font_size(12)`

---

### `set_label(self, text)`
#### Description
Set the color of the border around the widget.

#### Parameters
`text: str`
A string for the widget's label.

#### Returns
None

#### Usage
`Slider.set_label("Some text")`

---

### `set_label_alignment(self, alignment)`
#### Description
Set the alignment of the label when its position is either "top" or "bottom".

#### Parameters
`alignment: str`
A string from the list ["left", "center", "right"]

#### Returns
None

#### Usage
`Slider.set_label_side("top")`

---

### `set_label_side(self, side)`
#### Description
Set the relative position of the label to the widget.

#### Parameters
`side: str`
A string from the list ["top", "bottom", "left", "right"]

#### Returns
None

#### Usage
`Slider.set_label_side("top")`

---

### `set_length(self, length)`
#### Description
Set the length of the slider (height if vertical, width if horizontal)
The total length will be 15 pixels greater to include the pointer

#### Parameters
`length: int`
Length in pixels

#### Returns
None

#### Usage
`Slider.set_length(200)`

---

### `set_max(self, max)`
#### Description
Set maximum value for the selector

#### Parameters
`max: int`

#### Returns
None

#### Usage
`Slider.set_max(50)`

---

### `set_pointer_color(self, color)`
#### Description
Set the color of the selector/pointer.

#### Parameters
`color: tuple`
A 3-tuple containing an RGB value

#### Returns
None

#### Usage
`Slider.set_pointer_color((34,45,18))`

---

### `set_width(self, width)`
#### Description
Set the width of the widget (height if horizontal, width if vertical)

#### Parameters
`width: int`
Width in pixels

#### Returns
None

#### Usage
`Slider.set_width(20)`

---

### `update(self)`
#### Description
Update the widget

#### Usage
`Slider.update()`

---
[Go back to index](index.md)