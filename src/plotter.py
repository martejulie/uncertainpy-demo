import prettyplot as pp
import uncertainpy as un
import numpy as np
import matplotlib.pyplot as plt

def plot_w_two_uncertain(filename):
    """
    Visualize the uncertainty quantification and sensitivity analysis
    of the PMRTD model with two uncertain parameters.
    """
    
    # load data
    data = un.Data()
    data.load(filename=filename)
    R_mean = data['acquisition_range']['mean']
    R_p5 = data['acquisition_range']['percentile_5']
    R_p95 = data['acquisition_range']['percentile_95']
    gamma = data['acquisition_range']['time']

    # name parameters
    params = [r'$\Delta T_\mathrm{N}$', r'$x_\mathrm{c}$']

    # initialize plot
    fig = plt.figure()
    axA = plt.subplot(221)
    axB = plt.subplot(222)
    axC = plt.subplot(223)
    axD = plt.subplot(224)
    fig.set_figwidth(10)
    fig.set_figheight(10)
    pp.set_style("seaborn-white")

    # plot panel A
    ax = pp.prettyPlot(gamma, R_mean,
                    color='#8c564b',
                    nr_colors=7,
                    palette='tab10',
                    ax=axA)


    colors = pp.get_current_colormap()
    ax.fill_between(gamma,
                    R_p5,
                    R_p95,
                    color=colors[6],
                    linewidth=0)

    # plot panel B
    for i in range(len(params)):
        pp.prettyPlot(gamma, data['acquisition_range']['sobol_total'][i,:],                   
                   palette='muted',
                   nr_colors=2,
                   color=i,
                   ax=axB)

    # plot panel C
    width = 0.2
    index = np.arange(1, len(data.uncertain_parameters)+1)*width
    pp.prettyBar(data['acquisition_range']['sobol_first_average'],            
              palette='muted',
              index=index,
              xlabels=params,
              ax=axC)

    # plot panel D
    pp.prettyBar(data['acquisition_range']['sobol_total_average'],          
              palette='muted',
              index=index,
              xlabels=params,
              ax=axD)

    # set legends
    axA.legend([r'$\mathbb{E}[R]$', r'$I_{0.9}$'])
    axB.legend(params)

    # set labels
    axA.set_xlabel(r'$\gamma$ [1/km]')
    axB.set_xlabel(r'$\gamma$ [1/km]')
    axA.set_ylabel(r'$R$ [km]')
    axB.set_ylabel(r'$S_{T_i}$')
    axC.set_ylabel(r'$\hat{S}_{i}$')
    axD.set_ylabel(r'$\hat{S}_{T_i}$')

    # set limits
    axC.set_ylim([0, 1])
    axD.set_ylim([0, 1])

    # set titles
    axA.set_title(r'Usikkerhetskvantifisering av $R$')
    axB.set_title(r"Sobol-indekser av total orden")
    axC.set_title(r"Sobol-indekser av første orden")
    axD.set_title(r"Sobol-indekser av total orden")

    # ABC
    axes = [axA, axB, axC, axD]
    letters = ['A', 'B', 'C', 'D']
    i = 0
    for ax in axes:
        ax.text(-0.05, 1.1, letters[i], transform=ax.transAxes, fontsize=18, fontweight='bold', va='top', ha='right')
        i += 1

    # make pretty
    plt.tight_layout()

    # save figure
    plt.savefig('figures/two_uncertain.pdf', dpi=600)
    plt.savefig('figures/two_uncertain.png', dpi=600)
    
    return

def plot_w_three_uncertain(filename):
    """
    Visualize the uncertainty quantification and sensitivity analysis
    of the PMRTD model with three uncertain parameters.
    """
    
    # load data
    data = un.Data()
    data.load(filename=filename)
    R_mean = data['acquisition_range']['mean']
    R_p5 = data['acquisition_range']['percentile_5']
    R_p95 = data['acquisition_range']['percentile_95']
    gamma = data['acquisition_range']['time']

    # name parameters
    params = [r'$\Delta T_\mathrm{N}$', r'$x_\mathrm{c}$', r'$J_\mathrm{bcc}$']

    # initialize plot
    fig = plt.figure()
    axA = plt.subplot(221)
    axB = plt.subplot(222)
    axC = plt.subplot(223)
    axD = plt.subplot(224)
    fig.set_figwidth(10)
    fig.set_figheight(10)
    pp.set_style("seaborn-white")

    # plot panel A
    ax = pp.prettyPlot(gamma, R_mean,
                       color='#8c564b',
                       nr_colors=7,
                       palette='tab10',           
                       ax=axA)

    colors = pp.get_current_colormap()
    ax.fill_between(gamma,
                    R_p5,
                    R_p95,
                    color=colors[6],
                    linewidth=0)

    # plot panel B
    for i in range(len(params)):
        pp.prettyPlot(gamma, data['acquisition_range']['sobol_total'][i,:],           
                      palette='muted',
                      nr_colors=3,
                      color=i,
                      ax=axB)

    # plot panel C
    width = 0.2
    index = np.arange(1, len(data.uncertain_parameters)+1)*width
    pp.prettyBar(data['acquisition_range']['sobol_first_average'],           
                 palette='muted',
                 index=index,
                 xlabels=params,
                 ax=axC)

    # plot panel D
    pp.prettyBar(data['acquisition_range']['sobol_total_average'],           
                 palette='muted',
                 index=index,
                 xlabels=params,
                 ax=axD)

    # set legends
    axA.legend([r'$\mathbb{E}[R]$', r'$I_{0.9}$'])
    axB.legend(params)

    # set labels
    axA.set_xlabel(r'$\gamma$ [1/km]')
    axB.set_xlabel(r'$\gamma$ [1/km]')
    axA.set_ylabel(r'$R$ [km]')
    axB.set_ylabel(r'$S_{T_i}$')
    axC.set_ylabel(r'$\hat{S}_{i}$')
    axD.set_ylabel(r'$\hat{S}_{T_i}$')

    # set limits
    axC.set_ylim([0, 1])
    axD.set_ylim([0, 1])

    # set titles
    axA.set_title(r'Usikkerhetskvantifisering av $R$')
    axB.set_title(r"Sobol-indekser av total orden")
    axC.set_title(r"Sobol-indekser av første orden")
    axD.set_title(r"Sobol-indekser av total orden")

    # ABC
    axes = [axA, axB, axC, axD]
    letters = ['A', 'B', 'C', 'D']
    i = 0
    for ax in axes:
        ax.text(-0.05, 1.1, letters[i], transform=ax.transAxes, fontsize=18, fontweight='bold', va='top', ha='right')
        i += 1

    # make pretty
    plt.tight_layout()

    # save figure
    plt.savefig('figures/three_uncertain.pdf', dpi=600)
    plt.savefig('figures/three_uncertain.png', dpi=600)
    
    return
