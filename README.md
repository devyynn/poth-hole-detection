# Pothole Detection Model – Quick Start Guide

This repository contains a YOLOv8 segmentation model for pothole detection. Follow these instructions to run inference on your images.

---

## 1. Install Requirements

```bash
pip install ultralytics
```

---

## 2. Setup

- Download or copy the `best.pt` model file into this directory.
- Place your input images into a folder, e.g., `data/images/`.

---

## 3. Run Inference

You can run inference using the provided script:

```bash
python run_model.py
```

- The script will process all images in `data/images/` (or modify the `source` variable for your path).
- Results with segmentation masks will be saved in `runs/segment/predict`.

---

## 4. (Alternative) Use the Ultralytics CLI

```bash
yolo task=segment mode=predict model=best.pt source=data/images/
```

---

## 5. Customization

- Change the `source` variable in `run_model.py` to point to a different image, folder, or video file.
- Adjust the confidence threshold by editing `conf=0.25` in the script.

---

## 6. Troubleshooting

- Make sure you have Python 3.8+ installed.
- Ensure `best.pt` is in the same folder as `run_model.py`.
- If you encounter errors with the Ultralytics library, try upgrading:  
  ```bash
  pip install --upgrade ultralytics
  ```

---
