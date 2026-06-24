---
name: remove-ai-flavor
description: Edit Chinese prose to remove AI-flavored, template-like writing while preserving facts, judgment, source boundaries, author voice, and necessary roughness. Use for 去除AI味、降低AI感、改得更像人写、润色小说/评论/长文/短帖/教程/复盘/报告，or when text shows mechanical contrast, uniform paragraph rhythm, inflated meaning, promotional tone, vague authority, generic conclusions, or excessive explanatory narration.
---

# Remove AI Flavor

## 0. Core Principle

Do not “humanize” text by adding slang, sentiment, fabricated detail, or calculated imperfection. Edit toward truthful, specific writing with a visible point of view.

The goal is not to disguise AI. The goal is to retain real judgment, bodily sense, and stylistic boundaries.

Preserve what is already alive: the author’s sentence length, opening habits, favorite words, rough edges, repetitions, and unevenness when they belong to the voice.

## 1. Before Editing: Establish the Boundary

Before rewriting, identify these five items. If evidence is missing, narrow the revision; do not invent context.

1. **Genre** — short post, long article, tutorial, review, commentary, formal report, fiction, or other.
2. **Intent** — explain, persuade, review, complain, record, or establish a judgment.
3. **Reader** — what they already know and where the actual difficulty is. Do not invent a low-information reader just to correct them.
4. **Tone** — calm judgment, field review, personal complaint, mild irony, restrained explanation, or another stated register.
5. **Source boundary** — what is direct experience or verified data; what is inference, hearsay, or speculation.

If the user provides writing samples, calibrate to observable features only: sentence length, paragraph weight, opening habits, habitual expressions, degree of directness, and tolerance for roughness. Do not replace them with a generic “better style.”

## 2. Default Editing Workflow

Use this sequence unless the user explicitly asks for only a quick rewrite.

1. **Diagnose before changing.** Classify problems under: meaning inflation, promotional tone, vague attribution, formula sentences, AI vocabulary, rhythm/paragraph shape, and voice mismatch.
2. **Mark correct but empty sentences.** A sentence can be grammatically correct and still say nothing new.
3. **Delete first.** Remove padding before adding language. Aim for at least 20% reduction only when the draft clearly contains padding; do not force a quota on lean writing.
4. **Ground abstractions.** Replace an abstract word only with a supported action, number, scene, object, consequence, or one plain sentence.
5. **Repair rhythm.** When several sentences or paragraphs have the same length, grammar, or emotional pitch, shorten one, extend one with a concrete fact, merge one, or stop early.
6. **Produce a first revision.** Preserve claims, facts, and the author’s register.
7. **Run a residual audit.** Ask: “What still obviously sounds like AI?” Fix only actual remaining structural problems. Do not over-clean.

If the original has no strong AI trace, say so and make fewer changes. Over-editing creates another template.

## 3. High-Priority AI Traces

### 3.1 Meaning Inflation

High-risk language:

- 真正重要的是 / 真正决定 X 的是 / 本质上 / 核心在于 / 底层逻辑
- 赋能 / 认知升级 / 闭环 / 长期主义 / 关键抓手
- 历史性 / 全面 / 深刻 / 巨大 / 时代意义, when unsupported

Rules:

- Name the actual subject directly.
- Replace grand emphasis with evidence, action, condition, or consequence.
- Do not make every paragraph reach a conclusion.
- Do not scale a small event up to “the era / society / future” unless the material earns it.

### 3.2 Promotional Tone and Vague Authority

Watch for:

- 大幅提升 / 显著优化 / 全面赋能 without measurement.
- 业内人士认为 / 不少人表示 / 有研究显示 without a named source.
- 广泛关注 / 引发热议 without observable evidence.
- Generic praise, guaranteed outcomes, or branded optimism.

Rules:

- Delete unsupported intensity.
- Use a name, data point, scene, quotation, or reduce the claim.
- Never invent a source, number, action, or experience.

### 3.3 Formula Sentences

High-risk shells:

- 不是 A，而是 B / 并非 A，而是 B / 不在于 A，而在于 B
- 不只是 A，更是 B / 与其说 A，不如说 B
- 先 A，再 B / 第一步、第二步 / 从 A 到 B
- 这个问题很简单：/ 答案很简单：/ 这次只看……
- 观点句 + 解释 + 段尾总结, repeated across paragraphs

Rules:

- Keep a contrast only when A is a real reader belief, a character’s voice, or a necessary technical distinction.
- Keep sequence only when order changes the outcome.
- Delete ceremonial setup and enter the actual content.
- Do not build false opposition by first making the reader sound foolish.

### 3.4 Assistant Markers and Fake Engagement

Remove unless explicitly required:

- 总的来说 / 值得注意的是 / 不可否认的是 / 在这个过程中 / 这背后其实
- 下面我们来 / 接下来我会 / 我们可以看到 / 希望这能帮到你
- 划重点 / 拆一拆 / 捋一捋 / 盘一盘 / 聊一聊
- 你觉得呢？/ 你有没有类似经历？/ 是不是很有启发？

A question stays only when the user truly needs a CTA, poll, survey, or response prompt.

### 3.5 Uniform Paragraph Shape

Watch for:

