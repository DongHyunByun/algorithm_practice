#include <iostream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int snack[1000];



int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, M;
		cin >> N >> M;
		int ans = -1;
		int temp;
		for (int i = 0; i < N; i++) {
			cin >> snack[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i != j) {
					temp = snack[i] + snack[j];
					if (temp <= M and ans < temp) {
						ans = temp;
					}
				}
			}
		}
		cout << "#" << t + 1 << " " << ans<<endl;
	}

}