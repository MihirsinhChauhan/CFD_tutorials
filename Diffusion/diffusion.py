import os 
import numpy as np
import matplotlib.pyplot as plt

class MeshGenerator:
    def __init__(self):
        self.lengths = [0.0, 0.0]
        self.k = [0.0, 0.0]
        self.x = [0.0, 0.0]
        self.sec = [0, 0]
    
    def get_mesh_inputs(self,axis):
        grid_var = input(f"For axis {axis}, enter 'y' if you want a uniform grid: ")
        if grid_var.lower() == 'y':
            sec_var = input("Do you have the number of sections to be made? (y/n): ")
            if sec_var.lower() == 'y':
                self.sec[axis] = int(input("Enter the number of sections: "))
                self.x[axis] = self.lengths[axis] / self.sec[axis]
            else:
                sec_size = float(input("Enter section size: "))
                self.sec[axis] = int(self.lengths[axis] / sec_size)
                self.x[axis] = sec_size
        else:
            increment_ratio = float(input("Enter the increment ratio: "))
            sec_var = input("Do you have the number of sections to be made? (y/n): ")
            if sec_var.lower() == 'y':
                self.sec[axis] = int(input("Enter the number of sections: "))
                p = increment_ratio ** self.sec[axis]
                self.x[axis] = self.lengths[axis] * (increment_ratio - 1) / (p - 1)
            else:
                self.x[axis] = float(input("Enter the smallest division to be made: "))
                self.sec[axis] = int(np.log(1 + (self.lengths[axis] * (increment_ratio - 1) / self.x[axis])) / np.log(increment_ratio) + 1)

    def generate_mesh(self):
        Nx = np.zeros(self.sec[0])
        Nx[0] = self.x[0]
        p = self.x[0]
        for i in range(1, self.sec[0]):
            Nx[i] = p * self.k[0] + Nx[i - 1]
            p = p * self.k[0]

        Ny = np.zeros(self.sec[1])
        Ny[0] = self.x[1]
        p = self.x[1]
        for i in range(1, self.sec[1]):
            Ny[i] = p * self.k[1] + Ny[i - 1]
            p = p * self.k[1]

        return Nx, Ny
    