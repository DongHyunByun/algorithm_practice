#include <iostream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int dp[1001][1001];

int main() {
	string A, B;
	cin >> A >> B;
	int sizeA = A.size();
	int sizeB = B.size();

	for (int i = 1; i <= sizeA; i++) {
		for (int j = 1; j <= sizeB; j++) {
			//������ (���������� +1)
			if (A[i - 1] == B[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			//�ٸ��� max(��,�Ʒ�)
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}
	
	int ansL;
	string ansS="";
	int i = sizeA;
	int j = sizeB;

	// �ڿ������� Ž�� 
	while (dp[i][j] != 0) {
		if (A[i - 1] == B[j - 1]) {
			ansS = A[i - 1] + ansS;
			i -= 1;
			j -= 1;
		}
		else {
			if (dp[i - 1][j] < dp[i][j - 1]) {
				j -= 1;
			}
			else {
				i -= 1;
			}
		}
	}
	cout << ansS.size() << endl;
	cout << ansS;


	return 0;
}