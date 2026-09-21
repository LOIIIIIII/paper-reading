# Paper Reading · 世界模型研究笔记

> 🌐 GitHub Pages：`https://loiiiiiii.github.io/paper-reading/`

本仓库按“研究问题”组织世界模型论文，而不是把所有论文放在单一页面。

## 研究方向

### 1. 自动驾驶世界模型 · 解耦
关注 ego-motion / world-motion、场景动力学 / 观测过程分离，以及多视角一致性。

- FR3D — *Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion*

### 2. 世界模型 · 不可观测状态追踪
关注部分可观测、遮挡、persistent state、revisable state、long-horizon state tracking。

- *Can Video World Models Track Unobserved World States?* — arXiv:2608.30692 (2026)

## 阅读入口

网站采用三级导航：**项目首页 → 研究方向 → 论文页面**。

| 研究方向 | 论文 | Markdown 笔记 | 在线阅读 |
|---|---|---|---|
| 自动驾驶世界模型 · 解耦 | FR3D | [笔记](notes/FR3D_论文阅读笔记.md) | [项目首页](https://loiiiiiii.github.io/paper-reading/) → [解耦方向](https://loiiiiiii.github.io/paper-reading/decoupling/) → [FR3D](https://loiiiiiii.github.io/paper-reading/decoupling/fr3d.html) |
| 世界模型 · 不可观测状态追踪 | Can Video World Models Track Unobserved World States? | [笔记](notes/Can_Video_World_Models_Track_Unobserved_World_States_论文阅读笔记.md) | [项目首页](https://loiiiiiii.github.io/paper-reading/) → [不可观测状态追踪](https://loiiiiiii.github.io/paper-reading/unobserved-state/) → [论文页](https://loiiiiiii.github.io/paper-reading/unobserved-state/can-video-world-models-track-unobserved-world-states.html) |

## 目录结构

```text
docs/
├── index.html
├── decoupling/
│   ├── index.html
│   └── fr3d.html
└── unobserved-state/
    ├── index.html
    └── can-video-world-models-track-unobserved-world-states.html

notes/
├── FR3D_论文阅读笔记.md
└── Can_Video_World_Models_Track_Unobserved_World_States_论文阅读笔记.md
```

## 维护网页

FR3D 的原始 Markdown 笔记仍在 `notes/FR3D_论文阅读笔记.md`；需要重新生成其网页时，安装 Python `markdown` 包并运行 `python3 tools/build_site.py`。生成目标是 `docs/decoupling/fr3d.html`，不会覆盖研究方向首页。

新论文的 [论文原文](https://arxiv.org/html/2608.30692) 提供方法与 Figure 4/5 的核对依据。网站由 GitHub Pages 从 `docs/` 发布，原有图片仍保留在 `docs/images/`。

Maintained by @LOIIIIIII · 2026
