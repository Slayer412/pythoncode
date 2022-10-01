#include<bits/stdc++.h>
using namespace std;
stack<int> stk;
void push(int x){
    stk.push(x);
}
void pop(){
    stk.pop();
}
int main(){
    int n;cin>>n;
    while(n--){
        int x,y;
        if(x==1){
            push(y);
        }
        else{
            pop();
        }
    }

}
