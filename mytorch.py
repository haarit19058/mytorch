# author d0lph1n


import numpy as np 


class tensor:
    def __init__(self,data):
        self.data = np.array(data);
        self.grad = np.zeros_like(self.data,dtype=np.float64)


        return

    def test():
        print("hi there")
        return


if __name__ == "__main__":
    tensor.test()
