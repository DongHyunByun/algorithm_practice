#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int euclidean(int a, int b) {
	if (b == 0) {
		return a;
	}
	else {
		return euclidean(b, a%b);
	}
}

int main() {
	int up, down;
	int N1, N2, N3, N4;
	cin >> N1 >> N2 >> N3 >> N4;
	
	up = N1 * N4 + N3 * N2;;
	down = N2 * N4;

	int divider=euclidean(up, down);

	cout << up/divider << " " << down/divider;

	return 0;
}
