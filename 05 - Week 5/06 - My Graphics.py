from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Define circle size
    RADIUS = 50

    # Compute bounding box for the circle
    center_x = CANVAS_WIDTH / 2
    center_y = CANVAS_HEIGHT / 2
    left_x = center_x - RADIUS
    top_y = center_y - RADIUS
    right_x = center_x + RADIUS
    bottom_y = center_y + RADIUS

    # Draw the circle (as an oval with equal width and height)
    canvas.create_oval(left_x, top_y, right_x, bottom_y, "blue", "black")

if __name__ == '__main__':
    main()
