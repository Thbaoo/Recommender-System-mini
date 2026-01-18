import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from src.data_loader import load_transactions

class ItemBasedRecommender:
    def __init__(self):
        self.df = load_transactions()
        self.user_item_matrix = None
        self.item_similarity = None
        self._build_matrix()
        self._build_similarity()

    def _build_matrix(self):
        self.user_item_matrix = self.df.pivot_table(
            index="user_id",
            columns="product_id",
            values="rating",
            fill_value=0
        )

    def _build_similarity(self):
        self.item_similarity = cosine_similarity(self.user_item_matrix.T)

    def recommend(self, user_id, top_k=5):
        user_vector = self.user_item_matrix.loc[user_id]
        scores = self.item_similarity.dot(user_vector)
        scores = pd.Series(
            scores,
            index=self.user_item_matrix.columns
        )
        scores = scores[user_vector == 0]
        return scores.sort_values(ascending=False).head(top_k)
