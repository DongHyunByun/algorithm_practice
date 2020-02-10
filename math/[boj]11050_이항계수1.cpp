#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int fac(int a, int b) {
	int n = 1;
	for (int i = a; i <= b; i++) {
		n *= i;
	}
	return n;
}

int main() {
	
	int N, K;

	cin >> N >> K;
	cout<<fac(N - K + 1, N) / fac(1, K);

	return 0;
}