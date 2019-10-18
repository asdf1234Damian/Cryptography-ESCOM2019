#include <iostream>
#include <cmath>

unsigned char m[8] = {'D','i','a','m','a','n','t','e'};
unsigned char result[8]={0,0,0,0,0,0,0,0};


unsigned char table[] = {58,50,42,34,26,18,10, 2,
                60,52,44,36,28,20,12, 4,
                62,54,46,38,30,22,14, 6,
                64,56,48,40,32,24,16, 8,
                57,49,41,33,25,17, 9, 1,
                59,51,43,35,27,19,11, 3,
                61,53,45,37,29,21,13, 5,
                63,55,47,39,31,23,15, 7};


int main(int argc, char const *argv[]){
    unsigned char resRow = 0;
    unsigned char resCol = 0;
    for (unsigned char i=0 ; i<sizeof(table);i++){
        unsigned char pos = table[i];
        unsigned char row = floor(pos/8);
        unsigned char col = pos%8;
        unsigned char mask = 128;
        mask = mask>>col-1;
        result[i/8] = result[i/8] | ((m[row] & mask)<<col-1)>>i%8;
    }

    for (unsigned char c: result){
        printf("%x", c);
    }
    
    return 0;
}
