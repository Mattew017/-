#include <iostream>

struct Node {
    int number;
    Node *next;
    
    Node(int n, Node* t) {
        number = n;
        next = t;
    }
};


void show_list(Node* root) 
{
    Node* x = root;
    do {
        std::cout << x->number << " ";
        x = x->next;
    } while (x != root);
    std::cout << std::endl;
};

int main()
{
    int N, M;
    std::cout << "Input N and M:" << std::endl;
    std::cin >> N >> M;
    Node* root = new Node(1, nullptr);
    root->next= root;  //1-ый элемент указывает на самого себя
    Node* x = root;
    for (int i = 2; i <= N; i++) {
        x = (x->next = new Node(i, root));
    };
    x = root;
    show_list(x);
    
    while (x->next != x) //пока x не указывет на самого себя(т.е. остался 1 элемент)
    {
        for (int i = 2; i < M; i++)  //переходим к элементу m - 1
            x = x->next;
        Node* killed = x->next; // m -ый элемент
        x->next = (x->next)->next; //удаляем m -ый элемент из списка, m-1 указывает на m+1
        x = x->next;  //переходим к элементу m + 1
        delete killed; //очистка памяти
    }
    
    std::cout << x->number << std::endl;
    return 0;
}
