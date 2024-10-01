"""
Copyright © 2024 Datasciencelabs.org . All rights reserved.

This code is protected under copyright law and may be used under the following conditions:

1. Use, modification, and distribution of this code are permitted for personal or non-commercial purposes only.
2. Commercial use of this code is prohibited without the prior written permission of the copyright holder.
3. Any modified or redistributed versions of this code must retain this copyright notice.
4. The copyright holder is not liable for any damages or issues that arise from the use of this code.

For further inquiries, please contact: sjchun@dau.ac.kr
"""

import networkx as nx

# 소셜 네트워크 그래프 생성
G = nx.Graph()
# 인플루언서들 간의 상호작용을 나타내는 관계
edges = [('Influencer_A', 'Influencer_B'), 
         ('Influencer_A', 'Follower_1'), 
         ('Influencer_B', 'Follower_2'), 
         ('Influencer_B', 'Follower_3'), 
         ('Follower_1', 'Follower_2'), 
         ('Follower_2', 'Follower_3'), 
         ('Influencer_A', 'Influencer_C'), 
         ('Influencer_C', 'Follower_4')]

G.add_edges_from(edges)

# 각 노드의 중심성 계산 (많이 연결된 사람일수록 중심성이 높음)
centrality = nx.degree_centrality(G)

# 중심성이 가장 높은 인물 찾기
most_influential = max(centrality, key=centrality.get)
print("가장 영향력 있는 인물:", most_influential)

# 예상 결과: 'Influencer_A' 또는 'Influencer_B'가 가장 영향력 있는 인물일 가능성이 높음
