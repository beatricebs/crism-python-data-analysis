import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import PolygonSelector
from matplotlib.path import Path
from matplotlib import colors

#----------------polygonal selection----------------

class PolygonSelect:
    
    '''
    PolygonSelect class
    
    shows the RGB image and allows to draw a polygon on it by calling PolygonSelector from matplotlib
    vertexes of the polygon are stored in verts attribute and can be then accessed with .verts
    
    '''
    
    
    #class initialization, show the plot and call PolygonSelector function from matplotlib
    def __init__(self, RGB):
        fig, ax = plt.subplots(figsize=[10,10])
        ax.imshow(RGB)
        print("Click on the figure to create a polygon.")
        print("Press the 'esc' key to start a new polygon.")
        print("Try holding the 'shift' key to move all of the vertices.")
        print("Try holding the 'ctrl' key to move a single vertex.")
        self.verts=[]
        self.poly = PolygonSelector(ax, self.onselect, props = dict(color='r', linewidth=2))
        
     
    #onselect function, required by PolygonSelector
    def onselect(self, verts):
        self.verts=verts
            
#---------------
#references
#https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html

#visualizing polygonal selection 

def CreateMask(polygon, RGB): 
    
    '''
    Function to create the polygonal mask.
    
    Input: polygon's vertexes and the RGB image over which you want to visualize the polygon.
    
    Output: mask (array with True and False values). 
    
    '''

    # Create a mask based on the path
    path = Path(polygon.verts)

    #creating x and y coordinates for every point in the image 
    #y dimension 744, x dimension 781
    y, x = np.mgrid[:RGB.shape[0], :RGB.shape[1]] 
    points = np.vstack((x.ravel(), y.ravel())).T

    #creating the mask
    mask = path.contains_points(points) #points must be (N,2) array
    mask = mask.reshape(RGB.shape[:2]) #reshape 

    #plot
    cmap = colors.ListedColormap(['none', 'red']) #plot colors

    fig, ax = plt.subplots(figsize=[10,10])
    ax.imshow(RGB)
    ax.imshow(mask, alpha = 0.5, cmap=cmap)
    
    return mask
