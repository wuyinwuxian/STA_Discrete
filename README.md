# STA_Discrete
离散状态转移算法的实现

## 介绍
这是求解无约束李离散优化问题的DSTA python版本

DSTA是算法类，otherlib 是存放用户优化问题的目标函数，目前已经实现了3个 benchmark 函数，这三个benchmark可以在论文中查看，test为运行文件

如果你的目标函数包含一些额外信息，或者相关参数无法直接在函数中直接定义，请参考DSTA处理TSP问题版本，利用lambda函数来实现，[参考地址](https://github.com/wuyinwuxian/DSTA_TSP_python_version/blob/main/DSTA_TSP_python_version/Test.py#L11)
