#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
typedef struct Node {
    char str[26];
    struct Node* next;
} Node;
Node* createNode(const char* str) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(1);
    }
    strcpy(newNode->str, str);
    newNode->next = NULL;
    return newNode;
}
void appendNode(Node** head, Node** tail, const char* str) {
    Node* newNode = createNode(str);
    if (*head == NULL) {
        *head = *tail = newNode;
    } else {
        (*tail)->next = newNode;
        *tail = newNode;
    }
}
Node* getNodeAt(Node* head, int pos) {
    Node* current = head;
    for (int i = 0; i < pos && current != NULL; i++) {
        current = current->next;
    }
    return current;
}
void addNodeToNewList(Node** newHead, Node** newTail, Node* nodeToAdd) {
    if (nodeToAdd == NULL) return;
   
    nodeToAdd->next = NULL;
   
    if (*newHead == NULL) {
        *newHead = *newTail = nodeToAdd;
    } else {
        (*newTail)->next = nodeToAdd;
        *newTail = nodeToAdd;
    }
}
void interleaveList(Node** head) {
    if (*head == NULL) return;
   
    Node* groupStart = *head;
    Node* newHead = NULL;
    Node* newTail = NULL;
   
    while (groupStart != NULL) {
        Node* X = groupStart;
        Node* Y = getNodeAt(groupStart, 10);
        Node* nextGroupStart = getNodeAt(groupStart, 20);
       
        for (int i = 0; i < 10; i++) {
            if (X != NULL) {
                Node* nextX = X->next;
                addNodeToNewList(&newHead, &newTail, X);
                X = nextX;
            }
            if (Y != NULL) {
                Node* nextY = Y->next;
                addNodeToNewList(&newHead, &newTail, Y);
                Y = nextY;
            }
        }
        groupStart = nextGroupStart;
    }
   
    *head = newHead;
}
void printList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%s\n", current->str);
        current = current->next;
    }
}
void freeList(Node* head) {
    Node* current = head;
    while (current != NULL) {
        Node* next = current->next;
        free(current);
        current = next;
    }
}
int main() {
    int N;
    scanf("%d", &N);
    getchar();
   
    Node* head = NULL;
    Node* tail = NULL;
    for (int i = 0; i < N; i++) {
        char buffer[26];
        if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
            buffer[strcspn(buffer, "\n")] = '\0';
            appendNode(&head, &tail, buffer);
        }
    }
    interleaveList(&head);
   
    printf("Result:\n");
    printList(head);
    freeList(head);
   
    return 0;
}

