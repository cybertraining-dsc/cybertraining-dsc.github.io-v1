---
title: "Pandoc Sample"
linkTitle: "Pandoc"
weight: 100
date: 2020-08-15
categories: [sample]
tags: [pandoc,markdown]
description: >
  In this section we demonstrate the usage of pandoc within hugo.
markup: pandoc
---

{{% pageinfo %}}

In this section we demonstret the usage of pandoc within hugo.

{{% /pageinfo %}}

{{< table_of_contents >}}

# Pandoc Sample

We process this file with {{< param markup >}}.

## Footnote

Footnotes also workw in hugo's markdown.
Here is a footnote reference,[^1] and another [^2].

[^1]: Here is the first footnote.

[^2]: Here is the second footnote.

## Citation test

This paper describes the Java CoG Kit [@doi:10.1002/cpe.572].

## This is a section {#sec:test}

This is a refernce to @sec:test

## Math

A Math formula with equation can be done this way

$$ a^2 $$ {#eq:label}

As we see we can refer to @eq:label

Here is just an inline math equation

$b^2$

## References


