#include <iostream>
using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		ListNode *cur;
		cur = NULL;
	    int length_a = 0;
	    int length_b = 0;
		
		cur = headA;
		while(cur != NULL){
			length_a += 1;
			cur = cur->next;
		}
		cur = headB;
		while(cur != NULL){
			length_b += 1;
			cur = cur->next;
		}

		// Move ptr
		ListNode *ptr1, *ptr2;
		ptr1 = headA;
		ptr2 = headB;
		if(length_a < length_b){
			// Move ptr2 forward
			int cnt = length_b - length_a;
			while(cnt != 0){
				ptr2 = ptr2->next;
				cnt--;
			}	
		}else{
			// Move ptr1 forward
			int cnt = length_a - length_b;
			while(cnt != 0){
				ptr1 = ptr1->next;
				cnt--;
			}
		}
		// Find max joint list
		int length = 0;
		ListNode *joint_head;
		while(ptr1 && ptr2){
				if(ptr1 == ptr2){
						if(length == 0){
								joint_head = ptr1;
						}
						length++;
				}else{
						joint_head = NULL;
						length = 0;
				}
				ptr1 = ptr1->next;
				ptr2 = ptr2->next;
		}
		return joint_head;
    }
};

