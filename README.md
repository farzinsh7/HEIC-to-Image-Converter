# HEIC to Image Converter 🖼️

A simple Python script that recursively finds `.HEIC` image files in a given folder and converts them to `.JPG`, `.PNG`, `.TIFF`, `.WEBP`, and more, using [Pillow](https://python-pillow.org/) and [pillow-heif](https://github.com/carsales/pillow-heif).

You can easily extend this script to convert `.HEIC` files to various image formats.

---

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/farzinsh7/HEIC-to-Image-Converter.git
cd heic-to-jpg-converter
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install the requirements

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Put your `.HEIC` files in a folder (e.g. `files`)

Or set the path to wherever your images are.

### 2. Run the script

```bash
python convertor.py
```

By default, the script:

- Searches inside `files` (you can change the path in the script)
- Converts the **first 10 `.HEIC` files** it finds
- Saves the `.JPG` files into the `output/` directory

---

## ⚙️ Customize

- To convert all files (not just 10), increase or remove the `max_conversions` limit in the script.
- To change the output format (e.g., PNG), edit the `.save()` line:
  ```python
  image.save(jpg_path, "PNG")
  ```

---

## 🧾 Requirements

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)
- [pillow-heif](https://pypi.org/project/pillow-heif/)

These are listed in `requirements.txt`.

---

## 📂 Example Folder Structure

```
heic-to-jpg-converter/
│
├── convert_heic_to_jpg.py
├── requirements.txt
├── README.md
├── output/
└── files/
    ├── image1.HEIC
    └── ...
```

---

## 📝 License

This project is licensed under the MIT License.
