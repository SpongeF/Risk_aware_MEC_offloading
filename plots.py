'''
Plot functions to graphically present simulation results
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from parameters import SAVE_FIGS, ONE_FIGURE

def setup_plots(suptitle):

    '''
    Basic setup of plots so it can be reused on plot functions
    Parameters
    ----------
    suptitle: string
    Description of the plot that will appear on the top
    Returns
    -------
    Figure and axis matplotlib structs
    '''
    fig, ax = plt.subplots(1, 1, figsize=(15, 12))
    fig.suptitle(suptitle)
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
        item.set_fontsize(30)
    for item in (ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(26)
        item.set_fontweight("bold")
    font = {'weight' : 'bold'}
    matplotlib.rc('font', **font)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Provide tick lines across the plot to help viewers trace along
    # the axis ticks.
    plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)

    # Remove the tick marks; they are unnecessary with the tick lines we just
    # plotted.
    plt.tick_params(axis='both', which='both', bottom=True, top=False,
    labelbottom=True, left=False, right=False, labelleft=True)

    return fig, ax

def plot_b_converging(b_converging):
    '''
    Plot the data each user is trying to offload till convergence

    Parameters
    ----------

    b_converging: 2-d array
    Contains on each row the amount of data each user is trying to offload. Each row is
    a different iteration

    Returns
    -------
    Plot

    '''
    result = b_converging

    # Each row on the transposed matrix contains the data the user offloads
    # in each iteration. Different rows mean different user.
    result = np.transpose(result)

    suptitle = "Data each user is trying to offload in each iteration"

    if ONE_FIGURE == False:
        fig, ax = setup_plots(suptitle)

    for index, row in enumerate(result):
        # # display only some of the users on the plot
        # if index%11 == 0:
        #     line = plt.plot(row, lw=5)
        line = plt.plot(row, lw=5)

    plt.xlabel('iterations', fontweight='bold')
    plt.ylabel('amount of data (bytes)', fontweight='bold')

    path_name = "b_converging"
    if SAVE_FIGS == True and ONE_FIGURE == False:
        plt.savefig("plots/" + path_name + ".png")
    else:
        plt.show()
