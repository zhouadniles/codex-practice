---
name: remove-ai-flavor
description: Revise Chinese writing to remove AI-flavored, template-like expressions while preserving meaning, facts, author voice, and necessary roughness. Use when the user asks to 去除AI味, 降低AI感, 改得更像人写, 润色小红书/公众号/随笔/文案/评论/邮件/小说正文, or specifically remove patterns like “不是...而是”, “先...再”, “真正...的是”, “这次只看”, “X很简单：”, mechanical contrast/sequence framing, over-neat parallel rhythm, repeated route markers, and unexplained rhetorical questions at the end.
---

# Remove AI Flavor

## Goal

Make Chinese prose feel less machine-polished and more like a specific person wrote it. Preserve meaning, facts, stance, source boundaries, original register, and useful roughness. Remove only the structures that make readers feel the text is assembled from an assistant template.

Do not invent facts, examples, data, actions, jokes, personal experience, named sources, or emotional reactions merely to make text look human. Do not optimize for detector evasion. Optimize for truthful, specific writing.

## Before Editing

Establish these five items. If information is missing, narrow the edit rather than inventing context:

1. Genre: short post, long article, tutorial, review, commentary, formal report, fiction, or other.
2. Author intent: explain, persuade, review, complain, record, or establish a judgment.
3. Intended reader: what they already know and where the real difficulty is. Do not invent a low-information reader.
4. Tone: calm judgment, field review, personal complaint, mild irony, restrained explanation, or another stated register.
5. Source boundaries: what is direct experience or verified data, and what is inference, hearsay, or speculation.

If the user provides writing samples, calibrate to their sentence length, opening habits, habitual wording, and degree of roughness. Do not replace them with a more “correct” generic style.

## Default Workflow

1. Produce a diagnosis before rewriting when the user asks for editing analysis. Classify: meaning inflation, promotional tone, vague attribution, formula sentences, AI vocabulary, rhythm/paragraph-shape traces.
2. Mark sentences that are correct but carry little information.
3. Delete before rewriting. Target at least 20% reduction when the draft contains clear padding; do not force this target on already lean text.
4. Replace abstractions with a concrete action, number, scene, consequence, or one plain human sentence only when supported by the source.
5. Check rhythm. If consecutive sentences have similar length or structure, create a deliberate shift: shorten, expand, cut, turn, or stop.
6. Produce the first rewrite.
7. Audit once more: “What still obviously sounds like AI?” Fix only the remaining structural problems.

If the text has no obvious AI flavor, do not over-edit. Excessive cleanup produces a different template.

## High-Priority AI Traces

### Binary Contrast Shells

High-risk forms:

- “不是 A，而是 B”
- “并非 A，而是 B”
- “不在于 A，而在于 B”
- “不只是 A，更是 B”
- “与其说 A，不如说 B”

Keep one only when A is a real reader belief, a character’s voice, or a necessary technical distinction. Otherwise delete the false target and state the actual claim.

### Staged Sequence Shells

High-risk forms:

- “先 A，再 B”
- “第一步……第二步……”
- “从 A 到 B”
- “下面我们来……”
- “接下来我会……”

Keep sequence only when order changes the result. In instructions, use operational steps. In prose, enter the actual content directly.

### Meaning Inflation And Empty Emphasis

High-risk forms:

- “真正重要的是”
- “真正决定 X 的是”
- “本质上”
- “核心在于”
- “底层逻辑”
- “赋能”
- “认知升级”
- “闭环”
- “长期主义”
- “关键抓手”

Replace abstract emphasis with evidence, action, condition, or consequence. Do not turn every paragraph into a conclusion.

### Promotional Tone And Vague Authority

Watch for:

- “大幅提升”“全面赋能”“显著优化” without a measurement.
- “业内人士认为”“不少人表示”“有研究显示” without a named source.
- “广泛关注”“引发热议” without observable evidence.
- Grand endings that extend the claim beyond the material.

Delete unsupported intensity. Use names, data, scenes, or reduce the claim.

### Formula Sentences And Paragraph Shape

Watch for:

- “观点句 + 解释 + 段尾总结” repeated across paragraphs.
- “概念：解释”“问题：答案”“原因：结论” repeated as a paragraph template.
- Three or more clauses with the same grammar and emotional pitch.
- Paragraphs with suspiciously even length and function.
- Repeated rhetorical questions answered immediately by the author.

Break neatness by cutting a clause, grounding one clause in detail, letting a transition remain implicit, or ending on a fact, scene, consequence, or decision.

### Assistant Route Markers And Fake Engagement

Remove unless explicitly required:

- “总的来说”
- “值得注意的是”
- “不可否认的是”
- “在这个过程中”
- “这背后其实”
- “希望这能帮到你”
- “划重点”
- “拆一拆 / 捋一捋 / 盘一盘 / 聊一聊”
- “你觉得呢？”
- “你有没有类似经历？”

Do not fabricate a foolish reader statement just to correct it. Address only real, central objections.

## Register-Specific Rules

### Fiction

- Preserve scene continuity, character action, dialogue intention, and manuscript-only output unless diagnosis is requested.
- Prefer action, sensory detail, and consequence over explanatory verdicts such as “他意识到”“真正”“不禁”.
- Do not over-explain worldbuilding at the moment of emotional payoff.
- Keep dialogue roughness, repetition, simple words, and even a necessary formula shell when it reveals character.
- Do not force a moral conclusion. Let the image, object, decision, or unanswered residue carry the ending.

### Commentary And Public Writing

- Keep the author’s judgment. Do not pretend every counterargument deserves equal weight.
- Replace abstractions with observable stakes.
- Do not end by escalating to “the era / society / future” unless the material earns it.

### Formal Reports And Technical Writing

- Preserve terms, citations, variables, and qualified claims.
- Do not swap precise terms for colloquial words.
- If evidence is missing, narrow or hedge the claim; never invent a citation.
- Keep lists and sequence markers where they are required for compliance or operation.

### Social Posts

- Keep information density and readability.
- Do not add fake intimacy, exaggerated uplift, or comment bait.
- A hook is not mandatory. Start from the thing that actually needs saying.

## Quality Gate

Before finalizing, verify:

- The revision preserves the author’s claim, factual boundary, and voice.
- No unsupported number, scene, action, or source was added.
- Binary contrast, staged sequence, and “essence” language remain only where they are justified.
- Sentence length and paragraph weight vary naturally.
- The text does not solve every objection or conclude every paragraph with a slogan.
- The ending does not become a moral or an engagement prompt by habit.
- The revision has not become smoother, safer, and less individual than the original.

## Output Modes

- If asked only to revise: output the revised text, with minimal note.
- If asked to analyze: provide diagnosis, empty-information sentences, first rewrite, residual-AI audit, and final rewrite.
- If asked to preserve a specific author voice: identify only observable style features; do not claim certainty about hidden intent.

## Provenance

Installed from and adapted from B1lli/remove-ai-flavor-writing-skill (MIT). Local additions emphasize source boundaries, editorial diagnosis, deletion-first revision, author-voice calibration, and a second residual-AI audit.
