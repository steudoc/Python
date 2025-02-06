import random
import matplotlib.pyplot as plt

def window_average_filter(v, filter_size=3):
    # TODO
    """
    Create a parametric version of the window mean filter created before
    The filter's size can be any odd number ranging from 1 up to the length of the list.
    It is possible to employ a second list.
    Use the padding technique to avoid dealing with conditions.
    -
    Padding is useful to extend the data to apply the filter.
    Different types could be implemented, the most common is the zero padding
    which consists in inserting and appending zeros to the data
    For example: [1,2,3] could be 1-padded to [0,1,2,3,0]
    provide the best fit padding for the signal considering the window filter size to filter the head and tails without considering special cases
    -
    Search for another padding technique and apply it
    """
    return

def random_walk(n):
    #TODO
    """
    Random walks are widely used for the simulation of random processes
    The drunken sailor always moves forward, however, given his conditions
    at each step, he can move forward-straight, forward-right, or forward-left
    create a list of n steps, where at each step the drunken sailor changes his y-axis position of {-1, 0, +1}
    """
    path = []
    for i in range(n):
        move = random.randrange(-1,1+1)
        if i==0:
            path.append(move)
        else:
            path.append(path[i-1]+move)
    return path

def main():
    # define the number of steps the drunken sailor performs (and the length of the pier)
    N_STEPS = 100
    pier_size = 10
    filter_size = 9

    # define the path of the drunken sailor
    where_did_the_drunken_sailor_go = random_walk(N_STEPS)

    # creates the figure
    fig, ax = plt.subplots(figsize=(16,9))
    ax.set_title('Is the drunken sailor drowning?')

    # defines the borders of the pier
    # TODO
    # create two lists of N_STEPS elements to create the borders of the pier
    border = []
    border2 = []

    # color the pier and the water
    ax.fill_between(range(N_STEPS),min(min(where_did_the_drunken_sailor_go),-pier_size), border2, color='blue')
    ax.fill_between(range(N_STEPS),border,max(max(where_did_the_drunken_sailor_go),pier_size), color='blue', label='water')
    ax.fill_between(range(N_STEPS),border2,border, color='#663300', label='pier')

    # plot of the original signal
    ax.plot(where_did_the_drunken_sailor_go, label='GPS measured position', color='black', linewidth=3)

    # compute and plot of the filtered signal
    where_did_the_drunken_sailor_go_filtered = window_average_filter(where_did_the_drunken_sailor_go, filter_size=filter_size)
    ax.plot(where_did_the_drunken_sailor_go_filtered, label=f'window mean filtered position', color='red',  linestyle='--', linewidth=3)

    # TODO
    # Try to plot two filtered version together with different window sizes, change the color and the relative label

    # plot styling
    ax.set_ylabel('distance from the center of the pier (m)')
    ax.set_xlabel('steps')
    ax.legend(facecolor='white', framealpha=1)

    # actually show the figure
    plt.show()

main()
