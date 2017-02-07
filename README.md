# FaceRecognition
[ES] Reconocimiento Facial Basado en opencv.  
[EN] Facial recognition based in opencv.  

Fuente: [thecodacus](http://thecodacus.com/opencv-python-face-detection/#.WJi_Z7bhBE4)

## Requisitos

- Python 2.x.
- OpenCV 2.x.
- Numpy library.

Por defecto Ubuntu y OSX tienen instalado una version 2.7 de python, por lo que solo es necesario instalar las librerias.  
Install requisits. By default ubuntu and OSX has got a 2.7 python version. Only is necesary install the libraries.

```bash
pip install opencv-python
pip install numpy
```

## Ficheros // Files

[Es] Ficheros individuales creados para pruebas separadas.  
[En] Files used by test.  

- **cascade.py**  
  Identify the face with haarcascade and print it in the output windows.
- **dataSetGenerator.py**  
  Use the webcam take 20 pictures, cut the face and save the files.
- **train.py**   
  This script loads the pictures of dataSetGenerator, train the classificator and write the classifications results.
- **identify.py**   
  Loads the classifications results and identify the face of the picture.

---

[Es] Ficheros finales que contienen todo.  
[En] The final files, their contain all software.  

- **identificadorFacial.py**  
  It's the object that containt all identify process. We should call their methods.
- **main.py**  
  It's a terminal program to manage the identificadorFacial object. It call to identificadorFacial methods.


