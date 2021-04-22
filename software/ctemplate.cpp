#include<bits/stdc++.h>
using namespace std;
#define  vars(...)  "[ "<<#__VA_ARGS__<<" :- "
#define debug(a) cout<<vars(a);\
 helper(a);
\
void helper(vector<int>& a){
	for(auto i : a)
		cout<<i<<" ";
cout<<" ]"<<endl;
}
void helper(string a){
		cout<<a<<" ";
cout<<" ]"<<endl;
}
void helper(float a){
		cout<<a<<" ";
cout<<" ]"<<endl;
}
void helper(long long a){
		cout<<a<<" ";
cout<<" ]"<<endl;
}
void helper(int  a){
		cout<<a<<" ";
cout<<" ]"<<endl;
}

void testcase(){

puts("");
}
int main(){
int t;
cin>>t;
for(int i = 1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		testcase();
}
return 0;
}
