# codex-practice

我的 AI 编程实验仓库。

## 已实现功能（参考 Horizon 思路）

新增了一个 **Horizon Mini**：一个轻量的 AI 新闻雷达原型，核心流程包括：

- 从多个 RSS 源拉取内容
- 去重并截断到指定条目数
- 生成中英双语标题的 Markdown 日报

## 使用方法

```bash
cp config.example.json config.json
python3 horizon_mini.py --config config.json --output docs/daily.md
```

运行后会生成 `docs/daily.md`。

## 目标

- 学习 GitHub
- 学习 Codex
- 学习 AI 自动化
- 用 AI 做真实项目
