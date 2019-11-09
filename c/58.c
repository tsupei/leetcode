#include<stdio.h> 


int lengthOfLastWord(char * s){
    int i;
    int size;
    int end;
    size = 0;
    end = 0;
    i = 0;
    while(s[i] != '\0'){
        if(s[i] != ' '){
            if(end == 1){
                size = 0;
                end = 0;
            }
            size++;
        }else{
            end = 1;
        }
        i++;
    }
    return size;
}

int main(){
    int len;
    char* s;
    s = "";
    len = lengthOfLastWord(s);
    printf("%d\n", len);
}

