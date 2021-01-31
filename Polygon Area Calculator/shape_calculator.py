class Rectangle:
  """Initializer"""
  def __init__(self, width, height):
    self._width = width
    self._height = height

  """Sets width of the rectangle to given value"""
  def set_width(self, w):
    self._width = w

  """Sets height of the rectangle to given value"""
  def set_height(self, h):
    self._height = h

  """Returns the area of the rectangle"""
  def get_area(self):
    return (self._width * self._height)

  """Returns the perimeter of the rectangle"""
  def get_perimeter(self):
    return (2 * self._width) + (2 * self._height)
  
  """Returns length of the diagonal of the rectangle"""
  def get_diagonal(self):
    return ((self._width ** 2 + self._height ** 2) ** .5)

  """Returns a drawn rectangle using * based on dimensions"""
  def get_picture(self):
    if self._width > 50 or self._height > 50:
      return "Too big for picture."

    output = ""
    for i in range(self._height):
      for j in range(self._width):
        output += '*'
      output += '\n'
    return output

  """Determines how many of another shape can fit inside the rectangle"""
  def get_amount_inside(self, shape):
    num_fit_height = self._height // shape._height
    num_fit_width = self._width // shape._width

    if num_fit_height < 1 or num_fit_width < 1:
      return 0
    else:
      return num_fit_height * num_fit_width
  
  """Sets standard string representation of the Rectangle object"""
  def __str__(self):
    return "Rectangle(width={}, height={})".format(self._width, self._height)


class Square(Rectangle):
  """Initializer - sets width and height equal to side"""
  def __init__(self, side):
    super().__init__(side, side)
  
  """Sets width of the square to given value"""
  def set_width(self, side):
    self._width = side
    self._height = side

  """Sets height of the square to given value"""
  def set_height(self, side):
    self._height = side
    self._width = side

  """Sets side of the square to given value"""
  def set_side(self, side):
    self._height = side
    self._width = side

  """Sets standard string representation of the Square object"""
  def __str__(self):
    return "Square(side={})".format(self._width)