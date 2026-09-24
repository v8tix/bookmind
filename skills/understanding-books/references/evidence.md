# Evidence Basis and Limits

## Contents

- How to interpret the evidence
- Findings used by the protocol
- Design implications
- Sources

## How to interpret the evidence

No controlled trial compares whole methods for understanding an entire book. The protocol combines techniques that target different outcomes: initial comprehension, relational understanding, gap detection, and delayed retention.

Effect sizes from different meta-analyses cannot be ranked against each other. They differ in learners, materials, comparison conditions, outcome measures, delays, and settings. Treat them as support for design decisions, not as predictions for one reader.

The broad synthesis [1] is dominated by studies with surface or factual outcomes (93% of outcomes), and its authors caution against applying its findings to deeper, relational outcomes. Pooled across its ten techniques, effects on deep-processing outcomes were much smaller than effects on surface outcomes. For the relational goals of this skill, its headline numbers are probably overestimates.

## Findings used by the protocol

| Method | Representative result | Source | Protocol role |
|---|---|---|---|
| Distributed practice | d ≈ 0.85 in a broad synthesis; d ≈ 0.54 over massed practice in classroom studies | [1], [2] | Reviews spread across days (Phase 5) |
| Spacing and retention interval | No single gap is best for every retention interval; the best gap grows with how long material must be kept, but shrinks as a fraction of it | [3], [4] | Schedule derived from the deadline or horizon |
| Retrieval practice | d ≈ 0.74 in a broad synthesis; g ≈ 0.50 over restudy; benefits hold in real classrooms | [1], [5], [6] | Recall before reopening the source |
| Retrieval with feedback | g ≈ 0.73 in studies with feedback vs g ≈ 0.39 without | [5] | Claude checks and corrects after recall |
| Higher-order retrieval | Higher-order and mixed retrieval practice improved higher-order test performance; fact-only practice did not. Benefits largely matched the type of question practiced, and mixed practice helped both | [7] | Review prompts match the target task; mix factual and conceptual prompts when the task needs both |
| Successive relearning | Recalling items to criterion in one session, then relearning them in later sessions, improved course exam performance and long-term retention [8]. A dose study recommended 3 correct recalls at first, then 3 widely spaced relearning sessions; the first-session criterion mattered less as relearning sessions added up [18] | [8], [18] | Re-ask misses until correct once, relying on later relearning; about 3 correct spaced sessions is a heuristic for "stable", not a tested threshold |
| Learner-constructed concept maps | g ≈ 0.72 for creating maps and g ≈ 0.43 for studying supplied maps, each against its own comparison condition. Some pooled studies gave mapping more time than the control or combined it with another activity [11] | [9], [11] | The reader builds the map, from memory |
| Concept mapping from memory | Building a map with the text closed worked as retrieval practice: as well as free recall, not better, and better than the same activities with the text open [10]. Making a map with the text open before retrieval added 10–20 minutes and did not improve 1-week test performance over retrieval alone [11] | [10], [11] | Connect merged into Retrieve |
| Prompted self-explanation | g ≈ 0.55 overall; g ≈ 0.35 against receiving an instructional explanation (k = 6 effect sizes) | [12] | 2–3 explanation prompts per central idea |
| Prequestions | g ≈ 0.54 for prequestioned content and g ≈ 0.04 for other content; larger when learners guess; factual prequestions tended to outperform conceptual ones (marginal) | [13] | A few targeted questions; the reader guesses |
| Pretesting | Answering questions before reading improved later performance on those concepts compared with extra reading time, even for items answered wrongly beforehand | [14] | Wrong guesses still help when the text then supplies the answer |
| Interleaving | g ≈ 0.42 overall; strongest for similar categories; ambiguous, non-significant results for expository texts | [15] | Compare already-learned, confusable concepts |
| Correcting confident errors | On a retest shortly after feedback, general-knowledge errors made with high confidence were more likely to be corrected than low-confidence errors [16]. After a week the effect still held, but correction declined, and high-confidence errors were more likely than low-confidence ones to come back when the correction was forgotten, despite feedback [19] | [16], [19] | Confidence ratings at Deep depth flag confident errors; re-ask them at the next spaced review |
| Self-scoring of recall | Students overestimated the correctness of definitions they recalled. Seeing the correct definition while scoring improved accuracy, but some overconfidence remained | [17] | Claude assigns the recall categories |

Summarization, highlighting, and rereading are not forbidden. In the broad synthesis they were among the smallest effects (summarization and underlining d ≈ 0.44, the lowest; rereading d ≈ 0.47, the same as interleaving), in the authors' Low band (d < 0.53), yet the authors still judged them "sufficiently effective to be included in a student's toolbox" [1]. The protocol emphasizes generating from memory because passive review can hide retrieval gaps.

## Design implications

