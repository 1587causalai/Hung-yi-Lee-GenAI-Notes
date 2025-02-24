# PPO基础-策略梯度定理

李宏毅老师并不赞同这种讲法, 他的出发点是:


$$J = \mathbb{E}_{\tau \sim p_\theta(\tau)} [\sum_t A_t e_t] = \mathbb{E}_{\tau \sim p_\theta(\tau)} [\sum_t \log(\pi_\theta(a_t | s_t))^{A_t}]$$

where $e_t = \log \pi_\theta(a_t | s_t)$ 是动作被偏好的评价(评价越高, 动作被采样的概率越大, 是动作被偏好概率的单调递增关系), 而 $A_t$ 是优势函数, 衡量动作 $a_t$ 的优劣, $A_t$ 越大说明该动作 $a_t$ 将会产生越大的奖励. 请注意 $a^x(a \in (0, 1))$, 是关于 $x$ 单调递减非负函数. 所以总是要选择 $A_t$ 大的动作. 


## **什么是策略梯度定理？**

在强化学习中，智能体（agent）通过与环境（environment）交互，执行动作（action），获得奖励（reward），目标是最大化长期的累积奖励。**策略（policy）**定义了智能体如何根据当前状态（state）选择动作，通常表示为一个参数化的概率分布函数，例如 \( \pi_\theta(a|s) \)，其中 \(\theta\) 是策略的参数（比如神经网络的权重）。

**策略梯度方法**是一种直接优化策略参数 \(\theta\) 的方法，目的是最大化预期的累积奖励 \( J(\theta) \)。这个预期回报定义为：

\[ J(\theta) = \mathbb{E}_{\tau \sim p_\theta(\tau)} [R(\tau)] \]

- \(\tau\) 是一个**轨迹（trajectory）**，表示从初始状态到终止状态的一系列状态和动作：\(\tau = (s_0, a_0, s_1, a_1, ..., s_T, a_T)\)；
- \(p_\theta(\tau)\) 是轨迹 \(\tau\) 在策略 \(\pi_\theta\) 下的概率；
- \(R(\tau)\) 是轨迹 \(\tau\) 的累积奖励，通常是所有奖励之和：\(R(\tau) = \sum_{t=0}^T r_t\)。

**策略梯度定理**提供了一种计算 \( J(\theta) \) 关于 \(\theta\) 的梯度 \(\nabla_\theta J(\theta)\) 的方法，使得我们可以通过梯度上升来优化策略。其核心表达式为：

\[ \nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim p_\theta(\tau)} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) Q^{\pi_\theta}(s_t, a_t) \right] \]

- \(\pi_\theta(a_t | s_t)\) 是策略在状态 \(s_t\) 下选择动作 \(a_t\) 的概率；
- \(Q^{\pi_\theta}(s_t, a_t)\) 是**动作-价值函数**，表示在状态 \(s_t\) 执行动作 \(a_t\) 后，遵循策略 \(\pi_\theta\) 所能获得的预期累积奖励。

这个定理的优点在于，梯度被表示为一个期望形式，我们可以通过采样轨迹来估计它，而**无需知道环境的具体动态模型（即状态转移概率）**。接下来，我们详细推导这个定理。

---

## **推导过程**

为了推导策略梯度定理，我们需要一步步分解问题，从轨迹概率的定义开始，最终得到梯度的期望形式。

### 基本思路

#### 策略梯度的严格证明

在强化学习中，策略梯度方法的目标是通过梯度上升优化策略参数 \(\theta\)，从而最大化期望回报 \(J(\theta)\)。期望回报 \(J(\theta)\) 定义为智能体在环境中的累积奖励的期望值。我们将严格推导策略梯度的表达式，最终得到以下形式：

\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) A_t \right]
\]

其中：
- \(\tau = \{s_0, a_0, r_0, s_1, a_1, r_1, \dots, s_T, a_T, r_T\}\) 是智能体按照策略 \(\pi_\theta\) 生成的轨迹。
- \(A_t = Q(s_t, a_t) - V(s_t)\) 是优势函数。
- \(\nabla_\theta \log \pi_\theta(a_t | s_t)\) 是策略的对数概率的梯度。

