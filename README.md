# Paper Reading · 论文与技术研究笔记

> 🌐 [在线阅读（GitHub Pages）](https://loiiiiiii.github.io/paper-reading/)

本仓库按“研究问题”组织世界模型论文与 LLM Serving 技术笔记。

## 研究方向

### 1. 自动驾驶世界模型 · 解耦
关注 ego-motion / world-motion、场景动力学 / 观测过程分离，以及多视角一致性。

- FR3D — *Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion*

### 2. 世界模型 · 不可观测状态追踪
关注部分可观测、遮挡、persistent state、revisable state、long-horizon state tracking。

- *Can Video World Models Track Unobserved World States?* — arXiv:2608.30692 (2026)

### 3. LLM Serving / Inference Systems
从单请求推理生命周期出发，梳理排队、并发、Static / Dynamic / Continuous Batching、Prefill / Decode、KV Cache、ORCA、vLLM，以及 Ollama / Qwen3.5 的并行适配。

- *LLM Serving 研究笔记：从单请求串行推理到 Continuous Batching* — 16 个章节、14 张 SVG 技术图，运行时状态记录于 2026-10-14。
- [并发 Streaming 时间线验证脚本](examples/concurrency_probe.py)

## 阅读入口

世界模型笔记采用三级导航：**项目首页 → 研究方向 → 论文页面**；LLM Serving 单页长篇笔记可从首页直接进入。

| 研究方向 | 论文 | Markdown 笔记 | 在线阅读 |
|---|---|---|---|
| 自动驾驶世界模型 · 解耦 | FR3D | [笔记](notes/FR3D_论文阅读笔记.md) | [项目首页](https://loiiiiiii.github.io/paper-reading/) → [解耦方向](https://loiiiiiii.github.io/paper-reading/decoupling/) → [FR3D](https://loiiiiiii.github.io/paper-reading/decoupling/fr3d.html) |
| 世界模型 · 不可观测状态追踪 | Can Video World Models Track Unobserved World States? | [笔记](notes/Can_Video_World_Models_Track_Unobserved_World_States_论文阅读笔记.md) | [项目首页](https://loiiiiiii.github.io/paper-reading/) → [不可观测状态追踪](https://loiiiiiii.github.io/paper-reading/unobserved-state/) → [论文页](https://loiiiiiii.github.io/paper-reading/unobserved-state/can-video-world-models-track-unobserved-world-states.html) |
| LLM Serving / Inference Systems | 从单请求串行推理到 Continuous Batching | [HTML 笔记源码](docs/llm-serving/index.html) | [阅读完整笔记](https://loiiiiiii.github.io/paper-reading/llm-serving/) |

## 目录结构

```text
docs/
├── index.html
├── decoupling/
│   ├── index.html
│   └── fr3d.html
├── unobserved-state/
│   ├── index.html
│   └── can-video-world-models-track-unobserved-world-states.html
└── llm-serving/
    ├── index.html
    ├── style.css
    ├── script.js
    └── assets/                         # 14 张 SVG 技术图

notes/
├── FR3D_论文阅读笔记.md
└── Can_Video_World_Models_Track_Unobserved_World_States_论文阅读笔记.md

examples/
└── concurrency_probe.py
```

## 维护网页

FR3D 的原始 Markdown 笔记仍在 `notes/FR3D_论文阅读笔记.md`；需要重新生成其网页时，安装 Python `markdown` 包并运行 `python3 tools/build_site.py`。生成目标是 `docs/decoupling/fr3d.html`，不会覆盖研究方向首页。

新论文的 [论文原文](https://arxiv.org/html/2608.30692) 提供方法与 Figure 4/5 的核对依据。网站由 GitHub Pages 从 `docs/` 发布，原有图片仍保留在 `docs/images/`。

LLM Serving 页面是独立静态 HTML，直接维护 `docs/llm-serving/` 下的文章、样式、脚本与配图即可。其运行时兼容性说明保留了原笔记的状态日期。

## 并发验证示例

安装 `aiohttp`（`python3 -m pip install aiohttp`），启动本地 Ollama 服务并准备 `llama3.2:3b` 模型后，运行 `python3 examples/concurrency_probe.py`，可查看 4 条并发请求的开始、首次流数据返回与结束时间。脚本默认连接 `http://localhost:11434/api/chat`；需要更换模型或服务地址时，修改脚本中的 `MODEL` 与 `URL`。

Maintained by @LOIIIIIII · 2026
