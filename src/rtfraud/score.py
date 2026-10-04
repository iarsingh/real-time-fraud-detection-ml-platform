REQUIRED = ("amount", "device_changes", "merchant_risk",)
WEIGHTS = {"amount": 0.002, "device_changes": 1.2, "merchant_risk": 3.0}
INTERCEPT = -2.0
THRESHOLD = 0.0


class InputError(ValueError):
    pass


def score(body):
    missing = [name for name in REQUIRED if name not in body]
    if missing:
        raise InputError("missing " + ", ".join(missing))
    total = INTERCEPT
    parts = []
    for name, weight in WEIGHTS.items():
        value = body[name]
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise InputError(f"{name} must be a number")
        contrib = weight * value
        total += contrib
        parts.append({"feature": name, "contribution": round(contrib, 4)})
    label = "hold" if total >= THRESHOLD else "pass"
    return {"score": round(total, 4), "label": label, "threshold": THRESHOLD, "parts": parts}
