## About
This project focuses on image processing through convolutions and pooling using **TensorFlow** and **Google Cloud**. It utilizes **SciPy** and **NumPy** to load and manipulate images, apply 3x3 convolution filters, and analyze output effects. The project serves as a hands-on lab to explore fundamental concepts of deep learning and computer vision, including feature extraction and image analysis.

## Prerequisites
- Python 3.x
- TensorFlow
- Skimage
- Matplotlib
- SciPy
- NumPy
- Google Cloud Console access with configured credentials

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ljubogdan/gcloud-convolution-tensorflow.git
   ```
2. Install required dependencies:
   ```bash
   pip install tensorflow scipy numpy skimage matplotlib
   ```
3. Set up Google Cloud credentials (refer to [Google Cloud documentation](https://cloud.google.com/docs)).

## Usage
1. Navigate to the project directory:
   ```bash
   cd gcloud-convolution-tensorflow
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Follow the instructions to load an image, apply convolution filters, and observe pooling effects on the output.

## Project Structure
- `main.py`: Core script for image processing and convolution operations.
- `data/`: Directory for sample images (add your own images here).
- `filters/`: Example 3x3 filter configurations.

## Learning Outcomes
- Understand how convolutions extract image features.
- Apply pooling to compress and enhance image data.
- Gain hands-on experience with TensorFlow, SciPy, and NumPy in a Google Cloud environment.

## License
MIT License

---

Developed as part of a Google Cloud Training lab.
