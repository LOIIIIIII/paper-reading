# Can Video World Models Track Unobserved World States? · 论文阅读笔记

> 研究方向：世界模型 · 不可观测状态追踪（Unobserved State Tracking）

## 基本信息
- 标题：Can Video World Models Track Unobserved World States?
- 作者：Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang
- arXiv：2608.30692
- 日期：2026-08-31
- 项目主页：https://joonghyuk.com/stateful-vwm-web/

## 一句话总结
会生成逼真视频，不代表模型真的知道“世界现在是什么状态”；长期 hidden-state tracking 需要可跨 chunk 持续携带、且能被原地改写的内部状态。

## 核心实验
动作条件视频 Shell Game：先看到球在哪个杯子下，之后球被完全遮挡；输入一串杯子交换动作，模型自回归生成所有 swap 与最终揭示。训练只用 5-swap，测试外推到更长链。

## S3 / S5
S3 / S5 是 3 / 5 个元素的对称群。一次 swap 是一个 transposition；长序列状态追踪就是不断组合 permutation。作者先做符号 probe，再视觉化成 Shell Game。

## 主要发现
1. Transformer、Mamba2、标准非负特征值线性注意力能拟合 N=5，但长链外推趋近随机。
2. 视频仍可以保持高视觉保真度，说明 visual fidelity 与 hidden-state accuracy 分离。
3. 增加 diffusion denoising steps 只改善渲染，不增加所需的串行状态计算深度。
4. Transformer KV cache 更像 append-only visual history，而不是 compact running state。
5. GDN-neg 通过允许负特征值，使状态转移可表达类似 reflection / swap 的操作。
6. LaCT 用 nonlinear TTT fast weights 作为可持续改写的工作记忆；更新 feature map 比只更新 readout 更关键。

## 和遮挡的关系
Shell Game 是“visible → hidden → state still evolves → reveal”的受控抽象，不是自动驾驶遮挡本身。真正可迁移的是 persistent state + expressive/revisable transition，而不是 reflection 这一 S5 特化技巧。

## 对我们课题的启发
本文解决的是“hidden state 怎么存、怎么更新”，但没有解决“隐藏区间怎么获得真实监督”。同步多车/多视角可以进一步作为 privileged training supervision：当 ego 看不到某状态而其他同步观察者能看到时，用后者为 ego world model 的监督空窗期提供真实约束；测试仍保持单车推理。
