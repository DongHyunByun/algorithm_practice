#include <iostream>
#include <algorithm>

using namespace std;
int arr[1001];

int main() {
	int N, K;
	cin >> N >> K;
	int num=0;
	for (int i = 2; i <= N; i++) {
		if (arr[i] == 0) {
			for (int j = i; j <= N; j += i) {
				if (arr[j] == 0) {
					arr[j]++;
					num++;
				}
				if (num == K) {
					cout << j;
					return 0;
				}
			}
		}
	}
}
