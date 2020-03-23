#include <iostream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int K;
		cin >> K;
		int temp;
		stack<int> s;
		int ans = 0;
		int stackTemp;
		for (int i = 0; i < K; i++) {
			cin >> temp;
			if (temp == 0) {
				stackTemp = s.top(); s.pop();
				ans -= stackTemp;
			}
			else {
				s.push(temp);
				ans += temp;
			}
		}
		cout << "#" << t + 1 << " " << ans << endl;
	}
	return 0;
}