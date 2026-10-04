# CSE-307 Operating Systems Term Paper – Part B

## Resource Constraints, Memory Management, and Virtualization in Ubuntu/VMware

### Objective

This experiment studies how changes in virtual machine resources affect the
behavior and performance of a fixed workload running inside Ubuntu on VMware.

The same Python workload was used in every experiment so that the results
could be compared fairly.

The experiment focuses mainly on:

- Virtual memory and physical memory usage
- Page faults
- CPU utilization
- Execution time
- Virtual CPU allocation
- VM resource constraints

## Experimental Environment

- Guest OS: Ubuntu Linux
- Virtualization platform: VMware
- Workload: Python 3 program
- Measurement tool: `/usr/bin/time -v`
- Swap: Ubuntu swap file

## Workload

The workload allocates a list containing 8,000,000 integers and repeatedly
performs arithmetic operations on the data for five rounds.

The workload parameters were kept unchanged in all experiments.

Source code:

`scripts/workload.py`

## VM Configurations

Three configurations were tested:

| Configuration | RAM | vCPU |
|---|---:|---:|
| Baseline | 4 GB | 2 |
| Memory constrained | 2 GB | 2 |
| Memory + CPU constrained | 2 GB | 1 |

Three measured runs were performed for each configuration.

## Results

| Configuration | Avg. Execution Time | Avg. Wall Time | Avg. Major Page Faults |
|---|---:|---:|---:|
| 4 GB + 2 vCPU | 7.27 s | 7.54 s | 0 |
| 2 GB + 2 vCPU | 6.63 s | 6.95 s | 2.67 |
| 2 GB + 1 vCPU | 7.11 s | 7.45 s | 2.67 |

The maximum resident set size was approximately 316 MB in all
configurations.

## Observations

Reducing the VM memory from 4 GB to 2 GB introduced some major page faults.
The 4 GB baseline runs recorded no major page faults, whereas the 2 GB
configuration recorded several major page faults across the three trials.

However, reducing RAM did not increase the average execution time in this
experiment. The workload used only about 316 MB of resident memory, so 2 GB
of VM memory was still sufficient for the workload.

Reducing the VM from 2 vCPUs to 1 vCPU increased the average execution time
from approximately 6.63 seconds to 7.11 seconds. The workload itself is
largely single-threaded, so this result should not be interpreted as a direct
two-core versus one-core speedup. The guest OS and background processes also
share the available virtual CPU resources.

These results demonstrate that reducing a VM resource does not necessarily
cause proportional performance degradation. The effect depends on whether
that resource is actually a bottleneck for the workload.

## Repository Structure

```text
cse307-term-paper/
├── scripts/
│   ├── workload.py
│   └── make_figures.py
├── results/
│   ├── summary.csv
│   └── raw experiment output files
├── figures/
│   ├── execution_time.png
│   └── page_faults.png
└── README.md
