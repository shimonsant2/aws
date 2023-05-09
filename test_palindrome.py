# function to check string is
# palindrome or not


def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "12211"
ans = isPalindrome(s)

test_1 = '1221'
test_2 = '1221221'
test_3 = 'aaabbbcccbbbaaa'
test_4 = 'ttttsfsfsfsfsfsfsfsfsttttdddJenkinkurlGFIeXXX'
test_5 = 'ddd91ddd'
test_6 = 'ddd91ddd333666999'
test_7 = 'aaabaaa'
test_8 = 'aaabaaa'

if ans:
    print("Yes")
else:
    print("No")


    def test_answer1():
        assert isPalindrome(test_1) == True


    def test_answer2():
        assert isPalindrome(test_2) == True


    def test_answer3():
        assert isPalindrome(test_3) == True


    def test_answer4():
        assert isPalindrome(test_4) == False


    def test_answer5():
        assert isPalindrome(test_5) == False

    def test_answer6():
        assert isPalindrome(test_6) == False

    def test_answer7():
        assert isPalindrome(test_7) == True

    def test_answer8():
        assert isPalindrome(test_8) == False