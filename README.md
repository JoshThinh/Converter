# HW 1: Converter and Pixel System


## ASCII-to-Decimal Converter
The ASCII-to-decimal converter ([hw1_1_p1.py](https://github.com/JoshThinh/Converter/blob/main/hw_1_p1.py)) Converts a string into an integer list of ASCII deciaml values of each character in the input string along with delimiters separating each decimal value. 

### Examples
<img width="647" height="76" alt="hw1example.png" src="" />

## Number-Base Converter
The number-base-converter ([number_base_converter.py](https://github.com/trife0907/CS-240/blob/main/Assignment1/number_base_converter.py)) allows a user to convert any number to and from binary, decimal, octal, or hexadecimal.

### Examples
Decimal -> binary: 0

<img width="512" height="96" alt="image" src="https://github.com/user-attachments/assets/1e93a754-4a15-4497-8f9f-5d87aff407e4" />


Decimal -> binary: -5 (two's complement)

<img width="509" height="75" alt="image" src="https://github.com/user-attachments/assets/ab1ffea0-2502-4858-ab08-150e3cfa4224" />


Decimal -> binary: ~4.2B (largest supported unsigned value)

<img width="506" height="76" alt="image" src="https://github.com/user-attachments/assets/fe11029a-f3de-4279-9a8d-67569df8704a" />

## Image Reader
The image reader ([image_reader.py](https://github.com/trife0907/CS-240/blob/main/Assignment1/image_reader.py)) reads an image and prints out its pixel values in the image's dimensions.

Requires the Pillow dependency. Install it by running:

```bash
pip install pillow
```

### Examples
Input image

<img width="134" height="126" alt="image" src="https://github.com/user-attachments/assets/e113e259-432d-4e32-b454-b30f47989736" />


Output text

<img width="137" height="122" alt="image" src="https://github.com/user-attachments/assets/71010ee2-f15f-44d7-a46a-bef129e2a1bb" />

## Image Writer
The image writer ([image_writer.py](https://github.com/trife0907/CS-240/blob/main/Assignment1/image_writer.py)) reads in pixel values from a text file and generates an image.

Requires the Pillow dependency. Install it by running:

```bash
pip install pillow
```

### Examples
Input pixels

<img width="125" height="108" alt="image" src="https://github.com/user-attachments/assets/15e176f5-ad2e-4ad6-96d7-e92528219c63" />


Output image

<img width="118" height="119" alt="image" src="https://github.com/user-attachments/assets/b23b5f7e-0aa2-44ed-a17a-372af76cf8db" />

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE.txt) license.