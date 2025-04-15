#include <string>
#include <cassert>
#include <algorithm>

std::string reverse_words(const std::string &str) {
    std::string output;
    std::string partial;

    for (char c : str) {
        if (std::isalnum(c)) {
            partial += c;
        }
        else {
            reverse(partial.begin(), partial.end());
            output += partial + c;
            partial = "";
        }
    }
    reverse(partial.begin(), partial.end());
    output += partial;
    return output;
}

int main() {
    // test case given in assignment
    std::string test_str_1 = "String; 2be reversed...";
    std::string test_str_1_ans = "gnirtS; eb2 desrever...";
    // test case for null
    std::string test_str_2 = "";
    std::string test_str_2_ans = "";
    // test case for input ending in alphanumeric character
    std::string test_str_3 = "The quick brown fox";
    std::string test_str_3_ans = "ehT kciuq nworb xof";
    //test case with singular letters
    std::string test_str_4 = "T.h.e.e.n.d";
    std::string test_str_4_ans = "T.h.e.e.n.d";

    assert(reverse_words(test_str_1) == test_str_1_ans);
    assert(reverse_words(test_str_2) == test_str_2_ans);
    assert(reverse_words(test_str_3) == test_str_3_ans);
    assert(reverse_words(test_str_4) == test_str_4_ans);
    return 0;
}