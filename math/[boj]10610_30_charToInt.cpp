#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	string N;
	cin >> N;
	
	bool isInZero=false;
	int sum=0;

	//3의 배수 and 10의배수 ?
	for (int i = 0; i < N.size(); i++) {
		int temp = (N[i] - '0');
		sum += temp;
		if (!temp) {
			isInZero = true;
		}
	}

	if (sum % 3 != 0 or not isInZero) {
		cout << -1;
	}
	else {
		sort(N.begin(), N.end(),greater<char>());
		cout << N << endl;
	}
	return 0;
}
