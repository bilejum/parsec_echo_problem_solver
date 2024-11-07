最近使用parsec玩本地多人游戏，效果不错，但是使用过程中发现一个致命的问题：如果使用主机端设备连麦，那么客端会听到回音。

这个脚本主要用于自动化以下流程

# 解决方案
---
事实上，在parsec设置的host栏目内，自带回音消除的设置![[Pasted image 20240220153905.png]]

但可选项中没有QQ，Kook，YY等大陆能够流畅使用的语音软件。所以需要前往高级设置中对Echo Selection这一项自定义设置自己所使用的语音软件，本案例在windows11操作系统下，以QQ（QQ.exe）为例

1.在parsec中将上述设置项分别修改为`New`和`None`（已经是这个选项了也再点一遍）

2.打开资源管理器（filexplorer），在路径栏输入`%appdata%\Parsec\`，打开`config.json`文件

（如果安装时选了Shared installtion，请输入第二项的路径）
- Per User installation: `%appdata%\Parsec\` 
- Shared installation: `%programdata%\Parsec\`

3.找到`echo_app_selection`这一项（一般在文件顶端），将冒号之后的`None`改为`QQ.exe`（如果是其它软件，就改成相应的进程名，例如Kook.exe）
![[Pasted image 20240220155023.png]]

4.重启parsec（restart）