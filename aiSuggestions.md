import numpy as np
from scipy.spatial.transform import Rotation as R


def get_rotation_matrix(t, tmp_noise, noise_scale=0.05, spin_speed=1.0):
    """
    Computes a rotation matrix for time t, where the rotation AXIS
    drifts slowly according to Perlin/Simplex noise, while the
    rotation ANGLE increases steadily — this produces a smooth,
    intentional-looking spin instead of chaotic tumbling.

    Parameters
    ----------
    t : float
        Current time / frame value.
    tmp_noise : object
        Your noise generator (e.g. opensimplex.OpenSimplex instance),
        must expose .noise2(x, y) -> float in range [-1, 1].
    noise_scale : float
        Controls how fast the rotation axis drifts. Smaller = slower,
        smoother axis drift. Try 0.02–0.1.
    spin_speed : float
        Controls how fast the object spins around its (drifting) axis.
        Larger = faster spin.

    Returns
    -------
    np.ndarray, shape (3, 3)
        Rotation matrix to apply to your points.
    """
    axis_x = tmp_noise.noise2(t * noise_scale, 0)
    axis_y = tmp_noise.noise2(t * noise_scale, 10)
    axis_z = tmp_noise.noise2(t * noise_scale, 20)

    axis = np.array([axis_x, axis_y, axis_z])
    norm = np.linalg.norm(axis)

    # Guard against a near-zero vector (division by zero) — fall back
    # to a default axis (z-axis) if noise values happen to cancel out.
    if norm < 1e-8:
        axis = np.array([0.0, 0.0, 1.0])
    else:
        axis = axis / norm

    angle = t * spin_speed  # steady, monotonically increasing spin

    rot = R.from_rotvec(axis * angle)
    return rot.as_matrix()


def rotate_points(points, R_matrix):
    """
    Rotates a point cloud around its own centroid (not the world origin),
    which prevents the "orbiting/swinging" artifact that happens when
    rotating around (0,0,0) for an off-center shape.

    Parameters
    ----------
    points : np.ndarray, shape (N, 3)
        Your point cloud / vertex array.
    R_matrix : np.ndarray, shape (3, 3)
        Rotation matrix from get_rotation_matrix().

    Returns
    -------
    np.ndarray, shape (N, 3)
        Rotated points, same shape as input.
    """
    centroid = points.mean(axis=0)
    centered = points - centroid
    rotated = centered @ R_matrix.T
    return rotated + centroid
