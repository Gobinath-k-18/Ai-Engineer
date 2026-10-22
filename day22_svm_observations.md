# Day 22 — Support Vector Machines (SVM)

## 1. Definition
SVM is a machine learning algorithm mainly used for classification. It finds a decision boundary that aims to separate classes with a large margin.

## 2. Key Concepts
- **Hyperplane:** Decision boundary separating classes.
- **Margin:** Distance between the boundary and the nearest training points.
- **Support vectors:** Points that help determine the boundary.
- **Kernel:** Helps SVM model different patterns, including nonlinear ones.
- **C:** Controls the penalty for training errors.
- **Gamma:** In an RBF kernel, controls how locally each training point influences the boundary.

## 3. Experiment
Dataset: Student Study Hours and Attendance  
Training rows: 8  
Testing rows: 2  
Kernel: RBF  
C: 1.0  
Gamma: scale

| Metric | Without Scaling | With Scaling |
|---|---:|---:|
| Actual labels | [1, 0] | [1, 0] |
| Predicted labels | [1, 1] | [1, 0] |
| Test accuracy | 50% | 100% |

## 4. Observation
Scaling improved the test accuracy from 50% to 100% on this particular two-example test set. The unscaled model predicted the second example incorrectly, while the scaled model predicted both examples correctly.

The dataset and test set are too small to conclude that scaling will always improve performance.

## 5. When Is SVM Useful?
- Classification tasks with clear or learnable class boundaries.
- Datasets with many features and a moderate number of training examples.
- Nonlinear classification using kernels such as RBF.
- Problems where feature scaling can be applied carefully.

SVM can be less convenient on very large datasets and may require careful tuning of C, gamma, and the kernel.

## 6. What I Learned
- How hyperplanes and margins work.
- The purpose of kernels.
- The basic roles of C and gamma.
- How to train SVM with and without StandardScaler.
- Why scaling is important for distance-based kernels