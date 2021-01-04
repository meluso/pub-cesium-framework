# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:27:28 2020

@author: John Meluso
"""

import numpy as np

def get_params(exec_num=2):
    """Creates parameters for a simulation."""

    # Count of cases for each execution for unique indexing
    case_count = [3388,3388,3388,3388]

    # Index counter initialization for simulation runs
    index = sum(case_count[0:exec_num-1])-1

    # Empty parameter array for simulation
    params = []

    if exec_num == 2:

        # Create array for each input parameter.
        nod = [100]
        obj = ["absolute-sum","sphere","levy","ackley"]
        edg = [2]
        tri = np.round(np.arange(0,1.1,0.1),decimals=1)
        con = np.array([0.01,0.05,0.1,0.5,1,5,10])
        cyc = [100]
        tmp = [0.1]
        itr = [1]
        mth = ["future"]
        prb = np.round(np.arange(0,1.1,0.1),decimals=1)
        crt = [2.62]

    elif exec_num == 3:

        # Create array for each input parameter.
        nod = [500]
        obj = ["absolute-sum","sphere","levy","ackley"]
        edg = [2]
        tri = np.round(np.arange(0,1.1,0.1),decimals=1)
        con = np.array([0.01,0.05,0.1,0.5,1,5,10])
        cyc = [100]
        tmp = [0.1]
        itr = [1]
        mth = ["future"]
        prb = np.round(np.arange(0,1.1,0.1),decimals=1)
        crt = [2.62]

    elif exec_num == 4:

        # Create array for each input parameter.
        nod = [1000]
        obj = ["absolute-sum","sphere","levy","ackley"]
        edg = [2]
        tri = np.round(np.arange(0,1.1,0.1),decimals=1)
        con = np.array([0.01,0.05,0.1,0.5,1,5,10])
        cyc = [100]
        tmp = [0.1]
        itr = [1]
        mth = ["future"]
        prb = np.round(np.arange(0,1.1,0.1),decimals=1)
        crt = [2.62]

    else: # execu_num == 1:

        # Create array for each input parameter.
        nod = [50]
        obj = ["absolute-sum","sphere","levy","ackley"]
        edg = [2]
        tri = np.round(np.arange(0,1.1,0.1),decimals=1)
        con = np.array([0.01,0.05,0.1,0.5,1,5,10])
        cyc = [100]
        tmp = [0.1]
        itr = [1]
        mth = ["future"]
        prb = np.round(np.arange(0,1.1,0.1),decimals=1)
        crt = [2.62]

    # Iteratively construct dictionaries and populate the parameter list.
    for nn in np.arange(len(nod)):
        for oo in np.arange(len(obj)):
            for ee in np.arange(len(edg)):
                for tr in np.arange(len(tri)):
                    for co in np.arange(len(con)):
                        for cy in np.arange(len(cyc)):
                            for tm in np.arange(len(tmp)):
                                for ii in np.arange(len(itr)):
                                    for mm in np.arange(len(mth)):
                                        for pp in np.arange(len(prb)):
                                            for cr in np.arange(len(crt)):
                                                index += 1
                                                new_params \
                                                    = {'ind': index,
                                                       'run': -1,
                                                       'nod': nod[nn],
                                                       'obj': obj[oo],
                                                       'edg': edg[ee],
                                                       'tri': tri[tr,],
                                                       'con': con[co,],
                                                       'cyc': cyc[cy],
                                                       'tmp': tmp[tm],
                                                       'itr': itr[ii],
                                                       'mth': mth[mm],
                                                       'prb': prb[pp],
                                                       'crt': crt[cr]
                                                       }
                                                params.append(new_params)

    # Return parameters
    return params


if __name__ == '__main__':
    params = get_params()