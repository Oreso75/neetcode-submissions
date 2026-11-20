class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op.lstrip("-").isdigit(): 
                record.append(int(op))
            elif op == '+':
                record_sum = record[-1] + record[-2]
                record.append(int(record_sum))
            elif op == 'D':
                op_double = int(2*(record[-1]))
                record.append(op_double)
            elif op == 'C':
                del record[-1]
        
        return sum(record)
        


