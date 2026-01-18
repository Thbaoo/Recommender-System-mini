import pandas as pd
from src.recommender import ItemBasedRecommender
from src.data_loader import load_transactions

rec = ItemBasedRecommender()

print("\n=== USER–ITEM MATRIX ===")
print(rec.user_item_matrix)

print("\n=== ITEM SIMILARITY MATRIX ===")
sim_df = pd.DataFrame(
    rec.item_similarity,
    index=rec.user_item_matrix.columns,
    columns=rec.user_item_matrix.columns
)
print(sim_df)

print("\n=== RECOMMEND FOR U1 ===")
print(rec.recommend("U1"))
