def validate_numeric_list(x):
    out = []
    for i, v in enumerate(x):
        try:
            fv = float(v)
        except Exception:
            raise ValueError(f"Element {i} is not numeric: {v}")
        if fv != fv or fv in (float("inf"), float("-inf")):
            raise ValueError(f"Element {i} is not finite: {v}")
        out.append(fv)
    return out


import numpy as np

class SumModel:
    def predict(self, X):
        X = np.asarray(X, dtype=float)
        return X.sum(axis=1)