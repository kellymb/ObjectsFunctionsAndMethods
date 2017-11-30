"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Michael Kelly.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(800, 700)
    point1 = rg.Point(400, 350)
    point2 = rg.Point(200, 93)
    radius1 = 200
    radius2 = 50
    circle1 = rg.Circle(point1, radius1)
    circle1.fill_color = 'pink1'
    circle1.attach_to(window)
    circle2 = rg.Circle(point2, radius2)
    circle2.attach_to(window)
    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()
    x1 = 300
    y1 = 200
    center1 = rg.Point(x1, y1)
    thickness = 20
    color = "blue"
    circle = rg.Circle(center1, 50)
    circle.pen = rg.Pen('black', thickness)
    circle.fill_color = color
    circle.attach_to(window)

    print(thickness)
    print(color)
    print(center1)
    print(x1)
    print(y1)

    x2 = 50
    y2 = 50
    x3 = 140
    y3 = 100
    color2 = 'none'

    point1 = rg.Point(x2, y2)
    point2 = rg.Point(x3, y3)

    rectangle = rg.Rectangle(point1, point2)
    rectangle.pen = rg.Pen('black', thickness)
    rectangle.attach_to(window)

    print(thickness)
    print(color2)
    print('Point(', x2 + x3 / 2, ',', y2 + y3 / 2, ')')
    print(x2 + x3 / 2)
    print(y2 + y3 / 2)
    window.render()

    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow(800,800)
    x1 = 200
    y1 = 150
    x2 = x1 + 70
    y2 = y1 - 30
    point1 = rg.Point(x1, y1)
    point2 = rg.Point(x2, y2)
    line1 = rg.Line(point1, point2)
    line1.pen = rg.Pen('pink', 7)
    line1.attach_to(window)
    centerx1 = x1 + x2 / 2
    centery1 = y1 + y2 / 2
    centerpoint = rg.Point(centerx1,centery1)
    print(centerpoint)
    print(centerx1)
    print(centery1)

    x3 = 30
    y3 = 70
    x4 = 214
    y4 = 256
    point3 = rg.Point(x3, y3)
    point4 = rg.Point(x4, y4)
    line2 = rg.Line(point3, point4)
    line2.pen = rg.Pen('RoyalBlue2', 3)
    line2.attach_to(window)
    centerx2 = x3 + x4 / 2
    centery2 = y3 + y4 / 2
    print(rg.Point(centerx2, centery2))
    print(centerx2)
    print(centery2)
    window.render()

    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