以下是详细的推导步骤。

---

#### **第一步：定义基本概念**

在开始推导之前，我们先明确一些强化学习中的基本定义：

1. **状态（State）**：智能体所处的环境状态，记作 \(s\)。
2. **动作（Action）**：智能体在状态 \(s\) 下可以采取的行动，记作 \(a\)。
3. **策略（Policy）**：智能体在给定状态 \(s\) 下选择动作 \(a\) 的概率分布，记作 \(\pi(a|s)\)。在参数化策略下，用 \(\pi_\theta(a|s)\) 表示，其中 \(\theta\) 是策略的参数。
4. **即时奖励（Reward）**：在时间步 \(t\)，智能体从环境中获得的奖励，记作 \(r_t\)。
5. **回报（Return）**：从时间步 \(t\) 开始到轨迹结束的累积折扣奖励，记作：
   \[
   R_t = \sum_{k=t}^T \gamma^{k-t} r_k
   \]
   其中 \(\gamma \in [0, 1]\) 是折扣因子。
6. **状态价值函数（State Value Function）**：
   \[
   V^\pi(s) = \mathbb{E}_\pi[R_t | s_t = s]
   \]
   表示从状态 \(s\) 开始，遵循策略 \(\pi\) 的期望回报。
7. **动作价值函数（Action Value Function）**：
   \[
   Q^\pi(s, a) = \mathbb{E}_\pi[R_t | s_t = s, a_t = a]
   \]
   表示在状态 \(s\) 下选择动作 \(a\)，然后遵循策略 \(\pi\) 的期望回报。
8. **优势函数（Advantage Function）**：
   \[
   A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)
   \]
   衡量在状态 \(s\) 下选择动作 \(a\) 相对于平均水平的优劣。
9. **目标函数（Objective Function）**：期望回报 \(J(\theta)\)，定义为：
   \[
   J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \gamma^t r_t \right]
   \]
   其中 \(\tau \sim \pi_\theta\) 表示轨迹 \(\tau\) 是根据策略 \(\pi_\theta\) 生成的。

我们的目标是最大化 \(J(\theta)\)，为此需要计算 \(\nabla_\theta J(\theta)\)，即 \(J(\theta)\) 关于策略参数 \(\theta\) 的梯度。

---

#### **第二步：轨迹的概率分布**

一条轨迹 \(\tau = \{s_0, a_0, r_0, s_1, a_1, r_1, \dots, s_T, a_T, r_T\}\) 的概率分布为：

\[
p(\tau | \theta) = p(s_0) \prod_{t=0}^T \pi_\theta(a_t | s_t) p(s_{t+1} | s_t, a_t)
\]

其中：
- \(p(s_0)\) 是初始状态的分布，与 \(\theta\) 无关。
- \(\pi_\theta(a_t | s_t)\) 是策略，给出了在状态 \(s_t\) 下选择动作 \(a_t\) 的概率。
- \(p(s_{t+1} | s_t, a_t)\) 是环境的状态转移概率，取决于环境动态，与 \(\theta\) 无关。

轨迹的回报为：
\[
R(\tau) = \sum_{t=0}^T \gamma^t r_t
\]

因此，期望回报 \(J(\theta)\) 可以写成积分形式：
\[
J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} [R(\tau)] = \int p(\tau | \theta) R(\tau) d\tau
\]

---

#### **第三步：计算期望回报的梯度**

为了优化 \(J(\theta)\)，需要计算梯度 \(\nabla_\theta J(\theta)\)：
\[
\nabla_\theta J(\theta) = \nabla_\theta \int p(\tau | \theta) R(\tau) d\tau
\]

在满足一定条件下（例如积分和导数的可交换性），我们可以将导数移到积分内部：
\[
\nabla_\theta J(\theta) = \int \nabla_\theta p(\tau | \theta) R(\tau) d\tau
\]

---

#### **第四步：使用对数导数技巧**

为了计算 \(\nabla_\theta p(\tau | \theta)\)，我们使用对数导数技巧。注意到：
\[
\nabla_\theta \log p(\tau | \theta) = \frac{\nabla_\theta p(\tau | \theta)}{p(\tau | \theta)}
\]
因此：
\[
\nabla_\theta p(\tau | \theta) = p(\tau | \theta) \nabla_\theta \log p(\tau | \theta)
\]

