import numpy as np
class Linear:
    def __init__(self,dimension,alpha,param_init = None):
        if param_init:
            self.param = param_init
        else:
            self.param = np.zeros(dimension + 1)
        self.dimension = dimension + 1 #+1 for the constant term/bias term
        self.alpha = alpha
    # def logistic(self, x):
    #     """x is just a scalar here"""
    #     return 1/(1+np.exp(-x))
    # def grad_logistic(self,x):
    #     return np.exp(x)/((1+np.exp(x))**2)
    def get_val(self, feature_vector):
        # x is assumed to be a list of size self.dimension - 1 
        feature_vector = np.array([1]+feature_vector)
        return feature_vector.dot(self.param)
    def upd_param(self, est_val, feature_vector):
        feature_vector = np.array([1]+feature_vector)
        # print(feature_vector)
        arg = feature_vector.dot(self.param)
        delta_param = self.alpha*(est_val-arg)*feature_vector
        self.param += delta_param
        return 
    