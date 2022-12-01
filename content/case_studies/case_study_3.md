---
title: "John Conway's Game of Life"
weight: 3
---

![Animated GIF of the Game of Life](./../game_of_life.gif)

## Serial Approach

```python
{{% include "/content/case_studies/case_study_3_serial.py" %}}
```

* **Average wall time:** 31.07s

## Parallel Approach

```python
{{% include "/content/case_studies/case_study_3_parallel.py" %}}
```

* **Average wall time (2 MPI processes):** 20.8 (1.49 speedup)
* **Average wall time (4 MPI processes):** 13.4s (2.32 speedup)
* **Average wall time (8 MPI processes):** 9.64s (3.22 speedup)

(Speedup as compared to the serial approach code.)