1. **Separate stages.** Orientation, explanation, retrieval, and spacing do different jobs.
2. **Reader generation matters.** In guided mode, Claude should not replace the reader's own explanation, map, or recall attempt. Prompted self-explanation beat receiving an instructional explanation (g ≈ 0.35, k = 6 effect sizes) [12]. For maps, [9] measured creating and studying maps against different comparison conditions, so it does not show that building a map beats studying a supplied one; the reason for the reader to build the map is that doing it from memory is a retrieval attempt [10], [11].
3. **Feedback follows retrieval.** In [5], tests followed by feedback produced larger effects than tests without it (g ≈ 0.73 vs 0.39). Giving the answer before the attempt turns it into restudy, the weaker condition in [5], and hides which items the reader could not recall; this last point is an inference, not a tested result.
4. **Questions buy focus, not coverage.** Prequestions help the content they target, so aim them at central ideas and ask for a guess [13], [14]. The protocol's conceptual questions sit where the evidence is thinnest: conceptual prequestions showed a smaller effect than factual ones (marginally significant, from fewer studies) [13]. Preferring broad questions over narrow ones is a coverage choice, not a research finding.
5. **Schedules follow the goal.** No single spacing gap is optimal for every retention horizon, so derive the schedule from the deadline or horizon [3], [4]. Expanding schedules like the default rarely hurt, but there is little evidence that they beat evenly spaced ones [3].
6. **Cost matters.** More prompts per idea are not better when they crowd out reading and review; depth levels trade effort against the goal.
7. **Book type matters.** Most effects come from short learning materials and may not transfer unchanged to a long, technically dense book.

## Sources

1. Donoghue, G. M., & Hattie, J. A. C. (2021). A meta-analysis of ten learning techniques. *Frontiers in Education, 6*, 581216. https://doi.org/10.3389/feduc.2021.581216
2. Mawson, R. D., & Kang, S. H. K. (2025). The distributed practice effect on classroom learning: A meta-analytic review of applied research. *Behavioral Sciences, 15*(6), 771. https://doi.org/10.3390/bs15060771
3. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. https://doi.org/10.1037/0033-2909.132.3.354
4. Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. https://doi.org/10.1111/j.1467-9280.2008.02209.x
5. Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin, 140*(6), 1432–1463. https://doi.org/10.1037/a0037559
6. Agarwal, P. K., Nunes, L. D., & Blunt, J. R. (2021). Retrieval practice consistently benefits student learning: A systematic review of applied research in schools and classrooms. *Educational Psychology Review, 33*(4), 1409–1453. https://doi.org/10.1007/s10648-021-09595-9
7. Agarwal, P. K. (2019). Retrieval practice & Bloom's taxonomy: Do students need fact knowledge before higher order learning? *Journal of Educational Psychology, 111*(2), 189–209. https://doi.org/10.1037/edu0000282
8. Rawson, K. A., Dunlosky, J., & Sciartelli, S. M. (2013). The power of successive relearning: Improving performance on course exams and long-term retention. *Educational Psychology Review, 25*(4), 523–548. https://doi.org/10.1007/s10648-013-9240-4
9. Schroeder, N. L., Nesbit, J. C., Anguiano, C. J., & Adesope, O. O. (2018). Studying and constructing concept maps: A meta-analysis. *Educational Psychology Review, 30*(2), 431–455. https://doi.org/10.1007/s10648-017-9403-9
10. Blunt, J. R., & Karpicke, J. D. (2014). Learning with retrieval-based concept mapping. *Journal of Educational Psychology, 106*(3), 849–858. https://doi.org/10.1037/a0035934
11. O'Day, G. M., & Karpicke, J. D. (2021). Comparing and combining retrieval practice and concept mapping. *Journal of Educational Psychology, 113*(5), 986–997. https://doi.org/10.1037/edu0000486
12. Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review, 30*(3), 703–725. https://doi.org/10.1007/s10648-018-9434-x
13. St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024). Guessing as a learning intervention: A meta-analytic review of the prequestion effect. *Psychonomic Bulletin & Review, 31*(2), 411–441. https://doi.org/10.3758/s13423-023-02353-8
14. Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. https://doi.org/10.1037/a0016496
15. Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin, 145*(11), 1029–1052. https://doi.org/10.1037/bul0000209
16. Butterfield, B., & Metcalfe, J. (2001). Errors committed with high confidence are hypercorrected. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 27*(6), 1491–1494. https://doi.org/10.1037/0278-7393.27.6.1491
17. Rawson, K. A., & Dunlosky, J. (2007). Improving students' self-evaluation of learning for key concepts in textbook materials. *European Journal of Cognitive Psychology, 19*(4–5), 559–579. https://doi.org/10.1080/09541440701326022
18. Rawson, K. A., & Dunlosky, J. (2011). Optimizing schedules of retrieval practice for durable and efficient learning: How much is enough? *Journal of Experimental Psychology: General, 140*(3), 283–302. https://doi.org/10.1037/a0023956
19. Butler, A. C., Fazio, L. K., & Marsh, E. J. (2011). The hypercorrection effect persists over a week, but high-confidence errors return. *Psychonomic Bulletin & Review, 18*(6), 1238–1244. https://doi.org/10.3758/s13423-011-0173-y