- Paragraphs that are nearly equal in length and function.
- Repeated “claim → explanation → summary” architecture.
- Three or more parallel clauses with identical grammar and emotional pitch.
- One paragraph per sentence, pause, screen prompt, or glance.

Rules:

- Let paragraph lengths vary.
- Merge related movement, thought, speech, and memory.
- A short paragraph must mark a real turn: new information, interruption, changed decision, or a concrete image worth isolating.
- End paragraphs on a fact, object, scene, consequence, or unresolved decision rather than a slogan.

## 4. Register-Specific Rules

### 4.1 Fiction

#### Main Rule

Do not explain what dialogue, action, and objects already show.

#### Scene Pattern: Dialogue → Old Detail → Stop

For relationship scenes, arguments, misunderstandings, reunions, and quiet emotional turns:

1. Start with the immediate object, question, action, or line that causes friction. Do not begin with background explanation.
2. Let dialogue carry the argument in short, literal turns.
3. Do not polish dialogue into a debate. People repeat, dodge, answer half a question, change the subject, and say things a little clumsily.
4. After the exchange, place one compact paragraph of past habit or an ordinary old detail: a red pen, a rice bowl, an old bed, a routine, one line someone always says.
5. Let that object connect past and present. Do not explain its symbolism.
6. Stop before the author translates the emotion into a lesson.

#### Paragraphing

- Long paragraphs carry situation, movement, work, memory, and related action.
- Short paragraphs mark a true turn, interruption, or an image that needs air.
- Do not split every spoken line or pause into separate paragraphs.
- Do not aim for mechanically alternating long and short paragraphs. Let the scene determine the breath.

#### Dialogue

- Keep roughness, repetition, simple words, and slight mismatch when they reveal character.
- Speech tags are needed only for clarity or a meaningful gesture.
- Avoid replacing plain dialogue with clever, symmetrical, or aphoristic lines.
- Keep a formula shell in dialogue only when it belongs to the speaker.

#### Narration

- Prefer ordinary verbs: 看、扫、搁、说、写、走、停、等、抬、拿、放。
- Avoid decorative filler: 微微、缓缓、不禁、蓦地、猛然、若有所思、心中暗道, unless indispensable.
- Prefer action, sensory detail, and consequence over “他意识到”“她终于明白”“他感到愤怒”。
- Give worldbuilding only as much space as the immediate scene needs. Do not pause an emotional turn to explain the system.
- Let one physical detail arrive late and briefly. Do not interpret it immediately.

#### Endings

- Do not force a moral, a twist explanation, or a theme sentence.
- Do not end with “原来这说明了……”“不是考谁对，而是……”.
- End on an object, unfinished exchange, action, or residue when possible.

### 4.2 Commentary and Public Writing

- Keep the author’s judgment; do not pretend every objection deserves equal weight.
- Address only the real, central counterargument.
- Replace abstractions with observable stakes, people, scenes, documents, or consequences.
- Do not manufacture a grand historical ending.

### 4.3 Formal Reports and Technical Writing

- Preserve terms, citations, variables, compliance language, and qualified claims.
- Do not replace precision with colloquialism.
- If proof is missing, narrow or hedge the claim. Never invent a citation.
- Keep lists and sequences when operation, audit, or compliance requires them.

### 4.4 Social Posts and Short Public Writing

- Keep information density and readability.
- A hook is not mandatory; begin with the thing that needs saying.
- Avoid fake intimacy, exaggerated uplift, generic “save this” language, and comment bait.
- Use direct experience or concrete utility, not vague promises.

## 5. Output Modes

### Revision Only

Output the revised text with at most a brief note.

### Diagnosis + Revision

Use this order:

1. Diagnosis by category.
2. Correct-but-empty sentences.
3. What to delete and why.
4. First revision.
5. Residual-AI audit.
6. Final revision.

### Voice Calibration

State only observable style features. Do not claim certainty about private intent, personality, or life experience.

## 6. Final Quality Gate

Before finalizing, check all of the following:

- Meaning, facts, source boundaries, and author stance remain intact.
- No fact, quotation, number, named person, action, or personal experience was invented.
- The revision does not sound smoother, safer, or more generic than the original.
- Binary contrast, staged sequence, and grand conclusions remain only when justified.
- Sentence length and paragraph weight vary naturally.
- The text does not answer every objection or end every paragraph with a summary.
- No assistant route marker or fake engagement question remains unless requested.
- For fiction: emotion is carried by dialogue, action, object, or consequence—not author explanation.
- For fiction: paragraph breaks follow scene turns, not every line of speech.
- For fiction: the ending does not explain the story’s moral after the story has already shown it.

## 7. Quick Invocation Examples

- “用 remove-ai-flavor skill 检测这篇稿子的 AI 痕迹，先不要改。”
- “用 remove-ai-flavor skill 改这篇评论。先删能删的，再保留作者判断。”
- “用 remove-ai-flavor skill 改这篇小说：少分段，不解释人物情绪，对话后只用一件旧物或旧事接住关系。”
- “按作者样本校准这篇文章：保留句长和口头禅，不要升级成标准媒体腔。”

## Provenance

Adapted from B1lli/remove-ai-flavor-writing-skill (MIT), then expanded for Chinese editorial work: source boundaries, deletion-first revision, author-voice calibration, fiction paragraph rhythm, unpolished dialogue, and residual-AI audit.