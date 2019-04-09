# cnn_captcha
#感谢
首先要感谢nickliqian@outlook.com 慷慨的开源他的代码库 https://github.com/nickliqian/cnn_captcha 
选择这个库作为学习的初步是非常有意义的。

网上有很多ocr实现，但是，只有nickliqian的代码清晰可读，而且在他的readme里面详细的比较了各种实现的区别。
基本上，这是一个可以拿来即用的项目。

#为什么强烈推荐，因为他的文档结构非常不错，所以我也沿用了他的模式。
他的readme架构基本上是这样的
1）系统选型。简要的说明能找到的实现方案的名字和优缺点。
2）时间表。 记录了实现过程中的各种里程碑
3）项目目录和约定

#我的学习历程
 
## 1.1 tensorflow 安装和环境的配置
### 1.1.1 Unix 还是 Windows
tensorflow可以跑在unix和windows, 
windows:  优点： 熟悉，GPU支持多， 缺点，pyhon支持有限，怕是有bug， 系统开销比较大。特别是windows10各种不爽。因此不考虑
MAC  :没用过。。。
Ubunut: tensorflow教材就是用Ubuntu.没有困难。不折腾，就选ubuntu.

### 1.1.2 Linux 选择
Unix -CentOs :很好，但是安装起来不是非常顺利，折腾半天装上了，比windows下还花时间。因此tensorflow升级后，就不在centos上面用了。
优点：在企业环境下特别稳定。缺点：文档偏少，缺省安装tensorflow有不少问题要上网找答案。
Unix - Ubuntu :原生桌面版本： 优点：各种支持，缺点：不够稳定，x11桌面有时会崩溃。多来几下，就只能在重新安装桌面，太折腾。
Unix - Ubuntu 18.10  不稳定。经常死机
Unix - Ubuntu 18.04  稳定，速度快，系统占用少， 缺点：是一精简系统，如需要office,得自己装。优点，tensorflow教材就是用Ubuntu.没有困难。
lsb_release -a lubuntu 
Ubuntu 18.04.2 LTS
https://lubuntu.net/ 
https://lubuntu.net/lubuntu-18-04-bionic-beaver-released/
http://cdimage.ubuntu.com/lubuntu/releases/18.04/release/lubuntu-18.04-desktop-amd64.iso 

windows下的虚拟机：优点可以随意换系统。合适再装主机上面。

### 1.1.3 Tensorflow安装
https://www.tensorflow.org/install/pip 
这里就不重复了。

### 1.1.4 参考资料

《神经网络与深度学习》 Neural Network and Deep Learning https://nndl.github.io

https://github.com/nfmcclure/tensorflow_cookbook

https://zhuanlan.zhihu.com/p/29605049

下一步：https://github.com/matterport/Mask_RCNN


github config：
Set a Git username:

$ git config --global user.name "Mona Lisa"
Confirm that you have set the Git username correctly:

$ git config --global user.name
> Mona Lisa

$ git config --global credential.helper cache
$ git config --global credential.helper store

## 1.2 项目结构
### 1.2.1 根： 放readme, 主程序
### 1.2.2 /gen_image： 造图片


## 1.3 学习进度
### 1.3.1 把例子跑起来， 预计2 天
### 1.3.2 修改和调整 ， 预计1 周
### 1.3.3 学习mask rcnn,看看这个方式来处理会不会更好。


