#include <iostream>
#include <algorithm>

using namespace std;

int L[100000];

int main() {
	int N, S;
	cin >> N >> S;
	for (int i = 0; i < N; i++) {
		cin >> L[i];
	}
	int r=0, l=0;
	int sum = L[0];
	int ans=100000;

	while (l<=r and r<N) {
		if (sum < S) {
			r++;
			sum += L[r];
		}
		else if (sum == S) {
			ans = min(ans, (r - l + 1));
			r++;
			sum += L[r];
		}
		else {
			ans = min(ans, (r - l + 1));
			sum -= L[l];
			l++;
		}
	}

	if (ans == 100000) {
		cout << 0;
	}
	else {
		cout << ans;
	}
	return 0;
}