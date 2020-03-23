#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

priority_queue<int, vector<int>, less<int>> maxQ;
priority_queue<int, vector<int>, greater<int>> minQ;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N,num,maxSize=0,minSize=0;
	int maxQtop=1, minQtop=1;
	maxQ.push(-10001);
	minQ.push(10001);
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> num;
		
		// ��ġ�ľ��� ����	
		if (num <= minQ.top()) {
			maxQ.push(num);
		}
		else {
			minQ.push(num);
		}
		
		// ���

		// ��� ��������
		maxSize = maxQ.size();
		minSize = minQ.size();

		if (maxSize == minSize or maxSize == minSize+1) {
			cout << maxQ.top() <<"\n";
		}
		else {
			// 2�̻� max��Ŭ��
			if (maxSize > minSize) {
				minQ.push(maxQ.top());
				maxQ.pop();
			}
			// min�� Ŭ��
			else {
				maxQ.push(minQ.top());
				minQ.pop();
			}
			cout << maxQ.top() << "\n";
		}
	}
}