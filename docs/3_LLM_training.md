# LLM Training：从文字接龙到通用AI

## 训练大语言模型就是玩高级文字接龙

李宏毅老师把整个训练过程比喻成文字接龙，这个比喻简直绝了！看看这个基本框架：

<div style="display: flex; justify-content: center;">
  <img src="imgs/w3_1.png" alt="img1" style="width: 45%; margin-right: 10px;"/>
  <img src="imgs/w3_2.png" alt="img2" style="width: 45%;"/>
</div>

整个过程分三个阶段：pretrain, SFT, RLHF。每一步都是在为下一步打基础，就像堆积木一样，一层比一层高级。

## 本周课程的精彩之处

老李这次又是干货满满，我们一个一个来品：

1. **文字接龙的艺术**
   把 next token prediction说成文字接龙，瞬间就能get到点了。这哥们儿讲故事的本事真是一流。

2. **数据质量才是王道**
   讲到pre-train corpus，老李强调了数据质量过滤和去重的重要性。最近两篇论文"Quality is all you need"[1]和"Less is more for alignment"[2]也在狠狠地强调这一点。看来以后大家比的就是谁的数据更香了。

3. **从BERT到GPT：专才到通才的进化**
   - BERT时代：多个NLP任务dataset -> QA dataset，搞得挺麻烦。
   - GPT时代：直接上通才模式。毕竟人类问题千奇百怪，与其费劲巴拉地标注，不如直接学习回答各种问题。
   - "Quality is all you need"[1]和"Less is more for alignment"[2]这两篇论文简直是GPT路线的最佳注脚。

4. **SFT：让模型懂规矩**
   老李讲SFT的动机时，用了不少生动的例子。从不受控的GPT-3到后来的各种instruction-following模型，这个进化过程讲得是真清楚。

5. **RLHF：模型开挂的秘诀**
   - 展示了ChatGPT如何收集人类反馈数据，这个很直观。
   - Online RL 需要 在当前策略下收集偏好数据的重要性。这个需要注意！
   - 奖励模型模拟人类偏好，给出即时反馈信号，让LLM有了超越人类的可能。但是老李也提醒我们，过度学习可能导致reward hacking，这个警示很及时。

6. **Next Token Prediction其实是多任务学习**
   这个观点我第一次是在Andrej Karpathy的斯坦福讲座里听到的[3]。再联系到GPT的通才路线，突然觉得这个观点太有道理了。每预测一个token，模型其实都在学习各种不同的任务。这不就是在朝着通用AI进发吗？

7. 老李提到了个性化回答的重要性，一个有趣的例子：NTU到底是国立台湾大学还是南洋理工大学？不同用户，台湾人还是新加坡人，答案会有所不同，所以 Personalized LLM 很重要！

总的来说，这节课把LLM训练的来龙去脉讲得明明白白，既有高度又有细节。老李这课，值！

## 参考文献

[1] Papakipos, Z., & Krishnan, S. (2023). Quality is all you need: How to improve large language models with high-quality data. arXiv preprint arXiv:2310.09363.

[2] Zhou, D., Shi, B., Chen, C., Zhang, Y., & Yu, N. (2023). Less is more for alignment: Refining language models with limited data. arXiv preprint arXiv:2310.14303.

[3] Karpathy, A. (2023). State of GPT. [YouTube Video]. https://www.youtube.com/watch?v=bZQun8Y4L2A




# 作业

- [quick start for SFT](https://github.com/AXYZdong/AMchat/blob/main/plus/02-InternLM2-Math-Plus-7B%20%E5%BE%AE%E8%B0%83.md)
- [quick start for DPO]()