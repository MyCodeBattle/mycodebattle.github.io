---
title: Spring、Hibernate、Struts 的整合
layout: post
date: 2016-05-08
categories: SSH
---

记一下 SSH 是怎么整合的，省得以后老是百度。

`applicationContext.xml`要复制一份放在 Tomcat 的 bin 目录下，否则会找不到。
然后这时候要包一下 Hibernate 的配置文件。

贴一份模板

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="sessionFactory" class="org.springframework.orm.hibernate5.LocalSessionFactoryBean">
        <property name="configLocations">
            <value>classpath:hibernate.cfg.xml</value>
        </property>
    </bean>

    <bean id="loginDAO" class="org.DAO.LoginDAOImpl">
        <property name="sessionFactory" ref="sessionFactory"/>
    </bean>

</beans>
```

`web.xml`是 IDEA 自己生成的，随便贴一下。

```
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">
    <context-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>/WEB-INF/applicationContext.xml</param-value>
    </context-param>
    <filter>
        <filter-name>struts2</filter-name>
        <filter-class>org.apache.struts2.dispatcher.ng.filter.StrutsPrepareAndExecuteFilter</filter-class>
    </filter>
    <filter-mapping>
        <filter-name>struts2</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    <listener>
        <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
    </listener>
    <servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>*.form</url-pattern>
    </servlet-mapping>
</web-app>
```

`struts.xml`的配置也不变。

```
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE struts PUBLIC
        "-//Apache Software Foundation//DTD Struts Configuration 2.3//EN"
        "http://struts.apache.org/dtds/struts-2.3.dtd">

<struts>
    <include file="struts-default.xml"/>
    <package name="default" extends="struts-default">
        <action name="login" class="org.action.LoginAction">
            <result name="success">success_login.jsp</result>
            <result name="error">login.jsp</result>
        </action>
    </package>
</struts>
```

