#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int arrA[1001];
int arrB[1001];

int euclid(int a, int b) {
	int temp;
	while (1) {
		if (b == 0) {
			return a;
		}
		else {
			temp = b;
			b = a % b;
			a = temp;
		}
	}
}

int main() {
	int N, M;
	long long ans=1;
	int d;
	int mod = 1000000000;

	// 숫자 A입력
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arrA[i];
	}

	// 숫자 B를 입력받으며 A와 비교
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> arrB[i];
		for (int indx = 0; indx < N; indx++) {
			// 더이상 B에서 약수를 뽑을 수 없으므로 break
			if (arrB[i] == 1) {
				break;
			}
			// A에서 약수를 뽑을 수 없으므로 다음 약수로 continue
			if (arrA[indx] == 1) {
				continue;
			}
			d = euclid(arrB[i], arrA[indx]);

			ans *= d;

			// A와 B에서 뽑은 d를 나눠줌
			arrA[indx] /= d;
			arrB[i] /= d;

			// ans가 메모리이상으로 커지는것을 막기위해 뒤에 9자리만 계속해서 보존 (ans가 바뀌지만 뒤에 9자리는 계속해서 똑같다)
			if (ans > mod) {
				ans = ans % mod + mod;
			}
		}
	}

	string ansS = to_string(ans);
	if (ans > mod) {
		cout << ansS.substr(1, 9);
	}
	else {
		cout << ansS;
	}

	return 0;
}