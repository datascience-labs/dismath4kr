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

# 유전자 상호작용 네트워크 생성
G = nx.Graph()
genes = [('Gene_TP53', 'Gene_BRCA1'),  # TP53과 BRCA1 유전자는 상호작용함
         ('Gene_TP53', 'Gene_PTEN'),   # TP53과 PTEN 유전자는 상호작용함
         ('Gene_BRCA1', 'Gene_PTEN'),  # BRCA1과 PTEN 유전자는 상호작용함
         ('Gene_PTEN', 'Gene_RB1'),    # PTEN과 RB1 유전자는 상호작용함
         ('Gene_RB1', 'Gene_BRCA1')]   # RB1과 BRCA1 유전자는 상호작용함

G.add_edges_from(genes)

# 중심성 계산 (가장 중요한 유전자 찾기)
centrality = nx.betweenness_centrality(G)

# 중심성이 가장 높은 유전자 찾기
key_gene = max(centrality, key=centrality.get)
print("가장 중요한 유전자:", key_gene)

# 예상 결과: 'Gene_PTEN'이 중심적인 역할을 할 가능성 높음
