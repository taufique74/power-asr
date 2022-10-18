from typing import List
from dataclasses import dataclass

from power.aligner import PowerAligner

@dataclass
class SentenceAlignment:
    ref: List[str]
    hyp: List[str]
    alignment: List[str]

    def get_sub_ids(self) -> List[int]:
        ''' 
            Returns index of substitutions
        '''
        # for idx, al in enumerate(self.alignment):
        return [idx for idx, al in enumerate(self.alignment.align) if al == 'S']

    def get_sub_pairs(self) -> List[str]:
        '''
            Return substitution pairs with the index
        '''
        pairs = []
        for idx, al in enumerate(self.alignment.align):
            if al == 'S':
                pairs.append({
                    'idx': idx,
                    'ref': self.ref[idx],
                    'hyp': self.hyp[idx],
                })
        
        return pairs

    def get_ref(self) -> List[str]:
        return self.alignment.s1

    def get_hyp(self) -> List[str]:
        return self.alignment.s2



class Aligner:
    def __init__(self):
        self.aligner = PowerAligner(
            lowercase=True, 
            verbose=False,
        )
        
    def create_source_target_pair(self, alignment: SentenceAlignment) -> dict:
        s1 = alignment.get_ref()
        s2 = alignment.get_hyp()
        sub_ids = alignment.get_sub_ids()

        hyp = []
        for idx, segment in enumerate(s1):
            if idx in sub_ids:
                hyp.append(s2[idx])
            else:
                hyp.append(segment)

        return {
            'source': s1,
            'target': s2,
            'sub_ids': sub_ids
        }
    
    def get_alignment(self, source: str, target: str) -> dict:
        source = source.strip()
        target = target.strip()

        try:
            self.aligner.align(source, target)
            aligned = self.create_source_target_pair(SentenceAlignment(
                ref = self.aligner.power_alignment.s1,
                hyp = self.aligner.power_alignment.s2,
                alignment = self.aligner.power_alignment
            ))
        except:
            # aligned = self.create_source_target_pair(SentenceAlignment(
            #     ref = source.split(),
            #     hyp = target.split(),
            #     alignment = []
            # ))
            aligned = dict(
                source = source.split(),
                target = target.split(),
                sub_ids = []
            )
            

        # aligned = self.create_source_target_pair(SentenceAlignment(
        #     ref = self.aligner.power_alignment.s1,
        #     hyp = self.aligner.power_alignment.s2,
        #     alignment = self.aligner.power_alignment
        # ))
        
        return aligned
