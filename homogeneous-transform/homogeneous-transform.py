import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    T_arr = np.asarray(T, dtype = float)
    points_arr = np.asarray(points, dtype = float)
    
    single_point = points_arr.ndim == 1

    points_arr = np.atleast_2d(points_arr)

    N = points_arr.shape[0]
    ones = np.ones((N, 1))

    points_h = np.concatenate((points_arr, ones), axis=1)

    Transformed = (T_arr @ points_h.T).T

    if single_point :
        return Transformed[0, :3]
    return Transformed[:,:3]




