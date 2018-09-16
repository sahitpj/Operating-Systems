# Assignment - 2

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

    c) virtual address 109 does cannot exist in a 6bit virtual space, hence a segmentation error

### Question 3

Memory usage of the CPU increases as more and more memory is touched.

This then halts, when the program is halted, as expected

for large values of memory however, after a certain point the memory is freed up
