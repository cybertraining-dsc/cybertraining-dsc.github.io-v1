---
title: Mermaid Sample
---

{{< mermaid >}}
graph LR
A[Introduction]
B[Usecases]
C[Physics]
D[Sports]
A-->B-->C-->D
{{</ mermaid >}}

{{< mermaid >}}
gantt
    title Class
    dateFormat  YYYY-MM-DD
    section Week 1
    Introduction     :w1, 2020-08-01, 7d
    Bio              :after w1  , 1d
    Github           :after w1  , 1d	
{{</ mermaid >}}
