#include <iostream>
#include <set>

using namespace std;


int UPPER_LIMIT = 28123;


bool is_num_abundant(int num){
	int sum_of_divisors = 1; //1 is a divisor of all numbers
	for (int j=2;j<(num/2)+1;j++){
		if(num%j==0){
			sum_of_divisors+=j;
		}
		if(sum_of_divisors>num){
			return true;
		}
	}
	return false;
}

bool is_num_abundant_sum(int num, set<int> abundants){
	for (auto i:abundants){
		if(i>=num){
			return false;
		}
		int partner = num-i;
		if(abundants.count(partner)==0){
			continue;
		}
		return true;
	}
}

int main(){
	set <int> abundants;
	for (int i=12;i<UPPER_LIMIT;i++){
		if(is_num_abundant(i)){
			abundants.insert(i);
		}
	}
	long long sum = 0;
  for (int i = 0; i < UPPER_LIMIT; i++)
  {
    if(!is_num_abundant_sum(i, abundants))
      sum += i;
  }
  cout << sum << endl;
	return 0;
}
