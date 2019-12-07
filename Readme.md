Name: Zhiyuan Ning 
USC ID: 1808644153
Class: Jack Furray ITP125

Method: In the brute force password crack file, I use two functions to solve the problem. The passwordCrack function to list the possible password. The multiprocessing_func() function to give the output and connect with the multiprocessing. In this file except of listing the passwords one by one in the characterlist made by my self, I create the multi processor core though multithreading package of Python. Seperate the threading to each of the password could have one threading that they could run parrallely.

Platform: The Python code is running on the linux Viterbi Student Virtual machine. It is where I do the programming with python and C++. I have not tried the code on Windows or other system and running shell. Because the Virtual Machine does not fully used the CPU, the time is relative slow.

Results: The first password Z costs 0.000247s
         The second password AD costs 0.017s
         The third password God costs 0.532s
         The fourth password 1234 costs 32.438s
         The fifth password AbCdE costs 679.859s
         The sixth password Trojans costs 40576.342s
         I have not cracked the seventh pasword F1ghtOn. The estimated cost should be 1.5*10^6
         I have not cracked the seventh pasword F1ghtOn. The estimated cost should be 3.5*10^8
         
Result Analysis: The result is affected largely by the length. Because if it is single threaded then the estimate average time complexity to crack n length of the password should be teta(64^n) as there are 64 characters in my characterBase. However, with the multithreaded CPU method the result is hard to estimate because I don't know how each thread performance and what's the relationship of the calculation time between 8 multithreaded process with single threaded process. But the time reduction should be more than linearly. Therefore, it is hard for me to do the time cost estimation. Except the length, the permutation of the character sequence is also a important factor. For instance, AAAA password costs less time than Z8!d in my character base sequence. Also the Computer you are running affect the result, the stronger the CPU, the better the result is.

Improvement: I add the comment in the code of using the GPU to calculate the result, which is the line 4 and line 7. I comment it because I do not have an Anaconda platform to run the packet. If anyone have an Anaconda platform, he/she could uncomment the code and run with the GPU. The result will be significantly better with calculation of GPU.

I use the concept of :  https://www.geeksforgeeks.org/running-python-script-on-gpu/
                        https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba
                        
                       
