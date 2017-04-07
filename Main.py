import tensorflow as tf
from multiGPU_Framework import get_cpu_variable, get_cpu_variable_shape, multiGPU_Framework

def loss_prediction_function():
    '''
    :param : None
    :return: loss, prediction
    
    Note :
            1 .use get_cpu_variable instead of tf.Variable
            OR get_cpu_variable_shape to specify shape(In case 
            initializer doesnt accept shape as argument)

            2. Add Loss to collection
            Use tf.add_to_collection('losses', loss)
    '''
    #Placeholder
    '''
      Calculate Prediction and Loss
    '''
    tf.add_to_collection('losses', loss)
    return loss, predictions

mgf = multiGPU_Framework(loss_prediction_function= loss_prediction_function)
mgf.train_model(num_epochs=1000, learning_rate=0.001, batches= data_reader.batches)
