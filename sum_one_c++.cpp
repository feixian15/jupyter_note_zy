#include <iostream>
#include <vector>
#include <string>
using namespace std;

//改进方法一：
//class Solution{
//public:
//    vector<int> plusOne(vector<int>& digits){
//        int number = digits.size()-1;
//        bool is_insert = true;
//        while (number>=0)
//        {
//            if (digits[number]==9){
//                digits[number] = 0;
//            }
//            else{
//                digits[number] += 1;
//                is_insert = false;
//            }
//            number--;
//        }
//
//        if(is_insert)
//        {
//            digits.insert(digits.begin(),1);
//        }
//        return digits;
//    }
//};

//别人写的版本
//class Solution {
//public:
//    vector<int> plusOne(vector<int>& digits) {
//        int i = digits.size() - 1;
//        digits[i] += 1;
//        while (i >= 0) {
//            if (digits[i] >= 10) {
//                if (i - 1 >= 0) {
//                    digits[i] = 0;
//                    digits[i - 1] += 1;
//                } else {
//                    digits[i] = 0;
//                    digits.insert(digits.begin(),1);
//                }
//            }
//            i--;
//        }
//
//        return digits;
//    }
//};

class Solution{
public:
    vector<int> plusOne(vector<int>& digits){
        string my_string;

        for (vector<int>::iterator iter = digits.begin(); iter!=digits.end(); iter++){
            my_string.append(to_string(*iter));
        }
        int temp = stoi(my_string) + 1 ;
        string temp1 = to_string(temp);

        vector<int> result;
        char temp_char;
        for (int i=0; i< temp1.size();i++){
            temp_char = temp1[i];
            result.push_back(atoi(&temp_char));
        }
        return result;
    }
};

int main(){

    vector<int> my_vec = {9};
    Solution solution;
    vector<int> result = solution.plusOne(my_vec);
    for (int i=0; i< result.size(); i++){
        cout << result[i] << endl;
    }
}
