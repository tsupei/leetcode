#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head){
	struct ListNode *L1, *L2, *p1, *p2, *cur, *tmp;
	int i = 0;
	if(!head){
		return NULL;
	}
	L1 = head;
	L2 = head->next;
	p1 = head;
	p2 = head->next;

	if(!L2){
		return head;
	}
	cur = L2->next;

	while(cur){
		// printf("cur: %d\n", cur->val);
		if(i%2 == 0){
			p1->next = cur;
			p1 = p1->next;
		}else{
			p2->next = cur;
			p2 = p2->next;
		}
		cur = cur->next;
		i++;
	}
	p1->next = NULL;
	p2->next = NULL;
	
	head = L2;
	p1 = L1;
	p2 = L2;
	while(p1 && p2){
		tmp = p2->next;
		p2->next = p1;
		p2 = tmp;

		tmp = p1->next;
		if(p2){
			p1->next = p2;
		}
		p1 = tmp;
	}
	return L2;
}


int main(){
	struct ListNode *n1, *n2, *n3, *n4;
	struct ListNode *cur, *ans;

	n1 = malloc(sizeof(struct ListNode* ));
	n2 = malloc(sizeof(struct ListNode* ));
	n3 = malloc(sizeof(struct ListNode* ));
	n4 = malloc(sizeof(struct ListNode* ));

	n1->val = 1;
	n2->val = 2;
	n3->val = 3;
	n4->val = 4;
	n1->next = NULL;
	n2->next = n3;
	n3->next = NULL;
	n4->next = NULL;
	ans = swapPairs(n1);
	cur = ans;
	while(cur){
		printf("%d\n", cur->val);
		cur = cur->next;
	}
	return 0;
}









