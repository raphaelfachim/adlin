# This is a sample Python script.
from model.ContactTemperature import ContactTemperature
from tools.Calculator import Calculator

if __name__ == '__main__':
    c = ContactTemperature(
        0, 0, 1, 0, 0.5, 0.5, 0.5, 0, 0, 1, 1, 1, 0, 0, 1, 4
    )

    #print(Calculator.contact_temperature_gamma(c, 1, 1))
    #print(Calculator.contact_temperature_phi(c, 1, 1))
    print(Calculator.contact_temperature_t(c, 1, 1, 0.5))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
