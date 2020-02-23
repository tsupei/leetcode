#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	int binary_search(vector<int>& numbers, int target, int start_index, int end_index){
		if(start_index == end_index) return -1;
		int mid = (start_index + end_index) / 2;
		if(numbers[mid] == target){
				return mid;
		}else if(numbers[mid] < target){
				return this->binary_search(numbers, target, mid+1, end_index);
		}else{
				return this->binary_search(numbers, target, start_index, mid);
		}
	}
    vector<int> twoSum(vector<int>& numbers, int target) {
			int len = numbers.size();
			vector<int> ans(2, -1);
			int index;
			for(int i=0; i<len; i++){
				index = this->binary_search(numbers, target-numbers[i], i+1, len);	
				if(index != -1){
						ans[0] = i+1;
						ans[1] = index+1;
						return ans; 
				}
			}	
			return ans;	
    }
};

int main(){
		Solution sol;
		vector<int> numbers;
		// initialize all values
		numbers.push_back(2);
		numbers.push_back(7);
		numbers.push_back(11);
		numbers.push_back(15);

		vector<int> ans;
		int target = 9;
		ans = sol.twoSum(numbers, target);
		cout << ans[0] << ans[1] << endl;
		return 0;
}

