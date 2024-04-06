from src.augment import rank_dict
import pandas as pd

def test_ranking():
    test_df = pd.DataFrame({'test': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'D']})
    ranks = rank_dict(test_df, 'test')
    assert ranks['A'] == ranks['B'] == 1 and ranks['C'] == 3 and ranks['D'] == 4