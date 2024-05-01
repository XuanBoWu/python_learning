# Django 技术笔记：创建和配置一个简单的Pizzeria Web应用

## 环境配置与安装

### 创建虚拟环境

虚拟环境是一个独立的Python环境，允许我们在不影响系统其他部分的情况下，为不同的项目安装不同版本的库和依赖。

为了创建一个新的虚拟环境，我们使用以下命令：

```bash
alex@Mac-alex Demo % cd Pizzeria
alex@Mac-alex Pizzeria % python3 -m venv pizzeria_env
```

这将在当前目录下创建一个名为`pizzeria_env`的新虚拟环境。

### 激活虚拟环境

在使用虚拟环境之前，需要先激活它。激活虚拟环境将确保我们使用的是虚拟环境中的Python解释器和库。

```bash
alex@Mac-alex Pizzeria % source pizzeria_env/bin/activate
(pizzeria_env) alex@Mac-alex Pizzeria % 
```

注意，命令提示符前的`(pizzeria_env)`表示虚拟环境已经被激活。

### 安装Django

Django是一个高级的Python Web框架，它鼓励快速开发和干净、实用的设计。使用pip安装Django：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % pip install django
```

在安装Django的过程中，pip会输出安装进度和结果。如果pip版本落后，会有一个警告提示升级pip。

## Django项目配置

### 创建Django项目

使用Django提供的工具创建一个新项目：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % django-admin startproject Pizzeria .
```

这将在当前目录下创建一个新的Django项目，名为`Pizzeria`。

使用`ls`命令查看创建的文件：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % ls Pizzeria 
```

### 创建数据库

Django使用迁移系统来同步数据库模式。默认情况下，Django使用SQLite。

执行迁移创建数据库表：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py migrate
```

这将应用所有默认的迁移，创建Django项目所需的表。

### 查看项目

要启动开发服务器并查看项目，运行：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py runserver
```

此命令启动Django的开发服务器，您可以在浏览器中访问`http://127.0.0.1:8000/`来查看您的网站。

## 创建应用程序

### 生成应用程序目录

在Django中，应用程序是一个包含模型、视图、模板和URLs的Python包。

创建一个新应用程序：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py startapp pizzas
```

这将创建一个名为`pizzas`的新应用程序目录。

### 定义数据模型

在Django中，数据模型是一个Python类，它定义了数据库中的表结构。

编辑`pizzas/models.py`来定义`Pizza`和`Topping`模型：

```python
# pizzas/models.py
from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
```

### 激活数据模型

为了让Django知道我们创建的应用程序和模型，我们需要在项目的`settings.py`文件中激活它。

在`Pizzeria/settings.py`文件中的`INSTALLED_APPS`列表添加我们的应用程序：

```python
# Pizzeria/settings.py
INSTALLED_APPS = [
    # My Apps
    'pizzas',
    # Default installed Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### 迁移数据模型

创建数据模型的迁移文件：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py makemigrations pizzas
```

然后应用迁移文件，创建数据库表：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py migrate
```

## Django 管理网站

### 创建超级用户

为了访问Django的管理网站，我们需要一个超级用户：

```bash
(pizzeria_env) alex@Mac-alex Pizzeria % python manage.py createsuperuser
```

按提示输入用户名、邮箱和密码来创建超级用户。

### 向管理网站注册数据模型

要在Django管理网站中管理我们的模型，我们需要在`pizzas/admin.py`文件中注册它们：

```python
# pizzas/admin.py
from django.contrib import admin
from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
```

现在，您可以使用超级用户账户访问管理网站：访问`http://localhost:8000/admin/`，并输入您刚创建的超级用户的用户名和密码。

这就完成了一个简单的Pizzeria Web应用的创建和配置。您可以继续开发更多功能，如添加视图、模板和表单，以丰富您的应用程序。
