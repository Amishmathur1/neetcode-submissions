class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        if '0000' in deadends:
            return -1
        
        dq = deque([start])

        visited = {start}
        count = 0

        while dq:
            size = len(dq)
            count += 1

            for _ in range(size):
                val = dq.popleft()
            
                for ind in range(4):
                    for j in [1, -1]:
                        digit = val[ind]
                        new_digit = str((int(digit) + j) % 10)
                        
                        if int(new_digit)  < 0:
                            continue

                        new_val = val[:ind] + new_digit + val[ind+1:]

                        if new_val == target:
                            return count

                        if (new_val not in deadends) and (new_val not in visited):
                            visited.add(new_val)
                            dq.append(new_val)

        return -1