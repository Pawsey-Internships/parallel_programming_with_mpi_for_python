---
title: "Monte Carlo Integration"
weight: 1
katex: true
math: 'mmark'
---

Monte Carlo integration is a technique for numerical integration using random numbers. To integrate function $f(x)$, it is evaluated at random points $x^\prime$ over a region of volume $V$. The ratio of the number of points that fall within the domain of the function, $\text{hits}$, and total sampled points, $N$, is proportional to the volume of $f(x)$. As such, with sufficiently high $N$ we can estimate the integral of $f(x)$ as:

$$ \int_D f(x) \text{ } dx dy \dots dz \approx V \frac{\text{hits}}{N} $$

## Integrating a Unit Circle

Consider the unit circle (a circle of radius one) centred at $x = (0, 0)$. To find its area, we need to integrate the region:

$$ \sqrt{(x_1^2 + x_2^2)} < 1 $$

To approximate the integral with Monte Carlo integration, we draw random points $x^\prime$ over a $2 \times 2$ square ($V=4$). With enough sampled points, we expect the following:

$$V \frac{\text{hits}}{N} \approx \pi$$

### Serial Appraoch

```python
{{% include "/content/case_studies/case_study_1_serial.py" %}}
```

* **Average wall time:** 14.085s

### Parallel Approach

```python
{{% include "/content/case_studies/case_study_1_parallel.py" %}}
```

* **Average wall time (1 MPI process):** 15.829s 
* **Average wall time (2 MPI processes):** 8.873s (1.78 speedup)
* **Average wall time (4 MPI processes):** 5.389s (2.94 speedup)
* **Average wall time (8 MPI processes):** 3.698S (4.28 speedup)
