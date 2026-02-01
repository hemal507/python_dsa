class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen_dna_set=set()
        repeated_dna_set=set()
        for i in range(len(s) - 9) :
            sub_str = s[i:i+10]
            if sub_str in seen_dna_set :
                repeated_dna_set.add(sub_str)
            else:
                seen_dna_set.add(sub_str)
        return list(repeated_dna_set)