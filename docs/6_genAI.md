# GenAI

生成式人工智能（Generative
AI）是一种能够产生**复杂有结构**的物件的机器系统。这里的**复杂性**指的是内容繁多到无法穷举，而**结构性**则
体现在这些物件是由有限的基本单位构成的。

<div style="text-align: center;">
  <img src="imgs/w6_1.png" alt="img" style="width: 80%;"/>
</div>

这种AI系统能够创造多种类型的内容，包**括文字、影像和声音**等，展现了机器在创造性任务中的多样化能力。
1. 文本
  - 由Token构成 关键问题：什么是Token？它与字符有什么区别？
2. 图像
   - 由像素(Pixel)构成
   - 每个像素包含颜色信息（BPP决定颜色深度） 关键问题：BPP如何影响图像的颜色表现？不同BPP (8, 16, 24, 32)的实际应用场景是什么？
       - Alpha 通道非常有意思
3. 声音
   - 由采样点(Sample)构成
   - 采样率决定每秒采样次数 关键问题：高采样率（如16kHz）是如何在物理上实现的？采样率如何影响音频质量？

图像生成、音乐创作也是文字接龙？ AR vs NAR 需要权衡利弊， 解决方案是什么？

- 产生随机数用于确定脑补的内容
- Autoregressive + Non-autoregressive
- multi-stage generation

这课程用一种非常漂亮的逻辑讲述梳理了经典图像生产方法：
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/w6_2.png" alt="img1" style="width: 48%;"/>
  <img src="imgs/w6_3.png" alt="img2" style="width: 48%;"/>
</div>

特别是对VAE中将输入编码为高斯噪声的解释，让我对这个概念有了新的理解。 视频生产领域的佼佼者如何生成：
<div style="display: flex; justify-content: space-between;">
  <img src="imgs/w6_5.png" alt="img1" style="width: 48%;"/>
  <img src="imgs/w6_4.png" alt="img2" style="width: 48%;"/>
</div>

此外，还有许多印象深刻的内容，比如说：

- 在多模态大模型中，patch 的概念在某些方面类似于大语言模型中的 token，对 patch 概念的抽丝剥茧阐述，让我对这个概念有了更深刻的理解。
- RLHF 有点像 GAN，但是不同的是 RLHF 是有监督的，而 GAN 是无监督的。
- 图片生成图片包括图片完成，风格转化，画质提升等等，Talking head 是一个有趣的应用。
- Genie(Generative Interactive Environments), 直接操作图片中的人物？非常有趣。


这节课的内容深入且广泛，需要多次复习才能完全消化。虽然现在还有些概念不太明确，但这些内容激发了我深入学习的兴趣。
所以有一个专门[课程笔记](https://swze06osuex.feishu.cn/docx/CNo1dz9LGoCyRDxFKABcUVbcnfb) 来记录这些内容，希望能够帮助我更好地理解这些概念。

