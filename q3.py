import turtle

def draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:
        return
    else:
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Draw the left subtree
        turtle.left(left_angle)
        draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        
        # Draw the right subtree
        turtle.right(left_angle + right_angle)  # Turn the turtle to the right angle
        draw_tree(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
        
        # Return to the original position
        turtle.left(right_angle)
        turtle.backward(branch_length)

# User input
left_angle = float(input("Enter the left branch angle: "))
right_angle = float(input("Enter the right branch angle: "))
branch_length = float(input("Enter the starting branch length: "))
depth = int(input("Enter the recursion depth: "))
reduction_factor = float(input("Enter the branch length reduction factor: "))

# Set up turtle
turtle.speed(0)
turtle.left(90)  # Start with the turtle facing upwards
draw_tree(branch_length, left_angle, right_angle, depth, reduction_factor)
turtle.done()