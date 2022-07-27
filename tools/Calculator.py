from model.ContactTemperature import ContactTemperature
import math
import cmath
import numpy as np


class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def contact_temperature_gamma(c: ContactTemperature, m, n):
        print('Calculating gamma')
        x_1 = math.pow((m * np.pi * 2 / c.width_block), 2)
        x_2 = math.pow((n * np.pi * 2 / c.length_block), 2)
        x_i = (m * np.pi * 2 / c.width_block) * c.sliding_speed / c.diffusivity
        gamma_sqr = (x_1 + x_2 + 1j * x_i)
        return cmath.sqrt(gamma_sqr)

    @staticmethod
    def contact_temperature_phi(c: ContactTemperature, m, n):
        print('Calculating phi')
        if m * n != 0:
            x_1 = math.sin(m * np.pi * c.width_pin / c.width_block)
            x_2 = math.sin(n * np.pi * c.length_pin / c.length_block)
            den = m * n * math.pow(np.pi, 2)
            return x_1 * x_2 / den
        else:
            return 0

    @staticmethod
    def contact_temperature_t(c, m, n, z):
        print('Calculating T(m,n,z)')
        gamma = Calculator.contact_temperature_gamma(c, m, n)
        den = c.convection_coef * cmath.sinh(gamma * c.thickness_block) + \
              c.thermal_conductivity_disc * gamma * cmath.cosh(gamma * c.thickness_block)
        if den != 0:
            phi = Calculator.contact_temperature_phi(c, m, n)
            num = phi * cmath.sinh(gamma * (c.thickness_block - z))
            return num / den
        raise ArithmeticError('Division by 0')

    @staticmethod
    def contact_temperature_t_xy(c, x, y, z):
        surface_ratio = 1   # surface ratio will determine the number of iterations

    @staticmethod
    def t_1(c, z):
        return Calculator.contact_temperature_phi(c, 0, 0, z)

    @staticmethod
    def t_2(c, z, iterations):
        soma = 0
        for i in range(iterations):
            soma += 1
        return soma

    @staticmethod
    def t_3(c, z):
        pass

    @staticmethod
    def t_4(c, z):
        pass
