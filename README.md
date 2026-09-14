# Paper Reading · 自动驾驶世界模型「解耦」方向

> 🌐 **在线阅读网页（GitHub Pages）**：
>
> ## 👉 https://loiiiiiii.github.io/paper-reading/
>
> 打开即可阅读排版好的论文笔记，无需下载。

本仓库用于记录**自动驾驶世界模型 · 解耦（Decoupling）方向**的论文阅读笔记。核心关注问题：

> 观测 = 物理世界演化（F） + 观测过程（G）。
> 世界模型如何把"世界本身的变化"与"观察者自身运动带来的视角变化"解耦，学到真正符合物理规律的场景动力学？

---

## 📚 已收录笔记

| 论文 | 主题 | 笔记 |
|---|---|---|
| **FR3D**：*Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion*（arXiv 2606.18250, TUM & BMW） | Ego-Motion / World-Motion 解耦 · 未来动态 3D 重建 | [FR3D_论文阅读笔记.md](notes/FR3D_论文阅读笔记.md) ｜ [网页版](https://loiiiiiii.github.io/paper-reading/) |

## 📖 笔记内容框架

每篇笔记统一按以下框架整理，方便组会汇报与横向对比：

1. 论文基本信息
2. 任务定义（在"解耦"视角下归纳）
3. 任务背景与动机
4. 解决了什么问题
5. 创新点（方法细节）
6. 实验结果
7. 与我们方法（同步多车动态解耦）的对比
8. 不足之处
9. 可借鉴点与启发

## 🗂 仓库结构

```
paper-reading/
├── README.md                          # 本文件（仓库首页）
├── notes/                             # 论文阅读笔记 Markdown
│   └── FR3D_论文阅读笔记.md
└── docs/                              # GitHub Pages 网页
    └── index.html                     # 在线阅读页面
```

## 🔗 相关链接

- 论文原文：https://arxiv.org/html/2606.18250v1
- FR3D 项目主页：https://fr3d-wm.github.io

---
*Maintained by [@LOIIIIIII](https://github.com/LOIIIIIII) · 2026*
