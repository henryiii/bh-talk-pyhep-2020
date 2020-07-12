import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator

plt.grid()
plt.xticks(np.arange(4), [])
plt.yticks(np.arange(3), [])
plt.tick_params(axis="both", which="minor", length=0)
ax = plt.gca()
for name, axis in zip("xy", (ax.xaxis, ax.yaxis)):
    axis.set_minor_locator(MultipleLocator(0.5))
    axis.set_minor_formatter(FormatStrFormatter(f"{name}-bin %d"))
for i in range(3):
    for j in range(2):
        plt.text(i + 0.5, j + 0.5, f"cell [{i}, {j}]", ha="center", va="center")
plt.xlabel("x-axis $\\longrightarrow$")
plt.ylabel("y-axis $\\longrightarrow$")
plt.title("histogram layout")
plt.savefig("histogram_layout.svg")
