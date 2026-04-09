import numpy as np

def acquisition_range(dT_N, x_c, dT_0, dT_min, L, J_bcc, epsilon):
    """
    Predicts the thermal acquisition range as a function of the
    atmospheric extinction coeffisient using the parameterised minimum
    resolvable temperature difference (PMRTD) method from Børve 2021.

    Parameters
    ----------
    dT_N : float
        MRTD at the Nyquist frequency
    x_c : float
        asymptotic frequency at infinite MRTD
    dT_0 : float
        true temperature difference
    dT_min : float
        MRTD at zero frequency
    L : float
        critical target dimension
    J_bcc : float
        Johnson bar cycle criteria
    epsilon : float
        instantenous field of view

    Returns
    -------
    gamma : array (float)
        atmospherpic extinction coefficient
    R : array (float)
        acquisition range

    """

    gamma = np.linspace(0.01, 4, 100)  # (1/km) extinction coefficient

    nu_N = 1 / (2 * epsilon)           # (1/mrad) Nyquist frequency
    R_N = L / J_bcc * nu_N             # (km) range estimate according to the pixels-on-target method
    y_0 = np.log(dT_0)
    y_min = np.log(dT_min)
    y_N = np.log(dT_N)
    E_y = y_0 - y_min
    D_y = y_N - y_min

    # predicted range
    Gamma = gamma * np.log(np.e) * R_N
    beta = Gamma * x_c + E_y + D_y * (x_c - 1)
    x = (beta - np.sqrt(beta**2 - 4 * Gamma * E_y * x_c)) / (2 * Gamma)  # normalised range
    R = R_N * x                                                          # physical range

    return gamma, R