#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> nums)
{
//N마리의 포켓몬 중 N/2 가져가도 됨
//같은 종류의 포켓몬은 같은 번호
    int n = nums.size();
    int max_pick = n / 2;
    
    sort(nums.begin(), nums.end());
    
    int unique_count = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] != nums[i - 1]) {
            unique_count++;
        }
    }
    // 2 2 3 3 3 4
    // 1 2 3 4
    return min(unique_count, max_pick);
}