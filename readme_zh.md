# 自动登录脚本

**其他语言版本: [English](readme.md)**

## 简介

因为有些账号时常要登录, 输入相同的用户名或者密码显得十分繁琐, 于是写下这个脚本用于简化登录过程。  
该脚本能够在将光标定位到登录表单的输入框后，自动填充并提交登录信息。

## 安全性

所有账户数据都存储在本地，脚本在执行过程中不进行任何网络请求，因此无需担心数据安全问题。

## 安装方法

### 本地运行

1. 确保您的计算机上已安装 Python 环境。
2. 下载脚本文件。
3. 将脚本文件放置在您希望运行的目录中。
4. 确保脚本所需的依赖库（如 `pyautogui`）已安装。如果未安装，可以通过运行 `pip install pyautogui` 来安装 `pyautogui` 库。
5. `python auto_login.py`

**方便使用小技巧:**
可以在桌面创建一个`auto_login.bat`批处理文件(windows), 双击即可快速运行。

```bat
@echo off
cd /d D:\code\python\scripts\auto_login\ REM (切换到脚本所在目录)
python auto_login.py
pause
```

## 使用方法

### 选择账户自动登录

1. 运行脚本后，您将看到一个菜单，选择 "1. Select account to auto login" 来开始自动登录过程。
2. 根据提示选择您要登录的账户。
3. 确保光标位于需要自动填充的用户名或密码输入框中。
4. 脚本将自动填充信息并尝试登录。

### 添加新账户

1. 选择 "2. Add account" 来添加一个新的账户。
2. 输入账户名，并根据提示输入登录所需的信息。
3. 输入完毕后，输入 "q" 并按 Enter 键保存账户信息。

### 删除账户

1. 选择 "3. Delete account" 来删除一个已有的账户。
2. 根据提示选择您要删除的账户。
3. 确认删除后，账户信息将被移除。

### 退出程序

1. 选择 "4. Exit" 来退出脚本。

## 注意事项

- 在使用自动登录功能之前，请确保光标位于正确的输入框中，以便脚本能够正确地填充信息。
- 为了保护您的账户安全，请不要在公共或不安全的计算机上使用此脚本。
- 定期更新您的账户信息，确保脚本中的登录信息是最新的。

## 后续优化改进的内容

### 增加更多异常处理流程

- 增强脚本的错误捕获和处理能力，确保在遇到意外情况时，能够给出清晰的错误提示，并安全地终止或恢复操作。

### 增加图形化界面简化操作

- 开发一个图形用户界面（GUI），使用户能够通过点击按钮和填写表单来完成账户的选择、添加和删除，从而简化操作流程。

### 更加美观

- 对图形化界面进行美化设计，提供更加直观和友好的用户交互体验。

通过这个自动登录脚本，您可以更快捷、更安全地管理您的在线账户。
