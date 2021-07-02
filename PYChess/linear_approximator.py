import numpy as np
class Linear:
    def __init__(self,dimension,alpha,param_init = None):
        if param_init:
            self.param = param_init
        else:
            self.param = np.zeros(dimension + 1)
        self.dimension = dimension + 1 #+1 for the constant term/bias term
        self.alpha = alpha
    def tanh(self, x):
        return np.tanh(x)

    def tanh_deriv(self, x):
        return 1.0 - np.tanh(x)**2

    def logistic(self, x):
        return 1/(1 + np.exp(-x))

    def logistic_derivative(self, x):
        return self.logistic(x)*(1-self.logistic(x))

    def linear(self, x):
        return x
    
    def linear_derivative(self, x):
        return 1

    def get_val(self, feature_vector):
        # x is assumed to be a list of size self.dimension - 1 
        feature_vector = np.array([1]+feature_vector)
        return self.tanh(feature_vector.dot(self.param))

    def upd_param(self, est_val, feature_vector):
        feature_vector = np.array([1]+feature_vector)
        # print(feature_vector)
        arg = feature_vector.dot(self.param)
        delta_param = self.alpha*(est_val- self.tanh(arg))*self.tanh_deriv(arg)*feature_vector
        self.param += delta_param
        return 
