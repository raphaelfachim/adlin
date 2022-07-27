import numpy as np
import matplotlib.pyplot as plt
import math


class ContactTemperature:
    def __init__(self,
                 cof,
                 normal_load,
                 sliding_speed,
                 wear_track,
                 length_pin,
                 width_pin,
                 thickness_pin,
                 diameter_disc,
                 thickness_disc,
                 length_block,
                 width_block,
                 thickness_block,
                 thermal_conductivity_pin,
                 thermal_conductivity_disc,
                 diffusivity,
                 convection_coef):
        self.cof = cof  # [-]

        self.wear_track = wear_track  # [m]

        # Pin dimensions
        self.length_pin = length_pin  # [m] (2*b)
        self.width_pin = width_pin  # [m] (2*a)
        self.thickness_pin = thickness_pin  # [m]

        # Disc dimensions
        self.diameter_disc = diameter_disc  # [m]
        self.thickness_disc = thickness_disc  # [m]

        # Block dimensions
        self.length_block = length_block  # [m] (2*B)
        self.width_block = width_block  # [m] (2*A)
        self.thickness_block = thickness_block  # [m] (z)

        self.normal_load = normal_load  # [N]
        self.sliding_speed = sliding_speed  # [m/s]

        self.contact_area = self.length_pin * self.width_pin
        self.sweept_area = 2 * np.pi

        self.thermal_conductivity_pin = thermal_conductivity_pin  # [W/m.K]
        self.thermal_conductivity_disc = thermal_conductivity_disc  # [W/m.K]

        self.diffusivity = diffusivity          # [] (alpha)
        self.convection_coef = convection_coef  # [] (h)

    @property
    def length_block(self):
        return self._length_block

    @length_block.setter
    def length_block(self, length_block):
        if length_block > 0:
            self._length_block = length_block
        else:
            raise Exception('Block length cannot be 0 nor negative')

    @property
    def width_block(self):
        return self._width_block

    @width_block.setter
    def width_block(self, width_block):
        if width_block > 0:
            self._width_block = width_block
        else:
            raise Exception('Block width cannot be 0 nor negative')

    @property
    def thickness_block(self):
        return self._thickness_block

    @thickness_block.setter
    def thickness_block(self, thickness_block):
        if thickness_block > 0:
            self._thickness_block = thickness_block
        else:
            raise Exception('Block thickness cannot be 0 nor negative')

    def contact_pressure(self):
        return self.normal_load / self.contact_area

    def q_total(self):
        return self.cof * self.contact_pressure() * self.sliding_speed
