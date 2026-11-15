import numpy
import pandas
import sklearn

print("sklearn", sklearn.__version__)
print("numpy", numpy.__version__)
print("pandas", pandas.__version__)
for name in ("torch", "tensorflow", "lightgbm"):
    try:
        mod = __import__(name)
        print(name, getattr(mod, "__version__", "unknown"))
    except Exception:
        print(name, "not installed")
