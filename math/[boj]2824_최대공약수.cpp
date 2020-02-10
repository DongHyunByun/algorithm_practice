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

	// ���� A�Է�
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arrA[i];
	}

	// ���� B�� �Է¹����� A�� ��
	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> arrB[i];
		for (int indx = 0; indx < N; indx++) {
			// ���̻� B���� ����� ���� �� �����Ƿ� break
			if (arrB[i] == 1) {
				break;
			}
			// A���� ����� ���� �� �����Ƿ� ���� ����� continue
			if (arrA[indx] == 1) {
				continue;
			}
			d = euclid(arrB[i], arrA[indx]);

			ans *= d;

			// A�� B���� ���� d�� ������
			arrA[indx] /= d;
			arrB[i] /= d;

			// ans�� �޸��̻����� Ŀ���°��� �������� �ڿ� 9�ڸ��� ����ؼ� ���� (ans�� �ٲ����� �ڿ� 9�ڸ��� ����ؼ� �Ȱ���)
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