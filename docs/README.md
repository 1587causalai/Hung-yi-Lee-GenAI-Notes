# Hung-yi Lee GenAI 2024 Course Notes

## 项目简介

结合[书生·浦语参大模型实战营](https://openxlab.org.cn/models/InternLM/subject)的内容，系统化学习李宏毅老师 2024
年[《生成式人工智能导论》](https://speech.ee.ntu.edu.tw/~hylee/genai/2024-spring.php). 我们将：

1. 跟随李宏毅老师 2024 年《生成式人工智能导论》课程的进度，系统学习理论知识。
2. 结合书生·浦语参大模型实战营的内容，进行实践操作和项目实战。
3. 整理、总结和分享学习过程中的笔记、见解和资源。

通过这种理论与实践相结合的方法，我们旨在为进入这个快速发展的领域奠定坚实的基础。 常用资料链接：
- [B站课程视频](https://www.bilibili.com/video/BV1BJ4m1e7g8?p=2&vd_source=d3d6c6260e5259a5e1b8b098679a13da)
- github: https://github.com/InternLM/Tutorial/tree/camp3
- 学员手册：https://aicarrier.feishu.cn/wiki/XBO6wpQcSibO1okrChhcBkQjnsf
- 个人笔记 [飞书文档](https://swze06osuex.feishu.cn/wiki/QEj6w26WsigOyJkRxWyck6qVnQe?fromScene=spaceOverview) & [github](https://github.com/1587causalai/InternLM-Tutorial-Personalized-LLM-Research-Assistent).

## 项目意义

这个项目的意义在于，展示一个学生的角色，去学习生成式AI的理论知识，同时也要参与实践操作，最终达到对生成式AI的全面理解。
由于大语言模型领域涵盖众多重要课题、应用和技术，我们不得不有所取舍，选择性地重点关注：
- 从增量预训练，到SFT，再到RLHF，这个过程是如何实践操作的
- ...

请注意本项目**不会**:
- 全面完整的梳理李宏毅老师的课程内容，仅仅是个性做一个非常精简的总结，并且记录个人觉得特有意思的关键知识点。

## 🔥News

- [2024/07/18] 从基于 MedicalGPT 的模型定制出发, 重新理解模型对齐所有的细节，包括IPT/SFT/RLHF。
- [2024/07/12] 完成实战营入门岛作业 [github](https://github.com/1587causalai/InternLM-Tutorial-Personalized-LLM-Research-Assistent)
- [2024/07/04] 参考[MedicalGPT](https://github.com/shibing624/MedicalGPT)完成模型训练(IPT/SFT/RLHF)流程。
- [2024/07/02] 李宏毅老师的课程课程笔记基本完成。


## 内容结构

- [0_course_intro](0_course_intro.md)：课程介绍和总体框架
- [1_intro_to_genAI](1_intro_to_genAI.md)：生成式 AI 概述
- [2_prompt_engineering](2_prompt_engineering.md)：提示工程技术
- [3_LLM_training](3_LLM_training.md)：大型语言模型训练
- [4_evaluation_and_ethics](4_evaluation_and_ethics.md)：评估方法和伦理考量
- [5_explainability](5_explainability.md)：可解释性研究
- [6_genAI](6_genAI.md)：多模态大模型
- [GPT4o](GPT4o.md)


## 项目特点

1. **系统化学习**：按照李宏毅老师课程的主题结构组织内容，确保全面覆盖关键知识点。

2. **理论结合实践**：我们将结合书生·浦语参大模型实战营的内容，深化对理论知识的理解，并获得实际操作经验。

3. **持续更新**：随着课程进展和技术发展，本仓库将不断更新和完善。

4. **开放讨论**：欢迎其他学习者参与讨论，分享见解，共同提高。


## 参考资源

- [李宏毅老师课程官方页面](https://speech.ee.ntu.edu.tw/~hylee/genai/2024-spring.php)
- [书生·浦语参大模型实战营](https://openxlab.org.cn/models/InternLM/subject)
- [快速课程笔记](https://swze06osuex.feishu.cn/docx/CNo1dz9LGoCyRDxFKABcUVbcnfb?from=from_copylink)

## 贡献

欢迎通过 Issues 或 Pull Requests 提供反馈、建议或贡献内容。让我们一起学习和探索生成式 AI 的精彩世界！

---

## 分支说明

- **master**: 包含基于李宏毅老师 2024 年《生成式人工智能导论》课程和书生·浦语实战营的笔记和实践内容。
- **note2025**: 一个新的实验性分支，用于整理李宏毅老师 **2025 年** 生成式 AI 课程的笔记，特别是关于 **AI Agent** 和 **非 Transformer 架构** 的内容。该分支为未来学习规划和初步探索。