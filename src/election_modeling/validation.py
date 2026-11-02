"""Numerical validation shared by observations, states and forecasts."""
from __future__ import annotations

import numpy as np


def nonnegative(value: float, name: str) -> float:
    value = float(value)
    if not np.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return value


def sample_size(value: int) -> int:
    if isinstance(value, bool) or not np.isfinite(value) or int(value) != value or value <= 0:
        raise ValueError("sample size must be a positive integer")
    return int(value)


def covariance_matrix(value: object, size: int, name: str = "covariance") -> np.ndarray:
    matrix = np.array(value, dtype=float, copy=True)
    if matrix.shape != (size, size) or not np.all(np.isfinite(matrix)):
        raise ValueError(f"{name} must be a finite {size}x{size} matrix")
    tolerance = 1e-14 + 1e-10 * float(np.max(np.abs(matrix), initial=0))
    if np.max(np.abs(matrix - matrix.T), initial=0) > tolerance:
        raise ValueError(f"{name} must be symmetric")
    matrix = (matrix + matrix.T) / 2
    eigenvalues, vectors = np.linalg.eigh(matrix)
    if eigenvalues.min(initial=0) < -tolerance:
        raise ValueError(f"{name} must be positive semidefinite")
    if np.any(eigenvalues < 0):
        matrix = (vectors * np.maximum(eigenvalues, 0)) @ vectors.T
    return (matrix + matrix.T) / 2