将此代入梯度表达式：
\[
\nabla_\theta J(\theta) = \int p(\tau | \theta) \nabla_\theta \log p(\tau | \theta) R(\tau) d\tau
\]

这可以写成期望形式：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log p(\tau | \theta) R(\tau) \right]
\]

---

#### **第五步：计算 \(\nabla_\theta \log p(\tau | \theta)\)**

接下来，我们计算 \(\nabla_\theta \log p(\tau | \theta)\)。首先，写出 \(\log p(\tau | \theta)\)：
\[
\log p(\tau | \theta) = \log p(s_0) + \sum_{t=0}^T \log \pi_\theta(a_t | s_t) + \sum_{t=0}^T \log p(s_{t+1} | s_t, a_t)
\]

对 \(\theta\) 求导：
\[
\nabla_\theta \log p(\tau | \theta) = \nabla_\theta \left( \log p(s_0) + \sum_{t=0}^T \log \pi_\theta(a_t | s_t) + \sum_{t=0}^T \log p(s_{t+1} | s_t, a_t) \right)
\]

注意到：
- \(\log p(s_0)\) 与 \(\theta\) 无关，导数为零。
- \(\log p(s_{t+1} | s_t, a_t)\) 是状态转移概率，与 \(\theta\) 无关，导数为零。
- 只有 \(\log \pi_\theta(a_t | s_t)\) 依赖于 \(\theta\)。

因此：
\[
\nabla_\theta \log p(\tau | \theta) = \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t)
\]

---

#### **第六步：代入梯度表达式**

将 \(\nabla_\theta \log p(\tau | \theta)\) 代入 \(\nabla_\theta J(\theta)\)：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \left( \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) \right) R(\tau) \right]
\]

由于期望是线性的，可以写成：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) R(\tau) \right]
\]

---

#### **第七步：引入因果性**

目前，梯度表达式中的 \(R(\tau)\) 是整个轨迹的回报，包含了过去和未来的奖励。然而，在时间步 \(t\) 处的策略更新应该只依赖于从 \(t\) 开始的未来回报，而不是过去的回报。这是策略梯度的因果性。

定义从时间步 \(t\) 开始的未来回报：
\[
R_t = \sum_{k=t}^T \gamma^{k-t} r_k
\]

我们可以证明：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) R_t \right]
\]

**证明因果性：**

为了证明这一点，我们需要利用条件期望和因果性。考虑 \(\nabla_\theta \log \pi_\theta(a_t | s_t)\)，它只依赖于时间步 \(t\) 的动作 \(a_t\) 和状态 \(s_t\)。对于 \(t' < t\)，过去的奖励 \(r_{t'}\) 与 \(\nabla_\theta \log \pi_\theta(a_t | s_t)\) 是独立的，因为策略在 \(t\) 处的选择不影响过去的奖励。

通过数学推导（涉及条件期望的分解），我们可以将 \(R(\tau)\) 替换为 \(R_t\)。这是策略梯度定理的核心部分，具体推导较为复杂，但结果是直观的：策略更新只依赖于未来的回报。

---

#### **第八步：引入基线以减小方差**

当前的策略梯度表达式为：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) R_t \right]
\]

然而，\(R_t\) 是未来的累积回报，具有较大的随机性，会导致梯度估计的高方差。为了减小方差，我们引入一个基线 \(b(s_t)\)，它不依赖于动作 \(a_t\)。策略梯度变为：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) (R_t - b(s_t)) \right]
\]

需要证明引入基线不会改变梯度的期望值。考虑：
\[
\mathbb{E}_{a_t \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(a_t | s_t) b(s_t)]
\]

由于 \(b(s_t)\) 不依赖于 \(a_t\)，可以提出：
\[
\mathbb{E}_{a_t \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(a_t | s_t) b(s_t)] = b(s_t) \mathbb{E}_{a_t \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(a_t | s_t)]
\]

