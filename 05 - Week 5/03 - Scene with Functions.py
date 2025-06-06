from graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw 3 clouds
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 30, 30, 'lightgray')
    draw_cloud(canvas, 250, 20, 'white')

    # Draw 3 trees
    draw_tree(canvas, 60, 'saddlebrown', 'forestgreen')
    draw_tree(canvas, 180, 'sienna', 'limegreen')
    draw_tree(canvas, 300, 'peru', 'darkgreen')

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, trunk_color, leaf_color):
    """
    Draws a single tree at the given x position.
    The trunk is a rectangle, and the leaves are a circle above the trunk.
    """
    # Trunk
    trunk_left = x
    trunk_top = TREE_BOTTOM_Y - TRUNK_HEIGHT
    trunk_right = x + TRUNK_WIDTH
    trunk_bottom = TREE_BOTTOM_Y
    canvas.create_rectangle(trunk_left, trunk_top, trunk_right, trunk_bottom, trunk_color)

    # Leaves
    leaf_center_x = x + TRUNK_WIDTH / 2
    leaf_top = trunk_top - LEAVES_SIZE / 2
    leaf_left = leaf_center_x - LEAVES_SIZE / 2
    leaf_right = leaf_center_x + LEAVES_SIZE / 2
    leaf_bottom = trunk_top + LEAVES_SIZE / 2
    canvas.create_oval(leaf_left, leaf_top, leaf_right, leaf_bottom, leaf_color)

if __name__ == '__main__':
    main()
