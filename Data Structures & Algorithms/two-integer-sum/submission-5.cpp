class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> a;
     
        for (int i = 0; i < (int)nums.size(); i++) {
            a.push_back({nums[i], i});
        }

        sort(a.begin(), a.end()); 

        int l = 0, r = (int)a.size() - 1;
        
        while (l < r) {
            int cur = a[l].first + a[r].first;
            if (cur == target) {
                return {min(a[l].second, a[r].second),
                        max(a[l].second, a[r].second)};
            } else if (cur < target) {
                l++;
            } else {
                r--;
            }
        }        
    }
};
