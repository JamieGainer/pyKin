import numpy as np

def transverse_sphericity(jet_list):
    transverse_sphericity_tensor = np.zeros((2,2))
    pt_squared_sum = 0.0
    for jet in jet_list:
        transverse_sphericity_tensor[0][0] += jet.px**2
        transverse_sphericity_tensor[0][1] += jet.px * jet.py
        transverse_sphericity_tensor[1][0] += jet.px * jet.py
        transverse_sphericity_tensor[1][1] += jet.py ** 2
        pt_squared_sum += jet.pt**2
    transverse_sphericity_tensor /= pt_squared_sum
    eigen_values = np.linalg.eigvalsh(transverse_sphericity_tensor)
    # do something with eigenvalues

