import numpy as np
class Linear:
    def __init__(self,dimension,alpha):
        self.param = np.zeros(dimension + 1)
        self.dimension = dimension + 1 #+1 for the constant term
        self.alpha = alpha
    def logistic(self, x):
        """x is just a scalar here"""
        return 1/(1+np.exp(-x))
    def grad_logistic(self,x):
        np.exp(x)/((1+np.exp(x))**2)
    def get_val(self, feature_vector):
        # x is assumed to be a list of size self.dimension - 1 
        # print(len(feature_vector),"feature_vec")
        feature_vector = np.array([1]+feature_vector)
        # print(feature_vector,"feature_vec")
        # print(self.param,"param")
        return self.logistic(feature_vector.dot(self.param))
    def upd_param(self, est_val, feature_vector):
        feature_vector = np.array([1]+feature_vector)
        arg = feature_vector.dot(self.param)
        delta_param = self.param + self.alpha*(est_val-self.logistic(arg))*feature_vector*self.grad_logistic(arg)
        self.param += delta_param
    

    