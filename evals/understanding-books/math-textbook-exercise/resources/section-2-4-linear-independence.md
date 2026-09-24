# Foundations of Linear Algebra: A First Course

Tobias Renner-Achebe · Northgate University Press · 3rd edition, 2024

---

## 2.4 Linear Independence

— p. 47 —

Section 2.3 introduced the span of a list of vectors: the set of everything you can build from them. This section asks the opposite question. When is a list of vectors free of waste, in the sense that no vector in it could be built from the others? The answer, linear independence, is the idea on which basis and dimension in Section 2.5 depend.

Throughout this section, V is a vector space over the real numbers ℝ. (Section 1.6 briefly introduced other fields of scalars, such as the two-element field F₂, in which 1 + 1 = 0. We return to them in Chapter 7.)

**Definition 2.6 (Linear combination).** A linear combination of vectors v₁, …, vₖ in V is a vector of the form a₁v₁ + a₂v₂ + ⋯ + aₖvₖ, where a₁, …, aₖ are scalars in ℝ.

**Definition 2.7 (Span).** The span of v₁, …, vₖ, written span(v₁, …, vₖ), is the set of all linear combinations of v₁, …, vₖ. By convention, the span of the empty list is {0}.

**Definition 2.8 (Linear independence).** Vectors v₁, …, vₖ are *linearly independent* if the only solution of

    a₁v₁ + a₂v₂ + ⋯ + aₖvₖ = 0

is a₁ = a₂ = ⋯ = aₖ = 0. Otherwise they are *linearly dependent*, and any solution in which some aᵢ ≠ 0 is called a *dependence relation*.

The zero combination always gives 0; independence says it is the only way to get 0. A useful reformulation: v₁, …, vₖ are independent exactly when each vector in their span can be written as a linear combination of them in only one way. If two different combinations gave the same vector, subtracting one from the other would give a nontrivial combination equal to 0.

— p. 48 —

**Example 2.9.** In ℝ³, the vectors e₁ = (1, 0, 0), e₂ = (0, 1, 0), and (1, 1, 0) are linearly dependent, since e₁ + e₂ − (1, 1, 0) = 0. Any two of them, however, are independent.

**Theorem 2.10 (Extending an independent list).** Suppose v₁, …, vₖ are linearly independent in V and w ∈ V. Then v₁, …, vₖ, w are linearly independent if and only if w ∉ span(v₁, …, vₖ).

*Proof sketch.* (⇒) If w were in the span, say w = c₁v₁ + ⋯ + cₖvₖ, then c₁v₁ + ⋯ + cₖvₖ − w = 0 would be a dependence relation, since the coefficient of w is −1 ≠ 0.

(⇐) Suppose a₁v₁ + ⋯ + aₖvₖ + bw = 0. If b ≠ 0, divide by b and solve for w; this puts w in the span, contrary to assumption. So b = 0. The equation then reads a₁v₁ + ⋯ + aₖvₖ = 0, and the independence of the vᵢ forces every aᵢ = 0. ∎

Two features of this proof are worth noticing, because you will use them again. First, the argument starts by writing down a general linear combination equal to 0 and asking what the coefficients must be; with independence, that is almost always the right first move. Second, the proof divides by a scalar. Division needs that scalar to be nonzero, and the hypothesis that we work over ℝ is doing quiet work whenever an argument divides by a number such as 2.

— p. 49 —

**Remark 2.11.** Independence is a property of the whole list, not of its members taken two at a time. Example 2.9 shows three vectors, no two of which are dependent, that are dependent as a list.

### Exercises

**2.12.** Decide whether (1, 2, 3), (2, 4, 6), and (0, 1, 1) are linearly independent in ℝ³. If they are dependent, give a dependence relation.

**2.13.** Show that any list of vectors that contains the zero vector is linearly dependent.

**2.14.** Let u, v, w be linearly independent vectors in V. Prove that u + v, v + w, w + u are also linearly independent. Then identify the step of your proof that uses the fact that the scalars are real numbers, and explain why the statement can fail in a field where 1 + 1 = 0.

**2.15.** Let v₁, …, vₖ be linearly independent and let w = v₁ + ⋯ + vₖ. Is the list v₁, …, vₖ, w linearly independent? Use Theorem 2.10.

Solutions to odd-numbered exercises appear in Appendix B.
