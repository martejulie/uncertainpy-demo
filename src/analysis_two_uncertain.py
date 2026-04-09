import chaospy as cp
import uncertainpy as un
from acquisition_range import acquisition_range
from plotter import plot_w_two_uncertain
import time

# if you use Windows, you must write your Uncertainpy script 
# inside a 'if __name__ == "__main__":' block
if __name__ == "__main__":

    start_time = time.time()

    # initialize the model
    model = un.Model(run=acquisition_range,  labels=["$\gamma$ (1/km)", "range (km)"])

    # define a parameter dictionary
    parameters = {"dT_N": cp.Uniform(0.25, 4),      # (K) MRTD at the Nyquist frequency
                  "x_c": cp.Uniform(1.4, 2.6),      # (unitless) asymptotic (normalized) frequency where MRTD value becomes infinite
                  "dT_0": 2.0,                      # (K) true temperature difference
                  "dT_min": 0.015,                  # (K) MRTD at zero frequency
                  "L": 0.95,                        # (m) critical target dimension
                  "J_bcc": 1.0,                     # (unitless) Johnson bar cycle count
                  "epsilon": 0.19}                  # (mrad) instantaneous field of view

    # create the parameters
    parameters = un.Parameters(parameters)

    # set up the uncertainty quantification
    UQ = un.UncertaintyQuantification(model, parameters=parameters, logger_level="info")

    # Perform the uncertainty quantification using
    # polynomial chaos with point collocation (by default)
    # We set the seed to easier be able to reproduce the result
    data = UQ.quantify(seed=10)

    elapsed_time = round(time.time() - start_time, 2)
    print('Elapsed time:', elapsed_time, 's')

    # make a nice plot     
    plot_w_two_uncertain('data/acquisition_range.h5')
