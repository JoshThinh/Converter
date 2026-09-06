# HW 1: Converter and Pixel System


## ASCII-to-Decimal Converter
The ASCII-to-decimal converter ([hw1_1_p1.py](https://github.com/JoshThinh/Converter/blob/main/hw_1_p1.py)) Converts a string into an integer list of ASCII deciaml values of each character in the input string along with delimiters separating each decimal value. 

### Examples
<img width="647" height="76" alt="Screenshot 2026-09-04 133729" src="https://github.com/JoshThinh/Converter/blob/main/hw1example.png" />

## Number-Base Converter
The number-base-converter ([hw1_p2.py](https://github.com/JoshThinh/Converter/blob/main/hw1_p2.py)) allows the user to insert a number they want to convert along with what base the number is in and output binary, decimal, octal, and hexadecimal for the input number.

### Examples
Decimal to binary: 0

<img width="512" height="96" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/hw2_0.png" />


Decimal to binary: -10 (two's complement)

<img width="509" height="75" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/hw2_negative.png" />


Decimal to binary: 4.2B (largest supported unsigned value)

<img width="506" height="76" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/hw2_highestInt.png" />

## Image Reader
The image reader ([hw1_p3.py](https://github.com/JoshThinh/Converter/blob/main/hw1_p3.py)) reads an image and prints out the pixel values of that image.

Pillow is required to use this file:

```bash
pip install pillow
```

### Examples
Input: 

<img width="134" height="126" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/smileyscrenshot.png" />


Output:

<img width="137" height="122" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/awesomepicture.png" />

## Image Writer
The image writer ([hw1_p4.py](https://github.com/JoshThinh/Converter/blob/main/hw1_p4.py)) reads pixel values from a text file and then outputs a image
Also requires the Pillow dependency:
```bash
pip install pillow
```

### Examples
Input txt:

<img width="125" height="108" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/awesomepicture.png" />


Output image:

<img width="118" height="119" alt="image" src="https://github.com/JoshThinh/Converter/blob/main/smileyscreenshot2.png" />

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE.txt) license.