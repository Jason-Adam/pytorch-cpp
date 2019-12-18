# PyTorch C++ Tutorial  
This repo follows along with the PyTorch C++ tutorial [here](https://pytorch.org/tutorials/advanced/cpp_frontend.html).  

The LibTorch distribution is needed for this tutorial. Navigate into your project directory and run the following:  

```bash  
wget https://download.pytorch.org/libtorch/cpu/libtorch-macos-1.3.1.zip  
unzip libtorch-macos-1.3.1.zip
```  

Please note that this is the distribution for MacOS with no CUDA.  

## Running the Program  
The program will run a Convolutional Neural Network on the MNIST data set.  You can download the data set with the following command:  

```bash  
python3 download_mnist.py  
```  

The model training can be run by the following sequence of commands. You should see the epoch output in the terminal after the final command is run.  

```bash  
cd build  
cmake -DCMAKE_PREFIX_PATH=/Users/jasonadam/github/pytorch-cpp/libtorch ..  
make && ./pytorch-cpp  
```  
