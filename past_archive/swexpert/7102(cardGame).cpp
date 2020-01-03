#include <iostream>

using namespace std;

int main() {
	int t;
	int N, M,temp; 
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> N >> M;
		if (M > N) {
			temp = N;
			N = M;
			M = temp;
		}
		cout << "#" << i + 1<<" ";
		for (int j = 1 + M;j <= 1 + N;j++) {
			cout << j << " ";
		}
		cout << endl;
	}
}