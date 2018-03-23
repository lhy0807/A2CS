import h5py
import numpy as np
from sklearn.utils import shuffle
X_train = []
X_test = []
for filename in ["gap_ResNet50.h5", "gap_Xception.h5", "gap_InceptionV3.h5", "gap_VGG19.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])
X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

from keras.models import *
from keras.layers import *
input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)
model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
model.save_weights('dog_cat.h5')

y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)
from keras.preprocessing.image import *
import xlsxwriter
import os	

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(y_pred)):
	worksheet.write(i,1,y_pred[i])
workbook.close()


gen = ImageDataGenerator()
test_generator = gen.flow_from_directory("test", (224, 224), shuffle=False, 
                                         batch_size=16, class_mode=None)

arranged_arr = np.zeros(len(test_generator.filenames))

list = os.listdir('test/test')
list.sort()
for i in range(len(list)):
	
	num = int(list[i].split('.')[0])
	arranged_arr[num-1] = y_pred[i]


workbook = xlsxwriter.Workbook('pred.xlsx')
worksheet = workbook.add_worksheet()
for i in range(len(arranged_arr)):
	worksheet.write(i,1,arranged_arr[i])
workbook.close()