而：
\[
\nabla_\theta \log \pi_\theta(a_t | s_t) = \frac{\nabla_\theta \pi_\theta(a_t | s_t)}{\pi_\theta(a_t | s_t)}
\]

因此：
\[
\mathbb{E}_{a_t \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(a_t | s_t)] = \int \pi_\theta(a_t | s_t) \cdot \frac{\nabla_\theta \pi_\theta(a_t | s_t)}{\pi_\theta(a_t | s_t)} da_t = \nabla_\theta \int \pi_\theta(a_t | s_t) da_t = \nabla_\theta 1 = 0
\]

所以：
\[
\mathbb{E}_{a_t \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(a_t | s_t) b(s_t)] = 0
\]

这表明引入基线不会改变梯度的期望值，但可以减小方差。

---

#### **第九步：选择基线，使用优势函数**

一个常用的基线是状态价值函数 \(V^\pi(s_t)\)。当 \(b(s_t) = V^\pi(s_t)\) 时：
\[
R_t - V^\pi(s_t)
\]
近似于优势函数 \(A_t = Q^\pi(s_t, a_t) - V^\pi(s_t)\)。因此，策略梯度可以写成：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) A_t \right]
\]

其中 \(A_t\) 是优势函数的估计。优势函数的优点是：
- 当 \(A_t > 0\) 时，说明动作 \(a_t\) 比平均水平好，梯度会增加 \(\pi_\theta(a_t | s_t)\) 的概率。
- 当 \(A_t < 0\) 时，说明动作 \(a_t\) 比平均水平差，梯度会减少 \(\pi_\theta(a_t | s_t)\) 的概率。

---

#### **第十步：优势函数的估计**

在实践中，优势函数 \(A_t\) 需要通过估计获得。常用的方法包括：
- **蒙特卡洛估计**：用实际回报 \(R_t\) 替代 \(Q(s_t, a_t)\)，然后用估计的 \(V(s_t)\) 计算 \(A_t = R_t - V(s_t)\)。
- **时序差分（TD）方法**：用单步或多步的TD误差来估计 \(A_t\)，例如：
  \[
  A_t \approx r_t + \gamma V(s_{t+1}) - V(s_t)
  \]
  （对于TD(0)）。

这些估计方法在实践中可以结合使用，以平衡偏差和方差。

---


#### **总结**

通过以上推导，我们得到了策略梯度的严格表达式：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) A_t \right]
\]

其中：
- \(\nabla_\theta \log \pi_\theta(a_t | s_t)\) 是策略的对数概率的梯度，决定了更新的方向。
- \(A_t = Q(s_t, a_t) - V(s_t)\) 是优势函数，衡量动作 \(a_t\) 的优劣。
- 期望是对轨迹 \(\tau \sim \pi_\theta\) 的采样均值。

这个表达式是策略梯度方法的基础，PPO（Proximal Policy Optimization）等现代强化学习算法在此基础上通过引入信任区域约束（如KL散度或裁剪目标函数）来进一步稳定训练过程。

### 关键步骤

好的，我会根据你的要求，详细推导如何通过数学方法（特别是条件期望的分解）将策略梯度中的 \(R(\tau)\) 替换为 \(R_t\)。这是策略梯度定理的核心部分，我会一步步展开，确保推导完整且清晰。

---

#### **目标**
我们要证明策略梯度定理的因果性形式，即：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) R_t \right]
\]
其中：
- \(J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} [R(\tau)]\) 是期望回报，\(\theta\) 是策略 \(\pi_\theta\) 的参数。
- \(\tau = (s_0, a_0, s_1, a_1, \dots, s_T, a_T)\) 是由策略 \(\pi_\theta\) 生成的轨迹。
- \(R(\tau) = \sum_{t=0}^T \gamma^t r_t\) 是整个轨迹的折扣回报，\(\gamma \in [0, 1]\) 是折扣因子。
- \(R_t = \sum_{k=t}^T \gamma^{k-t} r_k\) 是从时间步 \(t\) 开始的未来折扣回报。

我们需要从原始的策略梯度表达式开始，逐步推导到上述形式。

---

#### **1. 策略梯度的基本表达式**
首先，策略梯度定理的出发点是：
\[
\nabla_\theta J(\theta) = \nabla_\theta \mathbb{E}_{\tau \sim \pi_\theta} [R(\tau)]
\]

