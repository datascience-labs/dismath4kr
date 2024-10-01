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
from networkx.algorithms.community import girvan_newman

# 학생들 간의 친구 관계 그래프 생성
G = nx.Graph()
friendships = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Charlie'),
               ('Charlie', 'David'), ('David', 'Eve'), ('Eve', 'Frank'),
               ('Frank', 'Grace'), ('Grace', 'Eve'), ('David', 'Frank')]

G.add_edges_from(friendships)

# Girvan-Newman 알고리즘을 사용한 군집 탐지
communities = girvan_newman(G)
first_level_communities = next(communities)
community_list = [list(c) for c in first_level_communities]

print("첫 번째 레벨의 군집:", community_list)

# 예상 결과: ['Alice', 'Bob', 'Charlie']와 ['David', 'Eve', 'Frank', 'Grace']로 나뉠 가능성
