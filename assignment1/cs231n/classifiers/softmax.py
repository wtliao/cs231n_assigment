import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in range(num_train):
        soft_max_score = X[i].dot(W)
#         soft_max_score -=np.max(soft_max_score)
        soft_max_score = np.exp(soft_max_score)
        soft_max_score =soft_max_score/soft_max_score.sum()
        loss += -np.log(soft_max_score[y[i]])
        
        for c in range(W.shape[1]):
            dW[:,c] += (soft_max_score[c]-(y[i] == c))*X[i]
#             if y[i] == c:
#                 dW[:,c] +=(soft_max_score[c]-1)*X[i]
#             else:
#                 dW[:,c] +=soft_max_score[c]*X[i]
        
  loss /= num_train 
  loss += reg*np.sum(W*W)/2
  dW /= num_train
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_train = X.shape[0]
  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = X.dot(W)
  ps = np.exp(scores)/np.exp(scores).sum(axis=1,keepdims=True)
  loss = -np.log(ps[range(y.size), y]).sum()/num_train
  loss += 0.5*reg*np.sum(W*W)
  
  keep_ind = np.zeros_like(ps)
  keep_ind[range(y.size), y] =1.0
  dW += np.dot(X.T, ps-keep_ind)/num_train + reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

