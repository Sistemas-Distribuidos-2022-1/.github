#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#define PORT 8080
#define MAX 2048

   
int main(int argc, char const *argv[]){
    int sock = 0, valread, i, intlen;
    struct sockaddr_in serv_addr;
    char buffer[MAX] = {0};
    char len[64], len2[64];
    char msg[MAX], numero_quest[10];


    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)    {
        printf("\n Socket creation error \n");
        return -1;
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);       

    if(inet_pton(AF_INET, "127.0.1.1", &serv_addr.sin_addr)<=0)     {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)    {
        printf("\nConnection Failed \n");
        return -1;
    }

    //Escolhe o exercicio

    valread = read(sock, buffer, MAX);
    
    printf("%s\n", buffer);

    int run = 1;
    while(run){

        memset(buffer,0, sizeof buffer);
        memset(len,0, sizeof len);
        memset(len2,0, sizeof len2);
        memset(msg,0, sizeof msg);
        
        fgets(msg, MAX-1, stdin);
        msg[strcspn(msg, "\n")] = 0;
        if (strcmp(msg, "exit") == 0) run = 0;  


        intlen = strlen(msg);
        //printf("len: %d\n",intlen);
        sprintf(len2, "%d", intlen); 
                
        for(i=0; i<(64-(strlen(len2)));i++) len[i] = '0';
       
        
        strcat(len,len2);

        //printf("enviar: %s\n",len);
        send(sock, len, strlen(len), 0);

        //printf("enviar: %s\n",msg);
        send(sock, msg, strlen(msg), 0);

        //printf("escrevendo...\n");
        valread = read(sock, buffer, MAX);
        printf("%s\n", buffer);


        
    }
    

    return 0;
}