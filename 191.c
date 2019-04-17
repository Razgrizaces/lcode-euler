int hammingWeight(uint32_t n) {
    int output = 0;
    uint32_t prevN = 0;
    uint32_t and = 0xFFFFFFFF; //all 1
    while(and != 0)
    {
        prevN = n;
        n = n&and;
        if(n != prevN)
            output +=1;
        and = and >> 1;
        printf("%x\n", n);
    }
    if(n==1)
        output = output+1;
    return output;
}