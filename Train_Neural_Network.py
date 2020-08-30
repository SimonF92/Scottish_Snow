from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("Snow_ML_3")
model_trainer.trainModel(num_objects=2, num_experiments=200, enhance_data=True, batch_size=8, show_network_summary=True)