由于 \(\tau\) 的分布 \(p(\tau | \theta)\) 依赖于策略 \(\pi_\theta\)，我们需要对期望内部的 \(R(\tau)\) 关于 \(\theta\) 求梯度。利用强化学习中的梯度技巧（log-likelihood trick），有：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ R(\tau) \nabla_\theta \log p(\tau | \theta) \right]
\]

轨迹的概率分布为：
\[
p(\tau | \theta) = p(s_0) \prod_{t=0}^T \pi_\theta(a_t | s_t) p(s_{t+1} | s_t, a_t)
\]
其中 \(p(s_0)\) 是初始状态分布，\(p(s_{t+1} | s_t, a_t)\) 是环境的状态转移概率。对其取对数并求梯度：
\[
\log p(\tau | \theta) = \log p(s_0) + \sum_{t=0}^T \log \pi_\theta(a_t | s_t) + \sum_{t=0}^T \log p(s_{t+1} | s_t, a_t)
\]
\[
\nabla_\theta \log p(\tau | \theta) = \nabla_\theta \sum_{t=0}^T \log \pi_\theta(a_t | s_t) = \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t)
\]
注意，\(\nabla_\theta \log p(s_0) = 0\) 和 \(\nabla_\theta \log p(s_{t+1} | s_t, a_t) = 0\)，因为初始状态分布和环境动态不依赖于 \(\theta\)。因此：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \left( \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) \right) R(\tau) \right]
\]

这是策略梯度的基本形式，\(R(\tau)\) 是整个轨迹的回报。

---

#### **2. 分解期望**
现在，我们的目标是将 \(R(\tau)\) 替换为 \(R_t\)。由于期望是线性的，我们可以将上式按时间步展开：
\[
\nabla_\theta J(\theta) = \sum_{t=0}^T \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) R(\tau) \right]
\]

对于每一项 \(\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) R(\tau) \right]\)，\(\nabla_\theta \log \pi_\theta(a_t | s_t)\) 只依赖于当前状态 \(s_t\) 和动作 \(a_t\)，而 \(R(\tau) = \sum_{k=0}^T \gamma^k r_k\) 包含了过去、当前和未来的回报。我们需要利用因果性，证明梯度只依赖于从 \(t\) 开始的未来回报。

---

#### **3. 分解 \(R(\tau)\)**
将 \(R(\tau)\) 分解为过去和未来的部分：
\[
R(\tau) = \sum_{k=0}^{t-1} \gamma^k r_k + \sum_{k=t}^T \gamma^k r_k
\]
- \(\sum_{k=0}^{t-1} \gamma^k r_k\)：时间 \(t\) 之前的回报（过去）。
- \(\sum_{k=t}^T \gamma^k r_k\)：从时间 \(t\) 开始的回报（未来）。

将其代入期望：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) R(\tau) \right] = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \left( \sum_{k=0}^{t-1} \gamma^k r_k + \sum_{k=t}^T \gamma^k r_k \right) \right]
\]

由于期望是线性的，可以拆分为两部分：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) R(\tau) \right] = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=0}^{t-1} \gamma^k r_k \right] + \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=t}^T \gamma^k r_k \right]
\]

---

#### **4. 使用条件期望分析过去回报的贡献**
我们首先处理第一项，即过去的回报对梯度的贡献：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=0}^{t-1} \gamma^k r_k \right]
\]

注意到：
- \(\sum_{k=0}^{t-1} \gamma^k r_k\) 只依赖于轨迹的前 \(t\) 个时间步 \(\tau_{<t} = (s_0, a_0, \dots, s_{t-1}, a_{t-1}, s_t)\)，与未来的轨迹 \(\tau_{\geq t} = (a_t, s_{t+1}, a_{t+1}, \dots)\) 无关。
- \(\nabla_\theta \log \pi_\theta(a_t | s_t)\) 只依赖于 \(s_t\) 和 \(a_t\)。

