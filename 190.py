class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_str = str(bin(n))
        n_str = n_str[2:]
        left_zero = 0
        if len(n_str) < 32:
            left_zero = 32 - len(n_str)
        n_str = n_str[::-1]
        n_str += '0' * left_zero
        return int(n_str,2)
        