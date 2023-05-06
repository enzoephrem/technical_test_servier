# devide dataset into training testing and validation
import os
import random
import util
import numpy as np
from sklearn.model_selection import train_test_split


def load_data(test_size=0.2, random_seed=42):

	folder = "../Neuroflux_disorder"

	phases = [f.name for f in os.scandir(folder) if f.is_dir()]

	data, labels = [], []

	for phase_index, phase in enumerate(phases):
		phase_folder = os.path.join(folder, phase)
		for f in os.scandir(phase_folder):
			data.append(util.get_image(f.name))
			tmp_label = [0] * len(phases)
			tmp_label[phase_index] = 1
			labels.append(tmp_label)

	train_data, val_data, train_labels, val_labels = train_test_split(data, labels, test_size=test_size, random_state=random_seed)

	return train_data, val_data, train_labels, val_labels



	


	




