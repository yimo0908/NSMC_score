### 使用方法

1. 点击项目右上角的Fork，Fork此项目

2. 到自己Fork的项目点击Setting → Secrets → New repository secret

   ![](https://github.com/yimo0908/NSMC_score/blob/main/image/1.png)

3. Name填写`USERNAME`，Value填写 教务系统登录账号（通常为学号）

4. 再New一个，Name填写`PASSWORD`，Value填写 教务系统登录密码

5. 再New一个，Name填写`MAIL_ACCOUNT`，Value填写 QQ邮箱地址（`QQ号@qq.com`）

6. 再New一个，Name填写`MAIL_KEY`，Value填写 邮箱授权码

7. 再New一个，Name填写`YEAR`，Value填写 要查询的学年（如`2020-2021`）

8. 再New一个，Name填写`TERM` ，Value填写 要查询的学期（如`1`）

   ![](https://github.com/yimo0908/NSMC_score/blob/main/image/2.png)

9. 点击`action`，再点击`I understand my workflows,go ahead and enable them`→`run`→`Enable workflow`即可激活自动运行

   默认在1月.2月.6月.7月每周一中午12:00自动查询并发邮件，可自行修改

   ![](https://github.com/yimo0908/NSMC_score/blob/main/image/3.png)

   ![](https://github.com/yimo0908/NSMC_score/blob/main/image/4.png)

   