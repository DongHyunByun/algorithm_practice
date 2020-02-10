#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;

	long long int temp;
	long long int a = 0;
	long long int b = 1;


	if (N == 1) {
		cout << 1;
	}
	else {
		for (int i = 0; i < N-1; i++) {
			temp = b;
			b = a + b;
			a = temp;
		}
		cout << b << endl;
	}
	return 0;
}