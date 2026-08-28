class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # A palindrome can have at most one odd frequency
        odd = -1

        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        half = n // 2
        halfCnt = [x // 2 for x in cnt]

        targetHalf = target[:half]

        # First check if targetHalf itself can be formed
        # from the first half of the palindrome.
        temp = halfCnt[:]
        possible = True

        for ch in targetHalf:
            x = ord(ch) - 97

            if temp[x] == 0:
                possible = False
                break

            temp[x] -= 1

        if possible:
            first = targetHalf

            # Build the palindrome with exactly this first half
            middle = chr(odd + 97) if odd != -1 else ""
            candidate = first + middle + first[::-1]

            # If it is strictly greater, this is the smallest answer
            if candidate > target:
                return candidate

        # Otherwise find the smallest first half strictly
        # greater than targetHalf.
        for pos in range(half - 1, -1, -1):
            temp = halfCnt[:]

            # Match targetHalf before pos
            ok = True

            for j in range(pos):
                x = ord(targetHalf[j]) - 97

                if temp[x] == 0:
                    ok = False
                    break

                temp[x] -= 1

            if not ok:
                continue

            need = ord(targetHalf[pos]) - 97

            # Pick smallest character greater than target[pos]
            for c in range(need + 1, 26):
                if temp[c] == 0:
                    continue

                temp[c] -= 1

                first = targetHalf[:pos] + chr(c + 97)

                # Add remaining characters in sorted order
                for x in range(26):
                    first += chr(x + 97) * temp[x]

                middle = chr(odd + 97) if odd != -1 else ""

                return first + middle + first[::-1]

        return ""