我们可以将期望分解为：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=0}^{t-1} \gamma^k r_k \right] = \mathbb{E}_{\tau_{<t}} \left[ \sum_{k=0}^{t-1} \gamma^k r_k \cdot \mathbb{E}_{s_t, a_t | \tau_{<t}} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \right] \right]
\]

关键在于计算内部期望：
\[
\mathbb{E}_{s_t, a_t | \tau_{<t}} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \right] = \mathbb{E}_{s_t | \tau_{<t}} \left[ \mathbb{E}_{a_t | s_t} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \right] \right]
\]

由于 \(a_t \sim \pi_\theta(a_t | s_t)\)，我们知道：
\[
\mathbb{E}_{a_t | s_t} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \right] = \int \pi_\theta(a_t | s_t) \nabla_\theta \log \pi_\theta(a_t | s_t) \, da_t
\]
因为 \(\nabla_\theta \log \pi_\theta(a_t | s_t) = \frac{\nabla_\theta \pi_\theta(a_t | s_t)}{\pi_\theta(a_t | s_t)}\)，所以：
\[
\int \pi_\theta(a_t | s_t) \frac{\nabla_\theta \pi_\theta(a_t | s_t)}{\pi_\theta(a_t | s_t)} \, da_t = \int \nabla_\theta \pi_\theta(a_t | s_t) \, da_t = \nabla_\theta \int \pi_\theta(a_t | s_t) \, da_t = \nabla_\theta 1 = 0
\]

因此：
\[
\mathbb{E}_{s_t, a_t | \tau_{<t}} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \right] = 0
\]

这意味着：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=0}^{t-1} \gamma^k r_k \right] = 0
\]

过去的回报对梯度没有贡献！

---

#### **5. 处理未来回报**
现在只剩下第二项：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=t}^T \gamma^k r_k \right]
\]

注意到 \(\sum_{k=t}^T \gamma^k r_k\) 是从时间 \(t\) 开始的回报，但折扣因子以 \(k=0\) 为基准。为了与 \(R_t = \sum_{k=t}^T \gamma^{k-t} r_k\) 对齐，我们重写：
\[
\sum_{k=t}^T \gamma^k r_k = \gamma^t \sum_{k=t}^T \gamma^{k-t} r_k = \gamma^t R_t
\]

所以：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \sum_{k=t}^T \gamma^k r_k \right] = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \gamma^t R_t \right]
\]

将所有时间步的贡献加起来：
\[
\nabla_\theta J(\theta) = \sum_{t=0}^T \mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) \gamma^t R_t \right]
\]

---

#### **6. 转换为标准形式**
在策略梯度定理的经典形式中，通常使用动作值函数 \(Q^\pi(s_t, a_t)\)：
\[
Q^\pi(s_t, a_t) = \mathbb{E}_{\tau_{\geq t} | s_t, a_t} \left[ \sum_{k=t}^T \gamma^{k-t} r_k \right] = \mathbb{E}_{\tau_{\geq t} | s_t, a_t} [R_t]
\]

因此：
\[
\mathbb{E}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) R_t \right] = \mathbb{E}_{s_t \sim p(s_t | \theta), a_t \sim \pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a_t | s_t) Q^\pi(s_t, a_t) \right]
\]

但在蒙特卡洛采样中，我们直接使用 \(R_t\) 作为 \(Q^\pi(s_t, a_t)\) 的无偏估计。所以，最终形式为：
\[
\nabla_\theta J(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) R_t \right]
\]

注意，这里的表达式有时会保留 \(\gamma^t\)（如 \(\sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t | s_t) \gamma^t R_t\)），取决于 \(J(\theta)\) 的定义。如果 \(J(\theta)\) 是未折扣的期望回报，\(\gamma^t\) 可能被吸收进定义中。

---

#### **7. 总结**
通过条件期望的分解，我们证明了：
- 过去的回报 \(\sum_{k=0}^{t-1} \gamma^k r_k\) 在梯度中不产生贡献（期望为 0）。
- 只有从 \(t\) 开始的未来回报 \(R_t\) 影响梯度。
- 最终，\(R(\tau)\) 被替换为 \(R_t\)，体现了策略梯度的因果性。

这就是从 \(R(\tau)\) 到 \(R_t\) 的完整推导过程！


