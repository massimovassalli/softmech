# import the main panels structure, required
from ..panels import boxPanel
# import here your procedure-specific modules, no requirements (numpy as an example)
from scipy.signal import savgol_filter

# Set here the details of the procedure
NAME = 'SavGol'  # Name, please keep it short as it will appear in the combo box of the user interface
DESCRIPTION = 'Filter the curve with a Savitzky Golay filter; ideal to preserve steps'  # Free text
# set a DOI of a publication you want/suggest to be cited, empty if no reference
DOI = 'https://doi.org/10.1038/s41592-019-0686-2'

# Create your filter class by extending the main one
# Additional methods can be created, if required


class Filter(boxPanel):
    def create(self):
        # This function is required and describes the form to be created in the user interface
        # The last value is the initial value of the field; currently 3 types are supported: int, float and combo
        self.addParameter('win', 'float', 'Window size [m]', 25e-9)
        self.addParameter('order', 'int', 'Order of the interpolation', 3)

    def calculate(self, x, y, curve=None):
        win = self.getValue('win')
        xstep = (max(x) - min(x)) / (len(x) - 1)
        win = int(win / xstep)
        polyorder = self.getValue('order')
        if win % 2 == 0:
            win += 1
        if polyorder > win:
            return False
        y_smooth = savgol_filter(y, win, polyorder)
        return x, y_smooth
