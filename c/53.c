#include <stdio.h>
#include <stdlib.h>

int pm(int* nums, int numsSize){
	int i;
	for(i=0; i<numsSize; i++){
		printf("%d\n", nums[i]);
	}
	printf("\n");
	return 0;
}

int maxSubArray(int* nums, int numsSize){
	int maxValue;
	int curSum;
	int i;
	maxValue = nums[0];
	curSum = nums[0];
	for(i=1; i<numsSize; i++){
		if(curSum + nums[i] > nums[i]){
			curSum = curSum + nums[i];
		}else{
			curSum = nums[i];
		}
		maxValue = (curSum > maxValue) ? curSum: maxValue;
	}
	return maxValue;
}
int main(){
	int numsSize;
	numsSize = 2;
	int nums[2] = {1,2};
	printf("%d\n",maxSubArray(nums, numsSize));
	return 0;
}

