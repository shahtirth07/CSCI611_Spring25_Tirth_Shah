# CSCI 611 - Spring 2025 - Assignment 2

**Name:** Tirth Shah  
**Date:** 2/21/2025

## 📚 Introduction

This repository covers **Assignment 2** of **CSCI 611**, including implementations in:

- **Image Filtering**
- **CNN for CIFAR-10 Classification**

---

## 🛠️ Changes & Accuracy Impact

### 🔹 Image Filtering

- **Implemented Filters:**
  - Edge Detection (Horizontal, Vertical [Sobel/custom], Diagonal)
  - Blurring (2x2, 3x3, 5x5 average)
  
- **Key Observations:**
  - **Edge Detection:** Sobel operator effectively detected edges, improving feature visibility.
  - **Blurring:** Increased blur kernel size led to **better noise reduction** but at the cost of detail loss. This clarified the trade-off between noise removal and sharpness.

### 🔹 CNN Implementation Changes

- **Initial Architecture:** 3 conv layers, no batch normalization.
- **Final Architecture Improvements:**
  - Increased to **4 conv layers** (32→64→128→256 channels).
  - Added **Batch Normalization** (stabilized training).
  - Added **Dropout** (reduced overfitting, p=0.3).
  - Added **Data Augmentation** (horizontal flips, slight rotations).

**Optimizer Comparison:**

| Optimizer | Learning Rate | Accuracy |
|-----------|---------------|----------|
| SGD       | 0.01          | **76%**  |
| Adam      | 0.001         | 67%      |

- **Change in Optimizer:**
  - Tested Adam optimizer but observed a **decrease in accuracy** compared to SGD. This highlighted that **optimizer performance can vary significantly** based on dataset and architecture.

**Other Hyperparameter Changes:**

- **Epochs:** Increased from initial tests (5 epochs) to **10 epochs**, improving validation accuracy by **~5%**.
- **Batch Size:** Kept constant at **20** for stability.

---

## 📊 Summary of Accuracy Improvements

- **Initial accuracy (baseline CNN with SGD):** ~68%
- **Final accuracy (after architecture & data augmentation improvements):** **76%**
- **Accuracy decrease (Adam vs. SGD):** 9% lower with Adam, underscoring that SGD was better-suited for CIFAR-10 classification in this scenario.

---

## 💡 Key Observations & Thoughts

- **CNN Depth & Batch Norm:** Increasing depth with **batch normalization** stabilized and improved training, leading to higher accuracy.
- **Optimizer Sensitivity:** Surprisingly, **Adam underperformed**, indicating it's not always superior, especially without careful tuning. **SGD was more stable and reliable** for this architecture/dataset.
- **Data Augmentation:** A simple yet effective improvement, increasing accuracy by several percent without architectural complexity.

**Final Thought:**  
The experiment emphasized that **optimizers and architecture tweaks must be tailored** to the specific problem. **SGD** emerged as clearly better here, suggesting a critical need for experimentation and hyperparameter tuning in machine learning tasks.

---

## 📝 Future Improvements

- Tune Adam's **learning rate** and other hyperparameters further.
- Try **more complex CNN architectures** (e.g., ResNet) for better accuracy.
- Experiment with other optimizers like **RMSProp** or **AdamW**.

---

**End of README**
