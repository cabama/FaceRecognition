# Append the images with the extension .sad into image_paths
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainner/trainner2.yml')
imagen = ('dataSet/bea_0.jpg')

predict_image_pil = Image.open(imagen).convert('L')
predict_image = np.array(predict_image_pil, 'uint8')
nbr_predicted, conf = recognizer.predict(predict_image)

print "{} is Correctly Recognized with confidence {}".format(nbr_predicted, conf)



# def getImagesAndLabels(path):
#     imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
# 	for image_path in image_paths:
# 		predict_image_pil = Image.open(image_path).convert('L')
# 		predict_image = np.array(predict_image_pil, 'uint8')
# 		faces = faceCascade.detectMultiScale(predict_image)
# 		for (x, y, w, h) in faces:
# 			nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
# 			nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
# 			if nbr_actual == nbr_predicted:
# 				print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
# 			else:
# 				print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)
# 			cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
# 			cv2.waitKey(1000)


# faces,Ids = getImagesAndLabels('dataSet')
