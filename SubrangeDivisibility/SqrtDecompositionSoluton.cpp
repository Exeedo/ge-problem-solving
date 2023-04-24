// Time Complexity: O(n) precalculation + O(sqrt(n)) per query -> O(n + q*sqrt(n))
// Additional Memory: O(n)

#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    int N = s.length();
    int block_size = sqrt(N);
    int block_number = (N + block_size - 1) / block_size; // another way to calculate the ceiling of the division
    vector<int> blocks(block_number, 0);
    for (int i = 0; i < N; i++)
        blocks[i / block_size] += s[i] - '0';
    int Q;
    cin >> Q;
    while (Q--) {
        int L, R;
        cin >> L >> R;
        int i = L;
        int sum = 0;
        while (i <= R) {
            if (i % block_size == 0 && i + block_size - 1 <= R) {
                sum += blocks[i / block_size];
                i += block_size;
            } else {
                sum += s[i] - '0';
                i++;
            }
        }
        printf((sum % 3 == 0) ? "YES\n" : "NO\n");
    }

    return 0;
}
