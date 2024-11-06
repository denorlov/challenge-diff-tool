from unittest import TestCase
from edit_distance import minDistance


class Test(TestCase):
    def test_min_distance(self):
        word1 = "horse"
        word2 = "ros"
        #assert minDistance(word1, word2) == (3, "(h,r)_o_d(r)_s_d(e)")
        res = minDistance(word1, word2)
        print(res)
        assert res == "(h,r)_o_d(r)_s_d(e)"

        word1 = "intention"
        word2 = "execution"
        #assert minDistance(word1, word2) == (5, "(i,e)_(n,x)_(t,e)_(e,c)_(n,u)_t_i_o_n")
        res = minDistance(word1, word2)
        print(res)
        assert res == "(i,e)_(n,x)_(t,e)_(e,c)_(n,u)_t_i_o_n"

    def test_min_distance_abc(self):
        word1 = "abc"
        word2 = "abc"
        #assert minDistance(word1, word2) == (0, "a_b_c")
        assert minDistance(word1, word2) == "a_b_c"

        word1 = "abc"
        word2 = "abb"
        #assert minDistance(word1, word2) == (1, "a_b_(c,b)")
        assert minDistance(word1, word2) == "a_b_(c,b)"

        word1_2 = "bbc"
        word2_2 = "abc"
        #assert minDistance(word1_2, word2_2) == (1, "(b,a)_b_c")
        assert minDistance(word1_2, word2_2) == "(b,a)_b_c"

        # word1_2 = "abbc"
        # word2_2 = "abc"
        # #assert minDistance(word1_2, word2_2) == (1, "a_b_d(b)_c")
        # res = minDistance(word1_2, word2_2)
        # print(res)
        # assert res == "a_b_d(b)_c"

        word1_2 = "ab"
        word2_2 = "abc"
        #assert minDistance(word1_2, word2_2) == (1, "a_b_i(c)")
        assert minDistance(word1_2, word2_2) == "a_b_i(c)"

        word1_2 = "bc"
        word2_2 = "abc"
        #assert minDistance(word1_2, word2_2) == (1, "i(a)_b_c")
        assert minDistance(word1_2, word2_2) == "i(a)_b_c"

    def test_min_distance_abc_insert_at_the_start(self):
        word1 = "ros"
        word2 = "horse"
        #assert minDistance(word1, word2) == (3, "(r,h)_o_i(r)_s_i(e)")
        assert minDistance(word1, word2) == "(r,h)_o_i(r)_s_i(e)"
