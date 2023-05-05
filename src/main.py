import util
import preprocess

# Parse arguments
model_number, filepath = util.parse_arg()

if model_number == '1':
	from models import Model1
	model = Model1()
elif model_number == '2':
	from models import Model2
	model = Model2()

train_data, val_data, train_labels, val_labels = preprocess.load_data()
