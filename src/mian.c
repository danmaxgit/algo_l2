#include "stdio.h"
#include "stdlib.h"
#include "float.h"

struct Node { 
    int value;
    struct Node* next;
};

typedef struct {
    struct Node* head;
} LList;

void append(LList* l, int v){
    struct Node* i = l->head;
    if(!i){
        i = (struct Node *)malloc(sizeof(struct Node));
        i->value = v;
        i->next = NULL;
        l->head = i;
        return;
    }
    while (i->next) {
        i = i->next;
    }
    struct Node* temp = (struct Node *)malloc(sizeof(struct Node));
    temp->value = v;
    temp->next = NULL;
    i->next = temp;
}
void free_list(LList* l){
    struct Node* head = l->head;
    struct Node* temp;
    while (head->next) {
        temp = head->next;
        free(head);
        head = temp;
    }
    free(head);
}
void print(LList *l){
    struct Node* i = l->head;
    while (i->next) {
        printf("%d ", i->value);
        i = i->next;
    }
    printf("%d\n", i->value);
}

void delete(LList* l, int v){
    struct Node* i = l->head;
    struct Node* temp = NULL;
    while (i->next) {
        if (i->value == v) {
            break;
        }
        temp = i;
        i = i->next;
    }
    if(temp == NULL){
        temp = l->head->next;
        free(l->head);
        l->head = temp;
        return;
    }
    temp->next = i->next;
    free(i);
}

float mean(LList* l){
    struct Node* i = l->head;
    float res = 0;
    int size = 0;
    while (i->next) {
        res += (float) i->value;
        size++;
        i = i->next;
    }
    res += (float) i->value;
    size++;
    return res / (float) size;
}

float func(LList* l){
    struct Node* i = l->head;
    float m = mean(l);
    float temp;
    float min = FLT_MAX;
    while (i->next) {
        temp = (float)i->value - m;
        temp = (temp < 0) ? temp * -1 : temp;
        if (min > temp) {
            min = temp;
        }
        i = i->next;
    }
    temp = (float)i->value - m;
    temp = (temp < 0) ? temp * -1 : temp;
    if (min > temp) {
        min = temp;
    }
    return min;
}

int main(int argc, char** argv){
    LList* l = (LList *)malloc(sizeof(LList)); 
    append(l, 1);
    append(l, 2);
    append(l, 3);
    append(l, 4);
    print(l);
    float m = mean(l);
    printf("%f\n", m);
    float f = func(l);
    printf("%f\n", f);
    free_list(l);
    return 0;
}