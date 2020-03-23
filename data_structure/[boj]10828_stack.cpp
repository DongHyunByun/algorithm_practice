#include <iostream>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;
int L[10000];

int main() {
	int N;
	string com;
	int input;
	cin >> N;
	stack<int> s;

	for (int i = 0; i < N; i++) {
		cin >> com;
		if (com == "push") {
			cin >> input;
			s.push(input);
		}
		else if (com == "pop") {
			if (!s.empty()) {
				cout << s.top()<<endl;
				s.pop();
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (com == "size") {
			cout << s.size() << endl;
		}
		else if (com == "empty") {
			cout << s.empty() << endl;
		}
		else {
			if (!s.empty()) {
				cout << s.top() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
	}
	return 0;
}