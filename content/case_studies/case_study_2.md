---
title: "Image Processing"
weight: 2
---

A common task in machine learning is the pre-processing of large data sets. The below code resizes a folder of images and saves the resized images in a new directory. We'll process [a subset of the Oxford-IIIT Pet dataset](https://github.com/Pawsey-Internships/parallel_programming_with_mpi_for_python/blob/main/content/case_studies/images.zip?raw=true) [1].

### Serial Approach

```python
{{% include "/content/case_studies/case_study_2_serial.py" %}}
```

### Parallel Approach 1

* This approach creates the destination folder and retrieves the file paths at rank 0. 
* The list of image paths is divided into `size` sublists.
* We use `COMM.scatter` to send one sublist to each MPI process.
* Note that we're using the lower-case scatter version as we send Python objects (lists).
* Unlike the uppercase MPI methods (for NumPy arrays), we need to arrange the data we want to send into a list of `size` elements.

```python
{{% include "/content/case_studies/case_study_2_parallel_1.py" %}}
```

real 2.159000

* **Average wall time:** 15.42s
* **Average wall time:** 8.89s (1.73 speedup)
* **Average wall time:** 5.53s (2.79 speedup)
* **Average wall time:** 3.87s (3.98 speedup)



### Parallel Approach 2

* For this approach, we create the destination folder at rank 0.
* Each process retrieves its own complete list of the image paths.
* We then use the `rank` and `size` variables to compute the `start_index` and `end_index` variables, which define a unique slice of `image_paths` at each MPI process.

```python
{{% include "/content/case_studies/case_study_2_parallel_2.py" %}}
```

* **Average wall time (1 MPI process):** 15.45s
* **Average wall time (2 MPI processes):** 9.07s (1.70 speedup)
* **Average wall time (4 MPI processes):** 5.66 (2.72 speedup)
* **Average wall time (8 MPI processes):** 3.84 (4.02 speedup)


[1] [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
