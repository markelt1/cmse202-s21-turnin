from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    red = None
    ir = None
    '''
    This class creates an artificial night sky observer.
    '''
    
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self, f1, f2):
        '''
        This function is incomplete! It is missing the appropriate input vales
        and the "pass" should be replaced with the appropriate code.
        Update this docstring to explain what the function does (or should do).
        This will load in the data for the pictures
        '''
        self.red = fits.open(f1)
        self.ir = fits.open(f2)
        
        pass
    def calc_stats(self):
        self.image_data_red = self.red[0].data
        self.image_data_ir = self.ir[0].data
        
        print('The mean of red is', np.mean(self.image_data_red))
        print('The Standard Deviation of red is', np.std(self.image_data_red))
        
        print('The mean of ir is', np.mean(self.image_data_ir))
        print('The Standard Deviation ir is', np.std(self.image_data_ir))
    
    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
       
        # Define the array for storing RGB values
        rgb = np.zeros((self.image_data_red.shape[0],self.image_data_red.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.image_data_red.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.image_data_ir.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        rgb = np.zeros((self.image_data_red.shape[0],self.image_data_red.shape[1],3))
    
   
        # green
        rgb[:,:,1] = ((self.image_data_red.astype("float")+(self.image_data_red.astype("float")))/2)/norm_factor
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0

        #blue
        rgb[:,:,2] = ((self.image_data_red.astype("float"))/norm_factor)
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0

        plt.figure()
        hdu = fits.open(self.im2_filename)[0]
        wcs = WCS(hdu.header)
        plt.subplot(projection=wcs)
        plt.imshow(rgb, origin = 'lower')
        plt.xlabel('Right Ascension')
        plt.ylabel('Declination')