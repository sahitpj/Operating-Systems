# Assignment - 2

Answers can be viewd by cloning the following gist

```console
git clone https://gist.github.com/sahitpj/7157c7a37cd95238ce38a0a8d89eaf2b
```

### Question 1
The following question has been dome in an Jupyter Notebook, however individual files are located in the [gist](https://gist.github.com/sahitpj/7157c7a37cd95238ce38a0a8d89eaf2b) too

In order to test simply run the test.py file

```console
python test.py
```

### Question 2

Given the following information
 
- 6 bit virtual space
- 16bytes pages/ frames, this implies the offset is 4 bits and the rest 2bits are for converting from VPN to PFN

And we have the following mappsings

- (0,9)
- (1,1)
- (2,6)
- (3,8)

    a) 22 which is 010110

    VPN = 1 this is maps to PFN = 1
    offset = 0110
    physical address = 00010110

    b) 62 which is 111110
    VPN = 3 this maps to PFN = 8
    offset = 1110
    physical address = 10001110

    c) virtual address 109 does cannot exist in a 6bit virtual space, as it exceeds it, results in error

### Question 3

Memory usage of the CPU increases as more and more memory is touched.
This then halts, when the program is halted, as expected
For large values of memory however, after a certain point the memory is freed up

The c program for this question is in the [gist](https://gist.github.com/sahitpj/7157c7a37cd95238ce38a0a8d89eaf2b)
vmstats mac verison can be run using the vmstat.sh file in the gist, run by simply typing

```console
bash vmstat.sh
```
