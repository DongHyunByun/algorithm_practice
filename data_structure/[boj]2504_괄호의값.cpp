#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
	string word;
	cin >> word;
	char preChar='g';
	int ans=0;

	vector<int> v;

	for (int i = 0; i < word.size(); i++) {
		if (word[i] == '[') {
			v.push_back(3);
			preChar = '[';
		}
		else if (word[i] == '(') {
			v.push_back(2);
			preChar = '(';
		}
		else if (word[i] == ']') {
			// �ȿ��� ������?
			if (find(v.begin(), v.end(), 3) == v.end()) {
				ans = 0;
				break;
			}
			//�ٷδ����Ÿ�
			int num = 1;
			if (preChar == '[') {
				for (int indx = 0; indx < v.size(); indx++) {
					num *= v[indx];
				}
				ans += num;
				v.pop_back();
			}
			else {
				v.pop_back();
			}
			preChar = ']';
		}
		else {
			// �ȿ��� ������?
			if (find(v.begin(), v.end(), 2) == v.end()) {
				ans = 0;
				break;
			}
			//�ٷδ����Ÿ�
			int num = 1;
			if (preChar == '(') {
				for (int indx = 0; indx < v.size(); indx++) {
					num *= v[indx];
				}
				ans += num;
				v.pop_back();
			}
			else {
				v.pop_back();
			}
			preChar = ')';
		}
	}
	// �� �ȴ�����?
	if (v.size() != 0) {
		ans = 0;
	}
	cout << ans;
	return 0;
}