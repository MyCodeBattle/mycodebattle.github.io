---
title: 如何在服务器上跑 Selenium
layout: post
date: 2017-06-23
categories: 
---

# 前言

之前要写一个爬全民K歌的 Selemiun 代码，但是发现只能在本地跑跑，一旦部署到服务器上就会出现奇怪的找不到浏览器的错误，那有个毛用啊对吧。后来 Hcbbt 巨巨给我发了个教程，才发现少装了个东西。现在把这个完整的过程写一下，希望对大家有帮助。

# 依赖

全新的一个 Maven 项目，先在 pom.xml 里加上 Selenium 和编译打包的配置。
完整的 pom.xml 如下。

```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.zlx</groupId>
    <artifactId>selenium-example</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>2.53.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                    <encoding>UTF8</encoding>
                </configuration>
            </plugin>

            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>2.5.5</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>SeleniumExample</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

然后因为用的是 Chrome，所以要 Chrome 的 WebDriver 文件。去这里下  
https://sites.google.com/a/chromium.org/chromedriver/

# 开始

先写短最简单的代码看看在本地能不能跑起来。  
我们爬一下阿卡林的图~
代码如下。

那个 local 就是我们本地存放的 chromedriver 位置。

```
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.util.List;

/**
 * Created by purefrog on 23/06/2017.
 */
public class SeleniumExample {
    public static String local = "/Users/purefrog/Downloads/chromedriver";

    public static void main(String[] args) throws Exception {
        System.setProperty("webdriver.chrome.driver", local);

        ChromeOptions options = new ChromeOptions();
        options.addArguments("window-size=1280,728");   //设置窗口大小

        DesiredCapabilities cap = DesiredCapabilities.chrome();
        cap.setCapability(ChromeOptions.CAPABILITY, options);
        WebDriver webDriver = new ChromeDriver(cap);

        String url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%98%BF%E5%8D%A1%E6%9E%97&oq=%E9%98%BF%E5%8D%A1%E6%9E%97&rsp=-1";

        try {
            webDriver.get(url);
            Thread.sleep(10000);

            List<WebElement> webElements = webDriver.findElements(By.xpath("//img[@class='main_img img-hover']"));
            for (WebElement e : webElements) {
                System.out.println(e.getAttribute("src"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            webDriver.close();
        }
    }
}
```

然后应该会打印出一坨 Url 的。说明这样就可以了。

接下来我们尝试部署到没有桌面环境的服务器上。把刚才本地的 chromedriver 位置改成服务器上的位置。

# 部署

`mvn clean install`一下。这时候在项目目录的`target`下会看到一个`selenium-example-1.0-SNAPSHOT-jar-with-dependencies.jar`文件。

然后把这个文件搞到服务器上去。

服务器要装上 Chrome。  
如果还没装的话可以这么装  

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -f
dpkg -i google-chrome-stable_current_amd64.deb
```

然后之前我就卡在这里了。  
如果你现在直接用`java -jar xxx.jar`来跑的话，应该是会报这个错的！

```
Starting ChromeDriver 2.30.477691 (6ee44a7247c639c0703f291d320bdf05c1531b57) on port 14103
Only local connections are allowed.
Exception in thread "main" org.openqa.selenium.WebDriverException: unknown error: Chrome failed to start: exited abnormally
  (Driver info: chromedriver=2.30.477691 (6ee44a7247c639c0703f291d320bdf05c1531b57),platform=Linux 4.9.15-x86_64-linode81 x86_64) (WARNING: The server did not provide any stacktrace information)
Command duration or timeout: 60.13 seconds
Build info: version: 'unknown', revision: 'unknown', time: 'unknown'
System info: host: 'localhost', ip: '127.0.0.1', os.name: 'Linux', os.arch: 'amd64', os.version: '4.9.15-x86_64-linode81', java.version: '1.8.0_131'
Driver info: driver.version: ChromeDriver
	at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
	at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
	at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
	at java.lang.reflect.Constructor.newInstance(Constructor.java:423)
	at org.openqa.selenium.remote.ErrorHandler.createThrowable(ErrorHandler.java:215)
	at org.openqa.selenium.remote.ErrorHandler.throwIfResponseFailed(ErrorHandler.java:167)
	at org.openqa.selenium.remote.JsonWireProtocolResponse.lambda$new$0(JsonWireProtocolResponse.java:53)
	at org.openqa.selenium.remote.JsonWireProtocolResponse.lambda$getResponseFunction$2(JsonWireProtocolResponse.java:91)
	at org.openqa.selenium.remote.ProtocolHandshake.lambda$createSession$22(ProtocolHandshake.java:365)
	at java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:193)
	at java.util.Spliterators$ArraySpliterator.tryAdvance(Spliterators.java:958)
	at java.util.stream.ReferencePipeline.forEachWithCancel(ReferencePipeline.java:126)
	at java.util.stream.AbstractPipeline.copyIntoWithCancel(AbstractPipeline.java:498)
	at java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:485)
	at java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:471)
	at java.util.stream.FindOps$FindOp.evaluateSequential(FindOps.java:152)
	at java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)
	at java.util.stream.ReferencePipeline.findFirst(ReferencePipeline.java:464)
	at org.openqa.selenium.remote.ProtocolHandshake.createSession(ProtocolHandshake.java:368)
	at org.openqa.selenium.remote.ProtocolHandshake.createSession(ProtocolHandshake.java:159)
	at org.openqa.selenium.remote.HttpCommandExecutor.execute(HttpCommandExecutor.java:142)
	at org.openqa.selenium.remote.service.DriverCommandExecutor.execute(DriverCommandExecutor.java:82)
	at org.openqa.selenium.remote.RemoteWebDriver.execute(RemoteWebDriver.java:637)
	at org.openqa.selenium.remote.RemoteWebDriver.startSession(RemoteWebDriver.java:250)
	at org.openqa.selenium.remote.RemoteWebDriver.startSession(RemoteWebDriver.java:236)
	at org.openqa.selenium.remote.RemoteWebDriver.<init>(RemoteWebDriver.java:137)
	at org.openqa.selenium.chrome.ChromeDriver.<init>(ChromeDriver.java:184)
	at org.openqa.selenium.chrome.ChromeDriver.<init>(ChromeDriver.java:148)
	at SeleniumExample.main(SeleniumExample.java:25)
```

这是因为没安装 Xvfb 这个东西。

接下来安装 Xvfb：`sudo apt install Xvfb`  
启动 Xvfb 服务：`Xvfb -ac :7 -screen 0 1280x1024x8 &`  (注意这个是x, 不是* 哦)  
然后还需要一句这个东西：`export DISPLAY=:7`

然后就可以跑啦！

**这里要注意，不能用 root 权限来跑，不然会报一个 Chrome not reachable 的错误。**

`java -jar selenium-example-1.0-SNAPSHOT-jar-with-dependencies.jar`

然后就能看到输出了。

以上。