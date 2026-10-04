import csv
import matplotlib.pyplot as plt

data = {}

with open("results/summary.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        config = row["Configuration"]

        if config not in data:
            data[config] = {"execution": [], "faults": []}

        data[config]["execution"].append(
            float(row["Execution_Time_s"])
        )

        data[config]["faults"].append(
            int(row["Major_Page_Faults"])
        )

configs = ["Baseline", "Low_Memory", "Low_CPU_Memory"]
labels = ["4 GB + 2 vCPU", "2 GB + 2 vCPU", "2 GB + 1 vCPU"]

avg_execution = [
    sum(data[c]["execution"]) / len(data[c]["execution"])
    for c in configs
]

avg_faults = [
    sum(data[c]["faults"]) / len(data[c]["faults"])
    for c in configs
]

# Graph 1
plt.figure(figsize=(8, 5))
plt.bar(labels, avg_execution)
plt.ylabel("Average Execution Time (seconds)")
plt.xlabel("VM Configuration")
plt.title("Workload Execution Time Under Different VM Resources")
plt.tight_layout()
plt.savefig("figures/execution_time.png", dpi=300)
plt.close()

# Graph 2
plt.figure(figsize=(8, 5))
plt.bar(labels, avg_faults)
plt.ylabel("Average Major Page Faults")
plt.xlabel("VM Configuration")
plt.title("Major Page Faults Under Different VM Resources")
plt.tight_layout()
plt.savefig("figures/page_faults.png", dpi=300)
plt.close()

print("Figures created successfully.")
