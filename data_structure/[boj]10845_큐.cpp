#include <iostream>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int num;
	string word;
	int input;
	cin >> num;
	queue<int> q;
	for (int i = 0; i < num; i++) {
		cin >> word;
		if (word == "push") {
			cin >> input;
			q.push(input);
		}
		else if (word == "pop") {
			if (!q.empty()) {
				cout << q.front() << endl;
				q.pop();
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (word == "size") {
			cout << q.size() << endl;
		}
		else if (word == "empty") {
			cout << q.empty() << endl;
		}
		else if (word == "front") {
			if (!q.empty()) {
				cout << q.front() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
		else {
			if (!q.empty()) {
				cout << q.back() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
	}
	return 0;
}