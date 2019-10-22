#include <iostream>
#include <cmath>


unsigned char resulta[8]={0,0,0,0,0,0,0,0};
unsigned char resultb[8]={0,0,0,0,0,0,0,0};

unsigned char table[] = {58,50,42,34,26,18,10, 2,
                60,52,44,36,28,20,12, 4,
                62,54,46,38,30,22,14, 6,
                64,56,48,40,32,24,16, 8,
                57,49,41,33,25,17, 9, 1,
                59,51,43,35,27,19,11, 3,
                61,53,45,37,29,21,13, 5,
                63,55,47,39,31,23,15, 7};

unsigned char tabla[] = {40, 8,48,16,56,24,64,32,
                39, 7,47,15,55,23,63,31,
                38, 6,46,14,54,22,62,30,
                37, 5,45,13,53,21,61,29,
                36, 4,44,12,52,20,60,28,
                35, 3,43,11,51,19,59,27,
                34, 2,42,10,50,18,58,26,
                33, 1,41, 9,49,17,57,25};


int main(int argc, char const *argv[]){
    
    unsigned char offset;
    do{
        std::cout <<"Select mode \n";
        std::cout <<"0 = IP \n";
        std::cout <<"1 = IP^⁻1 \n";
        std::cout <<"mode : ";
        std::cin >> offset;
    } while (offset >= 50);
    

    if(offset == 49){
        offset = 64;
    }else{
        offset = 0;
    }

    std::string message;
    do{
        std::cout <<"Message must be 8 characters long\n";
        std::cout <<"m : ";
        std::cin >> message;
    } while (message.length() != 8 );
    
    for (unsigned char i = 0 ; i<64;i++){
        unsigned char pos = table[i+offset] - 1;
        unsigned char col = pos%8;
        unsigned char row = pos>>3;
        unsigned char mask = 128;
        mask = mask >> col;
        resulta[i/8] = resulta[i/8] | ((message[row] & mask)<< col) >> i%8;
    }
    

    if(offset == 64){
        std::cout<<"IP^-1 in char\n";
    }else{
        std::cout<<"IP in char\n";
    }
    for (unsigned char c: resulta){
        printf("%c", c);
    }
    std::cout<<std::endl;
    if(offset == 64){
        std::cout<<"IP^-1 in hex\n";
    }else{
        std::cout<<"IP in hex\n";
    }
    for (unsigned char c: resulta){
        printf("%x", c);
        c = 0;
    }
    std::cout<<std::endl;
    
    return 0;
}
