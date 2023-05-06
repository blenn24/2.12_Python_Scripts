#coordinate frame: robot starts at bottom left of competetion with to right +X, up +Y, theta angle in degrees from X axis using RHR

cone_positions = [(1,3)]


#x, y, theta(degrees) of current position in competition site coordinates
robot_current_pos = [0,0,0] 

#final position for picking up AED
AED_pickup_pos = [0, 1, 180]

#position for lining up for final approach of AED
AED_lineup_pickup_pos = [[0, 5, 180]]

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot_robot_position(robot_position, robot_direction, cone_positions, target_positions):
    """
    plot current pos, trajectory of robot
    """
    # Set up the plot
    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Robot Position')

    # Plot the cone positions
    for cone_position in cone_positions:
        plt.scatter(cone_position[0], cone_position[1], color='orange', label='Cone')

    # Plot the target zone positions
    for target_position in target_positions:
        plt.scatter(target_position[0], target_position[1], color='green', label='Target Zone')

    # Plot the robot position and direction arrow
    plt.scatter(robot_position[0], robot_position[1], color='blue', label='Robot')
    plt.arrow(robot_position[0], robot_position[1], robot_direction[0], robot_direction[1],
              width=0.1, head_width=0.3, head_length=0.3, fc='blue', ec='blue')

    # Add a legend
    plt.legend()

    # Set equal scaling of the axes
    plt.axis('equal')

    # Show the plot
    plt.show()
    
#state machine

#procedure for approaching AED
#constantly update coords based off of april tag
#go to approach zone, rotate to correct orientation


plot_robot_position(robot_current_pos, (0.5,0.5), cone_positions, AED_lineup_pickup_pos)