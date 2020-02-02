#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N, recSize;

int main() {
	cin >> N;
	cin >> recSize;
	vector<vector<int>> frame;
	int temp;
	bool isin;
	for (int c = 0; c < recSize; c++) {
		cin >> temp;
		isin = false;
		for (int i = 0; i < frame.size(); i++) {
			//�������� �ִٸ�
			if (temp == frame[i][2]) {
				frame[i][0]++;
				isin = true;
				break;
			}
		}
		if (!isin) {
			// ��������� �׳� �߰�
			if (frame.size() != N) {
				frame.push_back({ 1,c,temp });
			}
			// ���������� ����� �߰�
			else {
				frame.erase(frame.begin());
				frame.push_back({ 1,c,temp });
			}
		}
		sort(frame.begin(), frame.end());
	}
	vector<int> ans;
	for (int i = 0; i < N; i++) {
		ans.push_back(frame[i][2]);
	}
	sort(ans.begin(), ans.end());
	for (int i = 0; i < N; i++) {
		cout << ans[i] << " ";
	}
}