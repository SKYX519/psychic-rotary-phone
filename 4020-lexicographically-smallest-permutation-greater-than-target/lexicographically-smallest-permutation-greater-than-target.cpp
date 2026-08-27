class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        vector<int> cnt(26, 0);

        for (char c : s) {
            cnt[c - 'a']++;
        }

        int n = s.size();

        // Try to make the answer greater at some position.
        // We go from right to left because we want the
        // lexicographically smallest possible answer.
        for (int i = n - 1; i >= 0; i--) {
            vector<int> temp = cnt;

            // Match target[0 ... i-1]
            bool possible = true;

            for (int j = 0; j < i; j++) {
                int x = target[j] - 'a';

                if (temp[x] == 0) {
                    possible = false;
                    break;
                }

                temp[x]--;
            }

            if (!possible)
                continue;

            // At position i, choose the smallest character
            // strictly greater than target[i].
            int x = target[i] - 'a';

            for (int c = x + 1; c < 26; c++) {
                if (temp[c] > 0) {
                    string ans = target.substr(0, i);
                    ans += char('a' + c);

                    temp[c]--;

                    // Put remaining characters in sorted order.
                    for (int j = 0; j < 26; j++) {
                        while (temp[j] > 0) {
                            ans += char('a' + j);
                            temp[j]--;
                        }
                    }

                    return ans;
                }
            }
        }

        return "";
    }
};