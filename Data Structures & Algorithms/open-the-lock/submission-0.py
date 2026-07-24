class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        if '0000' in deadends:
            return -1
        
        if '0000' == target:
            return 0

        dq = deque([start])
        visited = {start}
        count =0

        while dq:
            size = len(dq)
            count += 1
            for _ in range(size):
                value = dq.popleft()

                for i in range(4):
                    for j in [1, -1]:
                        digit = value[i]
                        new_digit = str((int(digit) + j) % 10)
                        new_num = value[:i] + new_digit + value[i+1:]

                        if new_num == target:
                            return count 

                        if (new_num not in deadends) and (new_num not in visited):
                            visited.add(new_num)
                            dq.append(new_num)
        return -1