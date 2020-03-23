#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;


int main() {
	map<string, int> m;
	string s;
	int sum=0;

	while (getline(cin, s)) {
		if (s.size() == 0) {
			break;
		}
		m[s] += 1;
		sum += 1;
	}
	
	for (map<string,int>::iterator it = m.begin(); it != m.end(); it++) {
		double temp = (double(it->second) / sum) * 100;
		cout << it->first;
		printf(" %0.4f\n",temp);
	}
	cout<<m.count("Ash")
	return 0;
}